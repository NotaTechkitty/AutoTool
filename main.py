from recordModule.record import RecordModule

def main():
  
  # start record mouse and keyboard action
  # print("Recording start !")
  recordModule = RecordModule()
  # recordModule.start()
  
  dataRecording = recordModule.readSavedFile()
  recordModule.convertScript(dataRecording)

if __name__ == "__main__":
  main()