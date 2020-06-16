#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

rospy.init_node("controller",anonymous=True)
cmd_vel=rospy.Publisher("cmd_vel",Twist,queue_size=10)
rate=rospy.Rate(10)
dis=float(input("enter the distance for bot to move: "))
v=float(input("enter the velocity: "))
twist=Twist()
curr_dis=0.0
while not rospy.is_shutdown():
    t0=rospy.Time.now().to_sec()
    
    while(curr_dis<dis):
        twist.linear.x=v
        cmd_vel.publish(twist)
        t1=rospy.Time.now().to_sec()
        curr_dis=v*(t1-t0)

    twist.linear.x=0
    cmd_vel.publish(twist)
    
