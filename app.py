import os
import cv2
import numpy as np

"""
This script analyzes images in a specified folder to calculate the ratio of white pixels (representing circle areas) 
to the total number of pixels in the image. It uses OpenCV for image processing.

Functions:
    get_img_names(folder_name):
        Returns a list of image names in the specified folder that start with 'B&W-'.
    get_img_path(folder_name, image_name):
        Constructs and returns the full path of an image given the folder name and image name.
    get_image(img_path):
        Loads and returns the image from the specified path.
    get_gray_image(image):
        Converts and returns the given image to grayscale.
    get_white_pixels(gray):
        Returns the count of white pixels (value 255) in the grayscale image.
    get_total_pixels(gray):
        Returns the total number of pixels in the grayscale image.
    get_total_area(image):
        Returns the total area (number of pixels) of the given image.
    get_black_pixels(total_pixels, white_pixels):
        Returns the count of black pixels by subtracting white pixels from total pixels.
    get_white_to_total_ratio(white_pixels, total_pixels):
        Returns the ratio of white pixels to total pixels as a percentage.
Usage:
    Change the `folder_name` variable to the folder you want to analyze.
    Run the script to print the analysis results for each image in the specified folder.
"""


# Load the image
def get_img_names(folder_name):
    return [img_name for img_name in os.listdir(f'Images/{folder_name}') if img_name.startswith('B&W-')]

def get_img_path(folder_name, image_name):
    return f'./Images/{folder_name}/{image_name}'

def get_image(img_path):
    return cv2.imread(img_path)

def get_gray_image(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def get_white_pixels(gray):
    return np.sum(gray == 255)

def get_total_pixels(gray):
    return gray.size

def get_total_area(image):
    return image.shape[0] * image.shape[1]

def get_black_pixels(total_pixels, white_pixels):
    return total_pixels - white_pixels

def get_white_to_total_ratio(white_pixels, total_pixels):
    return white_pixels*100 / total_pixels

if __name__ == '__main__':
    folder_name = 'YOUR_FOLDER_NAME'
    img_names_lst = get_img_names(folder_name)
    for img_name in img_names_lst:
        img_path = get_img_path(folder_name, img_name)
        image = get_image(img_path)
        # Convert to grayscale
        gray = get_gray_image(image)
        # Count white pixels (representing the area of the circles)
        white_pixels = get_white_pixels(gray)
        # Count total pixels in the image
        total_pixels = get_total_pixels(gray)
        # Calculate black pixels (total pixels - white pixels)
        black_pixels = get_black_pixels(total_pixels, white_pixels)
        # Calculate the ratio of White area to total image area
        white_to_total_ratio = get_white_to_total_ratio(white_pixels, total_pixels)
        print(f"Image path: {img_path}")
        print(f"Total Pixels: {total_pixels}")
        print(f"White Pixels (circle area): {white_pixels}")
        print(f"Black Pixels (background area): {black_pixels}")
        print(f"Ratio of White Area to Total Area: {white_to_total_ratio:.4f}")
        print("-" * 100)

