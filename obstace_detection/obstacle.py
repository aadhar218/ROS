#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

rospy.init_node("obstacle",anonymous=True)
def scan_callback(msg):
    global o_range
    o_range=min(msg.ranges)

o_range=1
scan=rospy.Subscriber("scan",LaserScan,scan_callback)
cmd_vel=rospy.Publisher("cmd_vel",Twist,queue_size=1)
rate=rospy.Rate(10)

v=float(input("enter the bot velocity: "))
while not rospy.is_shutdown():
    twist=Twist()
    if(o_range < 0.8):
        twist.angular.z=2*v
        rospy.sleep(0.30)
        twist.linear.x=v
    else:
        twist.linear.x=v
    cmd_vel.publish(twist)
    rate.sleep
        

