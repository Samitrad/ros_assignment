import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TempPublisher(Node):  
    def __init__(self):
        super().__init__("temperature_publisher") 
        self.publisher = self.create_publisher(String, "temperature", 10)
        self.timer_period = 1.0
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

    def timer_callback(self):
        temperature = random.uniform(0, 50)
        msg = String()
        msg.data = str(temperature) 
        self.publisher.publish(msg)
        self.get_logger().info(f"{temperature:.2f} degrees")

def main(args=None):

    rclpy.init(args=args)
    temperature_publisher_node = TempPublisher()
    rclpy.spin(temperature_publisher_node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
