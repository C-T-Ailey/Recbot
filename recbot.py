# botbot.py
# version 0.32
import os
import random
from dotenv import load_dotenv
import discord
from discord.ext import commands

import datetime
import time
datetime.datetime.now().time()

tstart = 0
tstop = 0

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

guild = discord.Guild
client = discord.Client()
bot = commands.Bot(command_prefix = "&")

def is_in_guild(guild_id):
    async def predicate(ctx):
        return ctx.guild and ctx.guild.id == guild_id
    return commands.check(predicate)

"""@bot.event
async def on_command_error(ctx, error):
  embedVar = discord.Embed(color=0x4ae6b2, description='Command on cooldown, please wait %.2fs before retrying.' % error.retry_after)
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.channel.send(embed=embedVar)
  raise error"""

@bot.event
async def on_ready():
  print(f"{bot.user.name} has connected to Discord at ",(datetime.datetime.now().time()))
  await bot.change_presence(activity=discord.Game(name='&help for commands'))
  
@bot.event #callbacks
async def on_message(message):
  channel = message.channel
  if message.author.id == 465908845093453837:
    if str("say hi, recbot") in str(message.content).lower():
      await channel.send(str("hi, recbot"))
    elif str("hi recbot") in str(message.content).lower():
      await channel.send(str("hi"))
    elif str("play us out, recbot") in str(message.content).lower():
      await channel.send(str("https://www.youtube.com/watch?v=J---aiyznGQ"))
  await bot.process_commands(message)

#@bot.event
#async def on_reaction_add(reaction)

"""@bot.event
async def on_message(message):
  global tstart
  global tstop
  channel = message.channel
  role = discord.utils.get(message.guild.roles, id=)
  if role.mention in message.content: 
    if role.mentionable == True:
      tstart = time.time()
      tstop = (tstart + 60)
      await role.edit(mentionable=False)
      print("Role set to unmentionable.")
    
  elif ("@"+role.name) in message.content: 
    if role.mentionable == False:    
      if time.time() < (tstop):
        await channel.send("This role mention is on cooldown. Please wait another %ds before retrying." % (int(tstop - time.time())))
        print("Mention on cooldown.")
          
        
  elif message.content == "turn on rolemutetest":
    await role.edit(mentionable=True)
    await message.add_reaction("🤠")
    tstart = 0
    tstop = 0

  else:
    if time.time() >= tstop:
      await role.edit(mentionable=True)
      tstart = 0
      tstop = 0

  await bot.process_commands(message)"""
    
@bot.command(name='weird', help="Warning: May be distressing, 5sec cooldown between recs")
@commands.cooldown(1, 5, commands.BucketType.user)
async def weird_recs(ctx):
  weird_links = [
    'https://youtu.be/vKAzoXUC-vM', #fukuro
    'https://youtu.be/2BD-ba-aXQo', #58skywatching
    'https://youtu.be/NZ-vBhGk9F4', #58realsleep
    'https://youtu.be/jh09uIN6tl0', #58fastestroute
    'https://youtu.be/3c66w6fVqOI', #58contingency
    'https://youtu.be/2gMjJNGg9Z8', #uneditedfootageofabear
    'https://youtu.be/KH4NrUxcsYs', #alandrpepper
    'https://youtu.be/fQkJGdaZ5_U', #creepyeggs1
    'https://youtu.be/UYbh5AMDd_Q', #creepyeggs2
    'https://youtu.be/TzDS3w7uhDw', #creepyeggs3
    'https://youtu.be/BA8ct6MthaA', #creepyeggs4
    'https://youtu.be/kwgn5xvTnco', #creepyeggs5
    'https://youtu.be/rznECmgJj4A', #creepyeggs6
    'https://youtu.be/qNDnYLYXprA', #spongebobback
    'https://youtu.be/w_MSFkZHNi4', #doubleking
    'https://youtu.be/GxKPBLjHAEA', #rabbits
    'https://youtu.be/ZBvbNs7WSII', #pranktime
    'https://youtu.be/-MLIcnua1is', #sagazan
    'https://youtu.be/EBK5aKOr2Fw', #startacult
    'https://youtu.be/SN1GCoVzxGg', #schizophreniasimulator
    'https://youtu.be/W7JyjZI3LUM', #rejected
    'https://youtu.be/C-CNCP3_bE8', #danbellbaltimorecats
    'https://youtu.be/tS-FZrNBduo', #danbellhhhotel
    'https://youtu.be/I43pxV35MbY', #danbellneondreamsmall
    'https://youtu.be/pEjbiYwfUTA', #danbellowingsmallnight
    'https://youtu.be/2FDNQWnLx6g', #ultimatefuel
    'https://youtu.be/AdYaTa_lOf4', #teddyoperation
    'https://youtu.be/q1u7XZ9c8fI', #Симпсоны
    'https://youtu.be/kcHGo2nfWXs', #foodfight
    'https://youtu.be/Edil27RsAek', #youruinedit
    'https://youtu.be/tWdgAMYjYSs', #maxheadroom
    'https://youtu.be/rLy-AwdCOmI', #ifeelfantastic
    'https://youtu.be/jAXioRNYy4s', #ratmoviemayan
    'https://youtu.be/yTU7SebK6EE', #casinonight
    'https://youtu.be/dLCQGIwK-g0', #coopedup
    'https://youtu.be/4MjTb5A68VA', #pencilface
    'https://youtu.be/p9LWzr-_ibI', #worldscult
    'https://youtu.be/E3XE14upb4I', #ratatoing
    'https://youtu.be/xIADIqW30kM', #cinderarielMEP
    'https://youtu.be/i6vK5WT9v-c', #dollhouseMEP
    'https://youtu.be/T5h7h91GGHU', #kuzcolingMEP
    'https://youtu.be/H0DWR6J4jRM', #tarzankiara/janekenaiMEP
    'https://youtu.be/IFfLCuHSZ-U', #P O T A T O K N I S H E S
    'https://youtu.be/jPsX36m86zk', #takemetochurchMEP
    ]

  response = random.choice(weird_links)
  print("Weird video rec'd.")
  await ctx.send(response)
    
@bot.command(name='neat', help="mite b cool, 5sec cooldown between recs")
@commands.cooldown(1, 5, commands.BucketType.user)
async def cool_recs(ctx):
  cool_links = [
    'https://i.imgur.com/2snecmm.jpg', #amagictrick
    'https://youtu.be/J4gJY_5eNqQ', #trufaxleafhopper
    'https://youtu.be/XrUM8m2rnP0', #trufaxsloth
    'https://youtu.be/_y4DbZivHCY', #trufaxseapig
    'https://youtu.be/iHBvKDOfWiI', #underwaterriver
    'https://youtu.be/4ZcEtPFdRaQ', #bluehole
    'https://youtu.be/vQdK7gaZS0k', #pharaohserpent
    'https://youtu.be/SBl1tQlCkBo', #blackhole
    'https://youtu.be/lhjk5x54bsE', #MSMoney
    'https://youtu.be/9RHFFeQ2tu4', #FCFeverTheGhostSource
    'https://youtu.be/WABYmXoJCVE', #HIMmirror
    'https://youtu.be/NBihV_PoGWA', #HIMtoffee
    'https://youtu.be/sSZnI35m3hU', #HIMbowlingpin
    'https://youtu.be/5-n_pPbAYbg', #HIMchristree
    'https://youtu.be/YAOX1ekylnQ', #HIMbowlingball
    'https://youtu.be/qed4ynPYVIA', #HIMmagnets
    'https://youtu.be/2-eMOCMDQj8', #MRcorpsedisposal
    'https://youtu.be/M-rjtG_CHzU', #MRwhiskey
    'https://youtu.be/F2dcJ_cl34E', #MRdistilleddrpep
    'https://youtu.be/IXu7tXixrtQ', #MRghosthunts
    'https://youtu.be/TwIvUbOhcKE', #EBelectritar
    'https://youtu.be/hp97GjuULX8', #EBacdcpain
    'https://youtu.be/L5E4NiP4hpM', #EBtesla
    'https://youtu.be/lT3vGaOLWqE', #EBjacobsladder
    'https://youtu.be/FPHe-xWEdjE', #itsaliveempanadas
    'https://youtu.be/UGjCeAbWKPo', #itsalivehotsaus
    'https://youtu.be/Ng2zOFADe0s', #itsalivekombucha
    'https://youtu.be/lD2OOTx2G9k', #gourmettwinkies
    'https://youtu.be/-pAOuR8s03Q', #gourmetoreos
    'https://youtu.be/jYqRiKu7gY0', #gourmetpoptarts
    ]
  resp = random.choice(cool_links)
  print("Cool video rec'd.")
  await ctx.send(resp)

@bot.command(name='cute', help="so sweet you'll need to brush your teeth, 5sec cooldown between vids")
@commands.cooldown(1, 5, commands.BucketType.user)
async def cute_recs(ctx):
  cute_links = [
    'https://youtu.be/O7D-1RG-VRk', #totorobirb
    'https://youtu.be/ZLp-qhRN_Qc', #hedghegbath
    'https://youtu.be/Z8ZU04U-xAo', #borkcat
    'https://youtu.be/Jv3GJbA_mfk', #skoomacat
    'https://youtu.be/4o5baMYWdtQ', #arf
    'https://youtu.be/AWvefaN8USk', #goatflips
    'https://youtu.be/DmqikqvLLLw', #dumbopus
    'https://youtu.be/6opRWENmvwY', #cuttle
    'https://youtu.be/HBxn56l9WcU', #froge
    'https://youtu.be/W86cTIoMv2U', #tinykitte
    'https://youtu.be/FR3i0qKzRvg', #capywave
    'https://youtu.be/6w2UxDdhZPk', #fritzcantcatch
    'https://youtu.be/6peHtgK0-tM', #fritz2
    'https://youtu.be/sv0cdCSyW9c', #bunnyapples
    ]
  respo = random.choice(cute_links)
  print("Cute video rec'd.")
  await ctx.send(respo)
  
@bot.command(name='moth', help="This article is incomplete. You can help by DMing me ur moths")
@commands.cooldown(1, 5, commands.BucketType.user)
async def moth_recs(ctx):
  moth_links = [
    'https://i.imgur.com/rWgKBgV.jpg',
    'https://i.imgur.com/B4EE27b.jpg',
    'https://i.imgur.com/RWJu4za.jpg',
    'https://i.imgur.com/QWmioFU.jpg',
    'https://i.imgur.com/X802KTj.jpg',
    'https://i.imgur.com/008u5N3.gif',
    'https://i.imgur.com/rCh688r.gif',
    'https://i.imgur.com/L0RyXZt.jpg',
    'https://i.imgur.com/6VACygX.gif',
    ]
  call = random.choice(moth_links)
  print("Moth sent.")
  await ctx.send(call)

@bot.command(name='fortune', help="Gaze into my crystal ball...")
async def fortune(ctx):
  fortuneval = [
    "Your fortune: Reply hazy, try again",
    "Your fortune: Excellent Luck",
    "Your fortune: Good Luck",
    "Your fortune: Average Luck",
    "Your fortune: Bad Luck",
    "Your fortune: Good news will come to you by mail",
    "Your fortune: （　´_ゝ`）ﾌｰﾝ",
    "Your fortune: ｷﾀ━━━━━━(ﾟ∀ﾟ)━━━━━━ !!!!",
    "Your fortune: You will meet a dark handsome stranger",
    "Your fortune: Better not tell you now",
    "Your fortune: Outlook good",
    "Your fortune: Very Bad Luck",
    "Your fortune: Godly Luck"
  ]

  fortunehex = [
    0xf51c6a,
    0xfd4d32,
    0xe7890c,
    0xbac200,
    0x7fec11,
    0x43fd3b,
    0x16f174,
    0x00cbb0,
    0x0893e1,
    0x2a56fb,
    0x6023f8,
    0x9d05da,
    0xd302a7
  ]

  fortunechoice = random.choice(fortuneval)
  
  if fortunechoice in fortuneval:
    ndx = fortuneval.index(fortunechoice)
    fortunecolor= fortunehex[ndx]
  print("Fortune posted.")
  embedVar = discord.Embed(color=fortunecolor, description=fortunechoice)
  await ctx.send(embed=embedVar)

#Broken commands - figure out what the hell broke them
"""@bot.command(name='fetch', help="Sends a list of server users without a certain role.")
@commands.has_role('Moderator')
@is_in_guild(481578657039515648)
async def fetch_norole(ctx):
  rolelist = []
  for member in ctx.guild.members:
    if len(member.roles) < 2:
      rolelist.append(member.mention)
      print(member.name+" fetched!")
  await ctx.message.author.send(" ".join(rolelist))
  print("Outliers fetched.")
  
@bot.command(name='ping', help="DMs each server user without a certain role and reminds them to introduce themselves.")
@commands.has_role('Moderator')
@is_in_guild("")
async def ping_norole(ctx):
  note = "Hi! It looks like you haven't been given the roles necessary to fully join the Strange Aeons discord. If you haven't introduced yourself already (or we somehow missed your introduction - it happens!), just leave a short introduction giving us your name and Patreon username in the server's Introductions channel."
  rolelist = []
  namelist = []
  for member in ctx.guild.members:
    if len(member.roles) < 2:
      rolelist.append(member.mention)
      namelist.append(member.name)
      await member.send(note)
      print(member.name+" notified!")
  await ctx.message.author.send("Notified: " + ", ".join(namelist))
  print("Outliers pinged.")"""

bot.run(token)