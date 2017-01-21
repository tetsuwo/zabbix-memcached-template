#!/usr/bin/env sh
#
#

set -ue

digit_items="bytes bytes_read bytes_written cmd_get cmd_set curr_connections curr_items evictions get_hits get_misses limit_maxbytes uptime version"

for item in $digit_items
do
  value=$(python ./src/bin/memcached-stat.py --item=${item})
  echo "${item}: ${value}"
  expr "${value}" + 1 > /dev/null 2>&1
  if [ $? -lt 2 ]; then
    echo "Valid value"
  else
    echo "Invalid value"
    exit 1
  fi
done


string_items=""
