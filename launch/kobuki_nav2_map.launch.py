import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch.actions import ExecuteProcess


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='True')
    kobuki_navigation_path = get_package_share_directory('kobuki_navigation')
    map_path = LaunchConfiguration('map', 
                                default=os.path.join(kobuki_navigation_path, 'map', 'map.yaml'))
    param_path = LaunchConfiguration('params', 
                                default=os.path.join(kobuki_navigation_path, 'param', 'kobuki_nav.yaml'))
    
    nav2_launch_file_path = os.path.join(get_package_share_directory('nav2_bringup'), 'launch')

    # rviz_config_dir = os.path.join(get_package_share_directory('nav2_bringup'), 'launch', 'nav2_default_view.rviz')

    return LaunchDescription([
        DeclareLaunchArgument(
            'map', 
            default_value=map_path,
            description='Full path to map file to load'),

        DeclareLaunchArgument(
            'params', 
            default_value=param_path,
            description='Full path to param file to load'),

        DeclareLaunchArgument(
            'use_sim_time', 
            default_value='True', 
            description='Use simulation (Gazebo) clock if true'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([nav2_launch_file_path, '/nav2_bringup_launch.py']),
            launch_arguments={'map': map_path, 'use_sim_time': use_sim_time, 'params': param_path}.items(),
        ),

        # Node(
        #     package='rviz2',
        #     node_executable='rviz2',
        #     node_name='rviz2',
        #     arguments=['-d', rviz_config_dir],
        #     output='screen'),
    ])