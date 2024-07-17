import rclpy
from rclpy.node import Node
from std_msgs.msg import String


import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class TemperatureLogger(Node):

    def __init__(self):
        super().__init__('temperature_logger')
        self.subscription = self.create_subscription(
            String, '/temperature', self.temperature_callback, 10)
        self.logger = self.get_logger()
        self.f = open("temperature_log.txt", "a")

    def temperature_callback(self, msg):
        try:
            temperature = float(msg.data)  # Attempt to convert string to float
            self.logger.info(f"Received temperature: {temperature:.2f} °C")
            self.f.write(f"Temperature is: {temperature}")

        except ValueError:
            self.logger.warn("Failed to convert temperature data to float")
            return  # Skip processing if conversion fails

    def destroy(self):
        self.subscription.unsubscribe()
        self.f.close()  # Close the file on node destruction

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureLogger()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()