import aioredis

from application.settings import get_settings


redis_url = get_settings().redis_url
redis = aioredis.from_url(redis_url, encoding="utf-8", decode_responses=True)


async def get_redis():
    async with redis.client() as conn:
        try:
            yield conn
        except Exception as exc:
            # TODO logger
            pass
