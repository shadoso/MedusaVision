**Medusa Vision**
Project in progress.

Medusa Vision is a DQN that receives an image as input instead of an environment.

- Notes: What is required and some tips
- Challenges: All the problems that I had to face.
- Methods: Why I chose to use that method.



# Notes
- OS: Ubuntu, CentOS, Debian, Fedora, OpenSUSE, RHEL, SLES, WSL-Ubuntu and ~~Windows~~.  
I strongly recommend you to use **Linux** instead of windows, installing CUDA and other resources is easier on windows but you will probably face some problems.

- Make sure you have installed: FFmpeg, CUDA, cuDNN, Python 3.8 and scrcpy.

- Python packages: cv2, torch, numpy, PIL, pyautogui and tensorflow.

- Tips: Is being used Yolov5 to detect the objects, and Roboflow to label and manage the image database.

If you going to use **Roboflow** to label, never use the video extraction on the site it is **slow and uses an absurd amount of RAM**, because of that **FFmpeg** is on this list.

I recommend using -vf fps=1 or fps=2, and manually deleting all the duplicates or any useless content, and make sure to just upload 500 images per time, It will be much easier to manage it later, Roboflow is good but lacks in some aspects of handling the images.

The automatic labeling in Roboflow is just amazing, make sure to have at least 100 ~ 125 images per class before doing the first train, with your first train we just want some help, it will label many things wrong, but you will just have to adjust the label or change the name, it makes the work fast.

You should add some background images and some random images to the database, the main reason for this is easy when you label an object some part of the background is inside the labeling so there is a chance that the AI will consider the background as part of the object, the random images helps in another field for an example, if you are making an AI recognize bad eggs you should consider adding an object that is spherical and white as a golfball, all those images should be label as null this will reduce the amount of bad guessing, but make sure that all null images are not bigger than the training and valid sets.

All the images should be collected in the same resolution example, 1080x1080, later you will have the choice to reshape all of it in Roboflow if you going to use the Google collab to train, I recommend 736x736 Is a good shape and won’t use too much RAM “All the images are stored on cache for fast training”, bigger images helps to detect small objects if you don’t have any tiny class to label use a lower resolution like 640x640.

# Challenges
- Limited resources: Google collab will help you but he isn’t a good big brother, it will let you play on his Tesla K80 but for a limited amount of time, so if you have a database that contain more than 1500 images make sure to know the maximum amount of epochs you can do before you receive timeout.
- Lack of info: At “Deep Q-Learning for Atari Breakout”, they are using an incorrect method to teach the AI to play, “IT WORKS” but you shouldn’t stack frames on CNN! after hours of searching I found this explanation, since CNN solves a spatial problem stacking all images will make the CNN consider everything as just one single image, to it be able to understand the concept of Frames you should use LSTM which solves time series problems where the sequence matters, so your model should be a CNN-LSTM.
**https://stackoverflow.com/questions/53020898/multiple-input-cnn-for-images?rq=1**
