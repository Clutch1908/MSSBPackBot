import discord
from resources import MSSBCardDatabase
from resources import MSSBCharacters

def construct_discord_embed(card):
    #make user input case insensitive
    card = card.lower()
    cardID = MSSBCharacters.get_card_id(card)
    if cardID is not None:
        #determine which card information to return based on user input
        selectedCard = MSSBCardDatabase.card_dict[cardID]
        #set info to be built into Discord embed
        title = selectedCard.name
        embed = discord.Embed(title=title, color=0xfefe55)
        rarity = selectedCard.rarity
        kind = selectedCard.kind
        odds = selectedCard.odds
        description = selectedCard.description
        imageFile = selectedCard.image
        #upload file to Discord to be accessed by embed
        file = discord.File(imageFile, filename="image.png")
        imageLink = "attachment://image.png"
        #build Discord embed
        embed.set_image(url=imageLink)
        embed.add_field(name="Rarity", value=rarity, inline=True)
        embed.add_field(name="Type", value=kind, inline=True)
        embed.add_field(name="Odds", value=odds, inline=True)
        embed.add_field(name="", value=description, inline=False)
        embed.set_footer(text="In-Game Renders courtsey of Super63. Card Art created by Clutch1908")
        return embed, file   
    else:
        embed = "notfound"
        file = "notfound"
        return embed, file