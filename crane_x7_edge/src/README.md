## 動作環境

以下の環境にて動作確認を行っています。

ROS Melodic

OS: Ubuntu 18.04.3 LTS

ROS Distribution: Melodic Morenia 1.14.3

Rviz 1.12.16

MoveIt! 1.13.3

Gazebo 9.0.0

## インストール方法

- 'git clone'を使用して本パッケージをダウンロードします。

```sh	
cd ~/catkin_ws/src/crane_x7_ros

git clone -b final https://github.com/shuta-tech/crane_x7_ros/tree/final/crane_x7_edge
```

ダウンロードして、実行許可がない場合は次のコマンドで許可与えてください。

	chmod 777　ファイル名

- 追加したパッケージをコンパイルしてくれるように~/catkin_ws/src/crane_x7_ros/crane_xにあるpackage.xmlに記入
  以下の写真のように26行目に以下の文を追加

```sh
<run_depend>crane_x7_robot_edge</run_depend>
```

- 'catkin_make'を使用して本パッケージをビルドします。

```sh
cd ~/catkin_ws && catkin_make
```

## crane_x7_edge

CRANE-X7のためのパッケージ、'realsensD435i'を使って画像処理して'crane_x7'を動作させるためのパッケージです。

| 使用するプログラム | 機能 |
----|----
| crane_x7_pick_and_place_demo.py | 物体が検知した場合、物体をつかみに行く |
| opencv_fp.cpp | 点を認識する |
| set.py | 初期姿勢 |

## システムの起動方法

CRANE_X7の制御信号ケーブルを制御用パソコンへ接続します。 Terminalを開き、'crane_x7_moveit_config'の'demo.launch'を起動します。

### 実機

①準備
画像のように物体を置く

![bringup](https://github.com/piropann/crane_x7_ros/blob/master/crane_x7_examples/srv/wef.png "bringup")

②PCにマニピュレータをUSB経由で接続し、次のコマンドを入力

	sudo chmod 777/dexv/tty/USB0

	roslaunch crane_x7_bringup demo.launch fake_execution:=false

	roslaunch crane_x7_control crane_x7_control.launch

➂マニピュレータを初期姿勢に移動するため、次のコマンドを入力

	rosrun crane_x7_edge set.py

![bringup](https://github.com/piropann/crane_x7_ros/blob/master/crane_x7_examples/srv/ima.jpg "bringup")

➃realsenseを起動

	roslaunch realsense2_camera rs_camera.launch

➄マニピュレータのプログラムを以下のコードで起動

	rosrun crane_x7_edge  rosrun crane_x7_edge crane_x7_pick_and_place_demo.py


➅10秒ほど待って、検出プログラム起動

	rosrun crane_x7_edge edg input:=/camera/color/image_raw

![bringup](https://github.com/piropann/crane_x7_ros/blob/master/crane_x7_examples/srv/123.png "bringup")

プログラムを実行した際の成功動画

https://youtu.be/BpDZ0-9jQR0