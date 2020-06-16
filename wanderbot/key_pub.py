#!/usr/bin/env python
import rospy
import sys,select,tty,termios
from std_msgs.msg import String
pub=rospy.Publisher("keys",String,queue_size=10)
rospy.init_node("ley_pub",anonymous=True)
rate=rospy.Rate(100)
old_attr=termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin.fileno())
print("key_strokes")
while not rospy.is_shutdown():
    if select.select([sys.stdin],[],[],0)[0]==[sys.stdin]:
        pub.publish(sys.stdin.read(1))
    rate.sleep()
termios.tcsetattr(sys.stdin,termios.TCSADRAIN,old_attr)