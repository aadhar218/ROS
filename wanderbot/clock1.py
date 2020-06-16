#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32,String

rospy.init_node("clock1",anonymous=True)
def callback(msg):
    print msg.data

sub=rospy.Subscriber("clock",String,callback)

rospy.spin()