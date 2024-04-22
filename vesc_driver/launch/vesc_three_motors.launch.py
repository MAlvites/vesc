import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    vesc_config_motor1 = os.path.join(
        get_package_share_directory('vesc_driver'),
        'params',
        'vesc_config_motor1.yaml'
        )
    vesc_config_motor2 = os.path.join(
        get_package_share_directory('vesc_driver'),
        'params',
        'vesc_config_motor2.yaml'
        )
    vesc_config_motor3 = os.path.join(
        get_package_share_directory('vesc_driver'),
        'params',
        'vesc_config_motor3.yaml'
        )
    return LaunchDescription([
        DeclareLaunchArgument(
            name="config_1",
            default_value=vesc_config_motor1,
            description="VESC yaml configuration file Motor1.",
            ),
        DeclareLaunchArgument(
            name="config_2",
            default_value=vesc_config_motor2,
            description="VESC yaml configuration file Motor2.",
            ),
        DeclareLaunchArgument(
            name="config_3",
            default_value=vesc_config_motor3,
            description="VESC yaml configuration file Motor3.",
            ),
        Node(
            namespace= "motor1",
            package='vesc_driver',
            executable='vesc_driver_node',
            name='vesc_driver_node_1',
            parameters=[LaunchConfiguration("config_1")]
        ),
        Node(
            namespace= "motor2",
            package='vesc_driver',
            executable='vesc_driver_node',
            name='vesc_driver_node_2',
            parameters=[LaunchConfiguration("config_2")]
        ),
        Node(
            namespace= "motor3",
            package='vesc_driver',
            executable='vesc_driver_node',
            name='vesc_driver_node_3',
            parameters=[LaunchConfiguration("config_3")]
        ),
    ])
