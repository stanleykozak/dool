#!/bin/bash

# THERMAL
get_sensors=$(/usr/bin/sensors 2>/dev/null)

if [[ "$get_sensors" == "" ]]; then
    echo '-' > /tmp/dool_thermal
else
    echo "$get_sensors" | \
    grep ':.* +' | \
    tr -s ': +.' '|' | \
    cut -d'|' -f2 | \
    sort -n | \
    tail -1 > /tmp/dool_thermal
fi

# SYSTEMD
systemctl show --property SystemState --property NFailedUnits --property NNames | \
sort -h | \
cut -d'=' -f2 | \
tr '\n' ' ' > /tmp/dool_systemd
