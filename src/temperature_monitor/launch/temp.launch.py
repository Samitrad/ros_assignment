import launch
from launch_ros.actions import Node

def generate_launch_description():
   
    temp_publisher_node = Node(
        package= 'temperature_monitor',
        executable='temp_pubNode',  
        name='temperature_publisher'
    )
    threshold_subscriber_node = Node(
        package='temperature_monitor',
        executable='alert_node',  
        name='threshold_subscriber'
    )
    alert_publisher_node = Node(
        package='temperature_monitor',
        executable='threshold_node', 
        name='alert_publisher'
    )

    logging_node = Node(
    package='temperature_monitor',
    executable='logging_temp', 
    name='logging_temp'
    )
	
    
    return launch.LaunchDescription([
        temp_publisher_node,
        threshold_subscriber_node,
        alert_publisher_node,
        logging_node
    ])
