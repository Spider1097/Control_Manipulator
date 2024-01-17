# Control_Manipulator
ROS package for manipulator control.

![image](https://github.com/Spider1097/Control_Manipulator/assets/118929720/c5cbea40-7921-4aed-b6d4-52114f4a535a)

## A Set up drone workspace
First of all, we need to manipulator a workspace.

```
mkdir -p ~/manipulator/src
cd manipulator/src/
git clone https://github.com/Spider1097/Control_Manipulator.git
cd manipulator/
catkin_make
source devel/setup.bash
```

## Run basic code for moveit robot(panda)
  ```
  rosrun manipulator pick_and_place.py 
 ```
  ![image](https://github.com/Spider1097/Control_Manipulator/assets/118929720/f6377581-e447-430d-9a58-63489772e487)

## Run basic code for techman
```
  rosrun manipulator basic_code.py 
 ```
image

Additionally, you have the option to test it using simulation in Python.

 ```
 cd manipulator/src/manipulator/scripts/techman/
 python3 techman_simulation.py
 python3 techman_simulation_move.py
 ```

![techman_base](https://github.com/Spider1097/Control_Manipulator/assets/118929720/00066829-2323-42ae-94dd-224078187807)


