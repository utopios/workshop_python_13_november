import asyncio

async def send(data:str, port:int):
    reader, writer = await asyncio.open_connection('localhost', port=port)
    writer.write(data.encode())
    await writer.drain()

    data = await reader.read(1024)
    print("Server response:", data.decode())
    writer.close()

asyncio.run(send("ihab abadi", 8082))