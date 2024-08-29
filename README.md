
---

# liveRegionMarker-OpenCV

**liveRegionMarker-OpenCV** is a Python application that allows real-time image marking with OpenCV, integrated with live code reloading. This project provides a GUI to load images, mark regions using custom code, and automatically update the UI with the latest marked images whenever the code changes.

## Features

- **Load Images**: Load images from your local filesystem.
- **Real-Time Marking**: Mark regions on images using OpenCV and see updates in real-time.
- **Live Code Reloading**: Automatically reload and apply changes from the `mark_regions` module without restarting the application.
- **GUI Integration**: A Tkinter-based GUI to interact with the application.

## Requirements

Ensure you have Python 3.8 or higher installed. You can install the required packages using `pip`. Here's the list of packages required for the project:

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

To install the dependencies, use the following command:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/asishkumardas80/liveRegionMarker-OpenCV.git
    cd liveRegionMarker-OpenCV
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main Python script:

    ```bash
    python main.py
    ```

2. The application will launch a Tkinter-based GUI where you can:

   - Click the **"Load Image"** button to load an image.
   - The application will process the image and display it.
   - The `mark_regions` module is used to mark regions on the image.
   - Any changes made to the `mark_regions` module will be automatically applied, and the image will be updated in real-time.

## Project Structure

- **`main.py`**: The main script that initializes the Tkinter GUI and handles image processing and code watching.
- **`mark_regions.py`**: Contains functions to mark regions on images. This module is dynamically reloaded when code changes are detected.
- **`display_images.py`**: Handles the display of images on the Tkinter canvas.
- **`watch_code.py`**: Manages live code reloading by watching for changes in the code files.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

## Raising an Issue

If you encounter any problems or have questions, please [raise an issue](https://github.com/asishkumardas80/liveRegionMarker-OpenCV/issues) on GitHub. Provide as much detail as possible to help us address the issue effectively.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify any sections to better fit your needs or add more specific instructions if needed!
