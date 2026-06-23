import discord
from discord.ext import commands
from aiohttp import web
import asyncio
import os

intents = discord.Intents.default()
intents.members = True  

bot = commands.Bot(command_prefix="!", intents=intents)

LOG_CHANNEL_ID = 1518922160356327467  

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online and tracking joins!")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(LOG_CHANNEL_ID)
    if channel:
        log_message = f"`{member.name}` ← joined: {member.guild.name}!"
        await channel.send(log_message)

async def handle(request):
    return web.Response(text="Bot is running!")

async def start_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()

async def main():
    asyncio.create_task(start_server())
    # This reads the secret token from Render securely:
    token = os.environ.get('DISCORD_TOKEN')
    await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
