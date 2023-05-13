from random import shuffle, randint


def shuffle_deck() -> list:
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    deck = []

    for suit in suits:
        for card in cards:
            deck.append(f'{card}_of_{suit}')

    shuffle(deck)
    return deck


def deal(deck: list) -> tuple:
    player_hand = [deck.pop(randint(0, 51))]
    dealer_hand = [deck.pop(randint(0, 50))]

    player_hand.append(deck.pop(randint(0, 49)))
    dealer_hand.append(deck.pop(randint(0, 48)))

    return player_hand, dealer_hand, deck


def draw(deck: list) -> tuple:
    card = randint(0, len(deck) - 1)
    card = deck.pop(card)
    return card, deck
