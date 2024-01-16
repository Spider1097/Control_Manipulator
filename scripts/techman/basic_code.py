#!/usr/bin/env python3

import asyncio
import techmanpy
import rospy
import numpy as np
import signal
import time

class ArmControl:
	def __init__(self):
		
		self.ip = "192.168.1.5" 
		
		
async def move_to_point(move_axis_vec):
	async with techmanpy.connect_sct(robot_ip=ac.ip) as conn:
		conn.add_broadcast_callback(print)
		await conn.move_to_joint_angles_ptp(move_axis_vec, 0.5, 10)
		await conn.set_queue_tag(1)
		
ac=ArmControl()

while(1):
	asyncio.run(move_to_point([-137.0399, 11.47041, 98.60066, -90, 90, 0]))
	asyncio.run(move_to_point([-175.2401, -6.009818, 151.7819, -90, 90, 0]))
	asyncio.run(move_to_point([-135, 0, 0, -90, 90, 0]))
	asyncio.run(move_to_point([-135, 0, 90, -90, 90, 0]))
	break
