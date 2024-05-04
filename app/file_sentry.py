import sys
import time
import logging
from app_logger import AppLogger
from watchdog.observers import Observer
from monitor import Monitor

if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else "/Users/brijeshpatel/Downloads"
    # logging.basicConfig(level=logging.INFO,
    #                     format='%(asctime)s - %(message)s',
    #                     datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    app_logger = AppLogger("/mnt/c/Users/brpat/Projects/file-sentry/logs/fim_logs")
    app_logger.log_event("start watching directory {directory!r}")

    # logging.info(f'start watching directory {directory!r}')
    event_handler = Monitor()
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