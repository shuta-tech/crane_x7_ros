#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import moveit_commander
import geometry_msgs.msg
import rosnode
from tf.transformations import quaternion_from_euler
from std_msgs.msg import String
from subprocess import call
from subprocess import Popen
from subprocess import PIPE
flag_demo = 0
key = 0


def callback(msg):
    
    rospy.sleep(2)
    bool_c = msg.data
    print (bool_c)
    body_up()
    rospy.sleep(10000.0)
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("bool", String, callback)
    rospy.spin()
    


def body_up():
     # 取りに行く

    robot = moveit_commander.RobotCommander()
    arm = moveit_commander.MoveGroupCommander("arm")
    arm.set_max_velocity_scaling_factor(1)
    gripper = moveit_commander.MoveGroupCommander("gripper")

    gripper.set_joint_value_target([0.9, 0.9])
    gripper.go()
    rospy.sleep(2.0)
    
    #gripper.set_joint_value_target([0.7, 0.7])
    #gripper.go()

    # 左中
    target_pose = geometry_msgs.msg.Pose()
    target_pose.position.x =  0.337012862721
    target_pose.position.y =  0.0517014049579
    target_pose.position.z =  0.14309330885
    q = quaternion_from_euler(-3.14, 0.0, -3.14/2.0)  # 上方から掴みに行く場合
    target_pose.orientation.x = 0.632287438308
    target_pose.orientation.y = -0.771793636354
    target_pose.orientation.z = -0.0160233105463
    target_pose.orientation.w = 0.065501387472
    arm.set_pose_target(target_pose)  # 目標ポーズ設定
    arm.go()  # 実行

    rospy.sleep(2.0)


   
    
    rospy.sleep(2.0)

       # ハンドを閉じる
    gripper.set_joint_value_target([0.4, 0.4])
    gripper.go()
    rospy.sleep(2.0)
    arm.set_named_target("home")
    arm.go()
    rospy.sleep(2.0)
    arm.set_named_target("vertical")
    arm.go()
    print("done")

if __name__ == '__main__':

    listener()