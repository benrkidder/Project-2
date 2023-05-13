from tkinter import *
from login_controller import *
import bcrypt


# Login Modal
class LOGIN:
    def __init__(self, window):
        self.window = window

        # Variables
        self.__password = StringVar(value="Password*", name="pass")
        self.__username = StringVar(value="Email Address*", name="user")

        # Login Section
        self.frame = Frame(self.window)
        self.frame.grid(padx=20, pady=10, sticky="nsew")
        self.frame.grid_columnconfigure(0, weight=1, uniform="login")
        self.frame.grid_columnconfigure(1, weight=1, uniform="login")
        self.frame.grid_columnconfigure(2, weight=2, uniform="login")

        self.frame.grid_rowconfigure(0, weight=1, uniform="login")
        self.frame.grid_rowconfigure(1, weight=1, uniform="login")
        self.frame.grid_rowconfigure(2, weight=1, uniform="login")
        self.frame.grid_rowconfigure(3, weight=1, uniform="login")
        self.frame.grid_rowconfigure(4, weight=1, uniform="login")
        self.frame.grid_rowconfigure(5, weight=1, uniform="login")

        # Username
        self.username_label = Label(self.frame,
                                    anchor="w",
                                    text="Username")
        self.username_entry = Entry(self.frame,
                                    fg="#777",
                                    width=30,
                                    textvariable=self.__username)
        self.username_label.grid(row=0, column=0, sticky="sw")
        self.username_entry.grid(row=1, column=0, columnspan=2, sticky="nw")

        # Password
        self.password_label = Label(self.frame,
                                    anchor="w",
                                    text="Password")
        self.password_entry = Entry(self.frame,
                                    fg="#777",
                                    width=30,
                                    textvariable=self.__password)
        self.password_label.grid(row=2, column=0, sticky="sw")
        self.password_entry.grid(row=3, column=0, columnspan=2, sticky="nw")

        # Login Options
        self.login_checkbutton = Checkbutton(self.frame,
                                             text="Keep me signed in")
        self.forgot_button = Button(self.frame,
                                    text="Forgot password?")
        self.login_checkbutton.grid(row=4, column=0, sticky="nw")
        self.forgot_button.grid(row=4, column=1, sticky="nw")

        # Login Button
        self.login_button = Button(self.frame,
                                   command=self.login,
                                   text="Login")
        self.login_button.grid(row=5, column=0, pady=(0, 20), sticky="ew")

        # Sign Up Section
        self.signup_label = Label(self.frame,
                                  fg="#5577FF",
                                  font=("Helvetica Bold", 30),
                                  text="New Here?\nSign up for free today!")
        self.signup_button = Button(self.frame,
                                    text="Create Account")
        self.signup_label.grid(row=0, rowspan=5, column=2, padx=(10, 0))
        self.signup_button.grid(row=4, column=2)

    def login(self):
        usr = self.username_entry.get()
        pw = self.password_entry.get()

        # TODO: Implement Salt and Hash

        user = authUser(usr, pw)
        if user:
            self.window.quit()



if __name__ == "__main__":
    win = Tk()
    win.title('A Betting Chance')
    LOGIN(win)

    win.update()
    win_width = win.winfo_reqwidth()
    win_height = win.winfo_reqheight()
    scr_width = win.winfo_screenwidth()
    scr_height = win.winfo_screenheight()
    win_x = int((scr_width / 2) - (win_width / 2))
    win_y = int((scr_height / 2) - (win_height / 2))
    win.geometry(f'+{win_x}+{win_y}')
    win.resizable(False, False)

    win.mainloop()
