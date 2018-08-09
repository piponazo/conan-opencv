#include <opencv2/core/core.hpp>

#ifdef CV_WITH_OPENCL
#include <opencv2/core/ocl.hpp>
#endif

#ifdef CV_WITH_FEATURES2D
#include <opencv2/features2d.hpp>
#endif

#include <iostream>

using namespace std;

int main(int, char **)
{
    cv::Mat mat(3, 3, CV_8U);

    cout << "Compile & Link OpenCV test application correctly" << endl;

#ifdef CV_WITH_OPENCL
    cout << "Let's use some OpenCL code" << endl;
    cv::ocl::useOpenCL();
    cout << "cv::ocl::haveOpenCL(): " << cv::ocl::haveOpenCL() << endl;
    cv::ocl::Context context;

    if (!context.create(cv::ocl::Device::TYPE_GPU))
    {
        cout << "Failed creating the context..." << endl;
        //return;
    }

    cout << context.ndevices() << " GPU devices are detected." << endl; //This bit provides an overview of the OpenCL devices you have in your computer
    for (int i = 0; i < context.ndevices(); i++)
    {
        cv::ocl::Device device = context.device(i);
        cout << "name:              " << device.name() << endl;
        cout << "available:         " << device.available() << endl;
        cout << "imageSupport:      " << device.imageSupport() << endl;
        cout << "OpenCL_C_Version:  " << device.OpenCL_C_Version() << endl;
        cout << endl;
    }

    cv::ocl::Device(context.device(0)); //Here is where you change which 
#endif

#ifdef CV_WITH_FEATURES2D
    cout << "Let's use some Features2D code" << endl;
    vector<cv::KeyPoint> keypoints;
    const int fast_threshold = 20;
    const bool nonmaxSuppression = true;
    cv::FAST(mat, keypoints, fast_threshold, nonmaxSuppression);
#endif

    return EXIT_SUCCESS;

}
