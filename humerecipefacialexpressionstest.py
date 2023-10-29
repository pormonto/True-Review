import asyncio

from hume import HumeStreamClient, StreamSocket
from hume.models.config import FaceConfig


async def main():
    client = HumeStreamClient("y7wUAPHS6ihjAyZsZwp4AN8EZtTFtyIfGnKJR4nRwhwLprDa")
    config = FaceConfig(identify_faces=True)
    async with client.connect([config]) as socket:
        result = await socket.send_file("./mossman.JPG")
        print(result)

asyncio.run(main())