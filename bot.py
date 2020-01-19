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
players={}
songs = asyncio.Queue()
play_next_song = asyncio.Event()
client = commands.Bot(command_prefix='-')

###################Quotes#########################

gastoquotes = [
    "PERDON - DUKI"
]
matiquotes = [
    'TE AMO',
]
masterquotes = [
    'MENDOZAAAAAAAAAAAAAAAAAAAAAAAAAAA',
]
testquotes=[
    "test",
    "testeado",
    "gigatesteado"
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
        await ctx.send(file=discord.File(nombre+".gif"))
    else:
        channel = client.get_channel(186958407264108544)
        await ctx.send(file=discord.File(nombre+".jpg"))

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

@client.command(name="vaultdelete", help="Lista")
async def vaultdelete(ctx): #agregar nombre cuando vuelva a funcionar
    quote = [
    'El delete ahora mismo no está funcionando, llamalo a Mati para que borre la imagen manualmente'
    ]

    response = random.choice(quote)
    await ctx.send(response)
    #validacion=nombre[-3:]
    #cone=0
    #countone=0
    #if validacion=="gif":
        #nombre=nombre+"GIF"
        #with open("gif.txt", "r+") as f:
            #d = f.readlines()
            #f.seek(0)
            #for i in d:
                #if i != nombre:
                    #f.write(i+"\n")
                #if i == nombre:
                    #countone=countone+1
            #f.truncate()
        #if countone>0:
            #response="Archivo borrado correctamente"
            #await ctx.send(response)
        #else:         
            #response="El nombre de esa imagen no existe, borra otro o mira la lista, pelotudo."
            #await ctx.send(response)
    #else:
        #with open("imagenes.txt", "r+") as f:
            #d = f.readlines()
            #f.seek(0)
            #for i in d:
                #a=i[:-1]
                #print (i)
                #if str(a) != nombre:
                    #f.write(i+"\n")
                #if str(a) == nombre:
                    #cone=cone+1
            #f.truncate()
        #if cone>0:
            #response="Archivo borrado correctamente"
            #await ctx.send(response)
        #else:         
            #response="El nombre de esa imagen no existe, borra otro o mira la lista, pelotudo."
            #await ctx.send(response)

#################Juegos##########################
    
#@client.command(name='dadito', help='jaja que queria')
#async def roll(ctx, number_of_dice: int, number_of_sides: int):
    #dice = [
        #str(random.choice(range(1, number_of_sides + 1)))
        #for _ in range(number_of_dice)
    #]
    #await ctx.send(', '.join(dice))

    
@client.command(name='coin', help='matense')
async def coin(ctx):
    caracruz = [
        'Yo, el client de la razón absoluta, elijo **Cara**',
        'Yo, el client de la razón absoluta, elijo **Cruz**',
    ]

    response = random.choice(caracruz)
    await ctx.send(response)


@client.command(name='8ball', help='8ball')
async def ball(ctx):
    caracruz = [
        'Yo, el bot de la razón absoluta, te digo que **sí**',
        'Yo, el bot de la razón absoluta, te digo que **no**',
    ]

    response = random.choice(caracruz)
    await ctx.send(response)
    
@client.command(name="pick", help="Pick")
async def pick(ctx, *parametros):
    lista=[]
    lista.clear()
    for x in (str(len(parametros))):
        lista.append(parametros)
    response = random.choice(parametros)
    response="Yo, el bot de la razon absoluta elijo a **"+response+"**"
    await ctx.send(response)

@client.command(name="select", help="Select")
async def select(ctx):
    
    parametros=pick(lista)
    if parametros==():
        response="No existe ningun parametro"
        await ctx.send(response)
    else: 
        response = random.choice(parametros)
        response="Yo, el bot de la razon absoluta elijo a **"+response+"**"
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
    
@client.command(name='calc', help='eso')
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
    
#################Musica#########################

#################Mensajes#########################

@client.command()
async def on_message(message):
    mensaje=message.content

    mensaje=mensaje.lower()
    if message.author == client.user:
        return
    if mensaje == 'gasto': 
        response = random.choice(gastoquotes)
        await message.channel.send(response)
    if mensaje == 'mati':  
        response = random.choice(matiquotes)
        await message.channel.send(response)
    if mensaje == 'master':  
        response = random.choice(masterquotes)
        await message.channel.send(response)
    if mensaje == 'test':  
        response = random.choice(testquotes)
        await message.channel.send(response)

@client.command(name="prune", pass_context=True)
async def clear(ctx, amount=0):
    if amount==0:
        response="Por favor, selecciona la cantidad de mensajes"
        await ctx.send(response)
    if amount>=1 and amount<=50:
        response=str(amount)+" mensajes borrados"
        await ctx.channel.purge(limit=amount)
        await ctx.send(response)
    if amount>=51:
        response="Mas de 50 es mucho, ¿no?"
        await ctx.send(response)
        
@client.command(name="porfavornousar")
async def porfavornousar(ctx, nombre):
    await client.change_presence(status=discord.Status.online, activity=discord.Game(nombre))
    
client.run(token)
