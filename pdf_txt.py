import pathlib as pl
import os
import keyboard
import time
import io

folder = r"path/to/folder/with/files/here"

def get_files(folder):
    import os
    os.chdir(folder)
    files = os.listdir()
    files = [x for x in files if x.endswith(".pdf")]
    return files 



def create_txt_files(path, filename):
    KILL_KEY = 'esc'
    read_path  = pl.Path(str(path + "\\" + filename))
    write_path = pl.Path(str(read_path.parent/read_path.stem) + ".txt")
    overwrite_file = os.path.exists(write_path)
    
    os.startfile(read_path)
    time.sleep(5)
    keyboard.press_and_release('alt')
    time.sleep(5)
    keyboard.press_and_release('f')
    time.sleep(5)
    keyboard.press_and_release('v')
    time.sleep(5)
    keyboard.write(str(write_path))
    time.sleep(5)
    keyboard.press_and_release('alt+s')
    time.sleep(5)
    if overwrite_file:
        keyboard.press_and_release('y')
        
    return 

#RUN FILE 
files = get_files(folder)    

for i in files:
    create_txt_files(folder, i)