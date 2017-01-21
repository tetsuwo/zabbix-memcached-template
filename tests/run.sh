#!/usr/bin/env sh
#
#

set -ue

digit_items="bytes bytes_read bytes_written cmd_get cmd_set curr_connections curr_items evictions get_hits get_misses limit_maxbytes uptime"

for item in $digit_items
do
  value=$(python ./src/bin/memcached-stat.py --item=${item})
  expr "${value}" + 1 > /dev/null 2>&1
  if [ $? -lt 2 ]; then
    echo "Valid: ${item}=${value}"
  else
    echo "Invalid: ${item}=${value}"
    exit 1
  fi
  
  value=$(python ./src/bin/memcached-stat.py -i ${item})
  expr "${value}" + 1 > /dev/null 2>&1
  if [ $? -lt 2 ]; then
    echo "Valid: ${item}=${value}"
  else
    echo "Invalid: ${item}=${value}"
    exit 1
  fi
done


string_items="version"

for item in $string_items
do
  value=$(python ./src/bin/memcached-stat.py --item=${item})
  if [ -n "${value}" ]; then
    echo "Valid: ${item}=${value}"
  else
    echo "Invalid: ${item}=${value}"
    exit 1
  fi
  
  value=$(python ./src/bin/memcached-stat.py -i ${item})
  if [ -n "${value}" ]; then
    echo "Valid: ${item}=${value}"
  else
    echo "Invalid: ${item}=${value}"
    exit 1
  fi
done
