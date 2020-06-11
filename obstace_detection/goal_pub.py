#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist,PoseStamped,Point
from nav_msgs.msg import Odometry
import actionlib
from math import atan2,sqrt
from tf.transformations import euler_from_quaternion 
import numpy as np

class goal_control:
    def __init__(self):
        self.kp=0.2
    def newOdom(self,msg):
        global x,y,theta
        x=msg.pose.pose.position.x
        y=msg.pose.pose.position.y
        orientation_q=msg.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
        theta=yaw
    
    def main(self):
        global x ,y,theta
        x=0
        y=0
        theta=0
        rospy.init_node('goal_pub',anonymous=True)
        self.pub=rospy.Publisher('/cmd_vel',Twist,queue_size=1)
        self.sub=rospy.Subscriber('/odom', Odometry, self.newOdom)
        goal= Point()
        goal.x=5
        goal.y=5
        self.rate=rospy.Rate(10)
        twist=Twist()
        while not rospy.is_shutdown() and goal is not None:
            print(theta)
            angle=atan2(goal.y-y,goal.x-x)
            dis=self.get_distance(x,y,theta,goal)
            rospy.loginfo(dis)
            s=self.kp*(angle-theta)
            twist.angular.z=0.2
            twist.linear.x=0
            if(s<0.1):
                twist.linear.x=0.2
                twist.angular.z=0
            if(dis<0.1):
                goal=None
                twist.linear.x=0
                twist.angular.z=0
            self.pub.publish(twist)
            self.rate.sleep()
    def get_distance(self,x,y,theta,goal):
        if goal is None :
            return 0
        diffx=x-goal.x
        diffy=y-goal.y
        dis=sqrt(diffx*diffx + diffy*diffy)
        return dis
if __name__ == '__main__':
    try:
        node = goal_control()
        node.main()
    except rospy.ROSInterruptException:
        pass
