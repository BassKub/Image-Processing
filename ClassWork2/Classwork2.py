import cv2
import numpy as np

def draw_circle_center(image, center, radius):
    # Draw a circle on the image at the center coordinates
    cv2.circle(image, center, radius, (0, 255, 0), thickness=2)
    # Draw a crosshair at the center coordinates
    cv2.drawMarker(image, center, (0, 255, 0), cv2.MARKER_CROSS, 10, thickness=2)

def find_circle_center(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Hough Circle Transform to detect circles
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, minDist=50, param1=50, param2=30, minRadius=0, maxRadius=0)

    if circles is not None:
        # Get the center coordinates of the detected circle
        center_x = int(circles[0][0][0])
        center_y = int(circles[0][0][1])

        return (center_x, center_y)
    else:
        return None

# Load the image
image = cv2.imread('Circle Objects.png')

# Find the center of the circle
center = find_circle_center(image)

if center is not None:
    radius = 10  # Set the radius of the circle to be drawn
    draw_circle_center(image, center, radius)

    # Display the image
    cv2.imshow('Image with Circle Center', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Circle not found.")