"""Small random-chance game helpers."""

import random

CHOICES = ("rock", "paper", "scissors")
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def roll_dice(sides=6, count=1):
    """Roll `count` dice with `sides` sides each and return the results as a list."""
    if sides < 2:
        raise ValueError("A die must have at least 2 sides.")
    if count < 1:
        raise ValueError("You must roll at least 1 die.")
    return [random.randint(1, sides) for _ in range(count)]


def flip_coin():
    """Return 'heads' or 'tails' at random."""
    return random.choice(("heads", "tails"))


def pick_secret_number(low=1, high=100):
    """Return a random secret number between low and high (inclusive)."""
    if low > high:
        raise ValueError("low must not be greater than high.")
    return random.randint(low, high)


def check_guess(guess, secret):
    """Compare a guess with the secret number and return 'too low', 'too high' or 'correct'."""
    if guess < secret:
        return "too low"
    if guess > secret:
        return "too high"
    return "correct"


def computer_choice():
    """Return a random rock-paper-scissors choice for the computer."""
    return random.choice(CHOICES)


def rps_winner(player, computer):
    """Return 'player', 'computer' or 'draw' for a rock-paper-scissors round."""
    player, computer = player.lower(), computer.lower()
    if player not in CHOICES or computer not in CHOICES:
        raise ValueError(f"Choices must be one of: {', '.join(CHOICES)}.")
    if player == computer:
        return "draw"
    return "player" if BEATS[player] == computer else "computer"


# --- Higher or Lower (card game) ---

RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
SUITS = ("hearts", "diamonds", "clubs", "spades")


def new_deck():
    """Return a shuffled 52-card deck as a list of (rank, suit) tuples."""
    deck = [(rank, suit) for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck


def draw_card(deck):
    """Remove and return the top card of the deck. Raises ValueError if it is empty."""
    if not deck:
        raise ValueError("The deck is empty.")
    return deck.pop()


def card_value(card):
    """Return the numeric value of a card: 2-10 as numbered, J=11, Q=12, K=13, A=14."""
    return RANKS.index(card[0]) + 2


def card_name(card):
    """Return a readable name for a card, such as 'Q of hearts'."""
    return f"{card[0]} of {card[1]}"


def check_higher_lower(guess, current, next_card):
    """Return 'correct', 'wrong' or 'tie' for a guess of 'higher' or 'lower'."""
    guess = guess.lower()
    if guess not in ("higher", "lower"):
        raise ValueError("Guess must be 'higher' or 'lower'.")
    current_value, next_value = card_value(current), card_value(next_card)
    if current_value == next_value:
        return "tie"
    went_higher = next_value > current_value
    return "correct" if went_higher == (guess == "higher") else "wrong"



