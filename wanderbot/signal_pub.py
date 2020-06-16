#!/usr/bin/env python
import rospy
from std_msgs.msg import String
a=""
rospy.init_node("signal_sub",anonymous=True)
def callback(msg):
    if(msg.data=="red"):
        pub.publish("green")
        rospy.loginfo("red")
    else:
        pub.publish("green")
        rospy.loginfo("green")
sub=rospy.Subscriber("s1",String,callback)
pub=rospy.Publisher("s2",String,queue_size=10)
rate=rospy.Rate(0.1)
rospy.spin()