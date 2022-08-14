from database import init_database 
import tkinter
from tkinter.constants import BOTH, CENTER, END, LEFT, RIGHT, VERTICAL, Y
from tkinter import Canvas
from functools import partial
from vault import VaultMethods
import customtkinter
import hashlib
from generator import PasswordGenerator



customtkinter.set_default_color_theme("blue") # set default color theme
 # set default appearance mode

class PasswordManager(customtkinter.CTk): # class for password manager 

    def __init__(self): # constructor for password manager
        self.db, self.cursor = init_database() # initialize database and cursor for database operations 
        self.window = customtkinter.CTk() # create window for password manager
        self.window.update() # update window 
        self.window.title("Password Manager") # set title for window 
        self.window.geometry("650x400") # set size of window 
        

    def welcome_new_user(self): # function to welcome new user 
        self.window.geometry("450x250") # set size of window 

        
        text_var = tkinter.StringVar(value="Create New Master Password") # create text variable for label
        label1 = customtkinter.CTkLabel(self.window, 
                                        textvariable = text_var, 
                                        width = 20, 
                                        height = 2, 
                                        corner_radius = 8,
                                        text_font=("Roboto Medium", -16)) # create label for entering new master password                 
        label1.configure(anchor=CENTER) # set anchor for label 
        label1.pack(pady=10) # pack label 
        
        

        mp_entry_box = customtkinter.CTkEntry(self.window,
                                              width=150, 
                                              show="*",  
                                              height = 30, 
                                              text_font=("Roboto Medium", -16),
                                              corner_radius = 8)# create entry box for master password to sign up
        mp_entry_box.pack()# pack entry box
        mp_entry_box.focus() # set focus on entry box
        
        
        text_var = tkinter.StringVar(value="Enter the text again") # create text variable for label
        label2 = customtkinter.CTkLabel(self.window, 
                                        textvariable = text_var, 
                                        width = 20, 
                                        height = 2, 
                                        corner_radius = 8,
                                        text_font=("Roboto Medium", -16))# create label for entering new master password again to sign up
        label2.configure(anchor=CENTER) # set anchor for label 
        label2.pack(pady=10) # pack label 


        rmp_entry_box = customtkinter.CTkEntry(self.window,
                                              width=150, 
                                              show="*",  
                                              height = 30, 
                                              text_font=("Roboto Medium", -16),
                                              corner_radius = 8)# create entry box for master password
        mp_entry_box.pack()# pack entry box
        rmp_entry_box.pack() # pack entry box



        text_var = tkinter.StringVar(value="") # create text variable for label
        self.feedback = customtkinter.CTkLabel(self.window, 
                                               textvariable = text_var) # create label for feedback
        self.feedback.pack() # pack label


        save_btn = customtkinter.CTkButton(self.window, 
                                           text="Create Password",
                                           width=150,
                                           height=42,
                                           command=partial(self.save_master_password, mp_entry_box, rmp_entry_box),
                                           border_width=0,
                                           text_font=("Roboto Medium", -16),
                                           corner_radius=8) # create button for saving master password to database 
        save_btn.pack(pady=5) # pack button





    def login_user(self): # function to login user 
        for widget in self.window.winfo_children(): # for each widget in window 
            widget.destroy() # destroy widget 

        self.window.geometry("450x200") # set size of window

        text_var = tkinter.StringVar(value="Enter your master password") # create text variable for label
        label1 = customtkinter.CTkLabel(self.window, 
                                        textvariable=text_var, 
                                        width=20, 
                                        height=15, 
                                        corner_radius=8,
                                        text_font=("Roboto Medium", -16)) # create label for entering master password to login
        label1.configure(anchor=CENTER) # set anchor for label
        label1.place(x=228, y=50,anchor = CENTER) # place label 

        self.password_entry_box = customtkinter.CTkEntry(self.window,  height=20,
                                                         width=120, 
                                                         show="*",
                                                         border_width=2,
                                                         corner_radius=10,
                                                         text_font=("Roboto Medium", -16)) # create entry box for master password to login
        self.password_entry_box.place(x=165, y=80) # place entry box
        self.password_entry_box.focus() # set focus on entry box

        text_var = tkinter.StringVar(value="") # create text variable for label 
        self.feedback = customtkinter.CTkLabel(self.window, textvariable = text_var) # create label for feedback 
        self.feedback.place(x=170, y=105) # place label

        login_btn = customtkinter.CTkButton(self.window, 
                                            text="Log In",     
                                            command=partial(self.check_master_password, self.password_entry_box),
                                            width = 120,
                                            height = 32,
                                            text_font=("Roboto Medium", -16)) # create button for logging in
        login_btn.place(x=165, y=130) # place button

    def save_master_password(self, eb1, eb2): # function to check and save master password at sign up 
        password1 = eb1.get() # get master password from entry box 
        password2 = eb2.get() # get master password again from entry box 2 
        if password1 == password2: # if master password and master password again are same 
            hashed_password = self.encrypt_password(password1) # encrypt master password 
            insert_command = """INSERT INTO master(password) 
            VALUES(?) """ # create insert command 
            self.cursor.execute(insert_command, [hashed_password]) # execute insert command 
            self.db.commit() # commit changes to database 
            self.login_user() # login user 
        else: # if master password and master password again are not same 
            self.feedback.configure(text="Passwords do not match", fg="red") # send back that passwords do not match

    def check_master_password(self, eb): # function to check and login user
        hashed_password = self.encrypt_password(eb.get())  # encrypt master password
        self.cursor.execute(
            "SELECT * FROM master WHERE id = 1 AND password = ?", [hashed_password]) # execute select command
        if self.cursor.fetchall(): # if master password is correct
            self.password_vault_screen() # go to password vault screen
        else: # if master password is not correct 
            self.password_entry_box.delete(0, END) # delete entered password from entry box
            self.feedback.configure(text="Incorrect password", fg="red") # send back that password is incorrect 

    def password_vault_screen(self): # function to go to password vault screen
        for widget in self.window.winfo_children(): # for each widget in window
            widget.destroy() # destroy widget

        vault_methods = VaultMethods() # create vault methods object

        
        
        
        self.window.geometry("1166x500") # set size of window
        main_frame = customtkinter.CTkFrame(self.window) # create frame for main window
        main_frame.pack(fill=BOTH, expand=1) # pack frame

        

            
        main_canvas = Canvas(main_frame, bg='#2a2d2e') # create canvas for main window
        main_canvas.pack(side=LEFT, fill=BOTH, expand=1) # pack canvas

        main_scrollbar = customtkinter.CTkScrollbar(main_frame, 
                                          orientation=VERTICAL, 
                                          command=main_canvas.yview) # create scrollbar for main window
        main_scrollbar.pack(side=RIGHT, fill=Y) # pack scrollbar

        main_canvas.configure(yscrollcommand=main_scrollbar.set) # set scrollbar for main window
        main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))) # bind scrollbar to canvas 

        second_frame = customtkinter.CTkFrame(main_canvas) # create frame for second window
        main_canvas.create_window((0, 0), window=second_frame, anchor="nw") # create window for main canvas
        
        generate_password_btn = customtkinter.CTkButton(second_frame, 
                                                        text="Generate Password",
                                                        command=PasswordGenerator,
                                                        text_font=("Roboto Medium", -16)) # create button for generating password
        generate_password_btn.grid(row=1, column=1, pady=10) # pack button 

        add_password_btn = customtkinter.CTkButton(second_frame, 
                                                   text="Add New Password",
                                                   text_font=("Roboto Medium", -16),
                                                   command=partial(vault_methods.add_password, self.password_vault_screen)) # create button for adding new password
        add_password_btn.grid(row=1, column=2, pady=10) # pack button

        lbl = customtkinter.CTkLabel(second_frame, 
                                     text="Platform",
                                     text_font=("Roboto Medium", -16))# create label for platform
        lbl.grid(row=2, column=0, padx=40, pady=10) # pack label
        lbl = customtkinter.CTkLabel(second_frame, 
                                     text="Email/Username", 
                                     text_font=("Roboto Medium", -16),) # create label for email/username
        lbl.grid(row=2, column=1, padx=40, pady=10) # pack label 
        lbl = customtkinter.CTkLabel(second_frame, 
                                     text="Password",
                                     text_font=("Roboto Medium", -16)) # create label for password
        lbl.grid(row=2, column=2, padx=40, pady=10) # pack label 

        self.cursor.execute("SELECT * FROM vault") # execute select command

        if self.cursor.fetchall(): # if there are passwords in database
            i = 0 # set i to 0
            while True: # while true
                self.cursor.execute("SELECT * FROM vault") # execute select command
                array = self.cursor.fetchall()# get array of passwords
 
                platform_label = customtkinter.CTkLabel(second_frame, 
                                                        text_font=("Roboto Medium", -16),
                                                        text=(array[i][1]))# create label for platform
                platform_label.grid(column=0, row=i + 3)  # pack label

                account_label = customtkinter.CTkLabel(second_frame,
                                                       text_font=("Roboto Medium", -16),
                                                       text=(array[i][2])) # create label for account
                account_label.grid(column=1, row=i + 3) # pack label

                password_label = customtkinter.CTkLabel(second_frame, 
                                                        text_font=("Roboto Medium", -16),
                                                        text=(array[i][3])) # create label for password
                password_label.grid(column=2, row=i + 3) # pack label

                copy_btn = customtkinter.CTkButton(second_frame, 
                                                   text_font=("Roboto Medium", -16),
                                                   text="Copy Password",
                                                   command=partial(self.copy_text, array[i][3])) # create button for copying password
                copy_btn.grid(column=3, row=i + 3, pady=10, padx=10) # pack button
                update_btn = customtkinter.CTkButton(second_frame, 
                                                     text_font=("Roboto Medium", -16),
                                                     text="Update Password",
                                                     command=partial(vault_methods.update_password, array[i][0], 
                                                                     self.password_vault_screen)) # create button for updating password
                update_btn.grid(column=4, row=i + 3, pady=10, padx=10)
                remove_btn = customtkinter.CTkButton(second_frame, 
                                                     text_font=("Roboto Medium", -16),
                                                     text="Delete Password",
                                                     command=partial(vault_methods.remove_password, array[i][0], 
                                                                     self.password_vault_screen)) # create button for deleting password
                remove_btn.grid(column=5, row=i + 3, pady=10, padx=10) # pack button

                i += 1 # increment i 

                self.cursor.execute("SELECT * FROM vault") # execute select command
                if len(self.cursor.fetchall()) <= i: # if there are no more passwords in database
                    break # break loop

    def encrypt_password(self, password): # function to encrypt password 
        password = password.encode("utf-8") # encode password as utf-8
        encoded_text = hashlib.md5(password).hexdigest() # encrypt password using md5 algorithm and get hexadecimal digest
        return encoded_text # return encrypted password 

    def copy_text(self, text): # function to copy text
        self.window.clipboard_clear() # clear clipboard
        self.window.clipboard_append(text) # copy text to clipboard


if __name__ == '__main__': # if this file is being run directly 
    db, cursor = init_database() # initialize database 
    cursor.execute("SELECT * FROM master") # execute select command 
    manager = PasswordManager() # create password manager object 
    if cursor.fetchall():    # if there are passwords in database
        manager.login_user() # login user
    else: # if there are no passwords in database
        manager.welcome_new_user() #  welcome new user 
    manager.window.mainloop()# start main loop