# -*- coding:  UTF-8 -*-

import redis
from configs.redis import *


class REDIS:
    def __init__(self):
        config = get_local_redis_config()
        self.r = redis.Redis(host=config["host"], port=config["port"], password=config["password"])

    def __enter__(self):
        return self.r

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.r.close()
