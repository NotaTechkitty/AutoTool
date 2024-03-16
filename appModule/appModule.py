import tkinter as tk
from recordModule.record import RecordModule
from storeModule.storeModule import StoreModule

default_window_size = "400x300"
recordModule = RecordModule()
storeModule = StoreModule()


class AppModule:
    root = tk.Tk()
    
    def __init__(self):
        self.initApp()
        self.initElement()
    
    def initApp(self):
        self.root.title("Auto Tool")
        self.root.geometry(default_window_size)
    
    def initElement(self):
        
        def record_start():
            # Function to be executed when the button is clicked
            recordModule.start()
         
        def GenerateScript():
            dataRecording = recordModule.readSavedFile()
            script_path = recordModule.convertScript(dataRecording)
            storeModule.set("cur_script_path",script_path)
         
        def run_script():
            script_path = storeModule.get("cur_script_path")
            if not script_path:
                return
            recordModule.runScript(script_path)
        
        label = tk.Label(self.root, text="Auto Tool!")
        label.pack() 

        # Button start the record 
        label = tk.Label(self.root, text="Nút ghi lại hành động phím chuột")
        label.pack() 
        button = tk.Button(self.root, text="Record", command=record_start)
        button.pack()
        
        # Button generate script file based on recording
        label = tk.Label(self.root, text="Nút tạo lại file script")
        label.pack() 
        button = tk.Button(self.root, text="Generate Script", command=GenerateScript)
        button.pack()
        
        # Button execute script file 
        label = tk.Label(self.root, text="Nút chạy script")
        label.pack() 
        button = tk.Button(self.root, text="Run", command=run_script)
        button.pack()
            
    def app(self):
        
        self.root.mainloop()