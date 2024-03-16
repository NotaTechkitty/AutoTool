from recordModule.behavior import start_recording, stop_recording
from recordModule.convertRunFile import convert_to_pyautogui_script
from fileModule.fileModule import FileModule

from helper.datetime import convertUnixTime

fileModule = FileModule()



class RecordModule:
  _instance = None
  recording = [] 
  id = 0
  def __new__(cls):
    if not cls._instance:
      cls._instance = super(RecordModule, cls).__new__(cls)
    return cls._instance
  # declare behavior
  
  # start recording
  def start(self):
    start_recording()
    
  # convert into pyautogui code
  def readSavedFile(self):
    save_temp = fileModule.readTextFromFile("save_path_temp.txt")
    dataJson = fileModule.readJsonFile(save_temp)
    def excluded_actions(object):
        return "released" not in object["action"] and \
               "scroll" not in object["action"]

    record = list(filter(excluded_actions, dataJson))
    return record
  
  def convertScript(self, data):
    save_temp = fileModule.readTextFromFile("save_path_temp.txt")
    saveId = save_temp.split("_")[-1]
    convert_to_pyautogui_script(data,saveID=saveId)
  
  # stop recording
  def stop(self):
    stop_recording()

# Get the singleton instance
recordModule = RecordModule()