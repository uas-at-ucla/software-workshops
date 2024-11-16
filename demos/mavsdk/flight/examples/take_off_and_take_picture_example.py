import asyncio
import os
from mavsdk import System
from camera import Video
from mavsdk.gimbal import (GimbalMode, ControlMode)
import cv2

async def run():
    drone = System()
    camera = Video()
    offset = {}
    await drone.connect(system_address="udp://:14540")
    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break



    altitude = 1.5
    print(f"Setting takeoff altitude to {altitude} m")

    print("Arming drone...")
    await drone.action.arm()

    await drone.action.takeoff()

    await asyncio.sleep(10)
    
    print("Pointing camera gimbal straight down")
    await drone.gimbal.take_control(ControlMode.PRIMARY)
    await drone.gimbal.set_mode(GimbalMode.YAW_LOCK)
    await drone.gimbal.set_pitch_and_yaw(-90,0)
    await asyncio.sleep(5)

    print("Taking photo")
    frame = camera.frame()
    image_location = '../images/image.jpg'
    cv2.imwrite(image_location, frame)

    await drone.action.land()

if __name__ == "__main__":
    asyncio.run(run())

