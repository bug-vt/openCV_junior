<link rel="stylesheet" href="styles.css">

# Project Title
#### Aziz Shaik and Bug Lee
#### Fall 2021 ECE 4554 Computer Vision: Course Project
#### Virginia Tech
---
## Abstract



---
## Introduction

Although computer vision is a relatively new topic, great amounts of time and effort have been put into it by professionals and researchers in the last few decades. As a result, many sophisticated algorithms have been developed that most computer vision applications are built upon today. Fortunately, those algorithms are packaged and encapsulated into commercial/open-source libraries, so that users can focus on its application.  

As a student in the Computer Vision course, however, our goal is to gain a concrete idea of some of the well-known topics in computer vision by creating our own library from scratch. Topics include Harris corner detector, SIFT descriptor, and nearest-neighbor matching which lay the foundation for many correspondence problems in computer vision. The focus of the project is not to create a library that can compete with a known library such as OpenCV, but to gain a deeper understanding of existing libraries and the ability to implement ideas for an existing/future computer language that may not have support for computer vision and its application.

---
## Approach

- We will first prototype the library using Python since it reduces the burden of creating helper functions such as vector/matrix multiplication, displaying image buffer, and array/list manipulation. Two libraries that will be used are: 
  - NumPy
  - Python Imaging Library (PIL)
- During the prototyping step, we will also analyze what part of the algorithm is causing the performance bottleneck. This will provide a better understanding of the strengths and weaknesses of the given algorithm in computer vision and suggest when and where to use it for best performance.
- Each function will be unit tested for correctness by comparing output with the corresponding OpenCV library function.  
- Transition to C++ will be considered once we identify all the algorithms are implemented correctly and after the unit testing step.

---

## Harris corner detector
### **Pseudo code**
Following pseudo code describe the algorithm of Harris corner detector.

    Convert the given image to gray scale. 
    Compute the gradient components at each point in the image
    Create the M matrix from the gradient components
    Compute the eigenvalues of M
    Compute Harris response. 
    Find points with large response (above certain threshold)
    Choose the local maximum of those points as features

 Note that Harris response will be approximated to
 $$
 \lambda_{min} \approx \frac{determinant(M)}{trace(M)}
 $$

### **Automatic Scale Selection**
Harris Detector itself is not invariant to scaling. Therefore scaling of the input image might be necessary to find the local maximum of the Harris response and correctly identify corners. 
For our implementation, a Gaussian pyramid will be used to generate copies of the input image with different scales and choose the one that gives the best Harris response.

### **Experiments and Result**
First, two basic tests will be performed using the following images (Figure 1 and Figure 2).
Then, more advanced tests will be performed by comparing the result with the Harris detector from OpenCV (Figure 3).

![Basic test](images/harris_expected_result1.png)

#### Figure 1. (a)Input image, (b)Expected output. Red circles indicate feature points.  

![Basic scale invariant test](images/harris_expected_result3.png)

#### Figure 2. (a)Expected output from un-scaled image, (b)Expected output from scaled version of input image used in (a). Red circles indicate feature points.  

` `

![Advance test](images/harris_expected_result2.png)
#### Figure 3. Output using existing library such as OpenCV. Image was copied from the *Computer vision: models, learning and inference* by Simon Prince [1]. 

` `

Using the same threshold value, tests will consider success if
1. Difference in the number of feature points between our implementation and the existing library function is within 10%.  
2. Positions of resulting local maxima(s) match with the output from the existing library function.
3. Performance difference is within the range of a few magnitudes. This is only used as a rough guideline to check whether we are not introducing unnecessary computation or performance bottleneck in our implementation.


---
## SIFT descriptor
Following pseudo code was adapted from the *Computer vision: models, learning and inference* by Simon Prince [1]. 

    Compute gradient orientation and amplitude maps over a 16 X 16 pixel region around the interest point
    Divide 16 X 16 detector region into a regular grid of non-overlapping 4x4 cells
    Within each of these cells, compute an 8 dimensional histogram of the image orientations
    Weight the histogram by the associated gradient amplitude and by distance 
    Concatenate 16 histograms to make 128 X 1 vector
    Normalize the vector

### **Experiments and Result**
Certain well-defined feature points will be manually selected (perhaps using a Harris detector) for this testing. This will lead to automatic and more sophisticated matching problems in the next section. First, the correctness of the descriptor will be evaluated through 3 basic tests. Tests will be considered a success only if all following 3 tests pass. Note that all images below were copied from the *Computer Vision: Algorithms and Applications* by Richard Szeliski [2].
 1. Descriptors with matching feature points where two images are differed by translation (Figure 4)
 2. Descriptors with matching feature points where two images are differed by rotation (Figure 5)
 3. Descriptors with matching feature points where two images are differed by different points of view (Figure 6)
 
![Translation test](images/sift_expected_result2.png)

#### Figure 4. Two images differ by translation. Two red circles are expected to hold a matching descriptor.

![Translation test](images/sift_expected_result1.png)

#### Figure 5. Two images differ by rotation. Two red circles are expected to hold a matching descriptor.

![Translation test](images/sift_expected_result3.png)

#### Figure 6. Two images differ by point of view. Two red circles are expected to hold a matching descriptor.

Again, once the above 3 tests pass, the result will be compared to the SIFT function from the existing library. The following two tests should pass for pre-selected feature points:

1. Computed vector matches with the output vector from the exiting library. 
2. Performance difference is within the range of a few magnitudes. This is only used as a rough guideline to check whether we are not introducing unnecessary computation or performance bottleneck in our implementation.

---
## Nearest neighbor matching




---
## Qualitative results



---
## Conclusion



---
## References
[1] Simon Prince, *Computer vision: models, learning and inference*, Cambridge University Press, 2012.  
[2] Richard Szeliski, *Computer Vision: Algorithms and Applications*, 2nd Edition, Springer, 2021.

---
#### © Aziz Shaik and Bug Lee

