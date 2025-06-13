from tkinter import filedialog
from tkinter import messagebox

class UserInputManger():
    @staticmethod
    def select_file():
        path = filedialog.askopenfilename()
        if path == "" :
            return None
        return path
    @staticmethod
    def  ask_yes_or_no(title, question):
        return  messagebox.askyesno(title, question) 
