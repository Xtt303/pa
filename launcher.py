from customtkinter import *
import json
import os
import subprocess
SETTINGS_JSON="settings.json"

class ConnectWindow(CTk):
   def __init__(self):
       super().__init__()

       self.host = None
       self.port = None

       self.title('Launcher')
       self.geometry('500x480')
       set_appearance_mode("dark")
       set_default_color_theme("dark-blue")

       self.settings=self.load_settings()

       self.bild_ui()
       
   def bild_ui(self):
        CTkLabel(self, text='Розмфр екрану', font=('Comic Sans MS', 20, 'bold')).pack(pady=(10,0))
        CTkLabel(self, text='Ширина', font=('Comic Sans MS', 20, 'bold')).pack(pady=(5,0))
        self.entry_width=CTkEntry(self, placeholder_text='width ')
        self.entry_width.insert(0,str(self.settings["width"]))
        self.entry_width.pack(pady=5)
        CTkLabel(self, text='висота', font=('Comic Sans MS', 20, 'bold')).pack(pady=(5,0))
        self.entry_height=CTkEntry(self, placeholder_text='height ')
        self.entry_height.insert(0,self.settings["height"])
        self.entry_height.pack(pady=5)
        CTkLabel(self, text='гучність', font=('Comic Sans MS', 20, 'bold')).pack(pady=(5,0))
        self.slider=CTkSlider(self, from_=0, to=100)
        self.slider.set(self.settings["volume"])
        self.slider.pack(pady=10)
        
        
        self.host_entry = CTkEntry(self, placeholder_text='Введіть хост: ', height=50)
        self.host_entry.pack(padx=20, pady=15, anchor='w', fill='x')

        self.port_entry = CTkEntry(self, placeholder_text='Введіть порт сервера: ', height=50)
        self.port_entry.pack(padx=20, anchor='w', fill='x')

        CTkButton(self, text='Приєднатися', command=self.open_game,width=200, height=40).pack(pady=(15,10))

   def open_game(self):
       self.save_settings()
       subprocess.run(["pyhton","client.py"])
       self.host = self.host_entry.get()
       self.port = int(self.port_entry.get())
   def save_settings(self):
       settings={
           "width":int(self.entry_width.get()),
           "height":int(self.entry_height.get()),
           "volume":int(self.slider.get())
       }
       with open(SETTINGS_JSON,"w") as file:
           json.dump(settings,file,indent=4)
       self.destroy()
   def load_settings(self):
       if os.path.exists(SETTINGS_JSON):
           with open(SETTINGS_JSON,"r") as f:
               return json.load(f)
       return  {"width":800, "height":800, "volume":50} 

app = ConnectWindow()
app.mainloop()
