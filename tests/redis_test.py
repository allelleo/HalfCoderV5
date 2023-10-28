import aioredis


async def test_first():
    redis = await aioredis.from_url('redis://localhost:6379')
    await redis.set("foo1", "bar")
    if (await redis.get('foo1')).decode('utf-8') == "bar":
        print("[ Redis ] : OK")
    else:
        print("[ Redis ] : NO")

def test():
    import asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(test_first())
