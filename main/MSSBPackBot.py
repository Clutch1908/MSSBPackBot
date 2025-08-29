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
from services import MSSBPackBattle

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
intents.members = True
client = Client(command_prefix="!", intents=intents)     
    
#command to return card information
@client.tree.command(name="cardinfo", description="Return information for a specific card", guild=GUILD_ID)
async def cardInfo(interaction: discord.Interaction, card:str):
    embed, file = MSSBCardInfo.construct_discord_embed(card)
    if embed == "notfound":
        await interaction.response.send_message(f'Sorry, but I couldn\'t find that Card. Could you please verify your spelling and ensure there are no spaces in your input? I can take a look again once you do!', ephemeral=True)
    else:
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
        #send Discord embed
        await interaction.response.send_message(file=file,embed=embed) 

#command to open a single pack
@client.tree.command(name="openpack", description="Opens a single pack", guild=GUILD_ID)
async def openPack(interaction: discord.Interaction):
    embed, file = MSSBCardGenerator.openPack()
    embed.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(file=file, embed=embed)

#command to return the odds of each individual card
@client.tree.command(name="oddsinfo", description="See list of current cards with pull odds", guild=GUILD_ID)
async def buildOdds(interaction: discord.Interaction):
    #build message that will iterate through each MSSBCardDatabase dictionary to show the odds of drawing cards
    oddsMessage, oddsMessage_2, oddsMessage_3 = MSSBOddsInfo.construct_discord_message()
    await interaction.response.send_message(oddsMessage, ephemeral=True)
    await interaction.followup.send(oddsMessage_2, ephemeral=True)
    await interaction.followup.send(oddsMessage_3, ephemeral=True)

#class to set the buttons to be utilized in the follow up to Pack Battle outputs (for the recepient of the challenge)
class ViewRerollR(discord.ui.View):
    #set __init__ to store interaction IDs
    def __init__(self, challengerID, challengerName, recipientID, recipientName, timeout=300):
        super().__init__(timeout=timeout)
        self.challengerID = challengerID
        self.challengerName = challengerName
        self.recipientID = recipientID
        self.recipientName = recipientName

    @discord.ui.button(label="Yes", style = discord.ButtonStyle.success, emoji="✅")
    async def yes_button_callback_Reroll(self, interaction: discord.Interaction, button:discord.ui.button):
        if interaction.user.id != self.recipientID:
            await interaction.response.send_message("Hey get your own Reroll card grubby!", ephemeral=True)
        else:
            await interaction.response.edit_message(content="Great! Let me get you your new set of packs now...", view=None)
            embed_rr, file_rr, rerollOpened_rr, tradeOpened_rr = MSSBCardGenerator.openMultiplePacks(5)
            embed_rr.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
            if rerollOpened_rr and not tradeOpened_rr:
                await interaction.followup.send(file=file_rr, embed=embed_rr)
                view = ViewRerollR(challengerID=self.challengerID, challengerName = self.challengerName, recipientID = self.recipientID, recipientName = self.recipientName)
                await interaction.followup.send("Hey I see you ended up with a Reroll card there. Would you like to give me all your cards back for 5 new packs?", view=view)
            elif (not rerollOpened_rr) and tradeOpened_rr:
                await interaction.followup.send(file=file_rr, embed=embed_rr)
            elif rerollOpened_rr and tradeOpened_rr:
                await interaction.followup.send(file=file_rr, embed=embed_rr)
            else:
                await interaction.followup.send(file=file_rr, embed=embed_rr)

    @discord.ui.button(label="No", style = discord.ButtonStyle.danger, emoji="❌")
    async def no_button_callback_Reroll(self, interaction: discord.Interaction, button:discord.ui.button):
        if interaction.user.id != self.recipientID:
            await interaction.response.send_message("Hey get your own Reroll card grubby!", ephemeral=True)
        else:
            await interaction.response.edit_message(content="Glad you like what you have!", view=None)

#class to set the buttons to be utilized in the follow up to Pack Battle outputs (for the challenger of the challenge)
class ViewRerollC(discord.ui.View):
    #set __init__ to store interaction IDs
    def __init__(self, challengerID, challengerName, recipientID, recipientName, timeout=300):
        super().__init__(timeout=timeout)
        self.challengerID = challengerID
        self.challengerName = challengerName
        self.recipientID = recipientID
        self.recipientName = recipientName

    @discord.ui.button(label="Yes", style = discord.ButtonStyle.success, emoji="✅")
    async def yes_button_callback_Reroll(self, interaction: discord.Interaction, button:discord.ui.button):
        if interaction.user.id != self.challengerID:
            await interaction.response.send_message("Hey get your own Reroll card grubby!", ephemeral=True)
        else:
            await interaction.response.edit_message(content="Great! Let me get you your new set of packs now...", view=None)
            embed_cr, file_cr, rerollOpened_cr, tradeOpened_cr = MSSBCardGenerator.openMultiplePacks(5)
            embed_cr.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
            if rerollOpened_cr and not tradeOpened_cr:
                await interaction.followup.send(file=file_cr, embed=embed_cr)
                view = ViewRerollC(challengerID=self.challengerID, challengerName = self.challengerName, recipientID = self.recipientID, recipientName = self.recipientName)
                await interaction.followup.send("Hey I see you ended up with a Reroll card there. Would you like to give me all your cards back for 5 new packs?", view=view)
            elif (not rerollOpened_cr) and tradeOpened_cr:
                await interaction.followup.send(file=file_cr, embed=embed_cr)
            elif rerollOpened_cr and tradeOpened_cr:
                await interaction.followup.send(file=file_cr, embed=embed_cr)
            else:
                await interaction.followup.send(file=file_cr, embed=embed_cr)

    @discord.ui.button(label="No", style = discord.ButtonStyle.danger, emoji="❌")
    async def no_button_callback_Reroll(self, interaction: discord.Interaction, button:discord.ui.button):
        if interaction.user.id != self.challengerID:
            await interaction.response.send_message("Hey get your own Reroll card grubby!", ephemeral=True)
        else:
            await interaction.response.edit_message(content="Glad you like what you have!", view=None)

#class to set the buttons to be utilized by the Pack Battle command
class View(discord.ui.View):
    #set __init__ to store interaction IDs
    def __init__(self, challengerID, challengerName, recipientID, recipientName, timeout=300):
        super().__init__(timeout=timeout)
        self.challengerID = challengerID
        self.challengerName = challengerName
        self.recipientID = recipientID
        self.recipientName = recipientName
        
    @discord.ui.button(label="Yes", style = discord.ButtonStyle.success, emoji="✅")
    async def yes_button_callback(self, interaction: discord.Interaction, button:discord.ui.button):
        #check if user has the id of the recipient of the challenge
        if interaction.user.id != self.recipientID:
            await interaction.response.send_message("Hey you can't speak for them! Only the user being challenged can accept or decline the Pack Battle challenge.", ephemeral=True)
        else:
            await interaction.response.edit_message(content="Pack Battle Accepted!",view=None)
            await interaction.followup.send("Pack Battle Initiated! Ooo I'm excited let me get you your packs...")
            #open packs for the user challenged
            embed_r, file_r, rerollOpened_r, tradeOpened_r = MSSBCardGenerator.openMultiplePacks(5)
            embed_r.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
            if rerollOpened_r  and not tradeOpened_r:
                await interaction.followup.send(file=file_r, embed=embed_r)
                view = ViewRerollR(challengerID=self.challengerID, challengerName = self.challengerName, recipientID = self.recipientID, recipientName = self.recipientName)
                await interaction.followup.send("Hey I see you ended up with a Reroll card there. Would you like to give me all your cards back for 5 new packs?", view=view)
            elif (not rerollOpened_r) and tradeOpened_r:
                await interaction.followup.send(file=file_r, embed=embed_r)
            elif rerollOpened_r and tradeOpened_r:
                await interaction.followup.send(file=file_r, embed=embed_r)
                view = ViewRerollR(challengerID=self.challengerID, challengerName = self.challengerName, recipientID = self.recipientID, recipientName = self.recipientName)
                await interaction.followup.send("Hey I see you ended up with a Reroll card there. Would you like to give me all your cards back for 5 new packs?", view=view)
            else:
                await interaction.followup.send(file=file_r, embed=embed_r)
            #open packs for the user who sent the challenge
            embed_c, file_c, rerollOpened_c, tradeOpened_c = MSSBCardGenerator.openMultiplePacks(5)
            challenger_user = client.get_user(self.challengerID)
            embed_c.set_author(name=challenger_user.name, icon_url=challenger_user.display_avatar.url)
            if rerollOpened_c and not tradeOpened_c:
                await interaction.followup.send(file=file_c, embed=embed_c)
                view = ViewRerollC(challengerID=self.challengerID, challengerName = self.challengerName, recipientID = self.recipientID, recipientName = self.recipientName)
                await interaction.followup.send("Hey I see you ended up with a Reroll card there. Would you like to give me all your cards back for 5 new packs?", view=view)
            elif (not rerollOpened_c) and tradeOpened_c:
                await interaction.followup.send(file=file_c, embed=embed_c)
            elif rerollOpened_c and tradeOpened_c:
                await interaction.followup.send(file=file_c, embed=embed_c)
                view = ViewRerollC(challengerID=self.challengerID, challengerName = self.challengerName, recipientID = self.recipientID, recipientName = self.recipientName)
                await interaction.followup.send("Hey I see you ended up with a Reroll card there. Would you like to give me all your cards back for 5 new packs?", view=view)
            else:
                await interaction.followup.send(file=file_c, embed=embed_c)

    @discord.ui.button(label="No", style=discord.ButtonStyle.danger, emoji="❌")
    async def no_button_callback(self, interaction: discord.Interaction, button:discord.ui.button):
        if interaction.user.id != self.recipientID:
            await interaction.response.send_message("Hey you can't speak for them! Only the user being challenged can accept or decline the Pack Battle challenge.", ephemeral=True)
        else:
            await interaction.response.edit_message(content="Pack Battle Declined",view=None)
            await interaction.followup.send("Calm down now, no Pack Battle to be had here. Maybe another time?")

#command to trigger a pack battle
@client.tree.command(name='packbattle', description='Challenege a friend to rip packs and play a baseball game!', guild=GUILD_ID)
async def confirmParticipant(interaction: discord.Interaction, user: discord.Member):
    #set the id's of the parties involved
    challengerID = interaction.user.id
    challengerName = interaction.user.name
    recipientID = user._user.id
    recipientName = user._user.name
    #convert to id string's
    challengerIDStr = str(challengerID)
    recipientIDStr = str(recipientID)
    recipientNameStr = str(recipientName)
    challengeMessage, challengeConfirm = MSSBPackBattle.construct_challenge_message(challengerIDStr, recipientIDStr, recipientNameStr)
    view = View(challengerID=challengerID, challengerName=challengerName, recipientID=recipientID, recipientName=recipientName)
    await interaction.response.send_message(challengeMessage)
    await interaction.followup.send(challengeConfirm, view=view)
client.run(TOKEN)
