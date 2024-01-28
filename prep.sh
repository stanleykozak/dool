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

if [[ ! -f /tmp/dool_checkupdates ]]; then 
    touch /tmp/dool_checkupdates
fi

#CHECK UPDATES
if [[ "$(date +%R)" == "01:00" ]] || [[ "$(date +%R)" == "01:01" ]] || [[ "$(date +%R)" == "0:59" ]]; then
   apt list --upgradable 2>/dev/null | wc -l >/tmp/dool_checkupdates
fi
