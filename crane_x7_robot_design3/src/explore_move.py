#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import moveit_commander
import geometry_msgs.msg
import rosnode
from tf.transformations import quaternion_from_euler
from std_msgs.msg import String

def main():
    rospy.init_node("arm_move")
    robot = moveit_commander.RobotCommander()
    arm = moveit_commander.MoveGroupCommander("arm")
    arm.set_max_velocity_scaling_factor(1)
    gripper = moveit_commander.MoveGroupCommander("gripper")
        
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


    # SRDFに定義されている"home"の姿勢にする
    arm.set_named_target("vertical")
    arm.go()
    rospy.sleep(3)
    arm.set_named_target("home")
    arm.go()
    gripper.set_joint_value_target([0.1, 0.1])
    gripper.go()

    # 左
    target_pose = geometry_msgs.msg.Pose()
    target_pose.position.x = 0.29530626873
    target_pose.position.y = 0.10362120555
    target_pose.position.z =  0.245917491898
    q = quaternion_from_euler(-3.14, 0.0, -3.14/2.0)  # 上方から掴みに行く場合
    target_pose.orientation.x =-0.811127380552
    target_pose.orientation.y = 0.579297151378
    target_pose.orientation.z = -0.0118768496306
    target_pose.orientation.w = 0.0796625593835
    arm.set_pose_target(target_pose)  # 目標ポーズ設定
    arm.go()  # 実行

    

    #gripper.set_joint_value_target([0.7, 0.7])
    #gripper.go()
    '''
    # 左中
    target_pose = geometry_msgs.msg.Pose()/camera/depth/color/points
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
    '''
    

    # ハンドを閉じる
   # gripper.set_joint_value_target([0.05, 0.05])
   # gripper.go()

    # 右中
  
    rospy.sleep(1000)
    print("done")
if __name__ == '__main__':

    main()
   
  