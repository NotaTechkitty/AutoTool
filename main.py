from recordModule.record import RecordModule
from encrypt.encryptModule import EncryptModule

def main():
  
  # start record mouse and keyboard action
  print("Recording start !")
  recordModule = RecordModule()
  recordModule.start()
  

if __name__ == "__main__":
  main()