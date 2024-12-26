# Project Description

The script uses OpenCV for image processing and calculates the ratio of white pixels (representing circle areas) to the total number of pixels in each image.

## Steps to Run

1. **Open the Repository in a Devcontainer:**
    - Ensure you have the necessary tools to open the repository in a devcontainer.
2. **Install Dependencies:**
    - The devcontainer setup will handle the installation of all required packages and dependencies.

3. **Run the Application:**
    - Execute the `app.py` script to analyze the images.
    - Use the following command to run the script:
      ```bash
      python app.py
      ```

## Notes

- Refer to the `devcontainer.json` file for more details on the development container configuration.
- Ensure that all image files to be analyzed are placed in the appropriate directory as specified in the app.py script. The following guidelines should be followed to ensure proper integration with the code:

  1. **Folder Structure:**

      All images should be placed inside the Images/ directory, which is located at the root level of the repository.
      Within the Images/ directory, create subfolders for each specific category or group of images. Each subfolder should be named according to the context of the images, such as CategoryA, CategoryB, or any other relevant name.

  2. **Naming Convention:**

      The code expects images with filenames starting with the prefix B&W- in order to process them. For example, an image file could be named B&W-image001.jpg or B&W-sample.png.
      Ensure that all images to be analyzed follow this naming convention to ensure they are detected and processed correctly.