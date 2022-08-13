from database import init_database
import customtkinter 

class VaultMethods: # class for vault methods

    def __init__(self, ): # constructor for vault methods
        self.db, self.cursor = init_database()  # initialize database

    def popup_entry(self, what): # function for popup entry
        dialog = customtkinter.CTkInputDialog(title = "Enter details", text = what) # ask user to enter details for password entry 
        answer = dialog.get_input()
        return answer # return answer to calling function

    def add_password(self, vault_screen): # function for adding password to database
        platform = self.popup_entry(what = "Platform") # ask user to enter platform 
        userid = self.popup_entry(what = "Username/Email") # ask user to enter username/email
        password = self.popup_entry(what = "Password") # ask user to enter password    

        insert_cmd = """INSERT INTO vault(platform, userid, password) VALUES (?, ?, ?)""" # insert command
        self.cursor.execute(insert_cmd, (platform, userid, password)) # insert platform, username/email and password into database
        self.db.commit() # commit changes to database
        vault_screen() # call vault screen function

    def update_password(self, id, vault_screen): # function for updating password in database 
        password = self.popup_entry("Enter New Password") # ask user to enter new password
        self.cursor.execute("UPDATE vault SET password = ? WHERE id = ?", (password, id)) # update password in database 
        self.db.commit() # commit changes to database 
        vault_screen()   # call vault screen function

    def remove_password(self, id, vault_screen): # function for removing password from database
        self.cursor.execute("DELETE FROM vault WHERE id = ?", (id,)) # delete password from database
        self.db.commit() # commit changes to database
        vault_screen() # call vault screen function