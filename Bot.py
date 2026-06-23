import discord
from discord.ext import commands

# 1. Setup the bot with permissions to track members
intents = discord.Intents.default()
intents.members = True  # Tracks when people join

bot = commands.Bot(command_prefix="!", intents=intents)

# 2. Change this to your copied Channel ID number (remove the quotes, just keep the numbers)
LOG_CHANNEL_ID = 1518782566776442882  

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online and tracking joins!")

@bot.event
async def on_member_join(member):
    # This triggers the second someone joins your server
    channel = bot.get_channel(LOG_CHANNEL_ID)
    if channel:
        # Formats it exactly like your target image layout
        log_message = f"`{member.name}` ← (tap to copy) joined: {member.guild.name}!"
        await channel.send(log_message)

# 3. Paste your secret Bot Token inside the single quotes below
bot.run('MTUxODc1NTI4NTIxMTE1MjU3NA.G2S6wM.qEwUXshzZECiuoMDTStR7vDbZgr5N9IYB6nBnQ.GNjZ1f.2RCMeioaz_9oZ0KeEMUuR0ZofHSFlV8kdFXCPI')

