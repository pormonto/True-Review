import asyncio

from hume import HumeStreamClient
from hume.models.config import FaceConfig, ProsodyConfig

samples = [
    "/Users/jetlin/Desktop/CalHacks/humeai/HumeReactionsCompressed/HumeReactions1compress.mp4",
    "/Users/jetlin/Desktop/CalHacks/humeai/HumeReactionsCompressed/HumeReactions2compress.mp4",
    "/Users/jetlin/Desktop/CalHacks/humeai/HumeReactionsCompressed/HumeReactions3compress.mp4"
]

async def main():
    client = HumeStreamClient("y7wUAPHS6ihjAyZsZwp4AN8EZtTFtyIfGnKJR4nRwhwLprDa")
    configs = [FaceConfig(identify_faces=True), ProsodyConfig()]
    async with client.connect(configs) as socket:
        for sample in samples:
            result = await socket.send_file(sample)
            emotions = result["language"]["predictions"][0]["emotions"]
            print(emotions)

asyncio.run(main())