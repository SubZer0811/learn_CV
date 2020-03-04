#include <iostream>
#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"

int main(int argc, const char * argv[]) {

    cv::Mat image= cv::imread("balls.jpeg");
    if (!image.data) {
        std::cout << "Image file not found\n";
        return 1;
    }

    //Prepare the image for findContours
    cv::cvtColor(image, image, CV_BGR2GRAY);
    cv::threshold(image, image, 128, 255, CV_THRESH_BINARY);

    //Find the contours. Use the contourOutput Mat so the original image doesn't get overwritten
    std::vector<std::vector<cv::Point> > contours;
    cv::Mat contourOutput = image.clone();
    cv::findContours( contourOutput, contours, CV_RETR_LIST, CV_CHAIN_APPROX_NONE );

    //Draw the contours
    cv::Mat contourImage(image.size(), CV_8UC3, cv::Scalar(0,0,0));
    cv::Scalar colors[3];
    colors[0] = cv::Scalar(255, 0, 0);
    colors[1] = cv::Scalar(0, 255, 0);
    colors[2] = cv::Scalar(0, 0, 255);
    for (size_t idx = 0; idx < contours.size(); idx++) {
        cv::drawContours(contourImage, contours, idx, colors[idx % 3]);
    }

    cv::imshow("Input Image", image);
    cvMoveWindow("Input Image", 0, 0);
    cv::imshow("Contours", contourImage);
    cvMoveWindow("Contours", 200, 0);
    cv::waitKey(0);

    return 0;
}