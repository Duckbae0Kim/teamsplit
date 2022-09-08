from discord.ext import commands
import discord
import random
import asyncio
from discord.voice_client import VoiceClient
 
token = 'Your Token'

bot = commands.Bot(intents=discord.Intents.all() , command_prefix= "!" , description='The Best Bot For the Best User!')
 
@bot.event
async def on_ready():
    print('logged in as \nname: {}\n  id: {}'.format(bot.user.name, bot.user.id))
    print('='*80)
    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))
 
@bot.command(pass_context=True)
async def 팀짜기(ctx, count):
    voice_channel = ctx.message.author.voice.channel

    members = voice_channel.members
    member_names = []
    for member in members:
        member_names.append(member.mention)
    random.shuffle(member_names)
    
    team = []

    for i in range(0, int(len(member_names)/int(count))):
        temp = []
        for c in range(0, int(count)):
            temp.append(member_names.pop())
        team.append(temp)

    if member_names:
        team.append(member_names)

    for index in range(0, len(team)):
        await ctx.send('{} team : {}'.format(index+1, team[index]))

@bot.command(pass_context=True)
async def team_except(ctx, count, *args):
    voice_channel = ctx.message.author.voice.channel

    members = voice_channel.members
    member_names = []

    __MEMBER__ = {}
    
    for member in members:
        __MEMBER__[member.nick] = True

    for except_member in args:
        __MEMBER__[except_member] = False

    for member in members:
        if __MEMBER__[member.nick] != False:
            member_names.append(member.mention)
    random.shuffle(member_names)
    
    team = []

    for i in range(0, int(len(member_names)/int(count))):
        temp = []
        for c in range(0, int(count)):
            temp.append(member_names.pop())
        team.append(temp)

    if member_names:
        team.append(member_names)

    for index in range(0, len(team)):
        await ctx.send('{} team : {}'.format(index+1, team[index]))

@bot.command(pass_context=True)
async def choice(ctx, *args):
    voice_channel = ctx.message.author.voice.channel

    members = voice_channel.members

    member_names = []

    for member in members:
        member_names.append(member.mention)

    random.shuffle(member_names)

    await ctx.send('Hey! {}'.format(member_names[0]))


bot.run("")