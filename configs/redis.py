#!/usr/bin/python3
# redis配置


def get_local_redis_config():
    redis = {
        "host": "127.0.0.1",
        "port": 6379,
        "password": ""
    }
    return redis