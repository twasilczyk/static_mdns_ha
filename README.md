# Static mDNS integration for Home Assistant

## About

This integration re-publishes hostnames for flaky AirPrint printers, improving service reliability.

At this time there's no auto-detection of existing hosts on the network, so you have to scan your network and add these devices manually.

## Installation

1. Copy this entire repository to `custom_components/static_mdns`

## Configuration

1. On your laptop, install Avahi or other mDNS browser
2. On your printer, enable AirPrint and mDNS
3. Scan your network against AirPrint devices \
   `avahi-browse -r _ipp._tcp`
4. Note down hostname and address (ideally IPv4)
5. If you can't find your device, hostname will be likely configurable on the printer itself, but the actual hostname will be suffixed with `.local`
6. To your `configuration.yaml` add the following config:
   ```
   static_mdns:
     - hostname: <NameOfMyPrinter>.local
       address: 1.2.3.4
   ```
7. Restart HA
8. Optional: disable mDNS on your printer (but not AirPrint)

As a result, printers should be showing up almost immediately (within half a second) in the print dialog on iPhones.
