#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
rospy.init_node('clock',anonymous=True)
pub1=rospy.Publisher('sec',Int32,queue_size=10)
pub2=rospy.Publisher('minute',Int32,queue_size=10)
pub3=rospy.Publisher('hour',Int32,queue_size=10)
pub4=rospy.Publisher('clock',String,queue_size=1)

sec=0
minute=0
hour=0
rate=rospy.Rate(1)
while not rospy.is_shutdown():
    if(sec<60):
        sec=sec+1
        pub1.publish(sec)
    else:
        sec=0
        minute=minute+1
        pub2.publish(minute)
        if(minute==60):
            hour=hour+1
            pub3.publish(hour)
    clock=str(hour)+":"+str(minute)+":"+str(sec) 
    pub4.publish(clock)
    rospy.loginfo(clock)
    rate.sleep()

