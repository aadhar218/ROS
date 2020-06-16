#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


rospy.init_node("wander_motion",anonymous=True)
cmd_vel_pub=rospy.Publisher("cmd_vel",Twist,queue_size=1)
rate=rospy.Rate(10)

move=Twist()
r=float(input("enter radius of the circle for bot to make: "))


#w=self.move.angular.x
move.linear.x=r*0.5 
while not rospy.is_shutdown():
   cmd_vel_pub.publish(move)
   rospy.loginfo("Publishing")
   rate.sleep()

