from resources import MSSBCardDatabase

def construct_discord_message():
    #initalize the message with the start of the code block
    oddsMessage = '```'
    #denote the maximum length of characters per line
    lineLength = 46
    #create odds header for entire message
    oddsHeader = "***DROP RATES***"
    centerBufferH = " " * int(((lineLength - len(str(oddsHeader)))/2))
    oddsMessage += centerBufferH + oddsHeader + centerBufferH + "\n"
    #add the header for the section of the odds
    oddsMessage += "\n" + "*COMMON CHARACTERS*"
    #interate through the dictionary related to the section
    for card in MSSBCardDatabase.common_dict.values():
        #add buffer between card name and card odds for right aligned card odds
        buffer = " " * (lineLength - len(str(card.name)) - len(str(card.odds)))
        #add on card name and card odds (with buffer) to exisitng message
        oddsMessage += "\n" + card.name + buffer + card.odds
    oddsMessage += "\n\n" + "*RARE CHARACTERS*"
    for card in MSSBCardDatabase.rare_dict.values():
        buffer = " " * (lineLength - len(str(card.name)) - len(str(card.odds)))
        oddsMessage += "\n" + card.name + buffer + card.odds
    #complete first message code block
    oddsMessage += "\n" + "```"
    
    #initialize second message to work around Discord character limits
    oddsMessage_2 = "\n" + "```"
    oddsMessage_2 += "\n\n" + "*SUPER RARE CHARACTERS*"
    for card in MSSBCardDatabase.superrare_dict.values():
        buffer = " " * (lineLength - len(str(card.name)) - len(str(card.odds)))
        oddsMessage_2 += "\n" + card.name + buffer + card.odds
    oddsMessage_2 += "\n\n" + "*ULTRA RARE CHARACTERS*"
    for card in MSSBCardDatabase.ultrarare_dict.values():
        buffer = " " * (lineLength - len(str(card.name)) - len(str(card.odds)))
        oddsMessage_2 += "\n" + card.name + buffer + card.odds
    oddsMessage_2 += "\n\n" + "*SECRET RARE CHARACTERS*"
    for card in MSSBCardDatabase.secretrare_dict.values():
        buffer = " " * (lineLength - len(str(card.name)) - len(str(card.odds)))
        oddsMessage_2 += "\n" + card.name + buffer + card.odds
    #complete second message code block
    oddsMessage_2 += "\n" + '```'

    #initialize third message to work around Discord character limits
    oddsMessage_3 = '```'
    oddsMessage_3 += "\n" + "*STADIUMS*"
    for card in MSSBCardDatabase.stadium_dict.values():
        buffer = " " * (lineLength - len(str(card.name)) - len(str(card.odds)))
        oddsMessage_3 += "\n" + card.name + buffer + card.odds
    oddsMessage_3 += "\n\n" + "*STAR TOKENS*"
    for card in MSSBCardDatabase.starchance_dict.values():
        buffer = " " * (lineLength - len(str(card.name)) - len(str(card.odds)))
        oddsMessage_3 += "\n" + card.name + buffer + card.odds
    oddsMessage_3 += "\n\n" + "*CONSUMABLES*"
    for card in MSSBCardDatabase.consumables_dict.values():
        buffer = " " * (lineLength - len(str(card.name)) - len(str(card.odds)))
        oddsMessage_3 += "\n" + card.name + buffer + card.odds
    oddsMessage_3 += "\n\n" + "*MISC*"
    for card in MSSBCardDatabase.misc_dict.values():
        buffer = " " * (lineLength - len(str(card.name)) - len(str(card.odds)))
        oddsMessage_3 += "\n" + card.name + buffer + card.odds
    oddsDisclaimer_1 = "All odds are approximate." 
    centerBufferD_1 = " " * int(((lineLength - len(str(oddsDisclaimer_1)))/2))
    oddsDisclaimer_2 = "Some card odds may vary with rounding."
    centerBufferD_2 = " " * int(((lineLength - len(str(oddsDisclaimer_2)))/2))
    oddsDisclaimer_3 = "All odds subject to change without notice."
    centerBufferD_3 = " " * int(((lineLength - len(str(oddsDisclaimer_3)))/2))
    oddsMessage_3 += "\n\n" + centerBufferD_1 + oddsDisclaimer_1 + centerBufferD_1 + "\n" + centerBufferD_2 + oddsDisclaimer_2 + centerBufferD_2 +  "\n" + centerBufferD_3 + oddsDisclaimer_3 + centerBufferD_3
    oddsMessage_3 += "\n" + '```'
    
    return oddsMessage, oddsMessage_2, oddsMessage_3