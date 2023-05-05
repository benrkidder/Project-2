from view import *


def main():
    window = Tk()
    window.title('A Betting Chance')
    GAME(window)

    window.update()
    window_width = window.winfo_reqwidth()
    window_height = window.winfo_reqheight()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_x = int((screen_width / 2) - (window_width / 2))
    window_y = int((screen_height / 2) - (window_height / 2) - 50)
    window.geometry(f'+{window_x}+{window_y}')
    window.resizable(False, False)

    window.mainloop()


if __name__ == "__main__":
    main()
