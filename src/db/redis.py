from src.config import Config
import redis.asyncio as aioredis

JTI_EXPIRY = 3600

token_blocklist = aioredis.from_url(
    Config.REDIS_URL
)

async def add_token_to_blocklist(jti: str) -> None:
    await token_blocklist.set(name=jti, ex=JTI_EXPIRY, value="blocked")


async def is_token_in_blocklist(jti: str) -> bool:
    result = await token_blocklist.get(jti)
    return result is not None