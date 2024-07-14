#!/usr/bin/env python3

import time
import sys
from collections import defaultdict
import subprocess
from typing import Dict, List
import jc
import pprint
import json
from pydantic import BaseModel

first_base_station_id = 1
last_base_station_id = 3


def base_station_ssid(id: int) -> str:
    """Get the SSID for the base station with a certain id."""
    return "PiHotspot" + str(id)


def base_station_ids():
    return range(first_base_station_id, last_base_station_id + 1)


# The number of RSSI values to collect for each sample.
n = 5


class Fingerprint(BaseModel):
    x: float
    y: float
    facing_direction: str
    # Map each base stations ssid to n RSSI measurements.
    base_station_to_rssi: Dict[str, List[float]]


def collect_rssi_values_from_base_stations():
    base_station_to_rssi = dict()

    ssid_to_rssi = collect_ssid_rssi_map()

    for base_station_id in base_station_ids():
        ssid = base_station_ssid(base_station_id)

        if ssid not in ssid_to_rssi:
            raise Exception(f"SSID for base station {base_station_id} not found in SSID to RSSI map. Is the device on?")

        rssi = ssid_to_rssi[ssid]
        base_station_to_rssi[ssid] = rssi

    return base_station_to_rssi


def collect_ssid_rssi_map():
    """Collect and return a map from device SSID to RSSI for that device."""

    # NOTE: The name of the wifi interface might be different for every device.
    wifi_interface = "wlp3s0"
    result = subprocess.run(['iw', wifi_interface, 'scan'], capture_output=True, text=True)
    iw_scan_stdout = result.stdout

    iw_scan_json = jc.parse("iw-scan", iw_scan_stdout)

    ssid_to_rssi = dict()

    for device_info in iw_scan_json:
        ssid_field = "ssid"
        rssi_field = "signal_dbm"

        # Only store devices that have both an SSID and RSSI value.
        if ssid_field in device_info and rssi_field in device_info:
            ssid = device_info[ssid_field]
            rssi = float(device_info[rssi_field])
            ssid_to_rssi[ssid] = rssi

    return ssid_to_rssi


def try_until_success(f):
    """Try executing a function until it succeeds."""
    while True:
        try:
            return f()
        except Exception:
            print("sth went wrong, trying again...")


def fingerprint_at_location() -> List[Fingerprint]:
    print("Go to next fingerprinting location")

    # User has to input location.
    x = try_until_success(lambda: float(input("x: ")))
    y = try_until_success(lambda: float(input("y: ")))

    fingerprints = []

    for facing_direction in ["north", "east", "south", "west"]:
        print(f"Please face {facing_direction}")
        input("Press enter when ready")

        base_station_to_all_rssi = defaultdict(lambda: [])

        for i in range(0, n):
            print(f"Collecting sample {i}")

            rssi_base_station_values = try_until_success(collect_rssi_values_from_base_stations)

            for (base_station, rssi) in rssi_base_station_values.items():
                base_station_to_all_rssi[base_station].append(rssi)

        fingerprint = Fingerprint(x=x, y=y, facing_direction=facing_direction, base_station_to_rssi=dict(base_station_to_all_rssi))
        print(fingerprint)
        fingerprints.append(fingerprint)

    return fingerprints


def fingerprint_forever(output_json_file):
    fingerprints = []

    while True:
        fingerprints.extend((fingerprint.model_dump() for fingerprint in fingerprint_at_location()))

        # pprint.pprint(fingerprints)

        # Write fingerprints to file as JSON.
        with open(output_json_file, "w") as file:
            json.dump(fingerprints, file)


def main():
    try:
        output_json_file = sys.argv[1]
    except IndexError:
        raise Exception("Expected the output JSON filename as argument.")

    fingerprint_forever(output_json_file)


if __name__ == "__main__":
    main()
