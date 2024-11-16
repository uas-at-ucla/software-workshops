#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def run():
    # Define drone and connect to it
    drone = System()
    await drone.connect(system_address="udp://:14540")

    # Wait for connection
    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("-- Connected to drone!")
            break
    """
    Rest of routine is up to you.
    """

if __name__ == "__main__":
    asyncio.run(run())
