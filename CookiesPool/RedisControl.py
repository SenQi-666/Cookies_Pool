from conf import Settings
import random
import redis


class RedisClient:
    def __init__(self, website, kind):
        self.conn = redis.StrictRedis(
            host=Settings.REDIS_HOST, port=Settings.REDIS_PORT, password=Settings.REDIS_PASSWORD, decode_responses=True
        )
        self.website = website
        self.kind = kind

    def name(self):
        return '%s_%s' % (self.website, self.kind)

    def set(self, usr, val):
        return self.conn.hset(self.name(), usr, val)

    def get(self, usr):
        return self.conn.hget(self.name(), usr)

    def delete(self, usr):
        return self.conn.hdel(self.name(), usr)

    def random(self):
        return random.choice(self.conn.hvals(self.name()))
    
    def count(self):
        return self.db.hlen(self.name())
    
    def all_usr(self):
        return self.conn.hkeys(self.name())

    def all(self):
        return self.conn.hgetall(self.name())
