from tkinter import *
from tkinter import messagebox as mb


class GAME:
    def __init__(self, window):
        self.window = window

        self.frame = Frame(self.window, bg="#246242")

        self.start_label = Label(self.frame, height=3, font=("Helvetica Light", 20), width=25, text="Click 'Start' to play!")
        self.start_button = Button(self.frame, height=2, width=40, text="Start", command=self.clear)
        self.quit_button = Button(self.frame, height=2, width=40, text="Quit", command=self.warn)

        self.start_label.pack(pady=(10, 0))
        self.start_button.pack(anchor="center", pady=(20, 5))
        self.quit_button.pack(anchor="center")
        self.frame.pack(expand=True, fill="both", ipadx=10, ipady=10)

    def clear(self):
        self.start_label.destroy()
        self.start_button.destroy()
        self.quit_button.destroy()
        screen_width = int(self.window.winfo_screenwidth() - 200)
        screen_height = int(self.window.winfo_screenheight() - 200)
        self.window.geometry(f'{screen_width}x{screen_height}')
        self.window.geometry("+100+50")
        self.window.update()

    def warn(self):
        if mb.askyesno(title="No guts, no glory!", message="Are you sure you want to quit?"):
            self.window.quit()
        else:
            self.frame.focus_set()


if __name__ == "__main__":
    win = Tk()
    win.title('A Betting Chance')
    GAME(win)

    win.update()
    win_width = win.winfo_reqwidth()
    win_height = win.winfo_reqheight()
    scr_width = win.winfo_screenwidth()
    scr_height = win.winfo_screenheight()
    win_x = int((scr_width / 2) - (win_width / 2))
    win_y = int((scr_height / 2) - (win_height / 2) - 50)
    win.geometry(f'+{win_x}+{win_y}')
    win.resizable(False, False)

    win.mainloop()
