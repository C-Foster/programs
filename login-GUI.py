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
        message_alert = Label(window, width=30)
        message_alert.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

        # if username is incorrect
        if username != correct_username:
            message_alert.config(text="Username incorrect")
            entry_username.delete(0, END)
            entry_password.delete(0, END)
            entry_username.focus_set()

        # if password is incorrect
        if password != correct_password:
            message_alert.config(text="Password incorrect")
            entry_username.delete(0, END)
            entry_password.delete(0, END)
            entry_username.focus_set()

        # if both username and password are correct
        if password == correct_password and username == correct_username:
            message_alert.config(text="Password accepted")
            print("Password accepted")
            print("Username: '{}'".format(username))
            print("Password: '{}'".format(password))
            messagebox.showinfo(title="OK", message="Password OK")
            window.destroy()

    def hint():
        """Displays a password hint to the user in a message box """

        # displays a message window
        messagebox.showinfo(title="Password Hint", message="Hint: Try '{}'".format(correct_password))

    def reset_window():
        """Runs the window to reset password """

        def change_password():
            """Changes the password """

            # get old and new password from entry box
            old_password = old_entry.get()
            new_password = new_entry.get()

            # if input of old password matched correct password
            if old_password == correct_password:
                with open("passwords.txt", "w") as write_file:
                    write_file.write("{}\n".format(correct_username))
                    write_file.write("{}\n".format(new_password))

                reset.destroy()  # destroy reset window
                main_window()  # runs main window
            else:
                # displays message window
                messagebox.showinfo(title="Incorrect", message="Password did not match")
                # reset.destroy()
                # reset_window()
                old_entry.delete(0, END)
                new_entry.delete(0, END)
                old_entry.focus_set()

        try:
            # try to end main window
            window.destroy()
        except Exception:
            # if exception is raised
            # i.e. window cannot be destroyed due to already having been destroyed
            # do nothing
            pass

        # creates and configures 'reset' window
        reset = Tk()
        reset.geometry("300x180")
        reset.title("Reset Password:")
        reset.resizable(False, False)
        reset.configure(background="Light Green")

        Label(reset, text="Enter current password: ", width=20, anchor=E).grid(column=0, row=0, padx=5, pady=5)
        Label(reset, text="Enter new password: ", width=20, anchor=E).grid(column=0, row=1, padx=5, pady=5)

        # create entry boxes for current password and new password
        old_entry = Entry(reset, width=15, bg="white", show="*")
        new_entry = Entry(reset, width=15, bg="white", show="*")

        # position entry boxes
        old_entry.grid(column=1, row=0, padx=5, pady=5)
        new_entry.grid(column=1, row=1, padx=5, pady=5)

        # create button to submit changes
        change_button = Button(reset, text="Submit", width=20, command=change_password)
        change_button.grid(column=0, row=3, padx=5, pady=5)

        # runs the window
        reset.mainloop()

    # reads correct username and password from file
    with open("passwords.txt", "r") as read_file:

        # matches one or more alpha-numeric characters followed by
        # a new-line character
        patt = re.compile(r'\w+\n')

        correct_username = read_file.readline()  # read username from file
        matched = re.match(patt, correct_username)  # attempt to match regular expression on username

        # if there is a match (i.e. if ends with \n)
        if matched:
            correct_username = correct_username[:-1]  # remove new-line character \n

        correct_password = read_file.readline()  # read password from file
        matched = re.match(patt, correct_password)  # attempt to match regular expression on password

        # if there is a match (i.e. if ends with \n)
        if matched:
            correct_password = correct_password[:-1]  # remove new-line character \n

        # output correct username and password for debugging purposes
        print(repr(correct_username))
        print(repr(correct_password))

    # configure tkinter window
    window = Tk()
    window.geometry("250x250")
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
    submit_button = Button(button_frame, text="Submit", width=8, command=submit)  # calls submit()
    hint_button = Button(button_frame, text="Hint", width=8, command=hint)  # calls hint()
    change_button = Button(button_frame, text="Change Password", command=reset_window)  # calls reset_window()
    submit_button.grid(column=0, row=0, padx=5, pady=5)
    hint_button.grid(column=1, row=0, padx=5, pady=5)
    change_button.grid(column=0, row=1, padx=5, pady=5)

    # run window
    window.mainloop()


if __name__ == '__main__':
    # call main function
    main_window()

    # output to signify the window has closed successfully
    print("Finished")
