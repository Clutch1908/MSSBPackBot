#import count tool to track how often a class is called
from itertools import count

#Each class contains static information about each card
#Character Classes
class BabyLuigi:
    name = 'Baby Luigi'
    rarity = 'Rare'
    kind = 'Character'
    odds = '1 : 11.90'
    description = "The younger of the baby Mario brothers. After being abducted by Kamek, he was rescued by Yoshi and Baby Mario. If you see him and Luigi in the same game, try to ignore the temporal paradox. Baby Luigi is quick around the bases but doesn't hit for power. He is, after all, a baby."
    #store image path as a string to be utilized in other scripts
    image = 'main/trading_cards/BabyLuigi.png'
    #define variable to store number of times class has been called upon. 
    _count = count(1)
    #utilize function to count the number of times a class has been called
    def __init__(self):
        self.count = next(self._count)

class BabyMario:
    name = 'Baby Mario'
    rarity = 'Rare'
    kind = 'Character'
    odds = '1 : 11:90'
    description = "The elder of the baby Mario brothers. After arriving in a stork-related calamity, he and Yoshi rescued his little bro. Though he's supposed to be Mario in his youth, you can play them both at the same time for some reason. He has excellent foot speed but lacks power due to his diminutive size."
    image = 'main/trading_cards/BabyMario.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Birdo:
    name = 'Birdo'
    rarity = 'Super Rare'
    kind = 'Character'
    odds = '1 : 140'
    description: ""
    image = 'main/trading_cards/Birdo.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class BlackShyGuy:
    name = 'Black Shy Guy'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/BlackShyGuy.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class BlueDryBones:
    name = 'Blue Dry Bones'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/BlueDryBones.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class BlueNoki:
    name = 'Blue Noki'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/BlueNoki.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class BluePianta:
    name = 'Blue Pianta'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/BluePianta.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class BlueShyGuy:
    name = 'Blue Shy Guy'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/BlueShyGuy.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class BlueToad:
    name = 'Blue Toad'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/BlueToad.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Boo:
    name = 'Boo'
    rarity = 'Super Rare'
    kind = 'Character'
    odds = '1 : 81.6'
    description: ""
    image = 'main/trading_cards/Boo.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class BoomerangBro:
    name = 'Boomerang Bro'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 450'
    description: ""
    image = 'main/trading_cards/BoomerangBro.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Bowser:
    name = 'Bowser'
    rarity = 'Secret Rare'
    kind = 'Character'
    odds = '1 : 200'
    description: ""
    image = 'main/trading_cards/Bowser.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class BowserJr:
    name = 'Bowser Jr.'
    rarity = 'Rare'
    kind = 'Character'
    odds = '1 : 11.90'
    description: ""
    image = 'main/trading_cards/BowserJr.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Daisy:
    name = 'Daisy'
    rarity = 'Rare'
    kind = 'Character'
    odds = '1 : 11.90'
    description: "Sarasara Land's princess. Mario rescued Daisy from the nasty villain Tatanga. While often compared to Peach, Daisy is both stronger and more tomboyish than her blonde counterpart. She uses a Flower Ball that scatters confusing petals."
    image = 'main/trading_cards/Daisy.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class DiddyKong:
    name = 'Diddy Kong'
    rarity = 'Super Rare'
    kind = 'Character'
    odds = '1 : 81.5'
    description: "DK's partner and buddy. Diddy's trademark is his red baseball hat. While Donkey Kong boasts incredible power, Diddy's forte is his nimbleness. Using his prehensile tail to great effect, Diddy Kong is a natural feilder who won't ever boot routine balls."
    image = 'main/trading_cards/DiddyKong.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class DixieKong:
    name = 'Dixie Kong'
    rarity = 'Super Rare'
    kind = 'Character'
    odds = '1 : 81.6'
    description: ""
    image = 'main/trading_cards/DixieKong.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)        

class DK:
    name = 'Donkey Kong'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 150'
    description: "A gorilla known for raw power. DK leads a pretty carefree jungle life... unless someone messes with his bananas, in which case he just loses it. His ancestor, the original Donkey Kong, wore no necktie. His talent lie in beating on primate foes and kart-racing. Fear his Banana Ball!"
    image = 'main/trading_cards/DK.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class DryBones:
    name = 'Dry Bones'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/DryBones.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class FireBro:
    name = 'Fire Bro'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 450'
    description: ""
    image = 'main/trading_cards/FireBro.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Goomba:
    name = 'Goomba'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/Goomba.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class GreenDryBones:
    name = 'Green Dry Bones'
    rarity = 'Rare'
    kind = 'Character'
    odds = '1 : 11.90'
    description: ""
    image = 'main/trading_cards/GreenDryBones.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class GreenKoopaParatroopa:
    name = 'Green Koopa Paratroopa'
    rarity = 'Rare'
    kind = 'Character'
    odds = '1 : 11.90'
    description: ""
    image = 'main/trading_cards/GreenKoopaParatroopa.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class GreenMagikoopa:
    name = 'Green Magikoopa'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 600'
    description: ""
    image = 'main/trading_cards/GreenMagikoopa.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class GreenNoki:
    name = 'Green Noki'
    rarity = 'Rare'
    kind = 'Character'
    odds = '1 : 11.90'
    description: ""
    image = 'main/trading_cards/GreenNoki.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class GreenShyGuy:
    name = 'Green Shy Guy'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/GreenShyGuy.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class GreenToad:
    name = 'Green Toad'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/GreenToad.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class HammerBro:
    name = 'Hammer Bro'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 450'
    description: ""
    image = 'main/trading_cards/HammerBro.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class KingBoo:
    name = 'King Boo'
    rarity = 'Super Rare'
    kind = 'Character'
    odds = '1 : 120'
    description: ""
    image = 'main/trading_cards/KingBoo.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class KoopaParatroopa:
    name = 'Koopa Paratroopa'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/KoopaParatroopa.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class KoopaTroopa:
    name = 'Koopa Troopa'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/KoopaTroopa.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Luigi:
    name = 'Luigi'
    rarity = 'Super Rare'
    kind = 'Character'
    odds = '1 : 100'
    description: "The younger Mario bro. He's a better jumper than Mario but lacks good traction. Always in Mario's shadow, Luigi tends to be low-key but is always a dark horse in athletic contests. Despite perpetually finishing second, his excellent form and green Fireball make him a force."
    image = 'main/trading_cards/Luigi.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Magikoopa:
    name = 'Magikoopa'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 600'
    description: ""
    image = 'main/trading_cards/Magikoopa.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Mario:
    name = 'Mario'
    rarity = 'Super Rare'
    kind = 'Character'
    odds = '1 : 140'
    description: "Everyone's favorite hero. When Peach is in trouble, he always saves the day! A kart racer, tennis player, golf enthusiast, doctor... The list goes on and on, showing he's a jack-of-all-trades. His trademark Fireball will help him in his first foray into baseball."
    image = 'main/trading_cards/Goomba.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class MontyMole:
    name = 'Monty Mole'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/MontyMole.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Paragoomba:
    name = 'Paragoomba'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/Paragoomba.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Peach:
    name = 'Peach'
    rarity = 'Super Rare'
    kind = 'Character'
    odds = '1 : 81.5'
    description: "The Mushroom Kingdom's princess. Mario has come to her rescue every time she's been kidnapped... which has happened no less than 10 times! Some speculate that having an all-Toad security force may be the problem... She joins the game with a Heart Ball as her weapon."
    image = 'main/trading_cards/Peach.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Petey:
    name = 'Petey Piranha'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 150'
    description: ""
    image = 'main/trading_cards/Petey.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class PurpleToad:
    name = 'Purple Toad'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/PurpleToad.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class RedDryBones:
    name = 'Red Dry Bones'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/RedDryBones.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class RedKoopaTroopa:
    name = 'Red Koopa Troopa'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/RedKoopaTroopa.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class RedMagikoopa:
    name = 'Red Magikoopa'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 600'
    description: ""
    image = 'main/trading_cards/RedMagikoopa.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class RedNoki:
    name = 'Red Noki'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/RedNoki.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class RedPianta:
    name = 'Red Pianta'
    rarity = 'Rare'
    kind = 'Character'
    odds = '1 : 11.90'
    description: ""
    image = 'main/trading_cards/RedPianta.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class ShyGuy:
    name = 'Shy Guy'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/ShyGuy.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Toad:
    name = 'Toad'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description: ""
    image = 'main/trading_cards/Toad.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

#Stadium Classes
class BowserCastle:
    name = 'Bowser Castle'
    rarity = 'Common'
    kind = 'Stadium'
    odds = '1 : 10'
    description: "A hot, hot, hot stadium filled with hot, hot lava!"
    image = 'main/trading_cards/BowserCastle.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class DKJungle:
    name = 'Donkey Kong Jungle'
    rarity = 'Super Rare'
    kind = 'Stadium'
    odds = '1 : 29.41'
    description: "A jungle wilderness featuring barrels and Klaptraps."
    image = 'main/trading_cards/DKJungle.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class MarioStadium:
    name = 'Mario Stadium'
    rarity = 'Rare'
    kind = 'Stadium'
    odds = '1 : 23.81'
    description: "A sun-drenched beachside stadium."
    image = 'main/trading_cards/MarioStadium.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class PeachGarden:
    name = 'Peach Garden'
    rarity = 'Ultra Rare'
    kind = 'Stadium'
    odds = '1 : 50'
    description: "A Mushroom Kingdom field with floating blocks."
    image = 'main/trading_cards/PeachGarden.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class ToyField:
    name = 'Toy Field'
    rarity = 'Secret Rare'
    kind = 'Stadium'
    odds = '1 : 250'
    description: "Play with pals as you pitch, bat, and nab bases on this unique field."
    image = 'main/trading_cards/ToyField.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)
#A pastoral ball park infested with Piranha Plants.
#An opulent stadium built with Wario's hard-stolen riches.

#Star Token Classes
class CommonStar:
    name = 'Common Star'
    rarity = 'Common'
    kind = 'Star Token'
    odds = '1 : 50'
    description: "This token can be used to unlock the superstar potential of one common character"
    image = 'main/trading_cards/CommonStar.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class RareStar:
    name = 'Rare Star'
    rarity = 'Rare'
    kind = 'Star Token'
    odds = '1 : 66.67'
    description: "This token can be used to unlock the superstar potential of one rare (or lower) character"
    image = 'main/trading_cards/RareStar.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class SecretStar:
    name = 'Secret Star'
    rarity = 'Secret Rare'
    kind = 'Star Token'
    odds = '1 : 400'
    description: "This token can be used to unlock the superstar potential of one secret rare (or ultra rare/super rare) character. If used on a rare (or lower) chracter, this token will unlock the superstar potential of two characters."
    image = 'main/trading_cards/SecretStar.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class SuperStar:
    name = 'Super Star'
    rarity = 'Super Rare'
    kind = 'Star Token'
    odds = '1 : 133.33'
    description: "This token can be used to unlock the superstar potential of one super rare (or lower) character."
    image = 'main/trading_cards/SecretStar.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

#Consumables Classes
class ExtraPack:
    name = 'Extra Pack'
    rarity = 'Secret Rare'
    kind = 'Consumables'
    odds = '1 : 100'
    description: "Draw one additional pack for this opening!"
    image = 'main/trading_cards/ExtraPack.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Reroll:
    name = 'Reroll'
    rarity = 'Secret Rare'
    kind = 'Consumables'
    odds = '1 : 100'
    description: "You can choose to throw away your current opening and draw a new one!"
    image = 'main/trading_cards/Reroll.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Trade:
    name = 'Trade'
    rarity = 'Secret Rare'
    kind = 'Consumables'
    odds = '1 : 100'
    description: "You can choose to trade one character for another character within the same rarity!"
    image = 'main/trading_cards/Trade.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

#Miscellaneous Classes
class MissedStarChance: 
    name = 'Missed Star Chance'
    rarity = 'Common'
    kind = 'Miscellaneous'
    odds = '1 : 1.92'
    description: "Have to convert on your star chances! (No item obtained for this pack)"
    image = 'main/trading_cards/MissedStar.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)
