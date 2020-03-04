#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main (){

    VideoCapture cap(0);
    
    cv::InputArray Lgreen = (234, 255, 0), Ugreen = (0, 255, 85);
    
    int lh = 107, ls = 50, lv = 0, hh = 147, hs = 255, hv = 126;
    
    Mat frame;
    cap>>frame;

    while(!frame.empty()){

        Mat blur, hsv;
        
        /*start of bluring, converting, Thresholding*/
        GaussianBlur(frame, blur, Size(11, 11), 1);
        cvtColor(blur, hsv, COLOR_BGR2HSV);
        
        

        Mat thresh;
        
        inRange(hsv, Scalar(lh, ls, lv), Scalar(hh, hs, hv), thresh);
        
        /*End*/
        //waitKey(0);
        
        /*Start of Find contours*/

        vector<vector<Point>> cont;

        findContours(thresh, cont, RETR_LIST, CHAIN_APPROX_NONE);

        int max_adr = 0;
        for(int i = 0; i < cont.size(); i++){

            if(contourArea(cont[i]) > contourArea(cont[max_adr])){
                max_adr = i;
            }
        }

        //for(int i = 0; i<cont.max_size() - 1; i++)
        
        //drawContours(blur, cont, max_adr, Scalar(0, 255, 0), 10);
        cv::Rect bounding_max = boundingRect(cont[max_adr]);

        rectangle(blur, bounding_max, Scalar(0, 255, 0), 2);

        imshow("frame", blur);
        imshow("thresh", thresh);

        

        cap>>frame;
        char c=(char)waitKey(100);
        if(c==27)
            break;
    }

    cap.release();

    destroyAllWindows();
    return 0;

}
