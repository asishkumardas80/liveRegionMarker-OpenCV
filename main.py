import tkinter as tk
from tkinter import filedialog
from display_images import display_images
from watchdog.observers import Observer
from watch_code import CodeChangeHandler
import threading
import time
import importlib

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Code Viewer")

        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.canvas = tk.Canvas(root)
        self.canvas.pack(fill="both", expand=True)

        self.image_label = tk.Label(self.canvas)
        self.image_label.pack()

        self.image_path = None
        self.original_image_path = None  # To store the path of the original image
        self.output_dir = "output_images"
        self.update_interval = 1  # Update interval in seconds
        self.start_code_watcher()

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_path = file_path
            self.original_image_path = file_path  # Save the original image path
            print(f"Original image loaded: {self.original_image_path}")  # Debug print
            self.process_image()

    def process_image(self):
        if self.original_image_path:
            print(f"Processing image: {self.original_image_path}")  # Debug print
            # Dynamically import and reload the 'mark_regions' module
            mark_regions = importlib.import_module('mark_regions')
            importlib.reload(mark_regions)
            print(f"Reloaded mark_regions module")  # Debug print
            
            # Call the updated 'mark_regions' function
            results = mark_regions.mark_regions([self.original_image_path], self.output_dir)
            marked_image_path = results[0]['image_path']
            print(f"Marked image path: {marked_image_path}")  # Debug print
            display_images(marked_image_path, self.canvas, self.image_label)
            print("UI refresh done")

    def start_code_watcher(self):
        self.code_watcher_thread = threading.Thread(target=self.watch_code_changes)
        self.code_watcher_thread.daemon = True
        self.code_watcher_thread.start()

    def watch_code_changes(self):
        event_handler = CodeChangeHandler(self.process_image)
        observer = Observer()
        observer.schedule(event_handler, path='.', recursive=False)
        observer.start()
        try:
            while True:
                time.sleep(self.update_interval)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()  # Corrected: Added parentheses to call the function
