

import asyncio
import random

async def download_file(file_name: str):
    """Simulates downloading a file asynchronously."""
    print(f"Starting download: {file_name}")

    download_time = random.randint(1, 5)
    await asyncio.sleep(download_time)
    print(f"Finished downloading {file_name} in {download_time} seconds")
    return file_name

async def main():
    
    files = [f"file_{i}.txt" for i in range(1, 6)]

    print("Simulating concurrent file downloads...\n")

    
    tasks = [asyncio.create_task(download_file(f)) for f in files]

    
    results = await asyncio.gather(*tasks)

    print("\nAll downloads completed:", results)

if __name__ == "__main__":
    asyncio.run(main())
