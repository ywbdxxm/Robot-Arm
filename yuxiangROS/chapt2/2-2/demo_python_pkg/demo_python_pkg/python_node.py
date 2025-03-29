import rclpy
from rclpy.node import Node


def main():
    rclpy.init()
    node = Node("python_node")
    node.get_logger().info("hello world")
    node.get_logger().warn("hello world")
    rclpy.spin(node)
    rclpy.shutdown()
