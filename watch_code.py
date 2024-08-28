import importlib
from watchdog.events import FileSystemEventHandler
import mark_regions  # Ensure this is imported for reloading

class CodeChangeHandler(FileSystemEventHandler):
    def __init__(self, update_callback):
        super().__init__()
        self.update_callback = update_callback

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f"Detected changes in: {event.src_path}")  # Debug print
            # Reload the mark_regions module
            importlib.reload(mark_regions)
            print(f"Reloaded mark_regions module")  # Debug print
            # Call the update callback to refresh the image
            self.update_callback()
