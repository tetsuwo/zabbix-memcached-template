# Memcached Stats Templates for Zabbix

This Zabbix template is template for resource monitoring of Memcached.  
In this example the settings path of zabbix is `/etc/zabbix/`.


### Setting zabbix agent side

Setting config file.

    $ curl https://raw.githubusercontent.com/tetsuwo/zabbix-memcached-template/master/src/zabbix_agentd.d/userparameter_memcached.conf > /etc/zabbix/zabbix_agentd.d/userparameter_memcached.conf

Setting script file.

    $ curl https://raw.githubusercontent.com/tetsuwo/zabbix-memcached-template/master/src/bin/memcached-stat.py > /etc/zabbix/bin/memcached-stat.py
    $ sudo chown zabbix:zabbix /etc/zabbix/bin/memcached-stat.py
    $ sudo chmod +x /etc/zabbix/bin/memcached-stat.py

Restart `zabbix-agent`.

    $ sudo service zabbix-agent restart

Test with `zabbix_agentd`.

    $ zabbix_agentd -t memcached.stat[--host,localhost,--port,11211,--item,version]
    memcached.stat[--host,localhost,--port,11211,--item,version] [t|1.4.13]


### Setting zabbix server side

Macro 

- {$MEMCACHED_HOST} ... host for memcached reference from agent 
- {$MEMCACHED_PORT} ... port for memcached reference from agent 



