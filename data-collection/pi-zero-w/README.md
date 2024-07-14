# Collecting RSSI data using Raspberry Pi Zero W base stations

## Raspberry Pi setup

- Install OS: Raspberry Pi OS (Legacy, 32-bit, Debian Bullseye) Lite (no desktop environment)
- Once booted, login with username `pi` and password `raspberry`.
- Enable the `NetworkManager` service:
```sh
systemctl enable NetworkManager.sevice
systemctl start NetworkManager.sevice
```
- Set the id of the hotspot (must be different for each configured pi):
```sh
export i=1
```
- Setup a hotspot, which is needed so that the pi advertises its address and the tracked device can read its RSSI values. Use the following command:
```sh
nmcli device wifi hotspot con-name "PiHotspot${i}" ssid "PiHotspot${i}" password "password"
nmcli connection modify "PiHotspot${i}" connection.autoconnect yes
```
