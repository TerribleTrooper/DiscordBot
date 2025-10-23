import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
file = open("bad_words.txt").readlines()
bad_words_array = [x[:-1] for x in file]

token_const = os.getenv("BOT_TOKEN")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=">", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user.name} зашёл на сервер")

# TODO
@bot.event
async def on_member_join(member):
    print(f"Join {member}")
    await member.channel.send(f'{member} присоединился к серверу')


@bot.event  # swear word filter(text)
async def on_message(message):
    line_judge = "I knew you would say that! Guilty!"
    msg = message.content

    if message.author == bot.user:
        return

    if line_judge in msg:
        await message.delete()
        await message.channel.send("This is my phrase! You are not a Judge!")

    for i in bad_words_array:
        if i in msg:
            await message.delete()
            await message.channel.send(line_judge)
            break

bot.run(token_const)

