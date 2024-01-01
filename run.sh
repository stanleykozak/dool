#!/bin/bash

config=$(cat /persistent/dool/config.conf)
TEMP_FILE=$(echo "$config" | grep 'TEMP_FILE' | cut -d'=' -f2)
RESULT_FILE=$(echo "$config" | grep 'RESULT_FILE' | cut -d'=' -f2)
DOOL_PATH=$(echo "$config" | grep 'DOOL_PATH' | cut -d'=' -f2)

"${DOOL_PATH}/prep.sh"

rm -rf "$TEMP_FILE" 2>/dev/null

timecheck=$(date +%R)

if [[ "$timecheck" == "10:08" ]]; then
    rm -rf "$RESULT_FILE" 2>/dev/null
fi

"${DOOL_PATH}/dool" \
-l --blank \
-c --blank \
--top-cpu-custom-cli --blank \
-m --blank \
--top-mem-custom-cli --blank \
--proc --blank \
--proc-count --blank \
-n --blank \
-t --blank \
--uptime --blank \
--systemd --blank \
--thermal \
--output "$TEMP_FILE" 2 5

tail -1 "$TEMP_FILE" >> "$RESULT_FILE"
