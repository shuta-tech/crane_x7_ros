## 使用方法

#### プログラムダウンロード方法
以下のコマンドを入力すれば、ダウンロード可能
```
$ cd ~/catkin_ws/src/

$ rm -rf ./crane_x7_ros

$ git clone -b robot_design3 https://github.com/shuta-tech/crane_x7_ros.git

$ ( cd ~/catkin_ws && catkin_make )

$ rosdep install -r -y --from-paths --ignore-src crane_x7_ros
```

※プログラムをダウンロードする際にcrane_x7内のプログラムは削除するため、今あるプログラムをgithub上に上げておくこと。

今回使用するプログラムは[crane_x7_pick_and_place_demo2.py](https://github.com/shuta-tech/crane_x7_ros/blob/robot_design3/crane_x7_examples/scripts/crane_x7_pick_and_place_demo2.py)である。


### 実機の場合
実機の動作確認は[README.md](https://github.com/piropann/crane_x7_ros/blob/master/crane_x7_examples/README.md)参照

①PCにマニピュレータをUSB経由で接続し、次のコマンドを入力
```
 $ sudo chmod 777/dexv/tty/USB0

 $ roslaunch crane_x7_bringup demo.launch fake_execution:=false

 $ roslaunch crane_x7_control crane_x7_control.launch
 ```

②物体を写真のように配置

![robot.png](https://github.com/shuta-tech/crane_x7_ros/blob/master/crane_x7_examples/srv/robot.png)

③プログラムを実行するため、以下のコマンドを入力

```
 $ rosrun crane_x7_examples crane_x7_pick_and_place_demo2.py
```

プログラムを実行した際の成功動画

[https://youtu.be/m2CDxoViR-k](https://www.youtube.com/watch?v=m2CDxoViR-k&feature=youtu.be)

### シミュレータを使う場合

①PCでシミュレータを起動するため、以下のコマンドを入力

```
 $ roslaunch crane_x7_gazebo crane_x7_with_table.launch
```

②プログラムを実行するため、以下のコマンドを入力

```
 $ rosrun crane_x7_examples crane_x7_pick_and_place_demo2.py
```

※このプログラムではシミュレータ上に表示されている物体はつかまないため、動作確認のみです。また、

Move itでは動作が同じにならない可能性があります。
