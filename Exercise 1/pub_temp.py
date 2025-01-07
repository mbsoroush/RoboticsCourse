
import rclpy
from rclpy.node import Node
import random
from std_msgs.msg import String


class Publisher(Node):
    def __init__(self):
        super().__init__("publisher")
        self.publisher_ = self.create_publisher(String, "temperature_data", 10)
        self.timer_ = self.create_timer(1.0, self.publish_temp)
        self.get_logger().info("Temperature Publisher Node is active.")

    def publish_temp(self):
        temperature = round(random.uniform(15.0, 35.0), 2)
        message = String()
        message.data = f"{temperature}"
        self.publisher_.publish(message)
        self.get_logger().info(f"Published Temperature: {message.data}")


def main(args=None):
    rclpy.init(args=args)
    node = Publisher()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()




