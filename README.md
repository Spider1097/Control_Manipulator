# Control_Manipulator.
ROS package for manipulator control.

![image](https://github.com/Spider1097/Control_Manipulator/assets/118929720/c5cbea40-7921-4aed-b6d4-52114f4a535a)

## A Set up manipulator workspace.
First of all, we need to manipulator a workspace.

```
mkdir -p ~/manipulator_ws/src
cd manipulator_ws/src/
git clone https://github.com/Spider1097/Control_Manipulator.git
cd manipulator_ws/
catkin_make
source devel/setup.bash
```

## Run basic code for moveit robot(panda).
How to install moveit you can find here: " https://ros-planning.github.io/moveit_tutorials/doc/getting_started/getting_started.html ".
  ```
  roslaunch panda_moveit_config demo.launch

  rosrun manipulator pick_and_place.py 
 ```
  ![image](https://github.com/Spider1097/Control_Manipulator/assets/118929720/f6377581-e447-430d-9a58-63489772e487)

## Run basic code for TechmanTM12.
before run this code you must change in code an IP addres and check if you have contact with robot. 
Here you can find information how to do that: " https://github.com/TechmanRobotInc/tmr_ros1 ".
```
 rosrun manipulator basic_code.py 
 ```

https://github.com/Spider1097/Control_Manipulator/assets/118929720/558fd9ed-ddbe-48bb-8090-a9a7493d7bf1

Additionally, you have the option to test it using simulation in Python or Rviz.
For this you need to install the roboticstoolbox. " https://github.com/petercorke/robotics-toolbox-python ".
 ```
 cd manipulator_ws/src/manipulator/scripts/techman/
 python3 techman_simulation.py
 python3 techman_simulation_move.py
 ```

![techman_base](https://github.com/Spider1097/Control_Manipulator/assets/118929720/00066829-2323-42ae-94dd-224078187807)

Download a package containing URDF files, select the necessary URDF model, and place the package in your workspace.
 ```
git clone https://github.com/Spider1097/URDF_models.git
 ```
Your workspace will look like whis: 

![image](https://github.com/Spider1097/Control_Manipulator/assets/118929720/0f4dde37-d60b-495d-b9ff-b558617da5ca)

 ```
 cd manipulator_ws/
 catkin_make

 roslaunch techman3 demo.launch
 ```
![image](https://github.com/Spider1097/URDF_models/assets/118929720/07c23f55-5a6b-4783-96d9-78d984147499)


