import cv2
import os

def mark_regions(image_paths, output_dir):
    all_results = []

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for image_path in image_paths:
        print(f"Reading image: {image_path}")  # Debug print
        image = cv2.imread(image_path)

        if image is None:
            print(f"Error loading image: {image_path}")
            continue

        # Define threshold of regions to ignore
        THRESHOLD_REGION_IGNORE = 40

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian Blur
        blur = cv2.GaussianBlur(gray, (9, 9), 0)

        # Adaptive threshold to detect regions with text
        thresh = cv2.adaptiveThreshold(
            blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY_INV, 11, 30
        )

        # Dilate to combine adjacent text contours
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
        dilate = cv2.dilate(thresh, kernel, iterations=4)

        # Find contours, highlight text areas, and extract ROIs
        cnts, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        line_items_coordinates = []
        for c in cnts:
            area = cv2.contourArea(c)
            x, y, w, h = cv2.boundingRect(c)

            # Ignore small regions based on threshold
            if w < THRESHOLD_REGION_IGNORE or h < THRESHOLD_REGION_IGNORE:
                continue

            # Draw rectangles around detected text regions
            print(f"Marking region: x={x}, y={y}, w={w}, h={h}")  # Debug print
            image = cv2.rectangle(image, (x, y), (x + w, y + h), color=(255, 0, 255), thickness=1)
            line_items_coordinates.append([(x, y), (x + w, y + h)])

        # Use a fixed name for the marked image
        marked_image_path = os.path.join(output_dir, "marked_image.png")

        print(f"Saving marked image to: {marked_image_path}")  # Debug print
        cv2.imwrite(marked_image_path, image)

        # Collect results
        all_results.append({
            'image_path': marked_image_path,
            'coordinates': line_items_coordinates
        })

    return all_results
