#call secrets for Bot Key
import os
TOKEN = os.getenv("token")
#import Discord libraries
import discord
from discord.ext import commands
#import Service scripts
from services import MSSBCardGenerator
from services import MSSBCardInfo
from services import MSSBOddsInfo

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
#@app_commands.checks.cooldown(1, 5, key=lambda i:(i.user.id))
async def cardInfo(interaction: discord.Interaction, card:str):
    embed, file = MSSBCardInfo.construct_discord_embed(card)
    if embed == "notfound":
        await interaction.response.send_message(f'Sorry, but I couldn\'t find that Card. Could you please verify your spelling and ensure there are no spaces in your input? I can take a look again once you do!')
    else:
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
        #send Discord embed
        await interaction.response.send_message(file=file,embed=embed) 

@client.tree.command(name="openpack", description="Opens a single pack", guild=GUILD_ID)
#@app_commands.checks.cooldown(1, 5, key=lambda i:(i.user.id))
async def openPack(interaction: discord.Interaction):
    embed, file = MSSBCardGenerator.openPack()
    embed.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(file=file, embed=embed)

@client.tree.command(name="oddsinfo", description="See list of current cards with pull odds", guild=GUILD_ID)
#@app_commands.checks.cooldown(1, 5, key=lambda i:(i.user.id))
async def buildOdds(interaction: discord.Interaction):
    #build message that will iterate through each MSSBCardDatabase dictionary to show the odds of drawing cards
    oddsMessage, oddsMessage_2, oddsMessage_3 = MSSBOddsInfo.construct_discord_message()
    print(oddsMessage)
    print(oddsMessage_2)
    print(oddsMessage_3)
    await interaction.response.send_message(oddsMessage)
    await interaction.followup.send(oddsMessage_2)
    await interaction.followup.send(oddsMessage_3)

#@client.tree.error
#async def on_app_command_error(error: app_commands.AppCommandError, interaction: discord.Interaction):
    #if isinstance(error, app_commands.CommandOnCooldown):
        #await interaction.response.send_message(f"Wait for {error.retry_after} seconds, I'm only a one Toad shop!!!, ephemeral = True")

client.run(TOKEN)