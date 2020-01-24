#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import moveit_commander
import geometry_msgs.msg
import rosnode
from tf.transformations import quaternion_from_euler
from std_msgs.msg import String

def callback(msg):
    #rospy.sleep(12.0)
    print("ok")
    feature_c = msg.data
    print(feature_c)
    body_up()
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("feature", String, callback)
    rospy.spin()
    
def body_up():
    robot = moveit_commander.RobotCommander()
    arm = moveit_commander.MoveGroupCommander("arm")
    arm.set_max_velocity_scaling_factor(0.1)
    gripper = moveit_commander.MoveGroupCommander("gripper")
    sign = 0

    while len([s for s in rosnode.get_node_names() if 'rviz' in s]) == 0:
        rospy.sleep(1.0)
    rospy.sleep(1.0)

    print("Group names:")
    print(robot.get_group_names())

    print("Current state:")
    print(robot.get_current_state())

    # アーム初期ポーズを表示
    arm_initial_pose = arm.get_current_pose().pose
    print("Arm initial pose:")
    print(arm_initial_pose)

    # 何かを掴んでいた時のためにハンドを開く
    gripper.set_joint_value_target([0.9, 0.9])
    gripper.go()

    # 掴む準備をする
    '''target_pose = geometry_msgs.msg.Pose()
    target_pose.position.x = 0.37
    target_pose.position.y = 0.0
    target_pose.position.z = 0.3
    q = quaternion_from_euler(3.14, 0.0, 3.14/2.0)  # 上方から掴みに行く場合
    target_pose.orientation.x = q[0]
    target_pose.orientation.y = q[1]
    target_pose.orientation.z = q[2]
    target_pose.orientation.w = q[3]
    arm.set_pose_target(target_pose)  # 目標ポーズ設定
    arm.go()  # 実行

    # ハンドを開く
    gripper.set_joint_value_target([0.7, 0.7])
    gripper.go()'''

    # 掴みに行く
    target_pose = geometry_msgs.msg.Pose()
    target_pose.position.x = 0.38
    target_pose.position.y = 0.0
    target_pose.position.z = 0.11
    q = quaternion_from_euler(3.14, 0.0, 3.14/2.0)  # 上方から掴みに行く場合
    target_pose.orientation.x = q[0]
    target_pose.orientation.y = q[1]
    target_pose.orientation.z = q[2]
    target_pose.orientation.w = q[3]
    arm.set_pose_target(target_pose)  # 目標ポーズ設定
    arm.go()  # 実行

    # ハンドを閉じる
    gripper.set_joint_value_target([0.3, 0.3])
    gripper.go()

    # 持ち上げる
    target_pose = geometry_msgs.msg.Pose()
    target_pose.position.x = 0.38
    target_pose.position.y = 0.0
    target_pose.position.z = 0.3
    q = quaternion_from_euler(3.14, 0.0, 3.14/2.0)  # 上方から掴みに行く場合
    target_pose.orientation.x = q[0]
    target_pose.orientation.y = q[1]
    target_pose.orientation.z = q[2]
    target_pose.orientation.w = q[3]
    arm.set_pose_target(target_pose)  # 目標ポーズ設定
    arm.go()							# 実行

    print("done")

    
if __name__ == '__main__':
    listener()

