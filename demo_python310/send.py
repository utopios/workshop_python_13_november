import asyncio

async def send(data:str):
    reader, writer = await asyncio.open_connection('localhost', 8083)
    writer.write(data.encode())
    await writer.drain()

    data = await reader.read(1024)
    print("Server response:", data.decode())
    writer.close()

test_profiles = [
    {"role": "admin", "name": "Alice"},
    {"role": "member", "name": "Bob", "subscription_status": True},
    {"role": "member", "name": "Charlie", "subscription_status": False},
    {"role": "guest", "name": "David"},
    {"role": "unknown", "name": "Eve"},
    None
]

async def main():
    for profile in test_profiles:
        await send(str(profile))

asyncio.run(main())