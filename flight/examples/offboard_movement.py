#!/usr/bin/env python3
# Basic move routine using offboard

import asyncio
from mavsdk import System
from mavsdk.offboard import (VelocityBodyYawspeed)


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

        # Zero velocity position
        await drone.offboard.set_velocity_body(
            VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0)
        )

    # Try to arm and exit if unable
    try:
        print("Arming...")
        await drone.action.arm()

    except Exception as error:
        print(f"Unable to arm, not ready: {error}")
        return

    try:
        # Attempt to start offboard
        await drone.offboard.start()

        # Set velocity to upwards
        await drone.offboard.set_velocity_body(
            VelocityBodyYawspeed(0.0, 0.0, -1.0, 0.0)
        )

        print("Taking off upwards...")
        await asyncio.sleep(15)

        # Hover
        await drone.offboard.set_velocity_body(
            VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0)
        )

        await asyncio.sleep(10)

        # Fly in a circle
        print("Flying in a circle...")
        await drone.offboard.set_velocity_body(
            VelocityBodyYawspeed(5.0, 0.0, 0.0, 30.0)
        )

        await asyncio.sleep(15)

        # Stop drone
        await drone.offboard.set_velocity_body(
            VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0)
        )

    except Exception as error:
        print(f"Exception: {error}")

    # Land
    await drone.action.land()

if __name__ == "__main__":
    asyncio.run(run())
