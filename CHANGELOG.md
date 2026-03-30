## 0.2.0

Another test attempt:
- Redesigned as a HA integration, plugging into existing zeroconf service


## 0.1.0

Test release:
- Designed as a HAOS App (Docker container)
- It seems to work
- Apparmor enabled
- NOT Signed pre-built images
- Note: turned out to occasionally fail once a couple days, requiring restart
  This was most likely due to running two zeroconf/mDNS services on the same host
