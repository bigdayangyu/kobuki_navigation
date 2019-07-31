import os
from ament_index_python.packages import get_package_share_directory
import launch
import launch.action
import launch_ros.actions
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    kobuki_navigation_path = get_package_share_directory('kobuki_navigation')
    cartographer_config_path = os.path.join(kobuki_navigation_path, 'configuration_files')
    urg_node_path = get_package_share_directory('urg_node')
    rviz_config = os.path.join(kobuki_navigation_path, 'rviz', 'kobuki_carto_demo.rviz')

    kobuki_urdf = os.path.join(kobuki_navigation_path,'urdf', 'kobuki_carto.urdf')
    publish_period_sec = LaunchConfiguration('publish_period_sec', default='1.0')

    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package="turtlebot2_drivers",   
            node_executable="kobuki_node",
            node_name="kobuki_node", 
            output="screen"),

         launch_ros.actions.Node(
            package="urg_node",
            node_executable="urg_node",
            output="screen",
            arguments=["__params:="+ urg_node_path+ "/launch/urg_node.yaml"],
            on_exit=launch.actions.Shutdown()),
                
        launch_ros.actions.Node(
            package="tf2_ros",
            node_executable="static_transform_publisher",
            arguments=['0','0', '0.161', '0','0','0','1', 'base_link', 'laser']
            ),

        launch.actions.DeclareLaunchArgument(
            'publish_period_sec',
            default_value=publish_period_sec,
            description='OccupancyGrid publishing period'),

        launch_ros.actions.Node(
            package="robot_state_publisher",
            node_executable='robot_state_publisher',
            output='screen',
            arguments=[kobuki_urdf]),

        launch_ros.actions.Node(
            package="rviz2",
            node_executable="rviz2",
            arguments=['-d',rviz_config]
            ),

        launch_ros.actions.Node(
            package="cartographer_ros",
            node_executable="cartographer_node",
            output="screen",
            arguments=["-configuration_directory" , cartographer_config_path ,
            "-configuration_basename", "kobuki_2d.lua"],            
            on_exit=launch.actions.Shutdown()),

        launch_ros.actions.Node(
            package="cartographer_ros",
            node_executable="occupancy_grid_node",
            output="screen",
            arguments=["-resolution", "0.05", '-publish_period_sec', publish_period_sec],
            on_exit=launch.actions.Shutdown())

    ])
