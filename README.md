# FRA502_mobile-robot
This project is for FRA502 ROS assignment with the Basic level.

This project is to simulate a mobile robot in Gazebo with differential drive, camera, and laser scan plugin.
You can see the robot's camera view and laser scan via RViz.

To simulate the robot in Gazebo and visualize in RViz,the syntax is as follows:

    roslaunch my_ros_robot_des gazebo_room.launch

You can control the robot by using keyboard keys via my_ros_robot_teleop package.
        
          w
     a    s    d
          x

w: Increase the robot's linear velocity in x direction.
x: Increase the robot's linear velocity in -x direction.
a: Incroease the robot's angular velocity in counterclockwise rotation.
d: Incroease the robot's angular velocity in clockwise rotation.
s: Force stop the robot.

To use the my_ros_robot_teleop package, the syntax is as follows:

    roslaunch my_ros_robot_teleop teleop_key.launch 
    
You can install this project by entering this command

    git clone https://github.com/sunninety1/FRA502_mobile-robot.git
