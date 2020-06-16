#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node("signal_sub",anonymous=True)
pub=rospy.Publisher("s1",String,queue_size=10)
rate=rospy.Rate(0.1)
while not rospy.is_shutdown():
    pub.publish("green")
    rospy.loginfo("green")
    rate.sleep()
    pub.publish("red")
    rospy.loginfo("red")
    rate.sleep()


