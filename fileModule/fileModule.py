import os
import json


class FileModule:
  _instance = None
 
  def __new__(cls):
    if not cls._instance:
      cls._instance = super(FileModule, cls).__new__(cls)
    return cls._instance
  # declare behavior
  
  # start recording
  
  def checkExist(self, file_path):
    if os.path.exists(file_path):
     print("File exists")
    else:
     print("File does not exist")
     
  def writeJsonFile(self, fileName, data):
    with open("{}.json".format(fileName), 'w') as f:
        json.dump(data, f)

  def openFileData(self, filePath):
    with open(filePath, 'rb') as f:
      data = f.read()
      return data
      
  def readTextFromFile(self, filePath):
    with open(filePath, 'r') as f:
      data = f.read().replace('\n', '')
      return data 
      
  def writeTextFile(self, filePath, data):
    with open(filePath, 'w') as f:
      f.write(data)
    
  def writeFile(self, filePath, data):
    with open(filePath, 'wb') as f:
      f.write(data)

# Get the singleton instance
fileModule = FileModule()