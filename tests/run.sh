#!/usr/bin/env sh
#
#

set -ue

items=("bytes" "bytes_read" "bytes_written" "cmd_get" "cmd_set" "curr_connections" "curr_items" "evictions" "get_hits" "get_misses" "limit_maxbytes" "uptime" "version")

for item in ${items[@]}
do
  value=$(python ./src/bin/memcached-stat.py --item=${item})
  echo "${item}: ${value}"
done
