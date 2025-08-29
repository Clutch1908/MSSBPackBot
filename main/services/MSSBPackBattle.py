#import random module
import random
#set up SystemRandom to use non-seeded RNG for packs
_sysrand = random.SystemRandom()

def construct_challenge_message(challengerID, recepientID, recepientNameStr):
    challengeMessage= ""
    challengerIDconstructed = "<@" + challengerID + ">"
    recepientIDconstructed = "<@" + recepientID + ">" 
    challengeFlair = _sysrand.randint(1,5)
    if challengeFlair == 1:
        #reference: VGHS
        challengeMessage += "WOAH!!! Everybody, check out the size of this kid's Pokéballs! " + challengerIDconstructed + ",just challenged " + recepientIDconstructed + ", to a match!"
    elif challengeFlair == 2:
        #reference: YGO
        challengeMessage += recepientIDconstructed + ", it's time to d-d-d-d-d-d-d-duel! \nChallenge sent by:" + challengerIDconstructed
    elif challengeFlair == 3:
        #reference: MSSB
        challengeMessage += recepientIDconstructed + ", let's play, a baseball game, yeah! \nChallenge sent by:" + challengerIDconstructed
    elif challengeFlair == 4:
        #reference: Xiaolin Showdown
        challengeMessage += recepientIDconstructed + ", I challenge you to a Xiaolin Showdown! The game is Pack Battle. \nChallenge sent by:" + challengerIDconstructed
    elif challengeFlair == 5:
        #reference: LoZ
        challengeMessage += recepientIDconstructed + ", it's dangerous to go alone! Take this. (This being a bunch of cards... eh you get it) \nChallenge sent by:" + challengerIDconstructed
    else:
        #catch if somehow we spin a non-accounted for integer
        challengeMessage += "Huh, seems like the challenge machine is on the fritz... anyways " + recepientIDconstructed + " do you want to play a Pack Battle with " + challengerIDconstructed + "?" 

    #add Pack Battle Rules to the challenge
    challengeRules = "\n ```\n*PACK BATTLE RULES*\n\n--7 inning games, Star Skills On, Hazards On, Drop Spots On\n--All standard codes enabled, plus 'No Captain Code'\n--You will draw 5 packs to form your team\n--If you do not open a captain, you will select Yoshi as your captain and then remove them for 9 standard characters.\n--You cannot use duplicate characters if you pull multiple of the same character [Variants do not count as the same character ex. you can have one Dry Bones and one Blue Dry Bones on your team]. If you have less than 9 unique characters after opening your packs, you may use any 'Common' duplicates to fill out any remaining spots on your roster\n--If you draw a 'Star Token' and use it to star a character, that character is ineligible to pitch\n--If you draw an 'Extra Pack' consumable, you will get to open an additional pack to use for this game\n--If you draw a 'Reroll' consumable, you will be given the option to reroll your entire opening for 5 new packs and use that card pool instead\n--If you draw a 'Trade' consumable, you can trade one character in for a different character of the same rarity\n--Stadium and Home/Away is chosen by the player with more stadiums in their pack opening. You can choose any stadium that you opened. If there is a tie, choose from the stadiums shared by both player's collections and flip a coin/agree on who picks home or away.\n```"
    challengeMessage += challengeRules
    challengeConfirm = "\n" + recepientNameStr + ", do you accept this challenge?"
    return challengeMessage, challengeConfirm
