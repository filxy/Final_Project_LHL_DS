# **Deep Fake Detector**

## Goal:
#### Machine learning model that detects if an image or video is manipulated or authentic.It also detects youtube url & real-time webcam images. 


## **Tech Stack**

| **Libraries**    | **Links**                                                                                  |
| ----------------- | ------------------------------------------------------------------------------------------ |
| TensoFlow | [![PyPI](https://img.shields.io/pypi/v/Tensorflow)](https://pypi.org/project/tensorflow/2.5.0rc1/) |
|Face_Recognition|[![PyPI](https://img.shields.io/pypi/v/face_recognition.svg)](https://pypi.python.org/pypi/face_recognition) |
|imageio-ffmpeg |[![PyPI](https://img.shields.io/pypi/v/imageio-fmpeg)](https://pypi.org/project/imageio-ffmpeg/)  |
|   imageio     |  [![PyPI](https://img.shields.io/pypi/v/imageio)](https://pypi.org/project/imageio/)             |
|   pillow      |  [![PyPI](https://img.shields.io/pypi/v/pillow)](https://pypi.org/project/Pillow/)               |
| ffmpeg-python | [![PyPI](https://img.shields.io/pypi/v/ffmpeg-python)](https://pypi.org/project/ffmpeg-python/)  |
| opencv-pyton  | [![PyPI](https://img.shields.io/pypi/v/opencv-python)](https://pypi.org/project/opencv-python/)  |


## Dataset:
#### The dataset used in this project can be found on below links. This project can be tested on a different dataset as well and will require you to provide the path of your dataset at certain places in the project. 


| Data-Links                                            |                                                    |    Fake_image   |  Real_image |
| ----------------------------------------------------- | -------------------------------------------------- | --------------- | ----------- |
| [Images](https://www.kaggle.com/yihaopuah/deep-fake-images)| `Only Train dataset was used in this project` |     3,462       |     700     |
| [Videos](https://www.kaggle.com/sorokin/faceforensics)| `Only DeepFakes were used in this project`         |     1,000       |             |
| [Youtube](https://www.youtube.com/watch?v=DdZ163jzw4w)|                                                    |                 |             |

## Pre-Trained Weights:
#### The folder saved_model consists of 2 pre-trained weights which you will require to download in order to run this project and declare your path for meso weights in the `Deep_Fake_Detector` notebook accordingly

# Results:
## Images Output:
### Correct Deep Fake Output:
![alt text](https://github.com/filxy/Final_Project_LHL_DS/blob/main/Output/correct-deep%20fake.png)
### Misclassified Deep Fake Output:
![alt text](https://github.com/filxy/Final_Project_LHL_DS/blob/main/Output/misclassified-deep%20fake.png)
## WebCam Output:
![alt text](https://github.com/filxy/Final_Project_LHL_DS/blob/main/Output/web-cam-image-plot.png)
![alt text](https://github.com/filxy/Final_Project_LHL_DS/blob/main/Output/web-cam-image-pred.png)
## Youtube URL Output:
![alt text](https://github.com/filxy/Final_Project_LHL_DS/blob/main/Output/youtube%20-url%20prediction.png)
![alt text](https://github.com/filxy/Final_Project_LHL_DS/blob/main/Output/yt-prediction.png)

## Project Demo:
### Visit the streamlit app to try it yourself - [streamlit app](https://share.streamlit.io/filxy/deepfake-detection-app/main/app.py)

https://user-images.githubusercontent.com/20019696/155808772-98d93755-c75c-437d-b5eb-1e94fc91d7f5.mov

