import tkinter
from tkinter import Tk, Text
from secrets import choice
from tkinter.constants import END
from turtle import width
import customtkinter
customtkinter.set_appearance_mode("dark")


uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*","(",")","-","_","+","=","[","]","{","}","|",";",":","'",",","<",".",">","/","?","`","~"," "]



class PasswordGenerator(customtkinter.CTk):
    
    def __init__(self):


        self.window = Tk()

        self.window.title("Password Generator")
        self.window.geometry("450x245")



        # Entry box for number of characters
        self.length_entry_box = customtkinter.CTkEntry(self.window, 
                                                       width=220, 
                                                       height = 30, 
                                                       border_width = 2, 
                                                       corner_radius = 10,
                                                       placeholder_text="Enter number of characters",
                                                       text_font=("Roboto Medium", -16))
        self.length_entry_box.pack(padx=20, pady=20)

        # Declaring feedback if no length is found
        self.feedback = customtkinter.CTkLabel(self.window, 
                                               width=120, 
                                               height=25, 
                                               corner_radius=8)

        # Entry box for password
        self.password_entry_box = customtkinter.CTkEntry(self.window, 
                                                         text="", 
                                                         width=275, 
                                                         height = 30, 
                                                         border_width = 2, 
                                                         corner_radius = 10,
                                                         text_font=("Roboto Medium", -16))
        self.password_entry_box.pack(pady=20)

        # Frame for buttons
        self.button_frame = customtkinter.CTkFrame(self.window, 
                                                   width = 125, 
                                                   height = 35,
                                                   fg_color=("#f2f2f2"),
                                                   corner_radius=10)
        self.button_frame.pack(pady=20)

        # Generate Password Button
        generate_btn = customtkinter.CTkButton(self.button_frame, 
                                               corner_radius=8, 
                                               width = 120, 
                                               height = 35, 
                                               border_width = 0, 
                                               text="Generate Password", 
                                               command=self.generate_random_password,
                                               text_font=("Roboto Medium", -16))
        generate_btn.grid(row=0, column=0, padx=10)

        # Copy Password Button
        copy_btn = customtkinter.CTkButton(self.button_frame, 
                                           text="Copy Password", 
                                           corner_radius=8,
                                           width = 120, 
                                           height = 35, 
                                           border_width = 0, 
                                           command=self.copy_password,
                                           text_font=("Roboto Medium", -16))
        copy_btn.grid(row=0, column=1, padx=10)

 

    def generate_random_password(self):
        self.password_entry_box.delete(0, END)
        try:
            password_length = int(self.length_entry_box.get())
            self.feedback.destroy()  # Destroy feedback if length is there
            data = uppercase + lowercase + numbers + symbols
            password = ''.join(choice(data) for _ in range(password_length))
            self.password_entry_box.insert(0, password)
        except ValueError:
            text_var = tkinter.StringVar(value="Please enter number of characters")
            self.feedback = customtkinter.CTkLabel(self.window,  
                                                   corner_radius = 8, 
                                                   height = 25, 
                                                   width = 120,  
                                                   textvariable = text_var,
                                                    fg_color=("black"),
                                                   text_font=("Roboto Medium", -10))
            self.feedback.place(x=224, y=130, anchor=tkinter.CENTER)

    def copy_password(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(self.password_entry_box.get())
        
    
    
    
    
    
if __name__ == "__main__":
    PasswordGenerator().window.mainloop()     