from actions.start_game import start_the_game
import random

if __name__ == '__main__':
    called_result = input("[H]eads or [T]ails")

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

    player_1_board, player2_board = start_the_game()

    play_order = []
    if player_going_first == 1:
        play_order = [player_1_board, player2_board]
    else:
        play_order = [player2_board, player_1_board]
    
    game_over = False
    while not game_over:
        for player_turn in play_order:
            player_turn.start_turn()
            
        

