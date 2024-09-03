

# OpenCV Image Processing Toolkit

**OpenCV Image Processing Toolkit** is a Python-based tool that integrates OpenCV with real-time code reloading. Featuring a Tkinter-based GUI, users can load images, apply various OpenCV techniques, and see updates instantly. The toolkit supports live code reloading, ensuring any changes in the code reflect in real-time without restarting the application.

This toolkit is designed for users of all skill levels who want to explore OpenCV techniques in a hands-on environment. It offers flexibility to experiment with various image processing functionalities and see immediate results.

## Features

- **Image Processing**: Apply a variety of OpenCV image processing techniques, including filtering, thresholding, and edge detection.
- **Image Transformation**: Perform geometric transformations such as rotation and translation.
- **Image Segmentation**: Segment images into meaningful regions using thresholding and contour detection.
- **Text Recognition (OCR)**: Extract text from images using OCR technology.
- **Object Detection and Recognition**: Detect and recognize objects in images using object detection algorithms.

## Requirements

Ensure you have Python 3.8 or higher installed. Install the required packages using `pip`:

```plaintext
Flask==3.0.3
opencv-python==4.10.0.84
pytesseract==0.3.13
pdf2image==1.17.0
Pillow==10.4.0
watchdog==4.0.2
matplotlib==3.9.2
numpy==2.0.0
pandas==2.2.2
```

To install all dependencies, run:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/asishkumardas80/OpenCV-Image-Processing-Toolkit.git
    cd OpenCV-Image-Processing-Toolkit
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```bash
    python main.py
    ```

2. The Tkinter-based GUI will launch, allowing you to:

   - **Load an image** using the **"Load Image"** button.
   - **Apply various OpenCV techniques** directly from the UI.
   - **View live updates** as you modify image processing code.

## Project Structure

- **`main.py`**: Initializes the Tkinter GUI and handles image processing and code watching.
- **`image_processing.py`**: Contains functions for filtering, transformations, and object detection.
- **`display_images.py`**: Handles image display on the Tkinter canvas.
- **`watch_code.py`**: Watches for code changes and reloads the updated modules automatically.

## Study and Implementation

### Implemented Features

#### Image Processing

- **`apply_gaussian_blur(image)`**
  - **Description**: Applies Gaussian Blur to smooth the image, reducing noise.
  - **How it Works**: Uses `cv2.GaussianBlur()` with a kernel size to reduce image noise and detail.

- **`apply_canny_edge_detection(image)`**
  - **Description**: Detects edges in the image using the Canny algorithm.
  - **How it Works**: Converts the image to grayscale, applies Gaussian Blur, and then uses `cv2.Canny()` to detect sharp changes in intensity.

- **`apply_global_threshold(image)`**
  - **Description**: Converts the image to a binary format using global thresholding.
  - **How it Works**: Converts the image to grayscale and applies a fixed threshold to binarize the image.

- **`apply_adaptive_threshold(image)`**
  - **Description**: Binarizes the image using adaptive thresholding, suitable for varying lighting conditions.
  - **How it Works**: Divides the image into regions and applies thresholding to each using `cv2.adaptiveThreshold()`.

- **`apply_morphological_operations(image)`**
  - **Description**: Refines image features using dilation and erosion.
  - **How it Works**: Applies `cv2.dilate()` and `cv2.erode()` to adjust image features, typically after thresholding.

- **`apply_median_blur(image)`**
  - **Description**: Applies median blur to reduce noise while preserving edges.
  - **How it Works**: Replaces each pixel’s value with the median of neighboring pixels using `cv2.medianBlur()`.

- **`apply_bilateral_filter(image)`**
  - **Description**: Smoothens the image while preserving edges using bilateral filtering.
  - **How it Works**: Reduces noise and preserves edges with `cv2.bilateralFilter()`, making it useful for photo editing.


### Future Implementations

The following features are planned for future releases to enhance the toolkit:

#### Image Transformation

- **`apply_rotation(image, angle)`**
  - **Description**: Rotates the image by a given angle.
  - **How it Works**: Uses an affine transformation to rotate the image by computing a rotation matrix.

- **`apply_translation(image, x_shift, y_shift)`**
  - **Description**: Translates the image horizontally and vertically by the specified amounts.
  - **How it Works**: Constructs a translation matrix and shifts the image accordingly.

#### Image Segmentation

- **`find_contours(image)`**
  - **Description**: Detects contours in a binary image.
  - **How it Works**: Converts the image to grayscale, applies binary thresholding, and uses `cv2.findContours()` to identify object boundaries.

- **`draw_contours(image, contours)`**
  - **Description**: Draws detected contours on the image.
  - **How it Works**: Uses `cv2.drawContours()` to highlight the contours on a copy of the original image.

#### Text Recognition (OCR)

- **`apply_ocr(image)`**
  - **Description**: Extracts text from an image using OCR technology.
  - **How it Works**: Utilizes `pytesseract` to recognize and extract text from images.

#### Object Detection and Recognition

- **`detect_objects(image)`**
  - **Description**: Identifies and labels objects in the image.
  - **How it Works**: Utilizes object detection algorithms to detect objects and classify them using pre-trained models.

---


## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

## Raising an Issue

If you encounter any problems or have questions, please [raise an issue](https://github.com/asishkumardas80/OpenCV-Image-Processing-Toolkit/issues) on GitHub. Provide detailed information to help us resolve the issue effectively.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---