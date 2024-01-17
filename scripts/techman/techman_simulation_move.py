#%%
import numpy as np
import roboticstoolbox as rtb
from math import pi
import time

from spatialmath import *

import techmanpy
import asyncio

L1 = rtb.DHLink(theta=0.0, d=0.1652, a=0, alpha=pi/2, offset=pi)
L2 = rtb.DHLink(theta=0.0, d=0.18, a=0.6361, alpha=0, offset=pi/2) 
L3 = rtb.DHLink(theta=0.0, d=0.1297, a=0.5579, alpha=-pi)
L4 = rtb.DHLink(theta=0.0, d=0.106, a=0.0, alpha=-pi/2, offset=-pi/2)
L5 = rtb.DHLink(theta=0.0, d=0.106, a=0.0, alpha=pi/2)
L6 = rtb.DHLink(theta=0.0, d=0.113, a=0.0, alpha=0)

robot = rtb.DHRobot([L1, L2, L3, L4, L5, L6])

robot.plot([0.0, 0.0, 0.0, 0.0, 0.0, 0.0],movie='techman0.gif')

print(robot.fkine([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]))

trans = SE3(0.3, 0.1, 1.4)

y_rot = [0,0,1]
z_rot = [0,-1,0]
rot = SE3.OA(y_rot, z_rot)

T = trans * rot
mask = np.array([1, 1, 1, 0, 0, 0])
q0 = np.array([0.0, 0.0,0.0,0.0,0.0,0.0])
sol = robot.ikine_LM(T,q0=q0, mask=mask)

print(sol.q)
sol_degrees = np.rad2deg(sol.q)
print(sol_degrees)

print(robot.fkine(sol.q))
print(robot.fkine(sol_degrees))
 
robot.plot(sol.q, block=False, movie='techman1.gif')

time.sleep(1)

# %%


