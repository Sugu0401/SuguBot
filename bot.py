##client.py
import os
import random
import discord
import requests
import youtube_dl
import asyncio

from discord.ext import commands
from dotenv import load_dotenv
from discord.utils import get

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
c=0
count=0
client = commands.Bot(command_prefix='-')

###################Quotes#########################

gastoquotes = [
    "SOY UN ROBOT NO MIENTO"
]
matiquotes = [
    'TE AMO',
]
masterquotes = [
    'MENDOZAAAAAAAAAAAAAAAAAAAAAAAAAAA',
]
testquotes = [
    'testeado',
    'giga testeado',
    'hiper testeado',
    'mega testeado',
    'tera testeado',
    'giga ultra testeado',
]
testquotes1 = [
]
testquotes2 = [
]
testquotes3 = [
]
parametros = ()      
###############Vault#####################    
@client.command(name="vaultsave", help="Guarda una imagen")
async def vaultsave(ctx, nombre, url):
    img_data = requests.get(url).content
    validacion=str(url)[-3:]
    c=0
    if validacion=="gif":
        nombre=nombre+"GIF"
        a = open("gif.txt", "r")
        for x in a:
            x=x.strip()
            if nombre==x:
                  c=c+1
        if c>=1:
            response="El nombre de esa imagen ya existe, usa otro o mira la lista, pelotudo."
            await ctx.send(response)
        else:         
            with open(nombre+".gif", 'wb') as handler:
                handler.write(img_data)
                g = open("gif.txt","a+")
                g.write(nombre+"\n")
                g.close()
                response="Registro agregado correctamente"
            await ctx.send(response)
    if validacion=="jpg" or validacion=="png" or validacion=="jpeg":
        b = open("imagenes.txt", "r")
        for x in b:
            x=x.strip()
            if nombre==x:
                  c=c+1
        if c>=1:
            response="El nombre de esa imagen ya existe, usa otro o mira la lista, pelotudo."
            await ctx.send(response)
        else:         
            with open(nombre+".jpg", 'wb') as handler:
                handler.write(img_data)
                f = open("imagenes.txt","a+")
                f.write(nombre+"\n")
                f.close()
                response="Registro agregado correctamente"
            await ctx.send(response)

@client.command(name="vaultsend", help="Muestra una imagen")
async def vaultsend(ctx, nombre):
    validacion=nombre[-3:]
    validacion.lower()
    if validacion=="gif":
        channel = client.get_channel(186958407264108544)
        await channel.send(file=discord.File(nombre+".gif"))
    else:
        channel = client.get_channel(186958407264108544)
        await channel.send(file=discord.File(nombre+".jpg"))

@client.command(name="vaultlist", help="Lista")
async def vaultlist(ctx):
    f = open("imagenes.txt","r")
    contents = "**Listado de imagenes:\n**"
    d = f.readlines()
    for i in d:
        i=i.replace("\n", "")
        if i!=" " or h!="":
            i=i+"\n"
            contents = contents + i
    f.close()
    g = open("gif.txt", "r")
    contentsG = "\n**Listado de gifs:\n**"
    j = g.readlines()
    for h in j:
        h=h.replace("\n", "")
        if h!=" " or h!="":
            h=h+"\n"
            contentsG = contentsG + h
    contents = contents + contentsG
    await ctx.send(contents)

@client.command(name="vaultdelete", help="Borra una imagen")
async def vaultdelete(ctx, nombre):
    validacion=nombre[-3:]
    cone=0 #contadorimg
    countone=0  #contadorgif
    if validacion=="gif":
        nombre=nombre+"GIF"
        with open("gif.txt", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                a=i[:-1]
                print (i)
                if str(a) != nombre:
                    f.write(i+"\n")
                if str(a) == nombre:
                    countone=countone+1
            f.truncate()
        if countone>0:
            response="Archivo borrado correctamente"
            await ctx.send(response)
        else:         
            response="El nombre de esa imagen no existe, borra otro o mira la lista, pelotudo."
            await ctx.send(response)
    else:
        with open("imagenes.txt", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                a=i[:-1]
                print (i)
                if str(a) != nombre:
                    f.write(i+"\n")
                if str(a) == nombre:
                    cone=cone+1
            f.truncate()
        if cone>0:
            response="Archivo borrado correctamente"
            await ctx.send(response)
        else:         
            response="El nombre de esa imagen no existe, borra otro o mira la lista, pelotudo."
            await ctx.send(response)

#################Juegos##########################
    
@client.command(name='dado', help='Parametro 1: Numero de dados, parametro 2: caras del dado')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

    
@client.command(name='coin', help='Cara o cruz')
async def coin(ctx):
    caracruz = [
        'Yo, el bot de la razón absoluta, elijo **Cara**',
        'Yo, el bot de la razón absoluta, elijo **Cruz**',
    ]

    response = random.choice(caracruz)
    await ctx.send(response)

@client.command(name="pick", help="Pick")
async def pick(ctx, *parametros):
    lista=[]
    lista.clear()
    for x in (str(len(parametros))):
        lista.append(parmetros)
    response = random.choice(lista)
    response="Yo, el bot de la razón absoluta elijo a **"+response+"**."
    await ctx.send(response)

#################League of legends##########################

@client.command(name="lol", help="Partida de LoL")
async def lol(ctx, nombre):
    nombre=nombre.lower()
    url="https://porofessor.gg/live/las/"
    nombre.replace(" ", "_")
    response=url+nombre
    await ctx.send(response)

@client.command(name="tier", help="Tierlist")
async def loltier(ctx, rol):
    rol=rol.lower()
    if rol=="adc":
        url="https://u.gg/lol/tier-list?role=adc"
        response=url
    if rol=="sup":
        url="https://u.gg/lol/tier-list?role=support"
        response=url
    if rol=="mid":
        url="https://u.gg/lol/tier-list?role=middle"
        response=url
    if rol=="jg":
        url="https://u.gg/lol/tier-list?role=jungle"
        response=url
    if rol=="top":
        url="https://u.gg/lol/tier-list?role=top"
        response=url
    if rol!="adc" and rol!="sup" and rol!="mid" and rol!="top" and rol!="jg":
        response="Rol incorrecto, proba con sup, adc, mid, jg o top"
    await ctx.send(response)

@client.command(name="ugg", help="Champion")
async def ugg(ctx, nombre):
    nombre=nombre.lower()
    url="https://u.gg/lol/champions/"
    nombre.replace(" ", "_")
    response=url+nombre+"/build"
    await ctx.send(response)

@client.command(name="profile", help="Perfil de lol")
async def profile(ctx, region, nombre):
    region=region.lower()
    if region=="las":
        url="https://u.gg/lol/profile/la2/"
        response=url+nombre+"/overview"
    if region=="lan":
        url="https://u.gg/lol/profile/la1/"
        response=url+nombre+"/overview"
    if region=="br":
        url="https://u.gg/lol/profile/la2/"
        response=url+nombre+"/overview"
    if region=="na":
        url="https://u.gg/lol/profile/na1/"
        response=url+nombre+"/overview"
    if region!="las" and region!="lan" and region!="br" and region!="na":
        response="Region incorrecta, proba con LAS, LAN, BR o NA"
    await ctx.send(response)   

#################Funcionalidades#########################
    
@client.command(name='calc', help='Calculadora de dos numeros')
async def calc(ctx, number_one, ope, number_two):
    if ope=="+":
        response=int(number_one)+int(number_two)
    elif ope=="-":
        response=int(number_one)-int(number_two)
    elif ope=="*":
        response=int(number_one)*int(number_two)
    elif ope=="/":
        response=int(number_one)/int(number_two)
    else:
        response="Parameto no encontrado o no sabes poner numeros"
    await ctx.send(response)

@client.command(name="avatar", help="Muestra el avatar de un usuario")
async def avatar(ctx, member: discord.Member):
    avatar=discord.Embed(
        color = discord.Color.dark_blue(),
        title = f" Perfil de {member.name}",
    )
    avatar.set_image(url='{}'.format(member.avatar_url))
    #avatar.set_footer(text=f'Bastante feo e')
    await ctx.send(embed=avatar)

@client.command(name="prune", help="Borra mensajes")
async def prune(ctx, amount=100):
  channel = ctx.message.channel
  messages = []
  async for message in client.logs_from (channel, limit=init(amount)+1:
    messages.append(message)
  await client.delete_messages(messages)
  response = "Mensajes eliminados:"+amount
  await ctx.send(response)  

#################Tags##########################    

@client.command(name="", help="AAA")
async def aaaa(ctx, member:discord.Member):
  await ctx.send(f"PONG {member}")

#################Mensajes#########################

@client.event
async def on_message(message):
    mensaje=message.content

    mensaje=mensaje.lower()
    if message.author == client.user:
        return
    if message.content == 'gasto':
        response = random.choice(gastoquotes)
        await message.channel.send(response)
    if message.content == 'mati': 
        response = random.choice(matiquotes)
        await message.channel.send(response)
    if message.content == 'master':
        response = random.choice(masterquotes)
        await message.channel.send(response)
    if message.content == "test":
        response = random.choice(testquotes)
        await message.channel.send(response)
client.run(token)