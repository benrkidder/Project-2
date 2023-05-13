from tkinter import *


class MENU:
    def __init__(self, window):
        self.window = window

        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)

        # App Menu
        self.app_menu = Menu(self.menu)
        self.menu.add_cascade(label="A Betting Chance", menu=self.app_menu)
        self.app_menu.add_command(label="Account", command=self.account)
        self.app_menu.add_separator()
        self.app_menu.add_command(label="Sign In...", command=self.signin)
        self.app_menu.add_command(label="Logout", command=self.logout)

        # File Menu
        self.file_menu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New...", command=self.new)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.window.quit)

        # Edit Menu
        self.edit_menu = Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.undo)
        self.edit_menu.add_command(label="Redo", command=self.redo)

        self.frame = Frame(self.window,
                           height=300,
                           width=300)
        self.frame.pack()

    def account(self):
        pass

    def signin(self):
        pass

    def logout(self):
        pass

    def new(self):
        pass

    def redo(self):
        pass

    def undo(self):
        pass


if __name__ == "__main__":
    win = Tk()
    win.title('A Betting Chance')
    MENU(win)

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
