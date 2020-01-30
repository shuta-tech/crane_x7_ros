#include <ros/ros.h>
#include <cv_bridge/cv_bridge.h>
#include <image_transport/image_transport.h>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/video/tracking.hpp>
#include <vector>
#include <std_msgs/String.h>

using namespace std;
cv::Mat image;

void imageCallback(const sensor_msgs::ImageConstPtr& input) {
	ros::NodeHandle nh;
	ros::Publisher pub = nh.advertise<std_msgs::String>("feature",100);
	try {
		image = cv_bridge::toCvCopy(input, sensor_msgs::image_encodings::BGR8)->image;
	}
	catch (cv_bridge::Exception& e) {
		ROS_ERROR("cv_bridge exception: %s", e.what());
	}

// reset == TRUE のとき特徴点検出を行う
	// 最初のフレームで必ず特徴点検出を行うように、初期値を TRUE にする
	bool reset = true;
 
	// image_curr:  現在の入力画像、    image_prev:  直前の入力画像
	// points_curr: 現在の特徴点リスト、points_prev: 直前の特徴点リスト
	cv::Mat frame,  image_curr, image_prev;
	vector<cv::Point2f> points_prev, points_curr;
 

		cv::cvtColor(image, image_curr, cv::COLOR_BGR2GRAY);

 
		if (reset == true) {
			// 特徴点検出
            
			cv::goodFeaturesToTrack(image_curr, points_curr, 500, 0.01, 10, cv::Mat(), 3, 0, 0.04);
			cv::cornerSubPix(image_curr, points_curr, cv::Size(10, 10), cv::Size(-1, -1), cv::TermCriteria(cv::TermCriteria::COUNT | cv::TermCriteria::EPS, 20, 0.03));
			points_prev = points_curr;
			reset = false;
		} else {
			// 特徴点追跡
			vector<uchar> status;
			vector<float> err;
 
			cv::calcOpticalFlowPyrLK(image_prev, image_curr, points_prev, points_curr, status, err);
 
			// 追跡できなかった特徴点をリストから削除する
			int i, k;
			for (i = k = 0; i < status.size(); i++)
			{
				if (status[i] == 0) {
					continue;
				}
				points_prev[k]   = points_prev[i];
				points_curr[k++] = points_curr[i];
			}
			points_curr.resize(k);
			points_prev.resize(k);
		}
 
		// 特徴点を丸で描く
		for (int i = 0; i < points_curr.size(); i++) {
			cv::Scalar c(0, 255, 0);
			printf("%d\n", i);

			if(i > 300){
				std::string feature = "1";
				pub.publish(feature);
				feature = "0";
			}

			if (cv::norm(points_prev[i] - points_curr[i]) > 0.5) {
				c = cv::Scalar(0, 100, 255);
			}
			cv::circle(image_curr, points_curr[i], 3, c, -1, cv::LINE_AA);
		}
		cv::imshow("特徴点追跡", image_curr);
 
		int key = cv::waitKey(5);
		if (key == 'r') {
			// Rキーが押されたら特徴点を再検出
			reset = true;
		
		// image_curr を image_prev に移す（交換する）
		cv::swap(image_curr, image_prev);
		// points_curr を points_prev に移す（交換する）
		cv::swap(points_curr, points_prev);
	}

        //cv::imshow("image", image);
        //cv::waitKey(1);
}

int main(int argc, char** argv) {
        ros::init (argc, argv, "img_subscriber");
		ros::NodeHandle nh;
        ros::Subscriber image_sub = nh.subscribe("input", 10, imageCallback);
		
        ros::spin();
}