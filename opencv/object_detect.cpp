#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

using namespace cv;
using namespace std;

string window_detection_name = "HSV_IMAGE";
int slider_value = 0;
const int slider_max = 255;
Mat image, dst, hsv_image, mask;

int H_u = 0, high_S = 0, high_V = 0, high_H = 255, S_max = 255, V_max = 255, low_H = 0, low_S = 0, low_V = 0;

void on_trackbar (int, void *){

    threshold(image, mask, slider_value, 255, 0);
    imshow("Threshold_Trackbar", mask);
}

static void on_low_H_thresh_trackbar(int, void *)
{
    low_H = min(high_H-1, low_H);
    setTrackbarPos("Low H", window_detection_name, low_H);
}
static void on_high_H_thresh_trackbar(int, void *)
{
    high_H = max(high_H, low_H+1);
    setTrackbarPos("High H", window_detection_name, high_H);
}
static void on_low_S_thresh_trackbar(int, void *)
{
    low_S = min(high_S-1, low_S);
    setTrackbarPos("Low S", window_detection_name, low_S);
}
static void on_high_S_thresh_trackbar(int, void *)
{
    high_S = max(high_S, low_S+1);
    setTrackbarPos("High S", window_detection_name, high_S);
}
static void on_low_V_thresh_trackbar(int, void *)
{
    low_V = min(high_V-1, low_V);
    setTrackbarPos("Low V", window_detection_name, low_V);
}
static void on_high_V_thresh_trackbar(int, void *)
{
    high_V = max(high_V, low_V+1);
    setTrackbarPos("High V", window_detection_name, high_V);
}

int main( int argc, char** argv ){

    //Creating Windows
    namedWindow("Display Window", 1);
    namedWindow("Threshold_Trackbar", 1);
    //namedWindow("HSV_Trackbar", 1);
    namedWindow(window_detection_name, 1);

    /*Start -> Original Image*/
    image = imread("balls_move.mp4", CV_LOAD_IMAGE_COLOR);
    imshow("Display Window", image);
    /*End -> Original Image*/
    
//    threshold(image, dst, 50, 255, 0);
    cvtColor(image, dst, COLOR_BGR2HSV);
    
    //createTrackbar("threshold_value", "Threshold_Trackbar", &slider_value, slider_max, on_trackbar);
    
    int max_value = 255;

    createTrackbar("Low H", window_detection_name, &low_H, max_value, on_low_H_thresh_trackbar);
    createTrackbar("High H", window_detection_name, &high_H, max_value, on_high_H_thresh_trackbar);
    createTrackbar("Low S", window_detection_name, &low_S, max_value, on_low_S_thresh_trackbar);
    createTrackbar("High S", window_detection_name, &high_S, max_value, on_high_S_thresh_trackbar);
    createTrackbar("Low V", window_detection_name, &low_V, max_value, on_low_V_thresh_trackbar);
    createTrackbar("High V", window_detection_name, &high_V, max_value, on_high_V_thresh_trackbar);


    inRange(dst, Scalar(low_H, low_S, low_V), Scalar(high_H, high_S, high_V), hsv_image);

    imshow(window_detection_name, hsv_image);

    /*
    createTrackbar("H : ", "Threshold_Trackbar", &H_v, H_max, on_trackbar);
    createTrackbar("H : ", "Threshold_Trackbar", &H_v, H_max, on_trackbar);
    createTrackbar("H : ", "Threshold_Trackbar", &H_v, H_max, on_trackbar);
    */
    

    //namedWindow("Threshold_Trackbar", 1);
    //on_trackbar(slider_value, 0);
    
    waitKey(0);
    
    return 0;
}