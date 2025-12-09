from actions.start_game import start_the_game
from actions.player_turn import start_player_turn
from actions.deck_selection import select_deck
import random

if __name__ == '__main__':
    called_result = 'T' #input("[H]eads or [T]ails")

    die_roll = random.randint(1,6)
    result = ''
    if die_roll % 2 == 0:
        result = 'H'
    else:
        result = 'T'

    player_going_first = ''
    if called_result == result:
        player_going_first = '1'
    else:
        player_going_first = '2'

    player1_deck_selected = select_deck('20664')
    player2_deck_selected = select_deck('22012')

    player_1_board, player2_board = start_the_game(player1_deck_selected, player2_deck_selected)

    play_order = []
    if player_going_first == 1:
        play_order = [player_1_board, player2_board]
    else:
        play_order = [player2_board, player_1_board]
    
    game_over = False
    try:
        player1_board, player2_board = play_order
        while not game_over:
            start_player_turn(player1_board, player2_board)
            start_player_turn(player2_board, player1_board)

    except Exception as e:
        print(e)
        

