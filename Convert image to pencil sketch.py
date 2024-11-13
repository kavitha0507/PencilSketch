import cv2
import numpy as np


def convert_to_sketch(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)

    # Blur the inverted image using GaussianBlur
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), sigmaX=0, sigmaY=0)

    # Invert the blurred image
    inverted_blurred = cv2.bitwise_not(blurred)

    # Create the pencil sketch by dividing the grayscale image by the inverted blurred image
    sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

    # Save the pencil sketch
    cv2.imwrite(output_path, sketch)

    # Display the original image and the pencil sketch
    cv2.imshow('Original Image', image)
    cv2.imshow('Pencil Sketch', sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Replace 'input_image.jpg' with your input image file and 'sketch.png' with the desired output file name
input_image_path = 'family.jpg'
output_image_path = 'family.png'
convert_to_sketch(input_image_path, output_image_path)
