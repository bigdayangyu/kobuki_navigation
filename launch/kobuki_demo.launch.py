import os

from ament_index_python.packages import get_package_share_directory
import launch
import launch_ros.actions


from launch.substitutions import LaunchConfiguration
def generate_launch_description():
    kobuki_navigation_prefix = get_package_share_directory('kobuki_navigation')
    cartographer_ros_prefix = get_package_share_directory('cartographer_ros')

    cartographer_config_dir = os.path.join(cartographer_ros_prefix, 'configuration_files')
    urg_node_prefix = get_package_share_directory('urg_node')
    rviz_config = os.path.join(kobuki_navigation_prefix, 'include', 'kobuki_demo.rviz')

    kobuki_urdf = os.path.join(kobuki_navigation_prefix,'urdf', 'kobuki_carto.urdf')

    carto_demo_urdf = os.path.join(kobuki_navigation_prefix, 'urdf', 'backpack_2d.urdf')

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    publish_period_sec = LaunchConfiguration('publish_period_sec', default='1.0')


    return launch.LaunchDescription([
        # launch_ros.actions.Node(
        #     package="turtlebot2_drivers",   
        #     node_executable="kobuki_node",
        #     node_name="kobuki_node", 
        #     output="screen"),

        #  launch_ros.actions.Node(
        #     package="urg_node",
        #     node_executable="urg_node",
        #     output="screen",
        #     arguments=["__params:="+ urg_node_prefix+ "/launch/urg_node.yaml"],
            # on_exit=launch.actions.Shutdown()),
                
        # launch_ros.actions.Node(
        #     package="tf2_ros",
        #     node_executable="static_transform_publisher",
        #     arguments=['0.1','0', '0', '0','0','0','1', 'base_link', 'laser']
        #     ),

        # DeclareLaunchArgument(
        #     'publish_period_sec',
        #     default_value=publish_period_sec,
        #     description='OccupancyGrid publishing period'),




        # launch_ros.actions.Node(
        #     package="robot_state_publisher",
        #     node_executable='robot_state_publisher',
        #     output='screen',
        #     arguments=[carto_demo_urdf]),

        # launch_ros.actions.Node(
        #     package="rviz2",
        #     node_executable="rviz2",
        #     arguments=['-d',rviz_config]
        #     ),

        launch_ros.actions.Node(
            package="cartographer_ros",
            node_executable="cartographer_node",
            output="screen",
            arguments=["-configuration_directory" , cartographer_config_dir ,
            "-configuration_basename", "backpack_2d.lua"],            
            on_exit=launch.actions.Shutdown()),

        launch_ros.actions.Node(
            package="cartographer_ros",
            node_executable="occupancy_grid_node",
            output="screen",
            arguments=["-resolution", "0.05", '-publish_period_sec', publish_period_sec],
            on_exit=launch.actions.Shutdown())


    ])
