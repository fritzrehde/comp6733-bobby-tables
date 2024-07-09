import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass
import sys
import platform
import asyncio
from time import sleep
from typing import Any
from uuid import UUID
from bleak import BleakClient
from bleak import BleakScanner
from bleak.backends.characteristic import BleakGATTCharacteristic
import sys
import os


# Mac address
ADDRESS = (
    "FB:14:91:95:52:9C"  # Change to your device's address if on Linux/Windows
    if platform.system() != "Darwin"
    else "D5498244-E4AA-E00E-44CB-67B3B1DBD93F"  # Change to your device's address if on macOS
    # else "B9EA5233-37EF-4DD6-87A8-2A875E821C46"  # Change to your device's address if on macOS
)

custom_svc_uuid = UUID("4A981234-1CC4-E7C1-C757-F1267DD021E8")
custom_wrt_char_uuid = UUID("4A981235-1CC4-E7C1-C757-F1267DD021E8")
custom_read_char_uuid = UUID("4A981236-1CC4-E7C1-C757-F1267DD021E8")


@dataclass
class RssiSample:
    rssi: Any
    actual_distance_cm: int


REQUIRED_SAMPLES = 10
rssi_samples = []


def write_samples_to_file(rssi_samples, file_path):
    with open(file_path, 'w') as file:
        for sample in rssi_samples:
            file.write(f"{sample.rssi},{sample.actual_distance_cm}\n")


def read_samples_from_file(file_path):
    rssi_samples = []
    with open(file_path, 'r') as file:
        for line in file:
            rssi, distance = line.strip().split(',')
            rssi_samples.append(RssiSample(rssi=int(rssi), actual_distance_cm=int(distance)))
    return rssi_samples


def save_rssi_sample(rssi_sample):
    print(f"Collected RSSI sample: {rssi_sample}")
    rssi_samples.append(rssi_sample)


async def collect_single_rssi_sample():
    while True:
        actual_distance = input("What will the distance between the devices be (in cm)? ")

        print("Measurement will start scanning in...")
        for i in range(5, 0, -1):
            print(i)
            sleep(1)

        print("Scanning for bluetooth RSSI signals for 5 seconds, please wait...")
        devices = await BleakScanner.discover(return_adv=True)

        for d, _a in devices.values():
            # Get our connected bluetooth device, i.e. the arduino.
            if d.address == ADDRESS:
                save_rssi_sample(RssiSample(d.rssi, actual_distance))
                return

        print("Didn't find device, trying again.")


def analyse_rssi_values(rssi_samples, file_path):
    rssi = np.array([sample.rssi for sample in rssi_samples])
    distance = np.array([sample.actual_distance_cm for sample in rssi_samples])

    # From: https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html

    # Fit line y = mx + c where y = distance and x = rssi.
    A = np.vstack([distance, np.ones(len(distance))]).T
    m, c = np.linalg.lstsq(A, rssi)[0]
    fit_line = m * distance + c

    # Plot the data points.
    plt.scatter(distance, rssi, label='Data Points')
    # Plot the fitted line.
    plt.plot(distance, fit_line, 'r', label='Fitted Line')

    # Axis labels.
    plt.xlabel('Distance (cm)')
    plt.ylabel('RSSI')

    plt.title('Distance vs RSSI')
    plt.legend()

    # Save graph to file.
    plt.savefig(f"{file_path}.png")


async def main():
    global rssi_samples
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        print("Please provide the name of the file to save the collected rssi samples to, or analyze given that file")
        exit(1)

    # Only do data collection if target file does not yet exist, otherwise read data from file.
    if not os.path.exists(file_path):
        for _ in range(0, REQUIRED_SAMPLES):
            await collect_single_rssi_sample()

        write_samples_to_file(rssi_samples, file_path)
    else:
        rssi_samples = read_samples_from_file(file_path)

    analyse_rssi_values(rssi_samples, file_path)

if __name__ == "__main__":
    asyncio.run(main())
