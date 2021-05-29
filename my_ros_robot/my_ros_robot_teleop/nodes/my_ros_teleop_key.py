#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import sys, select, os
if os.name == 'nt':
  import msvcrt
else:
  import tty, termios

# linear velecity step size
lin_v_step = 0.01
# angular velocity step size
ang_v_step = 0.1

# robot speed limit
lin_max = 0.22
ang_max = 2.84

msg = """
---------------------------
Moving around:
        w
   a    s    d
        x

s : force stop
"""
# function

# get key from the pressed key 
def getKey():
    if os.name == 'nt':
      if sys.version_info[0] >= 3:
        return msvcrt.getch().decode()
      else:
        return msvcrt.getch()

    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

# print robot's velocity messages
def vels_msg(linear_vel, angular_vel):
    return "linear vel : %s\t angular vel : %s " % (linear_vel,angular_vel)

# limit the robot's speed
def constrain(input, min, max):
    if input < min:
      return min
    elif input > max:
      return max
    else:
      return input

# twist message that will be sent
def twistMSG(output, input, slop):
    if input > output:
        return min( input, output + slop )
    elif input < output:
        return max( input, output - slop )
    else:
        return input

# main code
if __name__=="__main__":
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)

    # create a publisher node which publishes a cmd_vel topic
    rospy.init_node('my_ros_robot_teleop')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    status = 0
    
    # initial velocity
    target_lin_v   = 0.0
    target_ang_v  = 0.0
    control_lin_v  = 0.0
    control_ang_v = 0.0

    try:
        print(msg)

        # create condition for controlling robot's direction 
        while(1):
            key = getKey()
            if key == 'w' :
                target_lin_v = constrain(target_lin_v + lin_v_step, -lin_max, lin_max)
                status = status + 1
                print(vels_msg(target_lin_v,target_ang_v))
            elif key == 'x' :
                target_lin_v = constrain(target_lin_v - lin_v_step, -lin_max, lin_max)
                status = status + 1
                print(vels_msg(target_lin_v,target_ang_v))
            elif key == 'a' :
                target_ang_v = constrain(target_ang_v + ang_v_step, -ang_max, ang_max)
                status = status + 1
                print(vels_msg(target_lin_v,target_ang_v))
            elif key == 'd' :
                target_ang_v = constrain(target_ang_v - ang_v_step, -ang_max, ang_max)
                status = status + 1
                print(vels_msg(target_lin_v,target_ang_v))
            elif key == 's' :
                target_lin_v   = 0.0
                control_lin_v  = 0.0
                target_ang_v  = 0.0
                control_ang_v = 0.0
                print(vels_msg(target_lin_v,target_ang_v))
            else:
                if (key == '\x03'):
                    break

            if status == 20 :
                print(msg)
                status = 0

            twist = Twist()

            # publish topic messages
            control_lin_v = twistMSG(control_lin_v, target_lin_v, (lin_v_step/2.0))
            twist.linear.x = control_lin_v; twist.linear.y = 0.0; twist.linear.z = 0.0

            control_ang_v = twistMSG(control_ang_v, target_ang_v, (ang_v_step/2.0))
            twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = control_ang_v

            pub.publish(twist)

    except rospy.ROSInterruptException as e:
        print(e)

    finally:
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rate.sleep()

    if os.name != 'nt':
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)