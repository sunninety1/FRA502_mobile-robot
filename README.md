# FRA502_mobile-robot
This project is for FRA502 ROS assignment with the Basic level.

This project is to simulate a mobile robot in Gazebo with differential drive, camera, and laser scan plugin.
You can see the robot's camera view and laser scan via RViz.

To install this project, you must create a workspace folder first.
In the terminal, enter this command:

    mkdir ${YOUR_WORKSPACE_NAME}

Then, create an src folder and this project will be installed in the src folder. After that, we will make your workspace folder become a catkin workspace. The steps are as follows:

1.Get into your workspace folder.

    cd ${YOUR_WORKSPACE_NAME}

2.Create an src folder. 
    
    mkdir src

3.Get into the src folder.

    `cd src
   
4.Clone this git.

    git clone https://github.com/sunninety1/FRA502_mobile-robot

5.Make your workspace folder become a catkin workspace.

    cd ~/${YOUR_WORKSPACE_NAME} && catkin_make
    
By these steps, your folder will become a catkin workspace and this project will be installed in your workspace.

Before you launch the following package, don't for get to source the distro specific setup file first. When you open a new terminal, enter this command:

    source ~/${YOUR_WORKSPACE_NAME}/devel/setup.bash
    
    

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
