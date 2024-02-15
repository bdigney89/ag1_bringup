from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os.path

def generate_launch_description():

    # rviz_config_file = PathJoinSubstitution(
    #     [FindPackageShare("ag1_bringup"), "rviz2", "ag1_odom.rviz"]
    # )

    camera_node = Node(
        package="v4l2_camera",
        executable="v4l2_camera_node",
        output="sreeen"
        parameters=[{
                    "image_size":[640,480],
                    "camera_frame_id":"camera_link_optical",
                    "time_per_frame":[1:6]
                    }],
        remappings=[],
    )
    
    nodes = [camera_node     
    ]
    return LaunchDescription(nodes)