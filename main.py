# Import Statements
import cv2
import numpy as np

# Load the image
image = cv2.imread('/Users/divijkohli/Desktop/WA_Coding_Challenge/images/red.png')

# Define the points for the lines (you may need to adjust these coordinates)
# These are example coordinates; you should replace them with the actual coordinates of the cones in your image
points_set1 = [(272, 1617), (454, 1225), (572, 983), (635, 845),(667,778),(709,704),(733,646)]
points_set2 = [(1585, 1635), (1416, 1253), (1289, 997), (1250, 866),(1185,790),(1161,715),(1117,654)]

# Draw lines over the first set of cones
for i in range(len(points_set1) - 1):
    cv2.line(image, points_set1[i], points_set1[i + 1], (0, 0, 255), 2)

# Draw lines over the second set of cones
for i in range(len(points_set2) - 1):
    cv2.line(image, points_set2[i], points_set2[i + 1], (0, 0, 255), 2)

# Display the image with lines
cv2.imshow('Image with Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the image
cv2.imwrite('answer.png', image)





