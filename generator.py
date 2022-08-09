import tkinter
from tkinter import Tk
from secrets import choice
from tkinter.constants import END
import customtkinter




uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*","(",")","-","_","+","=","[","]","{","}","|",";",":","'",",","<",".",">","/","?","`","~"," "]



class PasswordGenerator(): # class for password generator
    
    def __init__(self): # constructor

        self.window = Tk() # create window
        self.window.title("Password Generator") # set title
        self.window.geometry("450x245") # set size
        self.window.configure(bg='#2a2d2e')


       
        self.length_entry_box = customtkinter.CTkEntry(self.window, 
                                                       width=220, 
                                                       height = 30, 
                                                       border_width = 2, 
                                                       corner_radius = 10,
                                                       placeholder_text="Enter number of characters",
                                                       text_font=("Roboto Medium", -16)) # create entry box for length of password
        self.length_entry_box.pack(padx=20, pady=20) # pack entry box for length of password

        # Declaring feedback if no length is found
        
        
        self.feedback = customtkinter.CTkLabel(self.window, 
                                               width=120, 
                                               height=25, 
                                               corner_radius=8) # create feedback label for no length found

        
        self.password_entry_box = customtkinter.CTkEntry(self.window, 
                                                         text="", 
                                                         width=275, 
                                                         height = 30, 
                                                         border_width = 2, 
                                                         corner_radius = 10,
                                                         text_font=("Roboto Medium", -16)) # create entry box for generated password
        self.password_entry_box.pack(pady=20) # pack entry box for generated password 

        # Frame for buttons
        self.button_frame = customtkinter.CTkFrame(self.window, 
                                                   width = 125, 
                                                   height = 35,
                                                   corner_radius=10) # create frame for buttons
        self.button_frame.pack(pady=20) # pack frame for buttons 

        # Generate Password Button
        generate_btn = customtkinter.CTkButton(self.button_frame, 
                                               corner_radius=8, 
                                               width = 120, 
                                               height = 35, 
                                               border_width = 0, 
                                               text="Generate Password", 
                                               command=self.generate_random_password,
                                               text_font=("Roboto Medium", -16)) # create button for generating password
        
        generate_btn.grid(row=0, column=0, padx=10) # pack button for generating password

        # Copy Password Button
        copy_btn = customtkinter.CTkButton(self.button_frame, 
                                           text="Copy Password", 
                                           corner_radius=8,
                                           width = 120, 
                                           height = 35, 
                                           border_width = 0, 
                                           command=self.copy_password,
                                           text_font=("Roboto Medium", -16)) # create button for copying password to clipboard 
        copy_btn.grid(row=0, column=1, padx=10) # place copy button next to generate button

 
    
    def generate_random_password(self): # function for generating password
        self.password_entry_box.delete(0, END) # delete text in entry box for password to prevent duplicate passwords 
        try:  # try to get length of password from entry box 
            password_length = int(self.length_entry_box.get()) # get length of password from entry box 
            self.feedback.destroy()  # Destroy feedback if length is there
            data = uppercase + lowercase + numbers + symbols # create list of all possible characters for password
            password = ''.join(choice(data) for _ in range(password_length)) # create password by randomly choosing characters from list 
            self.password_entry_box.insert(0, password) # insert password into entry box 
        except ValueError: # if no length is found 
            text_var = tkinter.StringVar(value="Please enter number of characters") # create text variable for feedback 
            self.feedback = customtkinter.CTkLabel(self.window,  
                                                   corner_radius = 8, 
                                                   height = 25, 
                                                   width = 120,  
                                                   textvariable = text_var,
                                                    fg_color=("red"),
                                                   text_font=("Roboto Medium", -12)) # create feedback label for no length found 
            self.feedback.place(x=224, y=135, anchor=tkinter.CENTER) # place feedback label 

    def copy_password(self): # function for copying password to clipboard
        self.window.clipboard_clear() # clear clipboard 
        self.window.clipboard_append(self.password_entry_box.get()) # copy password to clipboard 
    

        
    
    
    
    
    
if __name__ == "__main__": # if program is run directly, run main function
    PasswordGenerator().window.mainloop()      # run main function of class PasswordGenerator and run window loop to keep window open until closed 