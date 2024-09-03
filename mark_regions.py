import cv2
import os
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk

# Function to apply Gaussian Blur to an image
def apply_gaussian_blur(image):
    """Applies Gaussian Blur to the input image to reduce noise."""
    return cv2.GaussianBlur(image, (9, 9), 0)

# Function to apply Canny Edge Detection to an image
def apply_canny_edge_detection(image):
    """
    Applies Canny Edge Detection to the input image.
    - Converts the image to grayscale if it is in color.
    - Applies Gaussian Blur to reduce noise.
    - Detects edges using the Canny algorithm.
    """
    if image is None:
        raise ValueError("Image is not loaded correctly.")
    
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif len(image.shape) == 2:
        gray = image
    else:
        raise ValueError("Unsupported image format.")
    
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    
    return edges

# Function to apply global thresholding to an image
def apply_global_threshold(image):
    """
    Applies global thresholding to convert the image to binary format.
    - Converts image to grayscale.
    - Applies binary thresholding.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return binary_image

# Function to apply adaptive thresholding to an image
def apply_adaptive_threshold(image):
    """
    Applies adaptive thresholding to convert the image to binary format.
    - Converts image to grayscale.
    - Applies adaptive thresholding with Gaussian mean.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                            cv2.THRESH_BINARY_INV, 11, 2)
    return adaptive_thresh

# Function to apply morphological operations to an image
def apply_morphological_operations(image):
    """
    Applies morphological operations (dilation and erosion) to the image.
    - Uses a rectangular kernel for operations.
    - Dilates and then erodes the image to refine features.
    """
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
    dilated_image = cv2.dilate(image, kernel, iterations=4)
    eroded_image = cv2.erode(dilated_image, kernel, iterations=4)
    return eroded_image

# Function to convert an image to HSV color space
def convert_to_hsv(image):
    """Converts the image to HSV color space."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Function to convert an image to grayscale
def convert_to_grayscale(image):
    """Converts the image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Function to analyze histogram of an image
def analyze_histogram(image):
    """
    Analyzes the histogram of the grayscale version of the image.
    - Converts image to grayscale.
    - Calculates histogram with 256 bins.
    """
    gray = convert_to_grayscale(image)
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    return hist

# Function to apply median blur to an image
def apply_median_blur(image):
    """Applies median blur to the image to reduce noise while preserving edges."""
    return cv2.medianBlur(image, 5)

# Function to apply bilateral filter to an image
def apply_bilateral_filter(image):
    """
    Applies bilateral filter to the image for noise reduction while preserving edges.
    - Uses a diameter of 9, sigma values of 75.
    """
    return cv2.bilateralFilter(image, 9, 75, 75)

# Function to rotate an image by a given angle
def apply_rotation(image, angle):
    """
    Rotates the image by the specified angle.
    - Calculates the rotation matrix.
    - Applies affine transformation to rotate the image.
    """
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, matrix, (w, h))
    return rotated

# Function to translate an image by a given shift in x and y directions
def apply_translation(image, x_shift, y_shift):
    """
    Translates the image by the specified x and y shifts.
    - Creates a translation matrix.
    - Applies affine transformation for translation.
    """
    matrix = np.float32([[1, 0, x_shift], [0, 1, y_shift]])
    translated = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))
    return translated

# Function to find contours in an image
def find_contours(image):
    """
    Finds contours in the binary image.
    - Converts the image to grayscale.
    - Applies binary thresholding.
    - Finds contours in the thresholded image.
    """
    gray = convert_to_grayscale(image)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

# Function to draw contours on an image
def draw_contours(image, contours):
    """
    Draws the given contours on a copy of the image.
    - Uses green color for contour lines.
    """
    return cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)

# Function to mark regions and apply various image processing techniques
def mark_regions(image_paths, output_dir, viewer=None):
    """
    Processes images, applies various image processing techniques, and saves the results.
    - Applies Gaussian blur, global and adaptive thresholding, morphological operations, Canny edge detection, and more.
    - Finds and marks contours in the image.
    - Saves the processed image and returns results.
    - Optionally updates the Tkinter image viewer with the processed image.
    """
    all_results = []

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for image_path in image_paths:
        print(f"Reading image: {image_path}")  # Debug print
        image = cv2.imread(image_path)

        if image is None:
            print(f"Error loading image: {image_path}")
            continue

        # Invert Colors (commented out as per your request)
        # inverted_image = invert_colors(image)
        inverted_image = image

        # Convert to grayscale for some operations
        gray = convert_to_grayscale(inverted_image)

        # Apply Gaussian Blur
        blur = apply_gaussian_blur(gray)

        # Apply Global Thresholding
        global_thresh = apply_global_threshold(inverted_image)

        # Apply Adaptive Thresholding
        adaptive_thresh = apply_adaptive_threshold(inverted_image)

        # Apply Morphological Operations
        morph_ops = apply_morphological_operations(adaptive_thresh)

        # Apply Canny Edge Detection
        edges = apply_canny_edge_detection(blur)

        # Apply Bilateral Filter
        bilateral_filtered = apply_bilateral_filter(inverted_image)

        # Apply Rotation (example: 45 degrees)
        rotated_image = apply_rotation(inverted_image, 45)

        # Apply Translation (example: 100px right, 50px down)
        translated_image = apply_translation(inverted_image, 100, 50)

        # Apply Median Blur
        median_blur = apply_median_blur(inverted_image)

        # Analyze Histogram
        hist = analyze_histogram(inverted_image)

        # Find and draw contours
        contours = find_contours(inverted_image)
        image_with_contours = draw_contours(inverted_image, contours)

        # Find contours on the adaptive threshold image
        cnts, _ = cv2.findContours(morph_ops, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        line_items_coordinates = []
        for c in cnts:
            area = cv2.contourArea(c)
            x, y, w, h = cv2.boundingRect(c)

            if w < 40 or h < 40:
                continue

            print(f"Marking region: x={x}, y={y}, w={w}, h={h}")  # Debug print
            inverted_image = cv2.rectangle(inverted_image, (x, y), (x + w, y + h), color=(255, 0, 255), thickness=2)
            line_items_coordinates.append([(x, y), (x + w, y + h)])

        marked_image_path = os.path.join(output_dir, "marked_image.png")

        print(f"Saving marked image to: {marked_image_path}")  # Debug print
        cv2.imwrite(marked_image_path, inverted_image)

        # Update the Tkinter viewer with the marked image if viewer is provided
        if viewer:
            viewer.update_image(inverted_image)

        # Clean up OpenCV windows
        cv2.destroyAllWindows()

        all_results.append({
            'image_path': marked_image_path,
            'coordinates': line_items_coordinates,
            'histogram': hist  # Include histogram data if needed
        })

    return all_results

# Tkinter Image Viewer class for updating image display in the same window
class ImageViewer:
    def __init__(self, root):
        """Initializes the Tkinter window and canvas for image display."""
        self.root = root
        self.root.title("Image Viewer")
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()
        self.image_id = None

    def update_image(self, image):
        """
        Updates the displayed image in the Tkinter canvas.
        - Converts OpenCV image (BGR) to PIL image (RGB).
        - Updates the existing canvas image or creates a new one if needed.
        """
        # Convert OpenCV image (BGR) to PIL image (RGB)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_image)
        tk_image = ImageTk.PhotoImage(pil_image)

        if self.image_id is not None:
            self.canvas.delete(self.image_id)
        
        self.image_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
        self.root.update_idletasks()  # Update the Tkinter GUI

def main():
    """Main function to initialize Tkinter window and image viewer."""
    root = tk.Tk()
    viewer = ImageViewer(root)

    # Example usage
    image_paths = ["your_image.png"]  # Load your images
    output_dir = "output_images"  # Define your output directory

    mark_regions(image_paths, output_dir, viewer)

    root.mainloop()

if __name__ == "__main__":
    main()
