#!/usr/bin/env python3

import json
import time
import os
from datetime import datetime
from elasticsearch import Elasticsearch
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ZeekLogHandler(FileSystemEventHandler):
    def __init__(self):
        self.es = Elasticsearch(['http://localhost:9200'])
        
    def process_log(self, file_path):
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    try:
                        data = json.loads(line)
                        log_type = os.path.basename(file_path).split('.')[0]
                        index_name = f"nids-zeek-{log_type}-{datetime.now().strftime('%Y.%m.%d')}"
                        self.es.index(index=index_name, document=data)
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith('.log'):
            self.process_log(event.src_path)

def main():
    path = "/opt/zeek/logs"
    event_handler = ZeekLogHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main() 