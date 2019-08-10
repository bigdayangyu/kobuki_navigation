# kobuki ROS 2 demo 
## Install Dependencie

```bash
git clone https://github.com/bigdayangyu/kobuki_navigation.git
vcs import src <kobuki_demo.repos
```
## kobuki Robot
### kobuki bring up 
* Launch the kobuki robot by exicuting the `kobuki_node.cpp`
* bring up the hukoyo laser scanner by calling the `urg_node`
* launch robot urdf description for static transformations of the robot
```bash
ros2 launch kobuki_navigation kobuki_bringup.launch.py 
```

### Kobuki Docking 
When the kobuki robot reaches the docking station, and the front bumper is in contact with the charging station for 5 seconds, the bumper trigger will send out a message through the `bumper_event` topic to let other node know that kobuki has reached the docking station. 

```bash
ros2 run kobuki_navigation bumper_trigger
```

### Launch the kobuki cartographer demo in ROS2
* launch turtlebo2_driver with kobuki_node
* urg_node laser scan
* Set up tf transformation from base_link to laser 
* launch rviz2 for visualization
* launch `cartographer_node` and `occupancy_grid_node`
```bash
ros2 launch kobuki_navigation kobuki_demo.launch.py 
```

### Control the robot
```bash 
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
### Save the map
```bash
ros2 run nav2_map_server map_saver -f ~/map_name 
```
## Gazebo Simulation
### Bring up the robot in Gazebo simulation 
```bash 

ros2 launch kobuki_gazebo_demo kobuki_empty_world.launch.py use_sim_time:=True # load a empty world with the robot 

ros2 launch kobuki_gazebo_demo kobuki_SYV_office.launch.py use_sim_time:=True   # simulation of the SYV office 

ros2 launch kobuki_gazebo_demo kobuki_obstacle.launch.py use_sim_time:=True # load robot and small obstacles 
```
### Run cartographer in simulation 
```bash
ros2 launch kobuki_navigation kobuki_gazebo_carto.launch.py use_sim_time:=True
```
## Navigation stack for ROS2
* If runing in simulation, set the `use_sim_time` to be `True` 
* Set the PATH to the saved map
* Click the `2D Pose Esitimation` to set the initial pose of the robot
* Click `Navigation2 goal` to set the goal point of the robot
* Click start to navigate
```bash
ros2 launch kobuki_navigation kobuki_nav2_map.launch.py use_sim_time:=false map:=/PATH/map.yaml autostart:=True
```
TODO dependencies 