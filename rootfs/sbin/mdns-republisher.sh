#!/usr/bin/with-contenv bashio

# Log to stdout
syslogd -n -O - &

# Check, if there's any hosts configured
if [ "$(bashio::config "hosts|length")" -eq 0 ]; then
    bashio::log.error "No hostnames configured, you must have at least one."
    bashio::exit.nok
fi

# Start DBUS locally
dbus-daemon --system --fork --nopidfile
while [ ! -S /run/dbus/system_bus_socket ]; do
    sleep 0.1
done

# Start avahi (mDNS) daemon
avahi-daemon --no-chroot &
while [ ! -S /run/avahi-daemon/socket ]; do
    sleep 0.1
done

# Republish mDNS name mapping from config (no autodetection for now)
for hostIt in $(bashio::config 'hosts|keys'); do
    HOSTNAME=$(bashio::config "hosts[${hostIt}].hostname")
    ADDRESS=$(bashio::config "hosts[${hostIt}].address")
    avahi-publish-address "${HOSTNAME}" "${ADDRESS}" &
done

# Consider the entire service running as long as all processes are up
wait -n
