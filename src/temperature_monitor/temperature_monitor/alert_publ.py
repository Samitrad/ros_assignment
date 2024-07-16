import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class AlertPublisherNode(Node):

    def __init__(self):
        super().__init__("alert_publisher")
        self.subscription = self.create_subscription(
            String, "alert_trigger", self.alert_callback, 10)
        self.publisher = self.create_publisher(String, "alert", 10)

    def alert_callback(self, msg):
        alert_msg = String()
        alert_msg.data = "Alert"
        self.publisher.publish(alert_msg)
        self.get_logger().info("Alert published")

def main(args=None):
    rclpy.init(args=args)

    alert_publisher_node = AlertPublisherNode()

    rclpy.spin(alert_publisher_node)

    rclpy.shutdown()

if __name__ == "__main__":
    main()
