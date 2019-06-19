#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import launch
import launch_ros.actions

def main():
    launch_description = launch.LaunchDescription()
    launch_description.add_action(
        launch_ros.actions.Node(
            package='urg_node',
            node_name="urg_node_node",
            node_executable="urg_node",
            output='screen',
        )
    )
    ls = launch.LaunchService()
    ls.include_launch_description(
        launch_ros.get_default_launch_description(
            prefix_output_with_name=False
        )
    )
    ls.include_launch_description(launch_description)
    return ls.run()
