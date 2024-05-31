import aiohttp
import asyncio
import matplotlib.pyplot as plt
from collections import Counter

# Define the endpoints of the servers
SERVERS = [
    'http://localhost:5001/home',
    'http://localhost:5002/home',
    'http://localhost:5003/home'
]

# Number of requests to send
NUM_REQUESTS = 10000

# Asynchronous function to send a request
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

# Asynchronous function to send multiple requests
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(NUM_REQUESTS):
            url = SERVERS[i % len(SERVERS)]
            tasks.append(fetch(session, url))

        responses = await asyncio.gather(*tasks)

        # Count responses from each server
        counter = Counter(response['message'] for response in responses)

        # Print the counts
        for server, count in counter.items():
            print(f'{server}: {count}')

        # Plot the results in a bar chart
        labels = [f'Server {i+1}' for i in range(len(SERVERS))]
        values = [counter.get(f"Hello from Server: {i+1}", 0) for i in
range(len(SERVERS))]

        plt.bar(labels, values)
        plt.xlabel('Server Instance')
        plt.ylabel('Number of Requests Handled')
        plt.title('Request Count Handled by Each Server Instance')
        plt.show()

# Run the main function
asyncio.run(main())
