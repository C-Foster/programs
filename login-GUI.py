import re
from tkinter import *
from tkinter import messagebox
    

def main_window():
    """Creates main window """

    def submit():
        """Checks that user input is correct. If not, resets window """

        # get username and password from entry box
        username = entry_username.get()
        password = entry_password.get()

        # create alert box
        messageAlert = Label(window, width=30)
        messageAlert.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

        # if username is incorrect
        if username != correct_username:
            messageAlert.config(text="Username incorrect")
            entry_username.delete(0, END)
            entry_password.delete(0, END)
            entry_username.focus_set()

        # if password is incorrect
        if password != correct_password:
            messageAlert.config(text="Password incorrect")
            entry_username.delete(0, END)
            entry_password.delete(0, END)
            entry_username.focus_set()

        # if both username and password are correct
        if password == correct_password and username == correct_username:
            messageAlert.config(text="Password accepted")
            print("Password accepted")
            print("Username: {}".format(username))
            print("Password: {}".format(password))
            messagebox.showinfo(title="OK", message="Password OK")
            message = "Press OK to continue"
            window.destroy()


    def hint():
        """Displays a password hint to the user in a message box """

        # displays a message window
        messagebox.showinfo(title="Password Hint", message="Hint: Try {}".format(correct_password))


    def resetter_window():
        """Runs the window to reset password """


        def change_password():
            """Changes the password """

            # get old and new password from entry box
            old_password = old_entry.get()
            new_password = new_entry.get()

            # if input of old password matched correct password
            if old_password == correct_password:
                with open("passwords.txt", "w") as file:
                    file.write("{}\n".format(correct_username))
                    file.write("{}\n".format(new_password))

                resetter.destroy()  # destroy resetter window                
                main_window()  # runs main window
            else:
                # displays message window
                messagebox.showinfo(title="Incorrect", message="Password did not match")
                resetter.destroy()
                resetter_window()

        try:
            window.destroy()  # end main window
        except Exception as e:
            pass
            
            
        # creates and configures 'resetter' window
        resetter = Tk()
        resetter.geometry("250x180")
        resetter.title("Reset Password:")
        resetter.resizable(False, False)
        resetter.configure(background="Light Green")

        Label(resetter, text="Enter current password: ").grid(column=0, row=0, padx=5, pady=5)

        # create entry boxes for current password and new password
        old_entry = Entry(resetter, width=15, bg="white", show="*")
        new_entry = Entry(resetter, width=15, bg="white", show="*")
        old_entry.grid(column=0, row=1, padx=5, pady=5)
        new_entry.grid(column=0, row=2, padx=5, pady=5)

        # create button to submit changes
        change_button = Button(resetter, text="Submit", width=8, command=change_password)
        change_button.grid(column=0, row=3, padx=5, pady=5)

        # runs the window
        resetter.mainloop()

    # reads correct username and password from file
    with open("passwords.txt", "r") as file:
        
        # matches one or more alpha-numeric characters followed by
        # a new-line character
        patt = re.compile(r'\w+\n')  
        
        
        correct_username = file.readline()  # read username from file
        m = re.match(patt, correct_username)  # attempt to match regular expression on username

        # if there is a match (i.e. if ends with \n)
        if m:
            correct_username = correct_username[:-1]  # remove new-line character \n

        correct_password = file.readline()  # read password from file
        m = re.match(patt, correct_password)  # attempt to match regular expression on password

        # if there is a match (i.e. if ends with \n)
        if m:
            correct_password = correct_password[:-1]  # remove new-line character \n

        # output correct username and password for debugging purposes
        print(repr(correct_username))
        print(repr(correct_password))

    # configure tkinter window
    window = Tk()
    window.geometry("250x180")
    window.title("Login Screen:")
    window.resizable(False, False)
    window.configure(background="Light Blue")

    # creates frame to contain entry boxes
    entry_frame = Frame(window)
    entry_frame.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

    # creates entry boxes with white background within entry frame, password is censored by "*"
    entry_username = Entry(entry_frame, width=15, bg="white")
    entry_password = Entry(entry_frame, width=15, bg="white", show="*")
    entry_username.grid(column=1, row=0, padx=5, pady=5)
    entry_password.grid(column=1, row=1, padx=5, pady=5)

    # creates labels next to the entry boxes
    Label(entry_frame, text="Enter Username: ").grid(column=0, row=0, padx=5, pady=5)
    Label(entry_frame, text="Enter Password: ").grid(column=0, row=1, padx=5, pady=5)

    # creates frame to contain buttons (submit and hint)
    button_frame = Frame(window)
    button_frame.grid(column=0, row=2, columnspan=3, padx=10, pady=10)

    # creates buttons within button frame
    submit_button = Button(button_frame, text="Submit", width=8, command=submit)
    hint_button = Button(button_frame, text="Hint", width=8, command=hint)
    change_button = Button(button_frame, text="Change Password", command=resetter_window)
    submit_button.grid(column=0, row=0, padx=5, pady=5)
    hint_button.grid(column=1, row=0, padx=5, pady=5)
    change_button.grid(column=0, row=1, padx=5, pady=5)

    # run window
    window.mainloop()

        
if __name__ == '__main__':
    # run main function
    main_window()

    # output to signify the window has closed successfully
    print("Finished")
