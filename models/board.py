from models.pokemon_cards import Card, Pokemon, Trainer, Energy
from actions.shuffle_deck import riffle_shuffle

import random



class Deck:

    def __init__(self,deck_list):
        self.deck_list = deck_list

    def __str__(self):
        return self.deck_list

    def shuffle_deck(self):
        self.deck_list = riffle_shuffle(self.deck_list, 7)


    def remove(self, card):
        self.deck_list.remove(card)

    def draw(self, amount):
        for _ in range(amount):
            drawn_card = self.deck_list.pop()
            yield drawn_card

    def look_at(self,amount):
        return self.deck_list[:amount]

    def put_card_into_deck(self,card, position):
        if position == 'bottom':
            self.deck_list.append(card)
            return
        if position == 'top':
            self.deck_list.insert(0,card)
            return 
        self.deck_list.add(card)
        self.deck_list.shuffle_deck()


class Hand:
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return str([card.name + ' ' + card.id for card in self.cards])
    
    def add(self,card):
        self.cards.append(card)

    def remove(self,card):
        return self.cards.pop(0)
    
    def discard(self, amount):
        random.shuffle(self.cards)
        for _ in range(amount):
            self.cards.pop(0)


    def play_card(self, card, board):
        if card.subtype == 'Pokemon':
            if board.bench_size > len(board.benched_pokemon):
                board.benched_pokemon.append(card)

            
class Prizes():
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return str([card.name + ' ' + card.id for card in self.cards])
    
class Board:
    def __init__(self, deck:Deck, prizes:Prizes, hand:Hand, active_pokemon:Pokemon, bench_size:int, benched_pokemon:list[Pokemon]):
        self.deck = deck
        self.prizes = prizes
        self.hand = hand
        self.active_pokemon = active_pokemon
        self.bench_size = bench_size
        self.benched_pokemon = benched_pokemon

    def __str__(self):
        deck_size = str(len(self.deck))
        prizes_left = len(self.prizes)
        active_pkmn = self.active_pokemon.card_name
        hp = self.active_pokemon.hp
        benched_left = self.bench_size  - len(self.benched_pokemon)
        return f'''Player
        {deck_size} cards left in deck
        has {prizes_left} prize cards
        active Pokemon is {active_pkmn}
        with remaining hp of {hp} 
        with {benched_left} spots open on bench
        '''
    def start_turn(self):
        self.hand.add(self.deck.draw(1))