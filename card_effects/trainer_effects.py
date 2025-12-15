from models.board import Board

from effect_utils import shuffle_hand_into_deck

### Supporters
def lillie_s_determination(player1_board:Board, player2_board:Board):
    prize_count = len(player1_board.prizes.cards)
    shuffle_hand_into_deck(player1_board)
    if prize_count == 6:
        player1_board.deck.draw(8)
    else:
        player1_board.deck.draw(6)


def lana_s_aid():
    raise NotImplemented()

def professor_s_research(hand, deck):
    hand.discard(len(hand))
    deck.draw(7)

def boss_s_orders():
    raise NotImplemented()

def hop(deck):
    deck.draw(3)

def bede():
    raise NotImplemented()

def sonia():
    raise NotImplemented()

def dan():
    raise NotImplemented()

def leon():
    raise NotImplemented()

def professor_turo_s_scenario():
    raise NotImplemented()

def nessa():
    raise NotImplemented()


def iono():
    raise NotImplemented()

def arven():
    raise NotImplemented()

def hilda():
    raise NotImplemented()

## Items
def prime_catcher():
    raise NotImplemented()

def earthen_vessel():
    raise NotImplemented()
def fighting_gong():
    raise NotImplemented()
def premium_power_pro():
    raise NotImplemented()
def superior_energy_retrieval():
    raise NotImplemented()
def evolution_incense():
    raise NotImplemented()
def ultra_ball():
    raise NotImplemented()
def great_ball():
    raise NotImplemented()
def nest_ball():
    raise NotImplemented()
def counter_catcher():
    raise NotImplemented()
def night_stretcher():
    raise NotImplemented()
def buddy_buddy_poffin():
    raise NotImplemented()

def ordinary_rod():
    raise NotImplemented()


def switch():
    raise NotImplemented()


def super_rod():
    raise NotImplemented()

##Tools

def air_balloon():
    raise NotImplemented()
def vitality_band():
    raise NotImplemented()
## Stadium

def jamming_tower():
    raise NotImplemented()
def artazon():
    raise NotImplemented()