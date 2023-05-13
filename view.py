from tkinter import *
from tkinter import messagebox as mb
import PIL.Image
import PIL.ImageTk
from login_controller import *
from controller import *


class GAME:
    def __init__(self, window):
        self.window = window
        self.frame = Frame(self.window, bg="#246242")

        # Variables
        self.__password = StringVar(value="Password*", name="pass")
        self.__username = StringVar(value="Email Address*", name="user")

        # Login Section
        self.login_frame = Frame(self.window)
        self.login_frame.grid(padx=20, pady=10, sticky="nsew")
        self.login_frame.grid_columnconfigure(0, weight=1, uniform="login")
        self.login_frame.grid_columnconfigure(1, weight=1, uniform="login")
        self.login_frame.grid_columnconfigure(2, weight=2, uniform="login")

        self.login_frame.grid_rowconfigure(0, weight=1, uniform="login")
        self.login_frame.grid_rowconfigure(1, weight=1, uniform="login")
        self.login_frame.grid_rowconfigure(2, weight=1, uniform="login")
        self.login_frame.grid_rowconfigure(3, weight=1, uniform="login")
        self.login_frame.grid_rowconfigure(4, weight=1, uniform="login")
        self.login_frame.grid_rowconfigure(5, weight=1, uniform="login")

        # Username
        self.username_label = Label(self.login_frame,
                                    anchor="w",
                                    text="Username")
        self.username_entry = Entry(self.login_frame,
                                    fg="#777",
                                    width=30,
                                    textvariable=self.__username)
        self.username_label.grid(row=0, column=0, sticky="sw")
        self.username_entry.grid(row=1, column=0, columnspan=2, sticky="nw")

        # Password
        self.password_label = Label(self.login_frame,
                                    anchor="w",
                                    text="Password")
        self.password_entry = Entry(self.login_frame,
                                    fg="#777",
                                    width=30,
                                    textvariable=self.__password)
        self.password_label.grid(row=2, column=0, sticky="sw")
        self.password_entry.grid(row=3, column=0, columnspan=2, sticky="nw")

        # Login Options
        self.login_checkbutton = Checkbutton(self.login_frame,
                                             text="Keep me signed in")
        self.forgot_button = Button(self.login_frame,
                                    text="Forgot password?")
        self.login_checkbutton.grid(row=4, column=0, sticky="nw")
        self.forgot_button.grid(row=4, column=1, sticky="nw")

        # Login Button
        self.login_button = Button(self.login_frame,
                                   command=self.login,
                                   text="Login")
        self.login_button.grid(row=5, column=0, pady=(0, 20), sticky="ew")

        # Sign Up Section
        self.signup_label = Label(self.login_frame,
                                  fg="#5577FF",
                                  font=("Helvetica Bold", 30),
                                  text="New Here?\nSign up for free today!")
        self.signup_button = Button(self.login_frame,
                                    text="Create Account")
        self.signup_label.grid(row=0, rowspan=5, column=2, padx=(10, 0))
        self.signup_button.grid(row=4, column=2)

        # Variables
        self.__player_hand = []
        self.__dealer_hand = []
        self.__deck = []
        self.__player_score = IntVar(name="p_score")
        self.__dealer_score = IntVar(name="d_score")

        # Images
        self.deck_raw_image = PIL.Image.open("files/decks/deck1.png")
        self.small_deck_image = self.deck_raw_image.reduce(2)
        self.small_deck_image.resize(size=(90, 150), resample=1)
        self.deck_image = PIL.ImageTk.PhotoImage(self.small_deck_image)
        self.dealer_deck_image = PIL.ImageTk.PhotoImage(self.small_deck_image.rotate(180))

        # Start up
        # self.start_label = Label(self.frame, height=3, font=("Helvetica Light", 20), width=25, text="Click 'Start' to play!")
        # self.start_button = Button(self.frame, height=2, width=40, text="Start", command=self.clear)
        # self.quit_button = Button(self.frame, height=2, width=40, text="Quit", command=self.warn)

        # self.start_label.pack(pady=(10, 0))
        # self.start_button.pack(anchor="center", pady=(20, 5))
        # self.quit_button.pack(anchor="center")
        # self.frame.pack(expand=True, fill="both", ipadx=10, ipady=10)

        # Table
        # Player
        self.player_frame = Frame(self.frame)
        self.player_label = Label(self.player_frame,
                                  font=("Helvetica Light", 40),
                                  text="Player")
        self.player_score_frame = Frame(self.player_frame)
        self.player_score = Label(self.player_score_frame,
                                  text="0",
                                  textvariable=self.__player_score)
        self.player_card1 = Label(self.player_frame, image=self.deck_image)
        self.player_card2 = Label(self.player_frame, image=self.deck_image)
        self.player_card3 = Label(self.player_frame, image=self.deck_image)
        self.player_card4 = Label(self.player_frame, image=self.deck_image)
        self.player_info_frame = Frame(self.player_frame)
        self.hit_radio = Radiobutton(self.player_info_frame,
                                     bg="white",
                                     borderwidth=0,
                                     command=lambda: self.hit("player"),
                                     fg="black",
                                     highlightthickness=0,
                                     indicatoron=False,
                                     text="HIT")
        self.stay_radio = Radiobutton(self.player_info_frame,
                                      bg="white",
                                      borderwidth=0,
                                      command=self.stay,
                                      fg="black",
                                      highlightthickness=0,
                                      indicatoron=False,
                                      text="STAY")
        self.player_card1.image = self.deck_image
        self.player_card2.image = self.deck_image

        # Dealer
        self.dealer_frame = Frame(self.frame)
        self.dealer_label = Label(self.dealer_frame,
                                  font=("Helvetica Light", 40),
                                  text="Dealer")
        self.dealer_score_frame = Frame(self.dealer_frame)
        self.dealer_score = Label(self.dealer_score_frame,
                                  text="0",
                                  textvariable=self.__player_score)
        self.dealer_card1 = Label(self.dealer_frame, image=self.dealer_deck_image)
        self.dealer_card2 = Label(self.dealer_frame, image=self.dealer_deck_image)
        self.dealer_card3 = Label(self.dealer_frame, image=self.dealer_deck_image)
        self.dealer_card4 = Label(self.dealer_frame, image=self.dealer_deck_image)
        self.dealer_info_frame = Frame(self.dealer_frame)
        self.deal_radio = Radiobutton(self.dealer_info_frame,
                                      command=self.new_game,
                                      borderwidth=0,
                                      highlightthickness=0,
                                      bg="white",
                                      fg="black",
                                      indicatoron=False,
                                      text="START GAME")
        self.dealer_card1.image = self.deck_image
        self.dealer_card2.image = self.deck_image

        # Menu
    def clear(self):
        # self.start_label.destroy()
        # self.start_button.destroy()
        # self.quit_button.destroy()
        self.login_frame.grid_remove()
        self.window.update()
        self.update()

    def login(self):
        usr = self.username_entry.get()
        pw = self.password_entry.get()

        # TODO: Implement Salt and Hash

        user = authUser(usr, pw)
        if user:
            self.clear()

    def new_game(self):
        deck = shuffle_deck()
        player_hand, dealer_hand, deck = deal(deck)
        self.__player_hand = player_hand
        self.__dealer_hand = dealer_hand
        self.__deck = deck

        pc1 = self.__player_hand[0]
        pc2 = self.__player_hand[1]

        dc1 = self.__dealer_hand[0]

        self.deal_cards(pc1, pc2, dc1)
        self.calc_score("player")
        self.calc_score("dealer")

    def hit(self, player: str):
        card, deck = draw(self.__deck)
        self.__deck = deck

        if player == "player":
            self.__player_hand.append(card)

            nc_raw = PIL.Image.open(f"files/cards/{card}.png")
            nc_small = nc_raw.reduce(3)
            nc_small.resize(size=(90, 150), resample=1)
            nc = PIL.ImageTk.PhotoImage(nc_small)
            self.player_card4.configure(image=nc)
            self.player_card4.image = nc
            self.player_card4.grid()

        elif player == "dealer":
            self.__dealer_hand.append(card)

            nc_raw = PIL.Image.open(f"files/cards/{card}.png")
            nc_small = nc_raw.reduce(3)
            nc_small.resize(size=(90, 150), resample=1)
            nc = PIL.ImageTk.PhotoImage(nc_small)
            self.dealer_card4.configure(image=nc)
            self.dealer_card4.image = nc
            self.dealer_card4.grid()

    def stay(self):
        d2 = self.__dealer_hand[1]
        dc3_raw = PIL.Image.open(f"files/cards/{d2}.png")
        dc3_small = dc3_raw.reduce(3)
        dc3_small.resize(size=(80, 140), resample=1)
        dc3 = PIL.ImageTk.PhotoImage(dc3_small)
        self.dealer_card3.configure(image=dc3)
        self.dealer_card3.image = dc3
        self.dealer_card3.grid()
        self.calc_score("dealer")

    def calc_score(self, player: str):
        string = ""
        score = 0
        if player == "dealer":
            for card in self.__dealer_hand:
                string += card[0]

            for char in string:
                if char.isalpha():
                    if char == "J" or char == "Q" or char == "K":
                        score += 10
                    elif char == "A":
                        if score + 11 > 21 and score + 1 <= 16:
                            score += 1
                        else:
                            score += 11
                    else:
                        score += int(char)

            self.__dealer_score.set(score)

        elif player == "player":
            for card in self.__player_hand:
                string += card[0]

            for char in string:
                if char.isalpha():
                    if char == "J" or char == "Q" or char == "K":
                        score += 10
                    elif char == "A":
                        if score + 11 > 21 and score + 1 <= 16:
                            score += 1
                        else:
                            score += 11
                    else:
                        score += int(char)

            self.__player_score.set(score)

    def deal_cards(self, p1, p2, d1):
        pc2_raw = PIL.Image.open(f"files/cards/{p1}.png")
        pc2_small = pc2_raw.reduce(3)
        pc2_small.resize(size=(90, 150), resample=1)
        pc2 = PIL.ImageTk.PhotoImage(pc2_small)
        self.player_card2.configure(image=pc2)
        self.player_card2.image = pc2
        pc3_raw = PIL.Image.open(f"files/cards/{p2}.png")
        pc3_small = pc3_raw.reduce(3)
        pc3_small.resize(size=(90, 150), resample=1)
        pc3 = PIL.ImageTk.PhotoImage(pc3_small)
        self.player_card3.configure(image=pc3)
        self.player_card3.image = pc3

        dc2_raw = PIL.Image.open(f"files/cards/{d1}.png")
        dc2_small = dc2_raw.reduce(3)
        dc2_small.resize(size=(90, 150), resample=1)
        dc2 = PIL.ImageTk.PhotoImage(dc2_small)
        self.dealer_card2.configure(image=dc2)
        self.dealer_card2.image = dc2

    def update(self):
        self.dealer_frame.grid(row=0, column=0, sticky="nsew")
        self.dealer_score_frame.grid(row=0, rowspan=2, column=0)
        self.dealer_score.grid(row=0, column=0)
        self.dealer_label.grid(row=0, column=1, columnspan=4, sticky="nsew")
        self.dealer_card1.grid(row=1, column=1, sticky="nsew")
        self.dealer_card2.grid(row=1, column=2, sticky="nsew")
        self.dealer_card3.grid(row=1, column=3, sticky="nsew")
        self.dealer_card4.grid(row=1, column=4, sticky="nsew")
        self.dealer_info_frame.grid(row=0, rowspan=2, column=5, sticky="nsew")
        self.deal_radio.grid(row=0, column=0, sticky="nsew")

        self.player_frame.grid(row=1, column=0, sticky="nsew")
        self.player_score_frame.grid(row=0, rowspan=2, column=0)
        self.player_score.grid(row=0, column=0)
        self.player_label.grid(row=0, column=1, columnspan=4, sticky="nsew")
        self.player_card1.grid(row=1, column=1, sticky="nsew")
        self.player_card2.grid(row=1, column=2, sticky="nsew")
        self.player_card3.grid(row=1, column=3, sticky="nsew")
        self.player_card4.grid(row=1, column=4, sticky="nsew")
        self.player_info_frame.grid(row=0, rowspan=2, column=5, sticky="nsew")
        self.hit_radio.grid(row=0, column=0)
        self.stay_radio.grid(row=1, column=0)

        self.dealer_frame.columnconfigure(0, weight=1, uniform="dealer")
        self.dealer_frame.columnconfigure(1, weight=1, uniform="dealer")
        self.dealer_frame.columnconfigure(2, weight=1, uniform="dealer")
        self.dealer_frame.columnconfigure(3, weight=1, uniform="dealer")
        self.dealer_frame.columnconfigure(4, weight=1, uniform="dealer")
        self.dealer_frame.columnconfigure(5, weight=1, uniform="dealer")
        self.dealer_frame.rowconfigure(0, weight=1, uniform="dealer")
        self.dealer_frame.rowconfigure(1, weight=4, uniform="dealer")

        self.player_frame.columnconfigure(0, weight=1, uniform="player")
        self.player_frame.columnconfigure(1, weight=1, uniform="player")
        self.player_frame.columnconfigure(2, weight=1, uniform="player")
        self.player_frame.columnconfigure(3, weight=1, uniform="player")
        self.player_frame.columnconfigure(4, weight=1, uniform="player")
        self.player_frame.columnconfigure(5, weight=1, uniform="player")
        self.player_frame.rowconfigure(0, weight=1, uniform="player")
        self.player_frame.rowconfigure(1, weight=4, uniform="player")

        self.dealer_info_frame.columnconfigure(0, uniform="dealer")
        self.dealer_info_frame.rowconfigure(0, uniform="dealer")

        self.player_info_frame.columnconfigure(0, weight=4, uniform="player")
        self.player_info_frame.rowconfigure(0, weight=1, uniform="player")
        self.player_info_frame.rowconfigure(1, weight=1, uniform="player")

        self.player_card1.grid_remove()
        self.player_card4.grid_remove()
        self.dealer_card1.grid_remove()
        self.dealer_card4.grid_remove()

        self.frame.grid(row=0, column=0, sticky="nsew")

        self.window.geometry("1200x1000+100+50")
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
    win.geometry(f'1500x1000+100+50')

    win.mainloop()
