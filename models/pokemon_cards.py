from card_effects import trainer_effects
from actions.utils import pythonize_name

class Card:
    def __init__(self, 
                 name, 
                 supertype, 
                 subtypes,
                 number, 
                 id,
                 
                 rarity, 
                 legalities,
                 images,
                 artist,
                 regulationMark = '',
                 rules = ''
                ):
        self.name = name
        self.supertype = supertype
        self.subtypes = subtypes
        self.set = set
        self.number = number
        self.id = id
        self.rules = rules
        self.rarity = rarity
        self.legalities = legalities
        self.regulationMark = regulationMark
        self.images = images
        self.artist = artist
    def __str__(self):
        return f' {self.name} {self.id}'


class Attack:
    def __init__(self, name, cost,converted_energy_cost, damage, text, effect_function):
        self.name = name
        self.cost = cost
        self.converted_energy_cost = converted_energy_cost
        self.damage = damage
        self.text = text
        self.effect_function = effect_function


class Pokemon(Card):
    def __init__(self,name, 
                 supertype, 
                 subtypes,
                 number, 
                 id,
                 
                 rarity, 
                 legalities,
                 regulationMark,
                 images,
                 artist,
                 hp, types, attacks, 
                 weaknesses, 
                 

                 nationalPokedexNumbers,
                 retreatCost='', 
                 convertedRetreatCost=0,
                 rules='', 
                 resistances = '',
                 abilities = [],
                 flavorText = '',
                 evolvesFrom = '',
                 evolvesTo = '' ):
        super().__init__(name, 
                 supertype, 
                 subtypes,
                   
                 number, 
                 id,
                 rules, 
                 rarity, 
                 legalities,
                 regulationMark,
                 images,
                 artist)
        self.hp = hp
        self.types = types,
        self.attacks = attacks
        self.weaknesses = weaknesses
        self.resistances  = resistances 
        self.retreatCost = retreatCost
        self.nationalPokedexNumbers = nationalPokedexNumbers
        self.evolvesFrom = evolvesFrom
        self.evolvesTo = evolvesTo
        self.abilities = abilities
        self.flavorText = flavorText
        self.convertedRetreatCost = convertedRetreatCost

    def is_basic_pokemon(self):
        if 'Basic' in self.subtypes:
            return True
        else:
            return False
    def __str__(self):
        return f' {self.name} {self.id}'


class Trainer(Card):
    def __init__(self,name, 
                 supertype, 
                 subtypes,
                 number, 
                 id,
                 rarity, 
                 artist,
                 legalities,
                 regulationMark,
                 images,
                 rules='', ):
        super().__init__(name, 
                 supertype, 
                 subtypes,
                 artist,
                 number, 
                 id,
                 rules, 
                 rarity, 
                 legalities,
                 regulationMark,
                 images)
        self.card_effect_func = self.get_trainer_func(name)

    def get_trainer_func(self, card_name):
        card_name = pythonize_name(card_name) 
        return getattr(trainer_effects, card_name)
    def __str__(self):
        return f' {self.name} {self.id}'

    def played(self):
        self.card_effect_func()
        
class Energy(Card):
    def __init__(self, name, 
                 supertype, 
                 subtypes,
                 number, 
                 id,
                 artist,
                 legalities,
                 images,  
                 energy_produced,
                 regulationMark = '',
                 energy_effect = '',
                 rules='',
                 rarity = ''  ):
        super().__init__(name, 
                 supertype, 
                 subtypes,
                 artist,
                 number, 
                 id,
                 rules, 
                 rarity, 
                 legalities,
                 regulationMark,
                 images)
        self.energy_produced = energy_produced
        self.energy_effect = energy_effect

    def attached(self):
        self.energy_effect()
    
    def __str__(self):
        return f' {self.name} {self.id}'