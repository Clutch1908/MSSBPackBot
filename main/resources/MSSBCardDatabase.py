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
    description = "A dinosaur that spits eggs from her huge mouth. Birdo is very particular when it comes to fashion, though her reliance on the color pink is a bit limiting. Her bow and ring are her pride and joy. Birdo's mouth has massive suction that can even catch a ball by sucking it in."
    image = 'main/trading_cards/Birdo.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class BlackShyGuy:
    name = 'Black Shy Guy'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "\"I could never figure out how a non-red Guy could hit fly balls so well... Don't tell anyone I said that though I don't want to get canceled.\" -- Cornpop"
    image = 'main/trading_cards/BlackShyGuy.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class BlueDryBones:
    name = 'Blue Dry Bones'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "\"I wonder if this is Koopley... haven't heard from him since he went off to Hooktail's Castle\" -- Cornpop"
    image = 'main/trading_cards/BlueDryBones.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class BlueNoki:
    name = 'Blue Noki'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "A mysterious member of a clan living on the southern paradise of Delfino Island. Nokis evolved from shellfish, and their ancestors are believed to have lived in the sea. While they are skillful and fast runners, they are hampered by a lack of power."
    image = 'main/trading_cards/BlueNoki.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class BluePianta:
    name = 'Blue Pianta'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "A cheerful islander living on the southern paradise called Delfino Island. Piantas are said to be born of the mountains, and they are distinguished by the palm tree growing from their heads. Their power makes them flashy, but they're clumsy and slow runners."
    image = 'main/trading_cards/BluePianta.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class BlueShyGuy:
    name = 'Blue Shy Guy'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "\"I hear this Guy does some selling on the side of some... not so great substances.\" -- Cornpop"
    image = 'main/trading_cards/BlueShyGuy.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class BlueToad:
    name = 'Blue Toad'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "\"He once shed a teardrop on my guitar.\" -- Cornpop"
    image = 'main/trading_cards/BlueToad.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Boo:
    name = 'Boo'
    rarity = 'Super Rare'
    kind = 'Character'
    odds = '1 : 81.6'
    description = "Bowser's underling ghost. Behind the scary face lies a very shy soul. Look most Boos in the eyes and they'll cover their faces... but turn around and they'll attack you! Boos confuse their enemies by flickering in and out of the visible realm, appearing at inconvenient times."
    image = 'main/trading_cards/Boo.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class BoomerangBro:
    name = 'Boomerang Bro'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 450'
    description = "\"For being a 'Bro', it's crazy how much of a 'Boomer' he actually is.\" -- Cornpop"
    image = 'main/trading_cards/BoomerangBro.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Bowser:
    name = 'Bowser'
    rarity = 'Secret Rare'
    kind = 'Character'
    odds = '1 : 300'
    description = "Mario's archrival and the king of the Koopa clan. He's challenged Mario and his friends to battles countless times, but his ambitions tend to get crushed every time. His lethal Killer Ball is powerful enough to drag anyone catching it across the field!"
    image = 'main/trading_cards/Bowser.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class BowserJr:
    name = 'Bowser Jr.'
    rarity = 'Rare'
    kind = 'Character'
    odds = '1 : 11.90'
    description = "Bowser's exuberant son. Bowser lied to him and convinced Jr. that Peach was his mom, resulting in a chaotic adventure for Mario and company. Bowser thinks the Koopa clan is in good hands with his son. He's not just powerful but also suprisingly skilled."
    image = 'main/trading_cards/BowserJr.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Daisy:
    name = 'Daisy'
    rarity = 'Rare'
    kind = 'Character'
    odds = '1 : 11.90'
    description = "Sarasara Land's princess. Mario rescued Daisy from the nasty villain Tatanga. While often compared to Peach, Daisy is both stronger and more tomboyish than her blonde counterpart. She uses a Flower Ball that scatters confusing petals."
    image = 'main/trading_cards/Daisy.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class DiddyKong:
    name = 'Diddy Kong'
    rarity = 'Super Rare'
    kind = 'Character'
    odds = '1 : 81.5'
    description = "DK's partner and buddy. Diddy's trademark is his red baseball hat. While Donkey Kong boasts incredible power, Diddy's forte is his nimbleness. Using his prehensile tail to great effect, Diddy Kong is a natural feilder who won't ever boot routine balls."
    image = 'main/trading_cards/DiddyKong.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class DixieKong:
    name = 'Dixie Kong'
    rarity = 'Super Rare'
    kind = 'Character'
    odds = '1 : 81.6'
    description = "Diddy Kong's partner and girlfriend. Her trademark golden ponytail is familiar to monkey fans everywhere. Dixie Kong is just as adventurous as both Diddy Kong and Donkey Kong. Combining great techniques with fast legs, she is a very dependable player."
    image = 'main/trading_cards/DixieKong.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)        

class DK:
    name = 'Donkey Kong'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 150'
    description = "A gorilla known for raw power. DK leads a pretty carefree jungle life... unless someone messes with his bananas, in which case he just loses it. His ancestor, the original Donkey Kong, wore no necktie. His talent lie in beating on primate foes and kart-racing. Fear his Banana Ball!"
    image = 'main/trading_cards/DK.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class DryBones:
    name = 'Dry Bones'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "A bony underling of Bowser. Some mysterious power binds the skeletal bodies of Dry Bones together, but they shatter to pieces when they take damage. Of course, over time, they go right back to the way they were without ill effect. Dry Bones throws cursed balls when he pitches."
    image = 'main/trading_cards/DryBones.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class FireBro:
    name = 'Fire Bro'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 450'
    description = "\"FireGOAT!\" -- CritNick"
    image = 'main/trading_cards/FireBro.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Goomba:
    name = 'Goomba'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "Though Goombas once lived in peace in the Mushroom Kingdom, they betrayed their homeland to side with Bowser. Exactly how Goomba uses his baseball gear is a bit of a mystery. Maybe you can spot the secret technique if you watch closely as he makes plays in the field..."
    image = 'main/trading_cards/Goomba.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class GreenDryBones:
    name = 'Green Dry Bones'
    rarity = 'Rare'
    kind = 'Character'
    odds = '1 : 11.90'
    description = "\"He'll be hitting line drives from beyond the grave for all of eternity.\" -- Cornpop"
    image = 'main/trading_cards/GreenDryBones.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class GreenKoopaParatroopa:
    name = 'Green Koopa Paratroopa'
    rarity = 'Rare'
    kind = 'Character'
    odds = '1 : 11.90'
    description = "\"Man I've seen Para hit liners into the gap as fast as he can fly!\" -- Cornpop"
    image = 'main/trading_cards/GreenKoopaParatroopa.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class GreenMagikoopa:
    name = 'Green Magikoopa'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 600'
    description = "\"Rumor has it that their cloak is green because they wipe all their boogers on their cloak. If it's true, they should get checked out by Dr. Mario!\" -- Cornpop"
    image = 'main/trading_cards/GreenMagikoopa.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class GreenNoki:
    name = 'Green Noki'
    rarity = 'Rare'
    kind = 'Character'
    odds = '1 : 11.90'
    description = "\"Lookin' good Ms. 800!\" -- Cornpop"
    image = 'main/trading_cards/GreenNoki.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class GreenShyGuy:
    name = 'Green Shy Guy'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "\"I've heard a lot of people have had a near-death experience with this Guy on the mound.\" -- Cornpop"
    image = 'main/trading_cards/GreenShyGuy.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class GreenToad:
    name = 'Green Toad'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "\"Good baseball player, better tractor driver.\" -- Cornpop"
    image = 'main/trading_cards/GreenToad.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class HammerBro:
    name = 'Hammer Bro'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 450'
    description = "One of Mario's oldest and most annoying foes. The Hammer Bro is said to be the mightiest warrior of Bowser's army. Besides the hammer-throwing varity, there are also Boomerang and Fire Bros as well. Teams fear his agressive play and lethal bat."
    image = 'main/trading_cards/HammerBro.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class KingBoo:
    name = 'King Boo'
    rarity = 'Super Rare'
    kind = 'Character'
    odds = '1 : 120'
    description = "The king of the Boos. The golden crown is his trademark, and while he looks similar to other Boos, it's obvious that he's much larger than the others. Not only is he powerful, but he's also a fast runner that gets his speed by hovering over the base paths."
    image = 'main/trading_cards/KingBoo.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class KoopaParatroopa:
    name = 'Koopa Paratroopa'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "Another longtime underling of Bowser. Paratroopa flies through the sky and delivers body checks to Mario and others, but he's vulnerable to a good stomping, which takes away his wings and turns him into a garden-variety Koopa. His wings allow him to leap up and make great catches."
    image = 'main/trading_cards/KoopaParatroopa.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class KoopaTroopa:
    name = 'Koopa Troopa'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "A familiar face of the Mario series, this member of the Koopa clan can pull his feet inside his shell to protect himself. Long ago, he didn't even walk upright, but now he's even playing baseball! Though he can do just about everything, he's slow because... well, you know."
    image = 'main/trading_cards/KoopaTroopa.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Luigi:
    name = 'Luigi'
    rarity = 'Super Rare'
    kind = 'Character'
    odds = '1 : 100'
    description = "The younger Mario bro. He's a better jumper than Mario but lacks good traction. Always in Mario's shadow, Luigi tends to be low-key but is always a dark horse in athletic contests. Despite perpetually finishing second, his excellent form and green Fireball make him a force."
    image = 'main/trading_cards/Luigi.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Magikoopa:
    name = 'Magikoopa'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 600'
    description = "A resident magician of the Koopa clan. The best of the Magikoopas, Kamek, once attempted to abduct the baby Mario brothers, but Yoshi and Baby Mario thwarted his sinister plan. The magic powers of the Magikoopa wand also come in handy in the game of baseball."
    image = 'main/trading_cards/Magikoopa.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Mario:
    name = 'Mario'
    rarity = 'Super Rare'
    kind = 'Character'
    odds = '1 : 140'
    description = "Everyone's favorite hero. When Peach is in trouble, he always saves the day! A kart racer, tennis player, golf enthusiast, doctor... The list goes on and on, showing he's a jack-of-all-trades. His trademark Fireball will help him in his first foray into baseball."
    image = 'main/trading_cards/Goomba.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class MontyMole:
    name = 'Monty Mole'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "A lively, sometimes surly mole who lives underground and leaps out whenever someone approaches his den. He usually keeps to himself but always gets fired up for a good baseball game. In fact, when he gets the ball, he almost gets TOO fired up!"
    image = 'main/trading_cards/MontyMole.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Paragoomba:
    name = 'Paragoomba'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "A Goomba with wings. Just like Koopa Paratroopa, Paragoombas lose their wings and turn into Goombas if they get stepped on. The Goomba family is made up of expert bunters, although no one really makes a big deal about it. Bunting, after all, isn't all that glamorous."
    image = 'main/trading_cards/Paragoomba.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Peach:
    name = 'Peach'
    rarity = 'Super Rare'
    kind = 'Character'
    odds = '1 : 81.5'
    description = "The Mushroom Kingdom's princess. Mario has come to her rescue every time she's been kidnapped... which has happened no less than 10 times! Some speculate that having an all-Toad security force may be the problem... She joins the game with a Heart Ball as her weapon."
    image = 'main/trading_cards/Peach.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Petey:
    name = 'Petey Piranha'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 150'
    description = "A mutation created this boss of the Piranha Plants. Petey can fly in the air for a short while, flapping the leaves that he has evolved into primitive arms. When Petey spits a ball out of his toothy mouth, it is lightning-fast."
    image = 'main/trading_cards/Petey.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class PurpleToad:
    name = 'Purple Toad'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "\"I'm tired of him always LEANING when I'm pitching to him\" -- Cornpop"
    image = 'main/trading_cards/PurpleToad.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class RedDryBones:
    name = 'Red Dry Bones'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "\"I've also heard people call him Dark Bones, but maybe he's really a Light Bones on the inside.\" -- Cornpop"
    image = 'main/trading_cards/RedDryBones.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class RedKoopaTroopa:
    name = 'Red Koopa Troopa'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "\"Wait!?! Is that THE RONald Acuna Jr.?\" -- Cornpop"
    image = 'main/trading_cards/RedKoopaTroopa.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class RedMagikoopa:
    name = 'Red Magikoopa'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 600'
    description = "\"With a slap power of 50 and a charge power of 45, you're mostly going to be going for his star hit, being a Falcon Pop.\" -- Mr. Joe... I mean Ravian... I mean Ravian posing as Mr. Joe?"
    image = 'main/trading_cards/RedMagikoopa.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class RedNoki:
    name = 'Red Noki'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "\"Does Red Noki ever get sunburnt?\" -- Cornpop"
    image = 'main/trading_cards/RedNoki.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class RedPianta:
    name = 'Red Pianta'
    rarity = 'Rare'
    kind = 'Character'
    odds = '1 : 11.90'
    description = "\"He's just standing there... MENACINGLY!\" -- Patrick Star"
    image = 'main/trading_cards/RedPianta.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class ShyGuy:
    name = 'Shy Guy'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "A charming, masked soldier. Shy Guys used to serve an evil king named Wart, but they nowadays make a lot of cameo appearances as friendly rivals of Mario. That said, they aren't always good... On the baseball diamond, Shy Guys are consistent players with few weaknesses."
    image = 'main/trading_cards/ShyGuy.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Toad:
    name = 'Toad'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "Princess Peach's subject. Though he tries to protect the princess from the evil hands of Bowser, she gets kidnapped with disturbing regularity. There are many Toads who look just alike, and though they are generally small and look cute, they are actually quite powerful."
    image = 'main/trading_cards/Toad.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Toadette:
    name = 'Toadette'
    rarity = 'Rare'
    kind = 'Character'
    odds = '1 : 11.90'
    description = "A cute Toad girl with plaited locks. Though her profile is relatively unknown, she is definitely a cheery, upbeat girl who is full of energy. Taking advantage of her fast legs and light weight, Toadette can make all sorts of difficult plays look completely routine."
    image = 'main/trading_cards/Toadette.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Toadsworth:
    name = 'Toadsworth'
    rarity = 'Rare'
    kind = 'Character'
    odds = '1 : 11.90'
    description = "Princess Peach's attendant. Though he says his life gets shorter every time Princess Peach gets abducted, he is always in good health and full of energy. While he lacks for stamina, he makes up for it by making cool plays that take advantage of his long life's worth of experience."
    image = 'main/trading_cards/Toadsworth.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Waluigi:
    name = 'Waluigi'
    rarity = 'Super Rare'
    kind = 'Character'
    odds = '1 : 120'
    description = "Luigi's eccentric rival. Waluigi is a hardworking player who has been training night and day to gain enough power to best Luigi. The eggplant that his Liar Ball delivers is said to have the power to make those who touch it almost lose their lunches."
    image = 'main/trading_cards/Waluigi.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Wario:
    name = 'Wario'
    rarity = 'Super Rare'
    kind = 'Character'
    odds = '1 : 100'
    description = "According to Wario, he's both Mario's rival and childhood friend. (This is unconfirmed.) He actually runs his own video-game company and has produced many hot sellers. Garlic is Wario's favorite food. It may lend him incredible stamina, which makes him excellent at daring plays."
    image = 'main/trading_cards/Wario.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class WildSR:
    name = 'Wild Super Rare'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 150'
    description = "This rainbow token has the power to call on any one Super Rare character"
    image = 'main/trading_cards/WildSR.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class WildUR:
    name = 'Wild Ultra Rare'
    rarity = 'Secret Rare'
    kind = 'Character'
    odds = '1 : 150'
    description = "This rainbow token has the power to call on any one Ultra Rare character"
    image = 'main/trading_cards/WildUR.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class YellowMagikoopa:
    name = 'Yellow Magikoopa'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 600'
    description = "\"I've heard Yellow Magikoopa has been working on some new spells to invent never before thrown pitches. I'm guessing Lakitu would make them illegal though.\" -- Cornpop"
    image = 'main/trading_cards/YellowMagikoopa.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class YellowPianta:
    name = 'Yellow Pianta'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "\"I heard he got his nickname 'Yif Daddy' from Don Pianta himself.\" -- Cornpop"
    image = 'main/trading_cards/YellowPianta.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class YellowShyGuy:
    name = 'Yellow Shy Guy'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "\"I'm convinced this Guy might be my long lost cousin, we have the same colored eyes!\" -- Cornpop"
    image = 'main/trading_cards/YellowShyGuy.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class YellowToad:
    name = 'Yellow Toad'
    rarity = 'Common'
    kind = 'Character'
    odds = '1 : 7.66'
    description = "\"Hey, how did I end up on a trading card?\" -- Cornpop"
    image = 'main/trading_cards/YellowToad.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Yoshi:
    name = 'Yoshi'
    rarity = 'Ultra Rare'
    kind = 'Character'
    odds = '1 : 150'
    description = "A denizen of Yoshi's Island. Mario's dependable buddy always helps him out of jams. Yoshis use their long tongues to eat anything and everything. It's said that Yoshis can turn anything they swallow into eggs. On the diamond, Yoshi's fast legs and accurate tounge make him a great fielder."
    image = 'main/trading_cards/Yoshi.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

#Stadium Classes
class BowserCastle:
    name = 'Bowser Castle'
    rarity = 'Common'
    kind = 'Stadium'
    odds = '1 : 10'
    description = "A hot, hot, hot stadium filled with hot, hot lava!"
    image = 'main/trading_cards/BowserCastle.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class DKJungle:
    name = 'Donkey Kong Jungle'
    rarity = 'Super Rare'
    kind = 'Stadium'
    odds = '1 : 29.41'
    description = "A jungle wilderness featuring barrels and Klaptraps."
    image = 'main/trading_cards/DKJungle.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class MarioStadium:
    name = 'Mario Stadium'
    rarity = 'Rare'
    kind = 'Stadium'
    odds = '1 : 23.81'
    description = "A sun-drenched beachside stadium."
    image = 'main/trading_cards/MarioStadium.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class PeachGarden:
    name = 'Peach Garden'
    rarity = 'Ultra Rare'
    kind = 'Stadium'
    odds = '1 : 50'
    description = "A Mushroom Kingdom field with floating blocks."
    image = 'main/trading_cards/PeachGarden.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class ToyField:
    name = 'Toy Field'
    rarity = 'Secret Rare'
    kind = 'Stadium'
    odds = '1 : 250'
    description = "Play with pals as you pitch, bat, and nab bases on this unique field."
    image = 'main/trading_cards/ToyField.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class WarioPalace:
    name = 'Wario Palace'
    rarity = 'Common'
    kind = 'Stadium'
    odds = '1 : 10'
    description = "An opulent stadium built with Wario's hard-stolen riches."
    image = 'main/trading_cards/WarioPalace.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class YoshiPark:  
    name = 'Yoshi Park'
    rarity = 'Common'
    kind = 'Stadium'
    odds = '1 : 10'
    description = "A pastoral ball park infested with Piranha Plants."
    image = 'main/trading_cards/YoshiPark.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)   

#Star Token Classes
class CommonStar:
    name = 'Common Star'
    rarity = 'Common'
    kind = 'Star Token'
    odds = '1 : 50'
    description = "This token can be used to unlock the superstar potential of one common character"
    image = 'main/trading_cards/CommonStar.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class RareStar:
    name = 'Rare Star'
    rarity = 'Rare'
    kind = 'Star Token'
    odds = '1 : 66.67'
    description = "This token can be used to unlock the superstar potential of one rare (or lower) character"
    image = 'main/trading_cards/RareStar.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class SecretStar:
    name = 'Secret Star'
    rarity = 'Secret Rare'
    kind = 'Star Token'
    odds = '1 : 400'
    description = "This token can be used to unlock the superstar potential of one secret rare (or ultra rare/super rare) character. If used on a rare (or lower) chracter, this token will unlock the superstar potential of two characters."
    image = 'main/trading_cards/SecretStar.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class SuperStar:
    name = 'Super Star'
    rarity = 'Super Rare'
    kind = 'Star Token'
    odds = '1 : 133.33'
    description = "This token can be used to unlock the superstar potential of one super rare (or lower) character."
    image = 'main/trading_cards/SecretStar.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class UltraStar:
    name = 'Ultra Star'
    rarity = 'Ultra Rare'
    kind = 'Star Token'
    odds = '1 : 200'
    description = "This token can be used to unlock the superstar potential of one ultra rare (or lower) character. If used on a common chracter, this token will unlock the superstar potential of two characters."
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
    description = "Draw one additional pack for this opening!"
    image = 'main/trading_cards/ExtraPack.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Reroll:
    name = 'Reroll'
    rarity = 'Secret Rare'
    kind = 'Consumables'
    odds = '1 : 100'
    description = "You can choose to throw away your current opening and draw a new one!"
    image = 'main/trading_cards/Reroll.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)

class Trade:
    name = 'Trade'
    rarity = 'Secret Rare'
    kind = 'Consumables'
    odds = '1 : 100'
    description = "You can choose to trade one character for another character within the same rarity!"
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
    description = "Have to convert on your star chances! (No item obtained for this pack)"
    image = 'main/trading_cards/MissedStar.png'
    _count = count(1)
    def __init__(self):
        self.count = next(self._count)


card_dict = {
        0:Mario, 
        1:Luigi, 
        2:DK, 
        3:DiddyKong, 
        4:Peach, 
        5:Daisy, 
        6:Yoshi, 
        7:BabyMario, 
        8:BabyLuigi, 
        9:Bowser, 
        10:Wario, 
        11:Waluigi, 
        12:KoopaTroopa, 
        13:Toad, 
        14:Boo, 
        15:Toadette, 
        16:ShyGuy, 
        17:Birdo, 
        18:MontyMole, 
        19:BowserJr, 
        20:KoopaParatroopa, 
        21:BluePianta, 
        22:RedPianta,
        23:YellowPianta, 
        24:BlueNoki, 
        25:RedNoki, 
        26:GreenNoki, 
        27:HammerBro, 
        28:Toadsworth, 
        29:BlueToad, 
        30:YellowToad, 
        31:GreenToad, 
        32:PurpleToad, 
        33:Magikoopa, 
        34:RedMagikoopa, 
        35:GreenMagikoopa, 
        36:YellowMagikoopa, 
        37:KingBoo, 
        38:Petey, 
        39:DixieKong, 
        40:Goomba, 
        41:Paragoomba, 
        42:RedKoopaTroopa, 
        43:GreenKoopaParatroopa, 
        44:BlueShyGuy, 
        45:YellowShyGuy, 
        46:GreenShyGuy, 
        47:BlackShyGuy, 
        48:DryBones, 
        49:GreenDryBones, 
        50:RedDryBones, 
        51:BlueDryBones, 
        52:FireBro, 
        53:HammerBro, 
        54:WildSR, 
        55:WildUR, 
        56:BowserCastle, 
        57:DKJungle, 
        58:MarioStadium, 
        59:PeachGarden, 
        60:ToyField, 
        61:WarioPalace, 
        62:YoshiPark, 
        63:CommonStar, 
        64:RareStar, 
        65:SecretStar, 
        66:SuperStar, 
        67:UltraStar,
        68:ExtraPack,
        69:Reroll,
        70:Trade,
        71:MissedStarChance
} 
common_dict = {
        1:BluePianta, 
        2:BlueNoki, 
        3:RedNoki, 
        4:ShyGuy, 
        5:BlackShyGuy, 
        6:YellowPianta, 
        7:PurpleToad, 
        8:RedKoopaTroopa, 
        9:RedDryBones, 
        10:Goomba, 
        11:Paragoomba, 
        12:KoopaParatroopa, 
        13:GreenShyGuy, 
        14:MontyMole, 
        15:BlueToad, 
        16:YellowToad, 
        17:GreenToad, 
        18:KoopaTroopa, 
        19:BlueShyGuy, 
        20:YellowShyGuy, 
        21:DryBones, 
        22:BlueDryBones, 
        23:Toad
}
rare_dict = {
        1:Toadette, 
        2:GreenDryBones, 
        3:Daisy, 
        4:BowserJr, 
        5:BabyMario, 
        6:BabyLuigi, 
        7:GreenKoopaParatroopa, 
        8:GreenNoki, 
        9:Toadsworth, 
        10:RedPianta
}
superrare_dict = {
        1:Peach, 
        2:DiddyKong, 
        3:Boo, 
        4:DixieKong,
        5:Luigi, 
        6:Wario, 
        7:Waluigi, 
        8:KingBoo, 
        9:Mario, 
        10:Birdo
}
ultrarare_dict = {
        1:WildSR, 
        2:Yoshi, 
        3:DK, 
        4:Petey, 
        5:HammerBro, 
        6:BoomerangBro, 
        7:FireBro, 
        8:Magikoopa, 
        9:RedMagikoopa,
        10:GreenMagikoopa, 
        11:YellowMagikoopa
}
secretrare_dict = {
        1:WildUR, 
        2:Bowser
}
stadium_dict = {
        1:YoshiPark, 
        2:BowserCastle, 
        3:WarioPalace, 
        4:MarioStadium, 
        5:DKJungle, 
        6:PeachGarden, 
        7:ToyField
}
starchance_dict = {
        1:CommonStar, 
        2:RareStar, 
        3:SuperStar, 
        4:UltraStar, 
        5:SecretStar
}
consumables_dict = {
        1: ExtraPack, 
        2:Reroll,
        3:Trade
}
misc_dict = {
        1: MissedStarChance
}