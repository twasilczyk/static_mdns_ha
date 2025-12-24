# mDNS Republisher add-on for Home Assistant

## About

This add-on re-publishes hostnames for flaky AirPrint printers, improving service reliability.

At this time there's no auto-detection of existing hosts on the network, so you have to scan your network and add these devices manually.

## Configuration

1. On your laptop, install Avahi or other mDNS browser
2. On your printer, enable AirPrint and mDNS
3. Scan your network against AirPrint devices \
   `avahi-browse -r _ipp._tcp`
4. Note down hostname and address (ideally IPv4)
5. If you can't find your device, hostname will be likely configurable on the printer itself, but the actual hostname will be suffixed with `.local`
6. Add the hostname and address to this add-on's configuration
7. Start the add-on and verify (in logs) the last line says `Established under name ...`
8. Optional: disable mDNS on your printer (but not AirPrint)

As a result, printers should be showing up almost immediately (within half a second) in the print dialog on iPhones.
