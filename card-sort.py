"""Code Ware Kata 7, Sort Deck of Cards."""


def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank."""
    deck = {
        "A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
        "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13
    }
    return sorted(cards, key=lambda x: deck[x])
