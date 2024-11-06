# Take off and land routine
import asyncio
from mavsdk import System
#!/usr/bin/env python3

async def run():
    # Define drone and connect to it
    drone = System()
    await drone.connect(system_address="udp://:14540")

    # Wait for connection
    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    # Set takeoff altitude to 5 meters
    await drone.action.set_takeoff_altitude(5)

    # Arm drone
    try:
        print("Arming...")
        await drone.action.arm()

    except Exception as e:
        print(f"Failed to arm: {e}")

    try:
        # Takeoff
        print("Taking off...")
        await drone.action.takeoff()

        # Hover for some time
        await asyncio.sleep(10)


    except Exception as e:
        print(f"Exception: {e}")

    # Land
    await drone.action.land()

if __name__ == "__main__":
    asyncio.run(run())
