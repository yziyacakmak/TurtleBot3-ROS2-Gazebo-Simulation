import rclpy
from rclpy.node import Node 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2 


class FrameSubNode(Node):
    def __init__(self):
        super().__init__('image_sub')

        topic_name= '/camera/image_raw'

        self.subscription = self.create_subscription(Image, topic_name, self.img_callback, 30)
        self.br = CvBridge()

    def img_callback(self, data):
        self.get_logger().info('Receiving video frame')
        current_frame = self.br.imgmsg_to_cv2(data)
        cv2.imshow("camera", current_frame)   
        cv2.waitKey(1)
        
def main(args=None):
    rclpy.init(args=args)
    frame_sub = FrameSubNode()
    rclpy.spin(frame_sub)
    frame_sub.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
  main()