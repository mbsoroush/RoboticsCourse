
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class TemperatureProcessor(Node):
    def __init__(self):
        super().__init__("temperature_processor")
        self.subscription_ = self.create_subscription(
            String, "temperature_data", self.process_temperature, 10
        )
        self.temperatures_ = []
        self.get_logger().info("Temperature Processor Node is active.")

    def process_temperature(self, msg):
        temperature = float(msg.data)
        self.temperatures_.append(temperature)
        self.get_logger().info(f"Received Temperature: {temperature}")

        avg_temp = sum(self.temperatures_) / len(self.temperatures_)
        self.get_logger().info(f"Average Temperature: {avg_temp:.2f}")


def main(args=None):
    rclpy.init(args=args)
    node = TemperatureProcessor()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()



