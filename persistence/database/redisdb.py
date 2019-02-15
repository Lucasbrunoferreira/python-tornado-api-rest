from logzero import logger

import redis
import settings


class RedisDb:
    redis_client: None

    def __init__(self):
        try:
            self.redis_client = redis.Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                password=settings.REDIS_PASS,
                db=0)
        except Exception as ex:
            logger.error(ex)
            raise ex
        else:
            pass

    def get_data(self, key):
        try:
            redis_data = self.redis_client.get(key)
        except Exception as ex:
            logger.error(ex)
            raise ex
        else:
            if redis_data is not None:
                return redis_data.decode('utf-8')
            else:
                return None

    def set_data(self, key, data, time):
        try:
            self.redis_client.set(key, str(data).encode('utf-8'), time)
        except Exception as ex:
            logger.error(ex)
            raise ex
        else:
            pass

    def delete_data(self, key):
        try:
            self.redis_client.delete(key)
        except Exception as ex:
            logger.error(ex)
            raise ex
        else:
            pass
