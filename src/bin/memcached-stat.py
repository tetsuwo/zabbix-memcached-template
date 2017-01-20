#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getopt, sys, telnetlib

MEMCACHED_SERVER = 'localhost'
MEMCACHED_PORT = '11211'
MEMCACHED_STAT_ITEMS = (
    'bytes',
    'bytes_read',
    'bytes_written',
    'cmd_get',
    'cmd_set',
    'curr_connections',
    'curr_items',
    'evictions',
    'get_hits',
    'get_misses',
    'limit_maxbytes',
    'uptime',
    'version',
)

COMMAND_SHORT_OPTIONS = 'h:p:i:'
COMMAND_LONG_OPTIONS = ['help', 'host=', 'port=', 'item=']

def get_memcached_stats(host, port):
    conn = telnetlib.Telnet(host, port, timeout=30)
    conn.write('stats\n')
    conn.write('quit\n')
    return conn.read_all()

def parse_memcached_stats(raw_stats):
    stats = {}
    for line in raw_stats.splitlines():
        if not line.startswith('STAT'):
            continue
        parts = line.split()
        if not parts[1] in MEMCACHED_STAT_ITEMS:
            continue
        stats[parts[1]] = parts[2]
    try:
        hit_ratio = float(stats['get_hits']) * 100 / float(stats['cmd_get'])
    except:
        hit_ratio = 0.0
    stats['hit_ratio'] = round(hit_ratio, 2)
    try:
        memory_usage = float(stats['bytes']) * 100 / float(stats['limit_maxbytes'])
    except:
        memory_usage= 0.0
    stats['memory_usage'] = round(memory_usage, 2)
    return stats

def main(host, port):
    item = 'version'
    try:
        opts, args = getopt.getopt(sys.argv[1:], COMMAND_SHORT_OPTIONS, COMMAND_LONG_OPTIONS)
        for opt, arg in opts:
            if opt in ('--host', '-h'):
                host = arg
            elif opt in ('--port', '-p'):
                port = arg
            elif opt in ('--item', '-i'):
                item = arg
            elif opt in ('--help'):
                usage()
            else:
                assert False
    except:
        usage()
    try:
        raw_stats = get_memcached_stats(host, port)
        stats = parse_memcached_stats(raw_stats)
        print stats[item]
    except:
        print 'FAILED: Invalid item'

def usage():
    print 'Usage: memcached-stat.py -h localhost -p 11211 -i <item>'
    sys.exit(2)

if __name__ == '__main__':
    main(MEMCACHED_SERVER, MEMCACHED_PORT)
