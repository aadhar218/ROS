import rospy
import tf2_ros
import geometry_msgs.msg

def callback(data):
    tf2broadcast=tf2_ros.transformBroadcater()
    tf2Stamp=geometry_msgs.msg.TransformStamped()
    tf2Stamp.header.stamp=rospy.TIme.now()
    tf2Stamp.header.frame_id='base_link'
    tf2Stamp.child_frame_id='base_laser'
    tf2Stamp.transform.translation=(0.1,0.0,0.2)
    tf2Stamp.transform.rotation=(0.0,0.0,0.0)
    tf2broadcast.sendTransform(tf2Stamp)

if __name__=="__main__":
    rospy.init_node("tf_broadcater")
    rospy.Subscriber('')