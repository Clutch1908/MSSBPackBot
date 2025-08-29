#import all cards to be called upon
from resources import MSSBCardDatabase
#import random module
import random
#import reload function to reset counts after opening has been completed
from importlib import reload
#import image helper script
from helpers import ImageBuilder
#set up SystemRandom to use non-seeded RNG for packs
_sysrand = random.SystemRandom()
#import Discord libraries
import discord

#define function to open 5 card packs
def openPack():
    #initialize card image variables
    selectedCardImage_1 = ''
    selectedCardImage_2 = ''  
    selectedCardImage_3 = ''
    selectedCardImage_4 = ''
    selectedCardImage_5 = ''
    #initalize card image list
    cardImageList = []
    #set up the first 3 card pulls, which will always be common cards
    cardOne = _sysrand.randint(1,23)
    selectedCard = MSSBCardDatabase.common_dict[cardOne]
    selectedCardImage_1 = selectedCard.image
    cardImageList.append(selectedCardImage_1)

    itemCard = _sysrand.randint (1, 10000)
    if itemCard <= 4000:
        stadiumCardWeight = _sysrand.randint (1, 10000)
        if stadiumCardWeight <= 2500:
            cardFour = 1
        elif stadiumCardWeight >= 2501 and stadiumCardWeight <= 5000:
            cardFour = 2
        elif stadiumCardWeight >= 5001 and stadiumCardWeight <= 7500:
            cardFour = 3
        elif stadiumCardWeight >= 7501 and stadiumCardWeight <= 8550:
            cardFour = 4
        elif stadiumCardWeight >= 8551 and stadiumCardWeight <= 9400:
            cardFour = 5
        elif stadiumCardWeight >= 9401 and stadiumCardWeight <= 9900:
            cardFour = 6
        elif stadiumCardWeight >= 9901:
            cardFour = 7
        else:
            print("Error in code")
        selectedCard = MSSBCardDatabase.stadium_dict[cardFour]
        selectedCardImage_4 = selectedCard.image
    elif itemCard >= 4001 and itemCard <= 4500:
        starCardWeight = _sysrand.randint (1, 10000)
        if starCardWeight <= 4000:
            cardFour = 1
        elif starCardWeight >= 4001 and starCardWeight <= 7000:
            cardFour = 2
        elif starCardWeight >= 7001 and starCardWeight <= 8500:
            cardFour = 3
        elif starCardWeight >= 8501 and starCardWeight <= 9500:
            cardFour = 4
        elif starCardWeight >= 9501:
            cardFour = 5
        else:
            print("Error in code")
        selectedCard = MSSBCardDatabase.starchance_dict[cardFour]
        selectedCardImage_4 = selectedCard.image
    elif itemCard >= 4501 and itemCard <= 4600:
        selectedCard = MSSBCardDatabase.consumables_dict[1]
        selectedCardImage_4 = selectedCard.image
    elif itemCard >= 4601 and itemCard <= 4700:
        selectedCard = MSSBCardDatabase.consumables_dict[2]
        selectedCardImage_4 = selectedCard.image
    elif itemCard >= 4701 and itemCard <= 4800:
        selectedCard = MSSBCardDatabase.consumables_dict[3]
        selectedCardImage_4 = selectedCard.image
    elif itemCard >= 4801:
        selectedCard = MSSBCardDatabase.misc_dict[1]
        selectedCardImage_4 = selectedCard.image
    else:
        print("Error in code")
    cardImageList.append(selectedCardImage_4)
    
    cardTwo = _sysrand.randint(1,23)
    selectedCard = MSSBCardDatabase.common_dict[cardTwo]
    selectedCardImage_2 = selectedCard.image
    cardImageList.append(selectedCardImage_2)

    cardRarity = _sysrand.randint(1, 10000)
    if cardRarity <= 8500:
        cardFive = _sysrand.randint(1,10)
        selectedCard = MSSBCardDatabase.rare_dict[cardFive]
        selectedCardImage_5 = selectedCard.image
    elif cardRarity >= 8501 and cardRarity <= 9500:
        cardFiveWeight = _sysrand.randint(1,10000)
        if cardFiveWeight <= 1227:
            cardFive = 1
        elif cardFiveWeight >= 1228 and cardFiveWeight <= 2454:
            cardFive = 2
        elif cardFiveWeight >= 2455 and cardFiveWeight <= 3680:
            cardFive = 3
        elif cardFiveWeight >= 3681 and cardFiveWeight <= 4906:
            cardFive = 4
        elif cardFiveWeight >= 4907 and cardFiveWeight <= 5906:
            cardFive = 5
        elif cardFiveWeight >= 5907 and cardFiveWeight <= 6906:
            cardFive = 6
        elif cardFiveWeight >= 6907 and cardFiveWeight <= 7739:
            cardFive = 7
        elif cardFiveWeight >= 7740 and cardFiveWeight <= 8572:
            cardFive = 8
        elif cardFiveWeight >= 8573 and cardFiveWeight <= 9286:
            cardFive = 9
        elif cardFiveWeight >= 9287:
            cardFive = 10
        else:
            print("Error in code")
        selectedCard = MSSBCardDatabase.superrare_dict[cardFive]
        selectedCardImage_5 = selectedCard.image
    elif cardRarity >= 9501 and cardRarity <= 9900:
        cardFiveWeight = _sysrand.randint(1,10000)
        if cardFiveWeight <= 1666:
            cardFive = 1
        elif cardFiveWeight >= 1667 and cardFiveWeight <= 3333:
            cardFive = 2
        elif cardFiveWeight >= 3334 and cardFiveWeight <= 5000:
            cardFive = 3
        elif cardFiveWeight >= 5001 and cardFiveWeight <= 6667:
            cardFive = 4
        elif cardFiveWeight >= 6668 and cardFiveWeight <= 7222:
            cardFive = 5
        elif cardFiveWeight >= 7223 and cardFiveWeight <= 7777:
            cardFive = 6
        elif cardFiveWeight >= 7778 and cardFiveWeight <= 8332:
            cardFive = 7
        elif cardFiveWeight >= 8333 and cardFiveWeight <= 8749:
            cardFive = 8
        elif cardFiveWeight >= 8750 and cardFiveWeight <= 9166:
            cardFive = 9
        elif cardFiveWeight >= 9167 and cardFiveWeight <= 9583:
            cardFive = 10
        elif cardFiveWeight >= 9584:
            cardFive = 11
        else:
            print("Error in code")
        selectedCard = MSSBCardDatabase.ultrarare_dict[cardFive]
        selectedCardImage_5 = selectedCard.image
    elif cardRarity >=9901:
        cardFiveWeight = _sysrand.randint (1,30000)
        if cardFiveWeight <= 20000:
            cardFive = 1
        elif cardFiveWeight >= 20001:
            cardFive = 2
        else:
            print("Error in code")
        selectedCard = MSSBCardDatabase.secretrare_dict[cardFive]
        selectedCardImage_5 = selectedCard.image
    cardImageList.append(selectedCardImage_5)
    
    cardThree = _sysrand.randint(1,23)
    selectedCard = MSSBCardDatabase.common_dict[cardThree]
    selectedCardImage_3 = selectedCard.image
    cardImageList.append(selectedCardImage_3)

    #pass card image list into Image Helper
    pack_image = ImageBuilder.build_pack_image(cardImageList)
    #pass card image back to helper to convert to file
    pack_file = ImageBuilder.convert_image_to_file(pack_image)

    #construct the Discord embed
    title = "Pack Results"
    embed = discord.Embed(title=title, color=0xfefe55)
    file = pack_file
    imageLink = "attachment://image.png"
    embed.set_image(url=imageLink)
    
    #refresh card counts
    reload(MSSBCardDatabase)

    return embed, file

def openMultiplePacks(packCount):
    #initialize variable to count the number of packs opened
    packsOpened = 0
    
    #initialize variable to determine if Reroll was opened in this opening
    rerollOpened = False
    #initialize variable to determine if Trade was opened in this opening
    tradeOpened = False

    #initialize card image variables
    selectedCardImage_1 = ''
    selectedCardImage_2 = ''  
    selectedCardImage_3 = ''
    selectedCardImage_4 = ''
    selectedCardImage_5 = ''
    #initialize list to store each pack image that is created
    pack_images = []

    #create while loop to run the function as long as the number of packs opened is less than the number of packs requested
    while packsOpened < packCount:
       #create the card image list for this set of opennings
        cardImageList = []
        
        #set up the first 3 card pulls, which will always be common cards
        cardOne = _sysrand.randint(1,23)
        selectedCard = MSSBCardDatabase.common_dict[cardOne]
        selectedCardImage_1 = selectedCard.image
        cardImageList.append(selectedCardImage_1)
        
        itemCard = _sysrand.randint (1, 10000)
        if itemCard <= 4000:
            stadiumCardWeight = _sysrand.randint (1, 10000)
            if stadiumCardWeight <= 2500:
                cardFour = 1
            elif stadiumCardWeight >= 2501 and stadiumCardWeight <= 5000:
                cardFour = 2
            elif stadiumCardWeight >= 5001 and stadiumCardWeight <= 7500:
                cardFour = 3
            elif stadiumCardWeight >= 7501 and stadiumCardWeight <= 8550:
                cardFour = 4
            elif stadiumCardWeight >= 8551 and stadiumCardWeight <= 9400:
                cardFour = 5
            elif stadiumCardWeight >= 9401 and stadiumCardWeight <= 9900:
                cardFour = 6
            elif stadiumCardWeight >= 9901:
                cardFour = 7
            else:
                print("Error in code")
            selectedCard = MSSBCardDatabase.stadium_dict[cardFour]
            selectedCardImage_4 = selectedCard.image
        elif itemCard >= 4001 and itemCard <= 4500:
            starCardWeight = _sysrand.randint (1, 10000)
            if starCardWeight <= 4000:
                cardFour = 1
            elif starCardWeight >= 4001 and starCardWeight <= 7000:
                cardFour = 2
            elif starCardWeight >= 7001 and starCardWeight <= 8500:
                cardFour = 3
            elif starCardWeight >= 8501 and starCardWeight <= 9500:
                cardFour = 4
            elif starCardWeight >= 9501:
                cardFour = 5
            else:
                print("Error in code")
            selectedCard = MSSBCardDatabase.starchance_dict[cardFour]
            selectedCardImage_4 = selectedCard.image
        elif itemCard >= 4501 and itemCard <= 4600:
            selectedCard = MSSBCardDatabase.consumables_dict[1]
            packCount += 1
            selectedCardImage_4 = selectedCard.image
        elif itemCard >= 4601 and itemCard <= 4700:
            selectedCard = MSSBCardDatabase.consumables_dict[2]
            rerollOpened = True
            selectedCardImage_4 = selectedCard.image
        elif itemCard >= 4701 and itemCard <= 4800:
            selectedCard = MSSBCardDatabase.consumables_dict[3]
            tradeOpened = True
            selectedCardImage_4 = selectedCard.image
        elif itemCard >= 4801:
            selectedCard = MSSBCardDatabase.misc_dict[1]
            selectedCardImage_4 = selectedCard.image
        else:
            print("Error in code")
        cardImageList.append(selectedCardImage_4)
        
        cardTwo = _sysrand.randint(1,23)
        selectedCard = MSSBCardDatabase.common_dict[cardTwo]
        selectedCardImage_2 = selectedCard.image
        cardImageList.append(selectedCardImage_2)

        cardRarity = _sysrand.randint(1, 10000)
        if cardRarity <= 8500:
            cardFive = _sysrand.randint(1,10)
            selectedCard = MSSBCardDatabase.rare_dict[cardFive]
            selectedCardImage_5 = selectedCard.image
        elif cardRarity >= 8501 and cardRarity <= 9500:
            cardFiveWeight = _sysrand.randint(1,10000)
            if cardFiveWeight <= 1227:
                cardFive = 1
            elif cardFiveWeight >= 1228 and cardFiveWeight <= 2454:
                cardFive = 2
            elif cardFiveWeight >= 2455 and cardFiveWeight <= 3680:
                cardFive = 3
            elif cardFiveWeight >= 3681 and cardFiveWeight <= 4906:
                cardFive = 4
            elif cardFiveWeight >= 4907 and cardFiveWeight <= 5906:
                cardFive = 5
            elif cardFiveWeight >= 5907 and cardFiveWeight <= 6906:
                cardFive = 6
            elif cardFiveWeight >= 6907 and cardFiveWeight <= 7739:
                cardFive = 7
            elif cardFiveWeight >= 7740 and cardFiveWeight <= 8572:
                cardFive = 8
            elif cardFiveWeight >= 8573 and cardFiveWeight <= 9286:
                cardFive = 9
            elif cardFiveWeight >= 9287:
                cardFive = 10
            else:
                print("Error in code")
            selectedCard = MSSBCardDatabase.superrare_dict[cardFive]
            selectedCardImage_5 = selectedCard.image
        elif cardRarity >= 9501 and cardRarity <= 9900:
            cardFiveWeight = _sysrand.randint(1,10000)
            if cardFiveWeight <= 1666:
                cardFive = 1
            elif cardFiveWeight >= 1667 and cardFiveWeight <= 3333:
                cardFive = 2
            elif cardFiveWeight >= 3334 and cardFiveWeight <= 5000:
                cardFive = 3
            elif cardFiveWeight >= 5001 and cardFiveWeight <= 6667:
                cardFive = 4
            elif cardFiveWeight >= 6668 and cardFiveWeight <= 7222:
                cardFive = 5
            elif cardFiveWeight >= 7223 and cardFiveWeight <= 7777:
                cardFive = 6
            elif cardFiveWeight >= 7778 and cardFiveWeight <= 8332:
                cardFive = 7
            elif cardFiveWeight >= 8333 and cardFiveWeight <= 8749:
                cardFive = 8
            elif cardFiveWeight >= 8750 and cardFiveWeight <= 9166:
                cardFive = 9
            elif cardFiveWeight >= 9167 and cardFiveWeight <= 9583:
                cardFive = 10
            elif cardFiveWeight >= 9584:
                cardFive = 11
            else:
                print("Error in code")
            selectedCard = MSSBCardDatabase.ultrarare_dict[cardFive]
            selectedCardImage_5 = selectedCard.image
        elif cardRarity >=9901:
            cardFiveWeight = _sysrand.randint (1,30000)
            if cardFiveWeight <= 20000:
                cardFive = 1
            elif cardFiveWeight >= 20001:
                cardFive = 2
            else:
                print("Error in code")
            selectedCard = MSSBCardDatabase.secretrare_dict[cardFive]
            selectedCardImage_5 = selectedCard.image
        cardImageList.append(selectedCardImage_5)
        
        cardThree = _sysrand.randint(1,23)
        selectedCard = MSSBCardDatabase.common_dict[cardThree]
        selectedCardImage_3 = selectedCard.image
        cardImageList.append(selectedCardImage_3)

        #pass card image list into Image Helper
        pack_image = ImageBuilder.build_pack_image(cardImageList)
        #convert the pack image to a file
        #pack_file = ImageBuilder.convert_image_to_tempfile(pack_image)
        #append the pack image into the list of images
        pack_images.append(pack_image)

        #increment packs opened by 1
        packsOpened += 1

    #pass pack_images list to helper to combine them into one image
    opening_image = ImageBuilder.build_opening_image(pack_images)

    #pass pack opening image back to helper to convert to file
    opening_file = ImageBuilder.convert_image_to_file(opening_image)
    
    #construct the Discord embed
    title = "Opening Results"
    embed = discord.Embed(title=title, color=0xfefe55)
    file = opening_file
    imageLink = "attachment://image.png"
    embed.set_image(url=imageLink)

    #refresh card counts
    reload(MSSBCardDatabase)

    return embed, file, rerollOpened, tradeOpened
