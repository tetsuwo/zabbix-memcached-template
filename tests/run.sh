#!/usr/bin/env sh
#
#

set -ue



VERSION = $(python ./src/bin/memcached-stat.py --item=version)
echo $VERSION
