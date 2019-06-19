### launch the kobuki node in ROS2
launch turtlebo2_driver with kobuki_node, urg_node laser scan
Set up tf transformation from base_link to laser 
launch rviz to visualize the laser scan
```bash
 ros2 launch kobuki_navigation kobuki_nav.launch.py
```