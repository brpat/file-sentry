from watchdog.events import FileSystemEvent, FileSystemEventHandler
from file_handler import FileHandler
# from app_logger import AppLogger

class Monitor(FileSystemEventHandler):
    def on_any_event(self, event) -> None:
        src_path = event.src_path
        event_type = event.event_type
        is_directory = event.is_directory
        is_synthetic = event.is_synthetic

        if is_directory == True:
            print("Directory Event:", src_path)

        else:
            if event_type == 'created':
                print("File Event: File Create:d", src_path)

            if event_type == "deleted":
                print("File Event: File Deleted:", src_path)

            if event_type == "modified":
                print("File Event: File Modified:", src_path)
        
