# PerceptionApplication

# Answer
![answer](https://github.com/user-attachments/assets/f220dacd-ed78-4259-b5aa-59d303d40985)

# Methodology
My solution actually consists of two seperate python files, these being main.py and points.py. The general ideology behind my solution was to use the cv2.line method to iterate through each cone in each line, respectively, and thus draw two boundary lines. However, doing this would require me to have the coordinates for each individual cone. As such, I created a second python file called points.py which listnes for a click event, and when the mouse is clicked the progam simply marks the given coordinate point (x,y) on the location of the mouse press on the image of cones itself. These obtained coordinate points are then inputted into two arrays within the main file, and thus we can now successfuly utilize the cv2.line method to draw boundary lines!

# What Didn't Work
My initial thought process was to use the contour functionality of opencv to identify the locations of where each of the two boundaries should have been in the answer image. I thought this would work well because the bright orange cones greatly contrast the rest of the image, and the contour function is built for the exact purpose of creating a connect curve between disjointed points. Unfortunately, my implementation must have been incorrect because my solution returned an image that drew contours (lines) between the bricks in the wall. I think this may have been due to the fact that I used a default findContours method which is only really applicable in an image with one clear contour. In this case not only are there two seperate lines of cones, there are also potential contours on the walls and on the floor.

# Libraries
- OpenCV
- Numpy
