# ROS
## PID controller
A PID controller simulation has been made for a differential drive robot. </br>
Clone the PID controller folder in your catkin workspace and buid the package </br>
To test the controller on turtlebot run the following commands
``` 
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch 
```
### to run the controller:
 ```
rosrun ROS my_controller.py
```
 The goal coordinates can be inputted.
