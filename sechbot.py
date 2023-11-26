#Sếch bot bằng python còn api bên nekobot.xyz
import discord
import requests
from discord.ext import commands

client = commands.Bot(command_prefix=".")

token = "tự nhập token"

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Sếch bot made by Bungee0001'))
    
#@commands.is_nsfw() chỉ vào kênh chỉ được set nsfw
@client.command()
@commands.is_nsfw()
async def hentai(ctx):
    await ctx.reply('Đợi vài giây', mention_author=True)
    r = requests.get("https://nekobot.xyz/api/image?type=hentai")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['message'])
    
    await ctx.send(embed=em)

client.run(token)