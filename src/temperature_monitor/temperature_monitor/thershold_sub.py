import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ThresholdSubscriber(Node):  # Capitalized class name (convention)
    def __init__(self):
        super().__init__("threshold_subscriber")
        self.subscription = self.create_subscription(
            String, "temperature", self.temp_callback, 10)
        self.threshold = 35.0
        self.publisher = self.create_publisher(String, "alert_trigger", 10)

    def temp_callback(self, msg):
        temperature = float(msg.data)  # Convert string to float
        if temperature > self.threshold:
            alert_msg = String()
            alert_msg.data = "Temp exceeded threshold"  # Use data field for string
            self.publisher.publish(alert_msg)
            self.get_logger().info("Alert triggered")

def main(args=None):
    rclpy.init(args=args)

    threshold_subscriber_node = ThresholdSubscriber()

    rclpy.spin(threshold_subscriber_node)

    rclpy.shutdown()

if __name__ == "__main__":
    main()
