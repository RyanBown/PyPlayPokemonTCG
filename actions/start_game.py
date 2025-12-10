import os
import json 

from models.board import Board, Deck, Hand, Prizes
from models.pokemon_cards import Pokemon, Trainer, Energy
from actions.utils import BASIC_ENERGY_TYPES


def convert_json_to_card(json_card):
    card_name = json_card['name']
    set_num = json_card['id']
    
    if json_card['supertype'] == 'Pokémon':
        return Pokemon(**json_card)
    if json_card['supertype'] == 'Trainer':
        return Trainer(**json_card)
    if json_card['supertype'] == 'Energy':
        if json_card['subtypes'] == ['Basic']:
            json_card['energy_produced'] = json_card['name'].split()[0]
            json_card['energy_effect'] = ''
        else:
            json_card['energy_produced'] = 'Colorless'
        return Energy(**json_card)

def get_decklist_from_deck_json(deck_json,deck_id):
    deck_dir = './pkmn_data/decks/en/'
    deck_path = os.path.join(deck_dir, deck_json + '.json')
    with open(deck_path, encoding='utf-8') as f: 
        decks = json.loads(f.read())
    for row in decks:
        if row['id'] == deck_id:
            return row['cards']
    return None

def get_cards_from_cards_json(cards):
    cards_dir = './pkmn_data/cards/en/'
    sets = {}
    deck_list = []
    for card in cards:
        card_id = ''
        if card['name'] in BASIC_ENERGY_TYPES:
            card_id = BASIC_ENERGY_TYPES[card['name']]
        else:
            card_id = card['id']
        set_name, set_number = card_id.split('-')
        set_list = {}

        if set_name in sets.keys():
            set_list = sets[set_name]
        else:
            card_path = os.path.join(cards_dir, set_name + '.json')
            with open(card_path, encoding='utf-8') as f:
                set_list = json.loads(f.read())
                sets[set_name] = set_list
        

        for set_card in set_list:
            if card_id == set_card['id']:
                for _ in range(card['count']):
                    card_obj = convert_json_to_card(set_card)
                    deck_list.append(card_obj)
                break
    return deck_list


def get_decks_from_deck_id(deck_id):
    deck_parts = deck_id.split('-')
    deck_json = deck_parts[1]
    deck_list = get_decklist_from_deck_json(deck_json,deck_id)
    cards = get_cards_from_cards_json(deck_list)
    return cards 

def player_mulligan(player_deck:Deck, mulligan = 0):

    player_deck.shuffle_deck()
    player_hand = player_deck.look_at(7)
    for card in player_hand:
        if isinstance(card, Pokemon):
            is_pkmn_basic = card.is_basic_pokemon()
            if is_pkmn_basic:
                player_hand = Hand(list(player_deck.draw(7)))
                return [player_hand, mulligan]

    if mulligan < 7:
        return player_mulligan(player_deck, mulligan + 1)
    else:
        player_deck.shuffle_deck()
        for card in player_deck.deck_list:
            if isinstance(card, Pokemon):
                if card.is_basic_pokemon():
                    player_hand = Hand([card])
                    player_deck.remove(card)
                    player_deck.shuffle_deck()
                    for card_drawn in player_deck.draw(6):
                        player_hand.add(card_drawn)
                    return [player_hand, mulligan]


def select_active_from_hand(player_hand):
    choices = []
    for card in player_hand.cards:
        if isinstance(card, Pokemon):
            if card.is_basic_pokemon():
                choices.append(card)
    
    for i, choice in enumerate(choices):
        print(f"press {str(i)} for choice {choice}")

    selected_pkmn = int(input("select your active Pokemon: "))
    return player_hand.remove(choices[selected_pkmn])


def start_the_game(player1_deck_list ='',player2_deck_list=''):
    player_1_deck = ''
    if player1_deck_list == '':
        player_1_deck = Deck(get_decks_from_deck_id('d-swsh4-1'))
    else:
        player_1_deck = Deck(get_cards_from_cards_json(player1_deck_list))
    player_2_deck = ''
    if player2_deck_list == '':
        player_2_deck = Deck(get_decks_from_deck_id('d-swsh4-2'))
    else:
        player_2_deck = Deck(get_cards_from_cards_json(player2_deck_list))


    player_1_hand, player_1_mulligan = player_mulligan(player_1_deck)
    player_2_hand, player_2_mulligan = player_mulligan(player_2_deck)

    player_1_prizes = Prizes(player_1_deck.draw(6))
    player_2_prizes = Prizes(player_2_deck.draw(6))

    if player_2_mulligan != player_1_mulligan:
        extra_draw = 0
        if player_1_mulligan > player_2_mulligan:
            extra_draw = player_1_mulligan - player_2_mulligan
            print(f'Player 2 has {extra_draw} mulligans')
            for card in list(player_1_deck.draw(extra_draw)):
                player_1_hand.add(card)
        else:
            extra_draw = player_2_mulligan - player_1_mulligan
            print(f'Player 1 has {extra_draw} mulligans')
            for card in list(player_2_deck.draw(extra_draw)):
                player_2_hand.add(card)
    else:
        print(f'both players had {player_1_mulligan} mulligans')

    print('player_1\n\thand\n\t\t', player_1_hand)
    print('prizes\n\t\t',player_1_prizes)

    print('player_2\n\thand\n\t\t', player_2_hand)
    print('prizes\n\t\t',player_2_prizes)

    player1_active = select_active_from_hand(player_1_hand)
    player2_active = select_active_from_hand(player_2_hand)

    player1_board = Board(player_1_deck, player_1_prizes, player_1_hand, player1_active, 5, [])
    player2_board = Board(player_2_deck, player_2_prizes,player_2_hand, player2_active, 5, [])
    
    
    return [player1_board, player2_board]
    

