import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='HarryQnkov Streams', type = 3))
    print('Loading...') 


@client.event
async def on_message(message):
    if message.content == 'ping':
        await client.send_message(message.channel,'pong')
        await client.send_message(message.channel, embed=em)
    if message.content == 'prefix':
        await client.send_message(message.channel,'!') 
        await client.send_message(message.channel, embed=em)
    if message.content == '!test':
        em = discord.Embed(description='Try To Test me????')
        em.set_image(url='https://i.imgur.com/0ajAutb.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == '!twitchcommands':
        em = discord.Embed(description='**Stream Commands** | ***!accountage ; !dicksize ; !discord ; !donate ; !followage ; !hate @име ; !iq ; !loot ; !love @име ; !shans ; !steam ; !uptime ; !пуси***')
        em.set_image(url='https://i.imgur.com/0ajAutb.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == '!cmd':
        em = discord.Embed(description='***ping ; prefix ; !twitchcommands ; !test ; !creator ; !steam ; !стийм ; !twitch ; !туич ; !g2a ; !г2а ; !ютуб ; !youtube ; !fb ; !фб ;  !info ;*** *If you want to add something other type to Legilitlan*')
        em.set_image(url='https://i.imgur.com/0ajAutb.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == '!creator':
        await client.send_message(message.channel,'Discord Bot Creator - Legilitlan#9791 <3')
    if message.content == '!youtube':
        await client.send_message(message.channel,'If you like my content please SUBSCRIBE : https://www.youtube.com/channel/UC6G-PTL7KkgAUBdQebPKsWw?view_as=subscriber')
    if message.content == '!ютуб':
        await client.send_message(message.channel,'If you like my content please SUBSCRIBE : https://www.youtube.com/channel/UC6G-PTL7KkgAUBdQebPKsWw?view_as=subscriber')
    if message.content == '!steam':
        await client.send_message(message.channel,'If you want we to be friends : http://s.team/p/wdf-fkwf/MHQNTWTB')
    if message.content == '!стийм':
        await client.send_message(message.channel,'If you want we to be friends : http://s.team/p/wdf-fkwf/MHQNTWTB')
    if message.content == '!twitch':
        await client.send_message(message.channel,'If you want to watch me how i play ON LIVE : http://www.twitch.tv/harryqnkov')
    if message.content == '!туич':
        await client.send_message(message.channel,'If you want to watch me how i play ON LIVE : http://www.twitch.tv/harryqnkov')
    if message.content == '!g2a':
        await client.send_message(message.channel,'If you want to help for me and for the stream : https://www.g2a.com/en/best-offers?reflink=harryqnkov')
    if message.content == '!г2а':
        await client.send_message(message.channel,'If you want to help for me and for the stream : https://www.g2a.com/en/best-offers?reflink=harryqnkov')
    if message.content == '!fb':
        await client.send_message(message.channel,'If you want to follow my FB page : https://www.facebook.com/Harryqnkov-army-307502446552124')
    if message.content == '!фб':
        await client.send_message(message.channel,'If you want to follow my FB page : https://www.facebook.com/Harryqnkov-army-307502446552124')
    if message.content == '!info':
        await client.send_message(message.channel,'Здравейте приятели, добре дошли в моя канал. Името ми е Хараламби, но предпочитам да ми казвате Хари. Роден съм и живея в град Русе, вече 17 години :D Обичам да играя игри, откакто се помня и съм изключително щастлив, че мога да правя любимото си нещо с Вас! Нов стриймър съм и ще се радвам ако се забавляваме заедно и продължаваме да правим вечерите забавни. Може да ме подкрепите по всякакъв начин, ако харесвате това, което правя !')

client.run('NTY1NjAzNjU5Mjc1MTczOTE4.XK7sKA.nb-Ui0dTN71JwseR6k88v7_x47Q')
