#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def point_gimbal_down():
    print("Pointing camera gimbal straight down")
    await drone.gimbal.take_control(ControlMode.PRIMARY)
    await drone.gimbal.set_mode(GimbalMode.YAW_LOCK)
    await drone.gimbal.set_pitch_and_yaw(-90,0)
    await asyncio.sleep(5)

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
