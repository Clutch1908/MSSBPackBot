#call secrets for Bot Key
import os
TOKEN = os.getenv("token")
#import Discord libraries
import discord
from discord.ext import commands
from discord import app_commands
#import Resource scripts
from resources import MSSBCardDatabase, MSSBCharacters

#declare Server ID for where bot is running
GUILD_ID = discord.Object(id=1408155647987548332)

#initalize Bot
class Client(commands.Bot):
    async def on_ready(self):
        print(f'{client.user} is open!')

        #manually sync commands on boot
        try:
            guild = GUILD_ID
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print(f'Error syncing commands: {e}')

#initialize slash commands           
intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)     

#command to return card information
@client.tree.command(name="cardinfo", description="Return information for a specific card", guild=GUILD_ID)
async def cardInfo(interaction: discord.Interaction, card:str):
    #make user input case insensitive
    card = card.lower()
    #pass the user input into a function to 
    cardID = MSSBCharacters.get_character_id(card)
    if cardID == None
        await message.channel.send(f'Card not found. Verify your spelling and ensure there are no spaces in your input')
    else:
        #determine which card information to find based on user inupt
        selectedCard = MSSBCardDatabase.card_dict(cardID)
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
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
        #send Discord embed
        await interaction.response.send_message(file=file, embed=embed)

client.run(TOKEN)