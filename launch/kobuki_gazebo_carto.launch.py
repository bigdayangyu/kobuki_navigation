import os

from ament_index_python.packages import get_package_share_directory
import launch


from launch.actions import DeclareLaunchArgument
from launch.actions import ExecuteProcess
from launch_ros.actions import Node 

from launch.substitutions import LaunchConfiguration
def generate_launch_description():
    kobuki_navigation_prefix = get_package_share_directory('kobuki_navigation')
    
    cartographer_config_dir = os.path.join(kobuki_navigation_prefix, 'configuration_files')

    rviz_config = os.path.join(kobuki_navigation_prefix, 'rviz', 'kobuki_carto_demo.rviz')

    kobuki_urdf = os.path.join(kobuki_navigation_prefix,'urdf', 'kobuki_gazebo_cato.urdf')

    use_sim_time = LaunchConfiguration('use_sim_time', default='True')
    publish_period_sec = LaunchConfiguration('publish_period_sec', default='1.0')


    return launch.LaunchDescription([

        # launch_ros.actions.Node(
        #     package="tf2_ros",
        #     node_executable="static_transform_publisher",
        #     arguments=['0.1','0', '0', '0','0','0','1', 'base_link', 'laser']
        #     ),

        # DeclareLaunchArgument(
        #     'publish_period_sec',
        #     default_value=publish_period_sec,
        # #     description='OccupancyGrid publishing period'),
  
        DeclareLaunchArgument(
           'use_sim_time', 
           default_value='True',
           description='Use simulation (Gazebo) clock if true'),

        Node(
            package="cartographer_ros",
            node_executable="cartographer_node",
            output='screen',
            arguments=["-configuration_directory" , cartographer_config_dir ,
            "-configuration_basename", "kobuki_gazebo_2d.lua"],         
            on_exit=launch.actions.Shutdown()),

        ExecuteProcess(
            cmd=['ros2', 'param', 'set', '/cartographer_node', 'use_sim_time', use_sim_time],
            output='screen'),

        Node(
            package="cartographer_ros",
            node_executable="occupancy_grid_node",
            output="screen",
            arguments=["-resolution", "0.05", '-publish_period_sec', publish_period_sec],
            on_exit=launch.actions.Shutdown()),

        ExecuteProcess(
            cmd=['ros2', 'param', 'set', '/cartographer_occupancy_grid_node', 'use_sim_time', use_sim_time],
            output='screen'),

        Node(
            package="rviz2",
            node_executable="rviz2",
            arguments=['-d',rviz_config]
            ),
    ])
