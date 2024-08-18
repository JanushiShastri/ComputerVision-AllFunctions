import cv2 
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('schoolBus.png')
if img is None:
    print("Error: Could not load image.")
    exit()

# Display the original image
cv2.imshow('Original Image', img)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray)

# Calculate the histogram
gray_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# Plot the histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel('Pixel Intensity')
plt.ylabel('Number of Pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])

# Save the plot to a file
plt.savefig("gray_histogram.png")

# Wait for a key press and then close all OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()
