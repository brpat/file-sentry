from watchdog.events import FileSystemEvent, FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def on_any_event(self, event) -> None:
        src_path = event.src_path
        event_type = event.event_type
        is_directory = event.is_directory
        is_synthetic = event.is_synthetic

        if is_directory == True:
            return

        if event_type == 'created':
            print(event)
