from models.board import Board
from models.pokemon_cards import Pokemon, Trainer, Energy





def turn_loop(player_board:Board, opp_board:Board, supporter_played, attach_for_turn, stadium_played, retreat_for_turn):
    print(player_board.hand)
    decision = input('[1] Play card from hand\n[2] retreat\n[3] Activate Ability \n[4] Attack\n[5] End Turn\n\tChoose:')
    is_energy_in_hand = False
    for i,card in enumerate(player_board.hand.cards):
        print(i, card.name)
        if isinstance(card, Pokemon):
            print(f'\tHP {card.hp}')
            for attack in card.attacks:
                print('\t',attack)
            print('retreat\n\t', card.convertedRetreatCost)
            print('weakness\n\t', card.weaknesses)
            print('resist\n\t', card.resistances)
        if isinstance(card, Trainer):
            print(f'\nText\n\t',card.rules)
        if isinstance(card, Energy):
            is_energy_in_hand = True
            if 'Basic' in card.subtypes:

                continue
            else:
                print(f'\nText\n\t',card.rules)
    if decision == '1':
        hand = player_board.hand
        print('play from hand')
        card_selected = input('card number:')
    if decision == '2':
        print('retreat')
    if decision == '3':
        print('ability')
    if decision == '4':
        print('attack')
        if attach_for_turn == 0 and is_energy_in_hand == True:
            answer = input("Are you you want to attack?\nYou haven't attached for turn")
            if answer == 'y':
                return 'End'
        else:
            return 'End'
    if decision == '5':
        answer = input('Are you sure to end the turn?[y/n]')
        if answer == 'y':
            return 'End'

    
    return turn_loop(player_board, opp_board, supporter_played, attach_for_turn, stadium_played, retreat_for_turn)

def start_player_turn(player_board:Board, opp_board:Board):
    supporter_played = 0
    attach_for_turn = 0
    stadium_played = 0
    retreat_for_turn = 0

    return turn_loop(player_board, opp_board, supporter_played, attach_for_turn, stadium_played, retreat_for_turn)

    