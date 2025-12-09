import os
import json

from actions.utils import BASIC_ENERGY_TYPES


def translate_ptcgl_set_to_set_id(intl_set, sets_data):
    for set in sets_data:
        if 'ptcgoCode' in set:
            if set['ptcgoCode'] == intl_set:
                return set['id']


def transform_deck_lines_to_cards(deck_lines):
    sets_data_path = './pkmn_data/sets/en.json'
    sets_data = ''
    with open(sets_data_path, encoding='UTF-8') as f:
        sets_data = json.loads(f.read())
    translated_data = {}
    deck_json = []
    for line in deck_lines:
        line_split = line.split()
        count = int(line_split[0])
        set = line_split[-2]
        set_id = ''
        if set in translated_data.keys():
            set_id = translated_data[set]
        else:
            set_id = translate_ptcgl_set_to_set_id(set,sets_data)
            translated_data[set] = set_id
        set_number = line_split[-1]
        card_name = ' '.join(line_split[1:-2])
        row_json = {}
        if card_name in BASIC_ENERGY_TYPES:
            set_id = BASIC_ENERGY_TYPES[card_name]
            row_json = {'name':card_name, 'count':count, 'id': set_id}
        else:
            row_json = {'name':card_name, 'count':count, 'id': set_id + '-' + set_number}
        deck_json.append(row_json)
    return deck_json




def select_deck(deck_selected = 0):
    if deck_selected == 0:
        deck_selected = input('Please Input Deck number:')

    deck_dir = './deck_list/'
    deck_path = os.path.join(deck_dir, deck_selected + '.txt')

    if not os.path.isfile(deck_path):
        select_deck()
    
    deck_text = ''
    with open(deck_path, encoding='UTF-8') as f:
        deck_text = ''.join(f.readlines())
    print(deck_text)
    deck_lines = deck_text.split('\n')
    deck_lines = [line for line in deck_lines if len(line) > 0 and line[0] not in ['P', 'T', 'E']]
    return transform_deck_lines_to_cards(deck_lines)