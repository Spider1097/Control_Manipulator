
# %%
import numpy as np
import roboticstoolbox as rtb
from spatialmath import *
from math import pi
import matplotlib.pyplot as plt
from matplotlib import cm
np.set_printoptions(linewidth=100, formatter={'float': lambda x: f"{x:8.4g}" if abs(x) > 1e-10 else f"{0:8.4g}"})

L1 = rtb.DHLink(theta=0.0, d=0.1652, a=0, alpha=pi/2, offset=pi)
L2 = rtb.DHLink(theta=0.0, d=0.18, a=0.6361, alpha=0, offset=pi/2) 
L3 = rtb.DHLink(theta=0.0, d=0.1297, a=0.5579, alpha=-pi)
L4 = rtb.DHLink(theta=0.0, d=0.106, a=0.0, alpha=-pi/2, offset=-pi/2)
L5 = rtb.DHLink(theta=0.0, d=0.106, a=0.0, alpha=pi/2)
L6 = rtb.DHLink(theta=0.0, d=0.113, a=0.0, alpha=0)

robot = rtb.DHRobot([L1,L2,L3,L4,L5,L6])

robot.plot([0.0, 0.0, 0.0, 0.0, 0.0, 0.0],movie='techman_base.gif')

print(robot.fkine([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]))

# %%


