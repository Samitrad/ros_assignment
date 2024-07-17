import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time


class TemperatureLogger(Node):

    def __init__(self):
        super().__init__('temperature_logger')
        self.subscription = self.create_subscription(
            String, '/temperature', self.temperature_callback, 10)
        self.logger = self.get_logger()
        self.filename = "temperature_log.txt"  # Set the log file name

    def temperature_callback(self, msg):
        try:
            temperature = float(msg.data)  # Attempt conversion to float
        except ValueError:
            self.logger.warn(f"Failed to convert temperature data: {msg.data}")
            return  
        
        try:
            with open(self.filename, "a") as logfile:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                logfile.write(f"{timestamp}: {temperature:.2f}\n")
                self.logger.info(f"Temperature logged: {temperature:.2f}")
        except FileNotFoundError:
            self.logger.error(f"Failed to open log file: {self.filename}")

    def destroy(self):
        self.subscription.unsubscribe() 

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureLogger()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
