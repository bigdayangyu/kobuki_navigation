import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
	use_sim_time = LaunchConfiguration('use_sim_time', default='false')
	kobuki_nav_prefix = get_package_share_directory('kobuki_navigation')
	kobuki_urdf = os.path.join(kobuki_nav_prefix,'urdf', 'kobuki_carto.urdf')
	return LaunchDescription([
        DeclareLaunchArgument(
           'use_sim_time', 
           default_value='true',
           description='Use simulation (Gazebo) clock if true'),

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