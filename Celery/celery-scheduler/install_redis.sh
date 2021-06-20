#!/bin/bash
# This script downloads redis-server
# if redis has not already been downloaded

if [ ! -d redis-6.2.4/src ]; then
    wget http://download.redis.io/releases/redis-6.2.4.tar.gz
    tar xzf redis-6.2.4.tar.gz
    rm redis-6.2.4.tar.gz
    cd redis-6.2.4
    make
else
    cd redis-6.2.4
fi