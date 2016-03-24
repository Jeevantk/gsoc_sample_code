#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core/core.hpp>
#include <iostream>
using namespace cv;
using namespace std;
int main()
{
  Mat dist;
  Mat img=imread("Contour_Image.jpg",0);
  /*bitwise_not(img,img);
  Mat src=imread("test.jpg");
  threshold(img,otsu, 0, 255, CV_THRESH_BINARY | CV_THRESH_OTSU);
  imshow("Initial Image",otsu);
  waitKey(0);
  Mat dist=Mat::zeros(img.rows,img.cols,CV_8UC1);
  vector<vector<Point> > contours;
  vector<Vec4i> hierarchy;
  //erode(otsu,otsu, Mat(), Point(-1, -1), 2, 1, 1);
  findContours(otsu, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, Point(0, 0) );
  for( int i = 0; i< contours.size(); i++ )
  {
    drawContours(dist, contours, i,255,1, 8, hierarchy, 0, Point() );
  }
  imshow("Detected Contours",dist);
  waitKey(0);*/
  distanceTransform(img,dist, CV_DIST_L2, 3);
  normalize(dist,img, 0.0, 1.0, NORM_MINMAX);
  imshow("After Distance transform",img);
  waitKey(0);


}
