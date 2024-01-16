#!/usr/bin/env python3
import numpy as np
import roboticstoolbox as rtb
from math import pi
import time

from spatialmath import *

import techmanpy
import asyncio

L1 = rtb.DHLink(theta=0.0, d=0.1652, a=0, alpha=pi/2)
L2 = rtb.DHLink(theta=0.0, d=0.18, a=0.6361, alpha=pi, offset=pi/2)
L3 = rtb.DHLink(theta=0.0, d=0.1297, a=0.5579, alpha=-pi)
L4 = rtb.DHLink(theta=0.0, d=0.106, a=0.0, alpha=-pi/2, offset=-pi/2)
L5 = rtb.DHLink(theta=0.0, d=0.106, a=0.0, alpha=pi/2)
L6 = rtb.DHLink(theta=0.0, d=0.11315, a=0.0, alpha=0)
robot = rtb.DHRobot([L1, L2, L3, L4, L5, L6])

position_manipulator=[]

class manipulator:
    def __init__(self):
        self.count = 0
     
    def set_position(self,x,y,z):
        global pose_save
        print(robot.fkine([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]))
        print("----------------------------------")
        trans = SE3(x, y, z)
        y_rot = [0,0,1]
        z_rot = [0,-1,0]
        rot = SE3.OA(y_rot, z_rot)
        T = trans * rot
        print("-------------------------------------")
        mask = np.array([1, 1, 1, 0, 0, 0])
        
        if self.count==1:
            q0=pose_save
        elif self.count == 0:
            q0=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            self.count=1

        sol = robot.ikine_LM(T, q0=q0,mask=mask)
        print(sol)
        pose_save=sol.q
        
        sol_degrees=np.rad2deg(sol.q)
  	    
        print("solving degrees:")
        print(sol_degrees)
        print("solving radian:")
        print(sol.q)
        return(sol_degrees)
		
manipulator1=manipulator()
ip="192.168.1.2"

async def move_to_point(move_axis_vec):
	async with techmanpy.connect_sct(robot_ip=ip) as conn:
		conn.add_broadcast_callback(print)
		await conn.move_to_joint_angles_ptp(move_axis_vec, 0.5, 10)#
		await conn.set_queue_tag(1)

while(1):
    val1 = float(input("Enter x: "))
    val2 = float(input("Enter y: "))
    val3 = float(input("Enter z: "))
    solution_kinematiok=manipulator1.set_position(val1, val2, val3)
    
    enter = input("Enter press: ")
    asyncio.run(move_to_point(solution_kinematiok))
    position_manipulator=[]
	
    

