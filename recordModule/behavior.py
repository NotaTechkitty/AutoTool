"""
Records mouse and keyboard and outputs the actions
to a JSON file recording.json 

To end recording:
- Hold right click for 2 seconds then release to end the recording for mouse.
- Press 'ESC' to end the recording for keyboard.
- Both are needed to finish recording.
"""
import time
import json
from pynput import mouse, keyboard
from helper.datetime import convertUnixTime
from fileModule.fileModule import FileModule
from encrypt.encryptModule import EncryptModule

recording = [] 
count = 0
fileModule = FileModule()
encryptModule = EncryptModule()

current_time_seconds = time.time()
local_time = time.localtime(current_time_seconds)

def on_press(key):
    try:
        json_object = {
            'action':'pressed_key', 
            'key':key.char, 
            '_time': time.time()
        }
    except AttributeError:
        if key == keyboard.Key.esc:
            print("Keyboard recording ended.")
            return False

        json_object = {
            'action':'pressed_key', 
            'key':str(key), 
            '_time': time.time()
        }
        
    recording.append(json_object)


def on_release(key):
    try:
        json_object = {
            'action':'released_key', 
            'key':key.char, 
            '_time': time.time()
        }
    except AttributeError:
        json_object = {
            'action':'released_key', 
            'key':str(key), 
            '_time': time.time()
        }

    recording.append(json_object)
        

def on_move(x, y):
    if len(recording) >= 1:
        if (recording[-1]['action'] == "pressed" and \
            recording[-1]['button'] == 'Button.left') or \
            (recording[-1]['action'] == "moved" and \
            time.time() - recording[-1]['_time'] > 0.02):
            json_object = {
                'action':'moved', 
                'x':x, 
                'y':y, 
                '_time':time.time()
            }

            recording.append(json_object)


def on_click(x, y, button, pressed):
    json_object = {
        'action':'clicked' if pressed else 'unclicked', 
        'button':str(button), 
        'x':x, 
        'y':y, 
        '_time':time.time()
    }

    recording.append(json_object)

    if len(recording) > 1:
        if recording[-1]['action'] == 'unclicked' and \
           recording[-1]['button'] == 'Button.right' and \
           recording[-1]['_time'] - recording[-2]['_time'] > 2:
            stop_recording()
            print("Mouse recording ended.")
            return False


def on_scroll(x, y, dx, dy):
    json_object = {
        'action': 'scroll', 
        'vertical_direction': int(dy), 
        'horizontal_direction': int(dx), 
        'x':x, 
        'y':y, 
        '_time': time.time()
    }

    recording.append(json_object)

def stop_recording():
    save_path = fileModule.readTextFromFile("constants/save_path.txt")
    filepath = save_path + "temp_save_{}".format(convertUnixTime())

    fileModule.writeJsonFile(filepath, recording)
    
    fileModule.writeTextFile("save_path_temp.txt", filepath)

def start_recording():
    keyboard_listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)

    mouse_listener = mouse.Listener(
            on_click=on_click,
            on_scroll=on_scroll,
            on_move=on_move)

    keyboard_listener.start()
    mouse_listener.start()
    keyboard_listener.join() 
    mouse_listener.join()
    



# if __name__ == "__main__":
#     start_recording()
    