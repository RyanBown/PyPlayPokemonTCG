import random
import math

def cut_deck(deck):
    deck_len = len(deck)
    deck_half = 0
    round_to = random.choice([0,1])
    margin_of_error = random.randint(-20, 20)

    
    if round_to == 0:
        deck_half = math.floor(deck_len / 2)
    else:
        deck_half = math.ceil(deck_len / 2 )

    deck_half = deck_half - margin_of_error

    half_one = deck[:deck_half]
    half_two = deck[deck_half:]

    half_two.extend(half_one)

    return half_two

def GetDeckInHalf(deck):
    deck_len = len(deck)
    deck_half = 0
    round_to = random.choice([0,1])
    margin_of_error = random.randint(-3, 3)

    
    if round_to == 0:
        deck_half = math.floor(deck_len / 2)
    else:
        deck_half = math.ceil(deck_len / 2 )

    deck_half = deck_half - margin_of_error

    half_one = deck[:deck_half]
    half_two = deck[deck_half:]

    return half_one, half_two

def riffle(deck):

    half_one, half_two = GetDeckInHalf(deck)

    shuffled_deck = []
    x= 0 
    for card in half_two:
        riffle_from_deck2 = random.choice([0,1,2,3])
        shuffled_deck.append(card)

        for i in range(riffle_from_deck2):
            if len(half_one) > 0:
                x = x + 1
                shuffled_deck.append(half_one[0])
                half_one.pop(0)

    return cut_deck(shuffled_deck)

def riffle_shuffle(deck,n):
    for _ in range(n):
        deck = riffle(deck)
    return deck