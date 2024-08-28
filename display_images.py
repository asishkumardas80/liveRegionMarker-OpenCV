import tkinter as tk
from PIL import Image, ImageTk

def display_images(image_path, canvas, image_label):
    try:
        print(f"Displaying image: {image_path}")  # Debug print
        img = Image.open(image_path)
        img = img.resize((800, 600), Image.LANCZOS)  # Use Image.LANCZOS for better quality
        tk_img = ImageTk.PhotoImage(img)

        # Clear the canvas before displaying the new image
        canvas.delete("all")

        # Update the label with the new image
        image_label.config(image=tk_img)
        image_label.image = tk_img  # Keep a reference to avoid garbage collection
    except FileNotFoundError:
        print(f"File not found: {image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")  # General error handling
