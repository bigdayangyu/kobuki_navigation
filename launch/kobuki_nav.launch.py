import os
import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    kobuki_navigation_prefix = get_package_share_directory('kobuki_navigation')
    cartographer_config_dir = os.path.join(kobuki_navigation_prefix, 'configuration_files')
    urg_node_prefix = get_package_share_directory('urg_node')
    
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package="turtlebot2_drivers",   
            node_executable="kobuki_node",
            node_name="kobuki_node", 
            output="screen"),

        launch_ros.actions.Node(
            package="cartographer_ros",
            node_executable="cartographer_node",
            output="screen",
            arguments=["-configuration_directory" , cartographer_config_dir ,
            "-configuration_basename", "kobuki_2d.lua"],            
            on_exit=launch.actions.Shutdown()),

        launch_ros.actions.Node(
            package="urg_node",
            node_executable="urg_node",
            output="screen",
            arguments=["__params:="+ urg_node_prefix+ "/launch/urg_node.yaml"],
            on_exit=launch.actions.Shutdown()),

        launch_ros.actions.Node(
            package="cartographer_ros",
            node_executable="occupancy_grid_node",
            output="screen",
            arguments=["-resolution", "0.05"],
            on_exit=launch.actions.Shutdown())
    ])