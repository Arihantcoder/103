import os 
import shutil
import sys
import time
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

fromdir="C:/Users/ariha/Downloads"
todir="C:/Users/ariha/Documents"

dir_tree = { "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
             "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'], 
             "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'], 
             "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'] }

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        name,extension=os.path.splitext(event.src_path)
        time.sleep(1)

        for key,value in dir_tree.items():
            time.sleep(1)
            if extension in value :
                filename=os.path.basename(event.src_path)
                print("downloaded "+filename)
    def on_deleted(self, event):
        print('somebody deleted'+event.src_path)
    def on_modifed (self,event):
        print('somebody modified'+event.src_path)



eventhandler=FileMovementHandler()
observer=Observer()
observer.schedule(eventhandler,fromdir,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running ")
except KeyboardInterrupt:
    print("stop")
    observer.stop()
    
                   

        