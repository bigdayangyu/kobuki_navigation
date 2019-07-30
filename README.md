# kobuki ROS 2 demo 
## kobuki Robot
### kobuki bring up 
* Launch the kobuki robot by exicuting the `kobuki_node.cpp`
* bring up the hukoyo laser scanner by calling the `urg_node`
* launch robot urdf description for static transformations of the robot
```bash
ros2 launch kobuki_navigation kobuki_bringup.launch.py 
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

### Bring up the robot in Gazebo simulation 
```bash 

ros2 launch kobuki_gazebo_demokobuki_empty_world.launch.py use_sim_time:=True # load a empty world with the robot 

ros2 launch kobuki_gazebo_demo kobuki_SYV_office.launch.py
use_sim_time:=True   # simulation of the SYV office 

ros2 launch kobuki_gazebo_demo kobuki_obstacle.launch.py 
	use_sim_time:=True # load robot and small obstacles 
```
### Run cartographer in simulation 
```bash
ros2 launch kobuki_navigation kobuki_gazebo_carto.launch.py use_sim_time:=True
```
TODO dependencies 