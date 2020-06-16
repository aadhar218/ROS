#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32


def callback(data):
    rospy.loginfo("{0}  : {1} : {2} :" .format(minute).format(hour).format(second))

    rospy.spin()

rospy.init_node(clock_o,anonymous=True)
sub1=rospy.Subscriber("second",Int32,callback)
sub2=rospy.Subscriber("hour",Int32,callback)
sub2=rospy.Subscriber("minutes",Int32,callback)