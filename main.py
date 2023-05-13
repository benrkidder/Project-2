from view import *


def main():
    window = Tk()
    window.title('A Betting Chance')

    GAME(window)

    window.update()
    window.geometry("1200x1000+100+50")
    window.resizable(False, False)

    window.mainloop()


if __name__ == "__main__":
    main()
