import os
import launch.actions
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription




def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    kobuki_navigation_path = get_package_share_directory('kobuki_navigation')
    urg_node_prefix = get_package_share_directory('urg_node')
    kobuki_urdf = os.path.join(kobuki_navigation_path,'urdf', 'kobuki_carto.urdf')

    return LaunchDescription([
        DeclareLaunchArgument(
           'use_sim_time', 
           default_value='false',
           description='Use simulation (Gazebo) clock if true'),
        Node(
            package="turtlebot2_drivers",   
            node_executable="kobuki_node",
            node_name="kobuki_node", 
            output="screen"),

        Node(
            package="urg_node",
            node_executable="urg_node",
            output="screen",
            arguments=["__params:="+ urg_node_prefix+ "/launch/urg_node.yaml"],
            on_exit=launch.actions.Shutdown()),

        Node(
            package="tf2_ros",
            node_executable="static_transform_publisher",
            node_name="static_transform_publisher",
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=['-0.020','0', '0.161', '0','0','0','1', 'base_link', 'laser']
            ),

        Node(
            package='robot_state_publisher',
            node_executable='robot_state_publisher',
            node_name="robot_state_publisher",
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
			      arguments=[kobuki_urdf])
])