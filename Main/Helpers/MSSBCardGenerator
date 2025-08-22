#import all cards to be called upon
import MSSBCardDatabase
#import random module
import random
#import regular expresions to format count outputs
import re
#import reload function to reset counts after opening has been completed
import importlib import reload

#set up SystemRandom to use non-seeded RNG for packs
_sysrand = random.SystemRandom()

#initalize gloabl variable that stores the number of packs that have been opened in a session
global packsOpened
packsOpened = 0

#initalize global variables to store card information as it is rolled by the function
global selectedCardOutput_1
global selectedCardOutput_2
global selectedCardOutput_3
global selectedCardOutput_4
global selectedCardOutput_5

#initalize global variable that determines if a Reroll item has been opened in this pack session
global rerollOpened
rerollOpened = False

#define function to open 5 card packs
def openPack():
    #set up the first 3 card pulls, which will always be common cards
    cardOne = _sysrand.randint(1,23)
    selectedCard = MSSBCardDatabase.common_dict[cardOne]
    #create callout to return the number of times a card has been pulled
    def count():
        return MSSBCardDatabase.common_dict[cardOne]()._count
    #define variable that alters count into a string
    countStr = str(count())
    #define variable that strips string formatting to return the integer value of the card pulled
    countStrNum = re.findall(r'\d+',countStr)
    #create variable to concatonate string to output the card selected by the Pack Opener. The join function is needed to output countStrNum as a list
