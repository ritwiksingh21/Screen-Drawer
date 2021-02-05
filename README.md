# Screen-Drawer
## A simple program that lets you draw on screen using your web camera.

### :art: Draw live on your screen!
There are two separate programs. 
1. `screenDrawer.py` : uses **color detection** to identify colored object and draw its motion path. 
2. `noseScreenDrawer.py`: uses **Facial Recognition** to identify a face in camera frame and track the nose and color its path.<br/>

Currently only three colors are reognized by the `screenDrawer.py` that are blue, orange and green. Anything that is blue, orange or green when comes in view of the camera, the program assigns it a marking dot on top of it. Then as the colored object is moved in front of the camera, the marking dot is tracked and the track is highlighted in the same color as that of the object.<br/>
On the otherhand, `noseSccreenDrawer.py` doesn't accurately track the location of nose by visual identification of nose, rather it takes an approximate location of nose depending upon the size of face.

### What you need to run this:
* Python 3
* OpenCV
* Numpy
* A webcam

### Contribute:
If you feel like adding something to this project or just found something wrong, please go ahead and make a PR or raise an issue. <br/>
Any help from your side would be highly appreciated!

### DEMO:
##### ScreenDrawer:
<img src="https://raw.githubusercontent.com/ritwiksingh21/Screen-Drawer/main/Images/oopens.png" title="screenDrawer" width="65%">
