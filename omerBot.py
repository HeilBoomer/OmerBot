import time
import discord
from discord.ext import commands
import random
from random import randint
import json
import os
rand = 0

vergistr = ""
def temizle():

    vergi = open("vergiler.txt","r",encoding = "utf8")
    vergistr = vergi.read()
    vergi.close()
    vergistr.replace("ç","c")
    vergistr.replace("Ç","C")
    vergistr.replace("Ö","O")
    vergistr.replace("Ş","S")
    vergistr.replace("ö","o")
    vergistr.replace("ş","s")
    vergistr.replace("İ","I")
    vergistr.replace("Ğ","G")
    vergistr.replace("ğ","g")
    vergistr.replace("ü","u")
    vergistr.replace("Ü","U")
    vergi = open("vergiler.txt","w",encoding = "utf8")
    vergi.write(vergistr)
    vergi.close()

temizle()

client = commands.Bot(command_prefix = "-")


@client.event
async def on_ready():
    print("BotReady")


i = 0
@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith("omer"):
        odevdosya = open("odevler.txt","r")
        await message.channel.send(odevdosya.read())
        odevdosya.close()
    if(message.content.startswith("napim")):
        await message.author.send("mal oc napim ne :cowboy:  :cowboy: ")
    if(message.content.startswith("ğ")):
        await message.author.send("bgy admin")
    if(message.content.startswith("sj")):
        await message.author.send("31")
    if(message.content.startswith("anan")):
        await message.author.send("kardeş miyiz yani ?!?:D:D:D:DD: :sunglasses: :sunglasses: :flushed: ")
    if(message.content.startswith("aga")):
        await message.author.send("https://www.youtube.com/user/TheProcuscihan")
    if(message.content.startswith("31")):
        await message.author.send("sj")
    if(message.content.startswith("@everyone")):
        await message.author.send("atma")
        await message.channel.send(f"boş everyone atma @{message.author}")




   # if message.content.startswith("1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9"or"0"):
    #    rand = random.randint(0,10)
     #   if ((int(message.content)+1)%5 == 0):
      #      if(rand <=6):
       #         if(rand == 1):
        #            await message.channel.send("boM")
         #       if(rand == 2):
         #           await message.channel.send("B0m")
          #      if(rand == 3):
           #         await  message.channel.send("Bo0m :boom:")
            #    if(rand >= 4):
             #       await message.channel.send("b0m")
            #return
    await client.process_commands(message)
#help Yeri
h = """
```
odevler -> ödevleri gösterir
odevekle -> ödev ekler
odevtemizle -> ödevleri temizler
dersprogrami -> ders programını gösterir
ping -> pingi gösterir
temizle -> girilen sayıda mesajı siler
omerhelp -> bu perncereyi açar
vergiler -> türkiye cumhuriyetindeki vergileri gösterir
```



    """

dersler ="""
`
| Gün \ Ders |   1  |   2  |   3  |   4  |   5  |   6  |   7  |   8  |
| ---------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Pazartesi  | BYD2 | BYD2 | BYD2 | BYD1 | BYD1 | REH  | ALM  | ALM  |
| Salı       | BYD2 | BYD2 | MAT  | BYD1 | BYD1 | BYD1 | TÜR  | TÜR  |
| Çarşamba   |      |      | BİL  | BİL  |      |      | BED  | BED  |
| Perşembe   | BYD1 | BYD1 | BYD1 | BYD2 | BYD2 | BYD2 | MAT  | MAT  |
| Cuma       | BYD1 | BYD1 | TÜR  | TÜR  | BYD2 | BYD2 | ALM  | ALM  |
| Cumartesi  | BİL  | BİL  |      |      |      |      |      |      |
`
"""
@client.command()
async def say(ctx,baslangic=0,miktar=0):
    if(baslangic==0 | miktar == 0):
        await ctx.send("bu komut 2 parametre ile calisir Basliyacagi sayi,Kac kere artacagi")
    a = baslangic
    for i in range(miktar):
        await ctx.send(a+i)
@client.command()
#@commands.has_permissions(manage_messages=True)
async def temizle(ctx, amount=0):
    if amount <= 0:
        await ctx.send("-temizle [miktar] (Ayrıca 0'dan büyük bir sayı gir)")
    elif amount >= 100:
        await ctx.send("Çok büyük değer")
    else:
        await ctx.channel.purge(limit=amount+1)
@client.event
async def on_member_join(member):
    print(f"{member} sınıfa geldi")
async def on_member_remove(member):
    print(f"{member} sınıftan ayrıldı")
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping is {round(client.latency*1000)}ms')



@client.command()
async def delchannels(ctx):
    if(ctx.message.author.guild_permissions.administrator):
        for c in ctx.guild.channels: # iterating through each guild channel
            await ctx.send(c)
            ##await c.delete()
    await ctx.send("şimdilik bütün kanalları silmiyim diye sadece chate yazıyorum bunu sadece Geliştirici bunu değiştirebilir")


@client.command()
async def deltext(ctx,channel: discord.TextChannel,count = 1):
    for i in range(count):
      await channel.delete()
    await ctx.send("Deleted " +str(channel) + " channel")
@client.command()
async def delvoice(ctx,channel: discord.VoiceChannel,count = 1):
    for i in range(count):
        await channel.delete()
    await ctx.send("Deleted " +str(channel) + " channel")




@client.command()
async def addchannel(ctx,amount = 1,Cname = "BlankChannel",channelcategory = ""):

    Cname = Cname.replace("_"," ")
    try:
        channelID = ctx.guild.categories[ctx.guild.categories.index(channelcategory)].split(" ")

        if(ctx.message.author.guild_permissions.administrator):


                for i in range(amount):


                        if(i > 0):
                            channel = await ctx.guild.create_text_channel(Cname +" "+ str(i))
                            await channel.edit(category = channelID)
                        else:
                            channel = await ctx.guild.create_text_channel(Cname)
                            await channel.edit(category = channelID)
    except:
        if(ctx.message.author.guild_permissions.administrator):


                for i in range(amount):


                        if(i > 0):
                            channel = await ctx.guild.create_text_channel(Cname +" "+ str(i))

                        else:
                            channel = await ctx.guild.create_text_channel(Cname)
                await ctx.send(f"I can't found {channelcategory} category so I make channels without a category :D.")
                await ctx.send(f"Categories : {ctx.guild.categories}")





@client.command()
#A fun function that gives you a list of taxes in Turkey
async def vergiler(ctx):
    if(ctx.message.author.guild_permissions.admin):
        verg = open("vergiler.txt","r",encoding = "utf8")
        verglist = verg.readlines()
        for i in range(372):
            await ctx.send(verglist[i])
            time.sleep(0.6)
        verg.close()
    else:
        ctx.send("Ab admin yetkin yko :flushed: ")

@client.command()
#Homeworks command you can change the name by changing the function name
async def odevler(ctx):
    odevdosya = open("odevler.txt","r",encoding = "utf8"    )
    await ctx.send("```"+odevdosya.read()+"```")
    odevdosya.close()
@client.command()
#Add homework command
async def odevekle(ctx,yeniodev):
    odevdosya = open("odevler.txt","a",encoding = "utf8")
    odevdosya.write("\n"+yeniodev)
    odevdosya.close()
@client.command()
#Clear homework command
async def odevtemizle(ctx):
    odevdosya = open("odevler.txt","w",encoding = "utf8")
    odevdosya.close()
@client.command()
#Alternative help command
async def omerhelp(ctx):
    await ctx.send(h)
@client.command()
#syllabus
async def dersprogrami(ctx):
    await ctx.send(dersler)




client.run("//Your token here.")
