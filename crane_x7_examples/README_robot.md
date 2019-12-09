## 使用方法


①ブランチをrobot_design3に変更する

②プログラムをクローンする



動作確認は[README.md](https://github.com/piropann/crane_x7_ros/blob/master/crane_x7_examples/README.md)参照

今回使用するプログラムは[crane_x7_pick_and_place_demo2.py](https://github.com/shuta-tech/crane_x7_ros/blob/robot_design3/crane_x7_examples/scripts/crane_x7_pick_and_place_demo2.py)である。


### 実機の場合

①PCにマニピュレータをUSB経由で接続し、次のコマンドを入力
/home/shuta/Downloads/robot.png
```
 $ sudo chmod 777/dexv/tty/USB0

 $ roslaunch crane_x7_bringup demo.launch fake_execution:=false

 $ roslaunch crane_x7_control crane_x7_control.launch
 ```

②プログラムを実行するため、以下のコマンドを入力

```
 $ rosrun crane_x7_examples crane_x7_pick_and_place_demo2.py
```

プログラムを実行した際の成功動画

[https://youtu.be/m2CDxoViR-k](https://www.youtube.com/watch?v=m2CDxoViR-k&feature=youtu.be)

### シミュレータを使う場合

①PCでシミュレータを起動するため、以下のコマンドを入力

```
 $ roslaunch crane_x7_gazebo crane_x7_with_table launch
```

②プログラムを実行するため、以下のコマンドを入力

```
 $ rosrun crane_x7_examples crane_x7_pick_and_place_demo2.py
```

※このプログラムではシミュレータ上に表示されている物体はつかまないため、動作確認のみです。また、

Move itでは動作が同じにならない可能性があります。
