import cv2

# Load the image
image = cv2.imread('/Users/divijkohli/Desktop/WA_Coding_Challenge/images/red.png')

# Function to display coordinates of the points clicked
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"({x}, {y})")
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, f"{x},{y}", (x, y), font, 0.5, (255, 0, 0), 2)
        cv2.imshow('image', image)

# Display the image
cv2.imshow('image', image)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()