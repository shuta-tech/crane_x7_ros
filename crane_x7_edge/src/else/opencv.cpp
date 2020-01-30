#include <ros/ros.h>
#include <sensor_msgs/Image.h>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/opencv.hpp>
#include <std_msgs/String.h>
#include <highgui.h>


using namespace::cv;
std::string msg = "0";
std::string msg_1 = "0"; 
class depth_estimater{
public:
    depth_estimater();
    ~depth_estimater();
    void rgbImageCallback(const sensor_msgs::ImageConstPtr& msg);
    void depthImageCallback(const sensor_msgs::ImageConstPtr& msg);
   
 
private:
    ros::NodeHandle nh;
    ros::Subscriber sub_rgb, sub_depth;
    ros::Publisher pub = nh.advertise<std_msgs::String>("bool",100);
};
cv::Mat img_1;
depth_estimater::depth_estimater(){
    sub_rgb = nh.subscribe<sensor_msgs::Image>("/camera/color/image_raw", 1, &depth_estimater::rgbImageCallback, this);
}
 
depth_estimater::~depth_estimater(){
}
 
void depth_estimater::rgbImageCallback(const sensor_msgs::ImageConstPtr& msg){
 
    cv_bridge::CvImagePtr cv_ptr;
 
    try{
        cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
    }catch (cv_bridge::Exception& ex){
        ROS_ERROR("error");
        exit(-1);
    }    
    cv::Mat hsv_img;
    cvtColor( cv_ptr->image,hsv_img,CV_BGR2HSV,3);
    Scalar lower = cv::Scalar(160,50,50);
    Scalar upper = cv::Scalar(180,255,255);

    // BGRからHSVへ変換
	Mat mask_image, output_image;
    int px_1,x,y,x_mem,y_mem;
    int flag = 0;

    // inRangeを用いてフィルタリング
	inRange(hsv_img, lower, upper, mask_image);

    //エッジ検出部
    int count = 0;
    cv::Canny(mask_image, output_image, 255, 255);
    cv::imshow("edge image", output_image);
    //コーナーを検出
   
    std::cout << count << std::endl;
    cv::waitKey(3);
}

int main(int argc, char **argv){
    ros::init(argc, argv, "depth_estimater");
    depth_estimater depth_estimater;
    ros::spin();
    return 0;
}


