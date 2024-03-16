from recordModule.behavior import start_recording, stop_recording
from recordModule.convertRunFile import convert_to_pyautogui_script
from fileModule.fileModule import FileModule

from helper.datetime import convertUnixTime

fileModule = FileModule()



class StoreModule:
  _instance = None
  
  state= {
      "cur_script_path": ""
  }
    
  def __new__(cls):
    if not cls._instance:
      cls._instance = super(StoreModule, cls).__new__(cls)
    return cls._instance
  # declare method
  def get(self, attr=""):
      if not attr:
          return self.state
      return self.state[attr]
  
  def set(self, key, data):
      self.state[key] = data
 
# Get the singleton instance
storeModule = StoreModule()