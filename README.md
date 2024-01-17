# Control_Manipulator
ROS package for manipulator control.

![image](https://github.com/Spider1097/Control_Manipulator/assets/118929720/c5cbea40-7921-4aed-b6d4-52114f4a535a)

## A Set up drone workspace
First of all, we need to create a workspace.

```
mkdir -p ~/manipulator/src
cd manipulator/src/
catkin_create_pkg manipulator std_msgs rospy roscpp sensor_msgs
catkin_make
cd manipulator/
source devel/setup.bash
```
