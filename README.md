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
- Lack of info: At **“Deep Q-Learning for Atari Breakout”**, they are using an incorrect method to teach the AI to play, “IT WORKS” but you shouldn’t stack frames on CNN! after hours of searching I found this explanation, since CNN solves a spatial problem stacking all images will make the CNN consider everything as just one single image, to it be able to understand the concept of Frames you should use LSTM which solves time series problems where the sequence matters, so your model should be a CNN-LSTM.
- More lack of info: Maybe you want to use raw pixels as an input or a custom environment, most of the “GOOD” material for this area isn’t free, I know there are many good articles or tutorials about this but most of it is really complex, most of the time you will be merely copying and pasting code and you won’t know why you are doing this, I strongly recommend you to search every single aspect of it instead just being a copy machine.
- Those 2 links will help to understand CNN-LSTM.  
**https://stackoverflow.com/questions/53020898/multiple-input-cnn-for-images?rq=1**  
**https://medium.com/smileinnovation/how-to-work-with-time-distributed-data-in-a-neural-network-b8b39aa4ce00**

# Methods

**Under manutence**
- Input: Your input can have many formats, you can use 3 channel colors or greyscale or edge, and you can even change a few things, I will give a short explanation about it and then I tell you why I choose my input shape.

**Let’s consider that in all these examples we are working with an image of 420x420.**
- Edge: When you use edge detection, most of the time you keep more than enough info to make the AI work and also make the training much faster, imagine that you have a Rubik’s cube, and just one side has white squares and the rest of it black square, you probably could solve it under 1 minute, is pretty clear what you need to do, you are not overwhelmed with info. Of course, there is a problem sometimes you lose some important info like color and depth.
- Greyscale: With Greyscale, you keep depth and colors, is strange to say colors when you just have 0 to 255 shades, but if you look at the raw number in the array you will notice the difference between a gray “Red” and a “ gray “Yellow”, and you may think how much hard is this for the AI?
Imagine that our Rubik’s cube now has a white side and 2 gray sides with different shades and the rest all black squares, it’s still much easier than a true Rubik’s cube, let’s say that you can solve this in 3 minutes. While training an AI time is priceless, when you do 1 “Greybiks Cube” you would already solve 3 “Edgik Cubes”, and of course, each one will have a different method to solve.
- RGB:
