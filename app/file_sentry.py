import sys
import time
import logging
from watchdog.observers import Observer
from handler import Handler


if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else "/Users/brijeshpatel/Downloads"
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    logging.info(f'start watching directory {directory!r}')
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    finally:
        observer.join()

