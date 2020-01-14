##bot.py
import os
import random
import discord
import requests

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
c=0
count=0
bot = commands.Bot(command_prefix='-')

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

parametros = ()      
###############Vault#####################    
@bot.command(name="vaultsave", help="Guarda una imagen")
async def vaultsave(ctx, nombre, url):
    img_data = requests.get(url).content
    validacion=str(url)[-3:]
    global c
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

@bot.command(name="vaultsend", help="Muestra una imagen")
async def vaultsend(ctx, nombre):
    validacion=nombre[-3:]
    validacion.lower()
    if validacion=="gif":
        channel = bot.get_channel(186958407264108544)
        await channel.send(file=discord.File(nombre+".gif"))
    else:
        channel = bot.get_channel(186958407264108544)
        await channel.send(file=discord.File(nombre+".jpg"))

@bot.command(name="vaultlist", help="Lista")
async def vaultlist(ctx):
    f = open("imagenes.txt","r")
    contents = "**Listado de imagenes:\n**"
    contents = contents + f.read()
    contents = contents + "\n"
    f.close()
    g = open("gif.txt", "r")
    contentsG = "**Listado de gifs:\n**"
    contents = contents + contentsG + g.read()
    await ctx.send(contents)

@bot.command(name="delete", help="Lista")
async def vaultdelete(ctx, nombre):
    validacion=nombre[-3:]
    global count
    if validacion=="gif":
        nombre=nombre+"GIF"
        with open("gif.txt", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if i != nombre:
                    f.write(i)
                else:
                    count=count+1
            f.truncate()
        if count>0:
            os.remove(file) for file in os.listdir('') if file.endswith('.gif')
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
                if i != nombre:
                    f.write(i)
                else:
                    c=c+1
            f.truncate()
        if c>0:
            os.remove(file) for file in os.listdir('') if file.endswith('.jpg')
            response="Archivo borrado correctamente"
            await ctx.send(response)
        else:         
            response="El nombre de esa imagen no existe, borra otro o mira la lista, pelotudo."
            await ctx.send(response)

#################Juegos##########################
    
@bot.command(name='dadito', help='jaja que queria')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

    
@bot.command(name='coin', help='matense')
async def coin(ctx):
    caracruz = [
        'Yo, el bot de la razón absoluta, elijo **Cara**',
        'Yo, el bot de la razón absoluta, elijo **Cruz**',
    ]

    response = random.choice(caracruz)
    await ctx.send(response)

@bot.command(name="pick", help="Pick")
async def pick(ctx, *parametros):
    lista=[]
    lista.clear()
    for x in (str(len(parametros))):
        lista.append(parmetros)
    response = random.choice(parametros)
    response="Yo, el bot de la razon absoluta elijo a **"+response+"**"
    await ctx.send(response)

@bot.command(name="select", help="Select")
async def select(ctx):
    
    parametros=pick(lista)
    if parametros==():
        response="No existe ningun parametro"
        await ctx.send(response)
    else: 
        response = random.choice(parametros)
        response="Yo, el bot de la razon absoluta elijo a **"+response+"**"
        await ctx.send(response)
        
#################Funcionalidades#########################
    
@bot.command(name='calc', help='eso')
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



@bot.command(name="avatar", help="Muestra el avatar de un usuario")
async def avatar(ctx, member: discord.Member):
    avatar=discord.Embed(
        color = discord.Color.dark_blue(),
        title = f" Perfil de {member.name}",
    )
    avatar.set_image(url='{}'.format(member.avatar_url))
    #avatar.set_footer(text=f'Bastante feo e')
    await ctx.send(embed=avatar)

#################Mensajes#########################

#@bot.event
#async def on_message(message):
    #mensaje=message.content

    #mensaje=mensaje.lower()
    #if message.author == bot.user:
        #return
    #if message.content == 'gasto': # or message.content == 'gasto' or message.content == 'GASTO':
        #response = random.choice(gastoquotes)
        #await message.channel.send(response)
    #if message.content == 'mati': # or message.content == 'mati' or message.content == 'MATI': 
        #response = random.choice(matiquotes)
        #await message.channel.send(response)
    #if message.content == 'master': # or message.content == 'master' or message.content == 'MASTER': 
        #response = random.choice(masterquotes)
        #await message.channel.send(response)
    
bot.run(token)
