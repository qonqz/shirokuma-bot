import discord
import asyncio
import random
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print('-------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

@client.event
async def on_message(message):
    if message.content.startswith('สวัสดี'):
        kawaii_1 = random.choice([message.author.mention + ' สวัสดีค่ะ',message.author.mention + ' จ๊ะจ๋า.. สวัสดีค่ะ','อ่าาาอ๊าาาา สวัสดีจ่าววววว','แอบมองเธออยู่นาจา..'])
        await client.send_message(message.channel, kawaii_1)
    elif message.content.startswith('ทำอะไรดี'):
        kawaii_2 = random.choice(['เล่นเกมไงจ๊ะ ' + message.author.mention,'ไปนอนสิค๊ะ ' + message.author.mention + ' อิอิ','ออกไปหาอะไรกินสิ' + message.author.mention,'ไม่รุ้อ่ะ'])
        await client.send_message(message.channel, kawaii_2)
    elif message.content.startswith('กรวย'):
        kawaii_3 = random.choice(['กร๊วยพ่องงงงง ' + message.author.mention + ' ดิ','ไม่เอาดิ' + message.author.mention +  ' ไม่หยาบคายน๊า','ทำไมพูดแบบนี้คะ','นิสัย! ' + message.author.mention])
        await client.send_message(message.channel, kawaii_3)
    elif message.content.endswith('กรวย'):
        kawaii_4 = random.choice(['กร๊วยพ่องงงงง ' + message.author.mention + ' ดิ','ไม่เอาดิ' + message.author.mention +  ' ไม่หยาบคายน๊า','ทำไมพูดแบบนี้คะ','นิสัย! ' + message.author.mention])
        await client.send_message(message.channel, kawaii_4)
    elif message.content.startswith('ง่วง'):
        kawaii_5 = random.choice([message.author.mention + ' ก็ไปนอนสิ','มานอนหนุนตักเค้าไหมล่ะ ' + message.author.mention,'บัย.. ' + message.author.mention +  ' อิอิ',message.author.mention + ' เกมเมอร์เค้านอนกันที่ไหน'])
        await client.send_message(message.channel, kawaii_5)
    elif message.content.startswith('555'):
        kawaii_6 = random.choice([message.author.mention + ' ขำอารัยจ๊ะ','ขำด้วยสิ ฮ่าๆๆๆ ' + message.author.mention,'o.O ' + message.author.mention, 'ฮ่าๆๆๆๆ ขำด้วย'])
        await client.send_message(message.channel, kawaii_6)
    elif message.content.endswith('555'):
        kawaii_7 = random.choice([message.author.mention + ' ขำอารัยจ๊ะ','ขำด้วยสิ ฮ่าๆๆๆ ' + message.author.mention,'o.O ' + message.author.mention, 'ฮ่าๆๆๆๆ ขำด้วย'])
        await client.send_message(message.channel, kawaii_7)



client.run("NDExNTcwODE5ODc4MzU0OTU0.DV9oww.BmpZspcD0SQ2jPW_y9tVzCI7MaQ")

#    elif message.content.startswith('.........'):
#        kawaii_X = random.choice(['choice1','choice2','choice3'])
#        await client.send_message(message.channel, kawaii_X)
#    elif message.content.endswith('.........'):
#        kawaii_Y = random.choice(['choice1','choice2','choice3'])
#        await client.send_message(message.channel, kawaii_Y)



#        kawaii_x = random.choice(['choice1','choice2','choice3'])
#        await client.send_message(message.channel, kawaii_x)
