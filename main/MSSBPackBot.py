#call secrets for Bot Key
import os
TOKEN = os.getenv("token")

if TOKEN is None:
        print("Error: TOKEN environment variable is not set.")
else:
    # Proceed with using token
    pass

import discord
from discord.ext import commands
from discord import app_commands
from resources import MSSBCardDatabase

class Client(commands.Bot):
    async def on_ready(self):
        print(f'{client.user} is open!')

        try:
            guild = discord.Object(id=1408155647987548332)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print(f'Error syncing commands: {e}')
            
    async def on_message(self, message):
        if message.author == self.user:
            return

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)     
 
GUILD_ID = discord.Object(id=1408155647987548332)

@client.tree.command(name="cardinfo", description="Return information for a specific card", guild=GUILD_ID)
async def cardInfo(interaction: discord.Interaction, card:str):
    selectedCard = MSSBCardDatabase.BabyMario()
    title = selectedCard.name
    embed = discord.Embed(title=title, color=0xfefe55)
    rarity = selectedCard.rarity
    kind = selectedCard.kind
    odds = selectedCard.odds
    description = selectedCard.description
    imageFile = selectedCard.image
    file = discord.File(imageFile, filename="image.png")
    imageLink = "attachment://image.png"
    embed.set_image(url=imageLink)
    embed.add_field(name="Rarity", value=rarity, inline=True)
    embed.add_field(name="Type", value=kind, inline=True)
    embed.add_field(name="Odds", value=odds, inline=True)
    embed.add_field(name="", value=description, inline=False)
    embed.set_footer(text="In-Game Renders courtsey of Super63. Card Art created by Clutch1908")
    embed.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(file=file, embed=embed)

client.run(TOKEN)