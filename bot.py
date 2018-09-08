#Unknow Bot by Unknow19

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import youtube_dl
from datetime import datetime
import os

#bot
bot = commands.Bot(command_prefix="s-")

#snipes
snipe_status = False

#ids
text_id = "476982525412245505"
command_id = "476982466461302794"

players = {}

#sound links
#thirty_minutes = "https://youtu.be/QRu1BEbOOZs"
#ten_minutes = "https://youtu.be/l_sSzwRkkGY"
#five_minutes = "https://youtu.be/xVpeHFZs16Q"
#three_minutes = "https://youtu.be/D5pkVfvuXE8"
#one_minute = "https://youtu.be/IhiTD-09bP4"
#thirty_seconds = "https://youtu.be/WcHv01Ubtvs"
#ten_seconds = "https://youtu.be/P8IbKVPIAeo"
#countdown = "https://youtu.be/3FJWOTHQMlo"


@bot.event
async def on_ready():
    print("Seems like i just started")
    print("I am running on " + bot.user.name)
    print("with the ID: " + bot.user.id)

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def playmymusic(ctx, url):
    server = ctx.message.server
    channel = ctx.message.author.voice.voice_channel
    voice_client = bot.voice_client_in(server)
    if voice_client != None:
        if voice_client.channel != channel:
            await bot.join_voice_channel(channel)
    else:
        await bot.join_voice_channel(channel)
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    player.start()

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def set_id(ctx):
    msg = ctx.message.content.split()
    array = []
    for word in msg[1:]:
        array.append(word)
    if len(array) == 2:
        if array[1] == "text" or array[1] == "Text":
            global text_id
            text_id = array[0]
            print("New text_id set! New id is " + array[0])
            await bot.say("New __***text_id***__ set!")
        elif array[1] == "command" or array[1] == "Command":
            global command_id
            command_id = array[0]
            print("New command_id set! New id is " + array[0])
            await bot.say("New __***command_id***__ set!")
        else:
            await bot.say("Command not correctly used! 'Set for' not correctly set!")
    else:
        await bot.say("Command not correctly used!")

@bot.command()
@commands.has_role("Admin")
async def ids():
    if text_id != "" and command_id != "":
        await bot.say("The current text id is __***" + text_id + "***__ and the current command id is __***" + command_id + "***__")
    elif text_id != "":
        await bot.say("The current text id is __***" + text_id + "***__. No command id set yet!")
    elif command_id != "":
        await bot.say("The current command id is __***" + command_id + "***__. No text id set yet!")
    else:
        await bot.say("There is no id set yet!")

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount+1)):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say("**I deleted the messages for you! :slight_smile:**", delete_after = 4.0)

@bot.command(pass_context=True)
@commands.has_role("Snipe Host")
async def activatesnipes(ctx):
    if text_id != "" and command_id != "":
        global snipe_status
        if snipe_status != True:
            snipe_status = True
            server = ctx.message.server
            channel = ctx.message.author.voice.voice_channel
            print("Snipes are now 24/7 in the voice channel " + channel.name + " on " + ctx.message.server.name)
            voice_client = bot.voice_client_in(server)
            if voice_client != None:
                if voice_client.channel != channel:
                    await bot.join_voice_channel(channel)
            else:
                await bot.join_voice_channel(channel)
            voice_client = bot.voice_client_in(server)

            while snipe_status:
                player = voice_client.create_ffmpeg_player('30minutes.mp3')
                print(ctx.message.timestamp)
                embed = discord.Embed(
                    title = "[Snipe Announcement]",
                    color = 0xffff00
                )
                embed.add_field(name="The next game will start in __27 minutes__", value="Please wait in the snipes voice channel and be patient.")
                embed.set_footer(text="Next game will start at " + str(ctx.message.timestamp))
                await bot.send_message(ctx.message.server.get_channel(text_id) ,embed=embed)
                players[server.id] = player
                player.start()
                await asyncio.sleep(1020)

                player = voice_client.create_ffmpeg_player('10minutes.mp3')
                embed = discord.Embed(
                    title = "[Snipe Announcement]",
                    color = 0xe6e600
                )
                embed.add_field(name="The next game will start in __10 minutes__", value="Please wait in the snipes voice channel and be patient.")
                embed.set_footer(text="Next game will start at ")
                await bot.send_message(ctx.message.server.get_channel(text_id) ,embed=embed)
                players[server.id] = player
                player.start()
                dt = datetime.now()
                strg = dt.strftime('%H:%M:%S:%f')
                print(strg)
                await asyncio.sleep(300)

                player = voice_client.create_ffmpeg_player('5minutes.mp3')
                embed = discord.Embed(
                    title = "[Snipe Announcement]",
                    color = 0xff8000
                )
                embed.add_field(name="The next game will start in __5 minutes__", value="Please wait in the snipes voice channel and be patient.")
                embed.set_footer(text="Next game will start at ")
                await bot.send_message(ctx.message.server.get_channel(text_id) ,embed=embed)
                players[server.id] = player
                player.start()
                dt = datetime.now()
                strg = dt.strftime('%H:%M:%S:%f')
                print(strg)
                await asyncio.sleep(120)

                player = voice_client.create_ffmpeg_player('3minutes.mp3')
                embed = discord.Embed(
                    title = "[Snipe Announcement]",
                    color = 0xe67300
                )
                embed.add_field(name="The next game will start in __3 minutes__", value="Please wait in the snipes voice channel and be patient.", inline=True)
                embed.add_field(name="Notice (only at first game after starting the game!) :", value="Make sure to preload your content by pressing 'Play' in-game and cancelling it when it reaches 100%")
                embed.set_footer(text="Next game will start at ")
                await bot.send_message(ctx.message.server.get_channel(text_id) ,embed=embed)
                players[server.id] = player
                player.start()
                dt = datetime.now()
                strg = dt.strftime('%H:%M:%S:%f')
                print(strg)
                await asyncio.sleep(120)

                player = voice_client.create_ffmpeg_player('1minute.mp3')
                await bot.send_message(ctx.message.server.get_channel(command_id), "+s solo")
                players[server.id] = player
                player.start()
                dt = datetime.now()
                strg = dt.strftime('%H:%M:%S:%f')
                print(strg)
                await asyncio.sleep(30)

                player = voice_client.create_ffmpeg_player('30seconds.mp3')
                dt = datetime.now()
                strg = dt.strftime('%H:%M:%S:%f')
                print(strg)
                embed = discord.Embed(
                    title = "[Snipe Announcement]",
                    color = 0xcc0000
                )
                embed.add_field(name="The next game will start in __***30 seconds***__", value="Please wait in the snipes voice channel! Countdown will soon start!")
                embed.set_footer(text="Next game will start at "+ strg)
                await bot.send_message(ctx.message.server.get_channel(text_id) ,embed=embed)
                players[server.id] = player
                player.start()
                await asyncio.sleep(20)

                player = voice_client.create_ffmpeg_player('10seconds.mp3')
                players[server.id] = player
                player.start()
                dt = datetime.now()
                strg = dt.strftime('%H:%M:%S:%f')
                print(strg)
                await asyncio.sleep(10)

                player = voice_client.create_ffmpeg_player('countdown.mp3')
                players[server.id] = player
                player.start()
                dt = datetime.now()
                strg = dt.strftime('%H:%M:%S:%f')
                print(strg)
                await asyncio.sleep(179)
        else:
            await bot.say("24/7 snipes are already active!")
    else:
        await bot.say("No ids set yet! Can't start snipes!")

@bot.command(pass_context=True)
@commands.has_role("Snipe Host")
async def deactivatesnipes(ctx):
    global snipe_status
    snipe_status=False
    print("24/7 snipes on " + ctx.message.server + " are deactivated now!")
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()

bot.run(os.environ.get('token'))
