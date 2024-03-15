from recordModule.behavior import start_recording, stop_recording

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
    
  
  # stop recording
  def stop(self):
    stop_recording()

# Get the singleton instance
recordModule = RecordModule()