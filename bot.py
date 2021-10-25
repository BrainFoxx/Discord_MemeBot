from bs4 import BeautifulSoup
import discord
from discord.ext import commands
import requests

bot = commands.Bot(".")
url = "https://dtf.ru/kek/entries/new"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36"
}
bot.remove_command("help")


@bot.event
async def on_ready():
    activity = discord.Game("GAME INFO")
    print(f"Bot connected {bot.user}")
    await bot.change_presence(status=discord.Status.dnd, activity=activity)


@bot.event
async def on_message(message):
    r = requests.get(url, headers=header).text
    soup = BeautifulSoup(r, 'html.parser')
    bs = soup.find('div', class_='content-image')
    bs2 = bs.find('div', class_='andropov_image')
    list = open("list.txt", "r")
    link = (bs2['data-image-src'])
    if link not in list:
        with open("list.txt", "w") as file:
            file.write(link)
        channel = bot.get_channel(123456) # ID чата куда нужно публиковать мемы
        await channel.send(bs2['data-image-src'])
    else:
        print('Ждём...')


bot.run("TOKEN")
