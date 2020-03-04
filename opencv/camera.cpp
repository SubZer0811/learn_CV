#include "opencv2/opencv.hpp"
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

using namespace cv;
using namespace std;


int main(int argc, char** argv)
{

    int lh = 29, ls = 42, lv = 61, hh = 47, hs = 165, hv = 221;

    VideoCapture cap;
    // open the default camera, use something different from 0 otherwise;
    // Check VideoCapture documentation.
    if(!cap.open(0))
        return 0;
    int i = 0;
   
    

    while(1)
    {
            cout<<i<<endl;
            Mat frame;
            cap>>frame;
            imshow("Video", frame);
            if( waitKey(1) == 27 ){ 
                imwrite("calibrate.jpg", frame);
                break; // stop capturing by pressing ESC 
            }
    
        Mat blur, hsv;
        
        /*start of bluring, converting, Thresholding*/
        
        GaussianBlur(frame, blur, Size(11, 11), 1);
        cvtColor(blur, hsv, COLOR_BGR2HSV);
        
        Mat thresh;
        
        inRange(hsv, Scalar(lh, ls, lv), Scalar(hh, hs, hv), thresh);
        
        /*End*/

        /*Start of Find contours*/

        vector<vector<Point>> cont;

        findContours(thresh, cont, RETR_LIST, CHAIN_APPROX_SIMPLE);

        int max_adr = 0;
        if(cont.size() > 1){
            
            for(int i = 0; i < cont.size(); i++){
            
                cout<<"cont\n";
                if(contourArea(cont[i]) > contourArea(cont[max_adr])){
                    max_adr = i;
                }
            }
        

        //for(int i = 0; i<cont.max_size() - 1; i++)
        //drawContours(blur, cont, max_adr, Scalar(0, 255, 0), 10);
        
        cv::Rect bounding_max = boundingRect(cont[max_adr]);

        rectangle(blur, bounding_max, Scalar(0, 255, 0), 2);
        
        }

        imshow("frame", blur);
        imshow("thresh", thresh);

    }
    //the camera will be closed automatically upon exit
    //cap.close(0);
    return 0;
}