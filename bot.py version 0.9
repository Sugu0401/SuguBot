##client.py
import os
import random
import discord
import requests
import youtube_dl
import asyncio
import itertools
import mysql.connector
import xml.dom.minidom
import requests
from discord.ext import commands
from dotenv import load_dotenv
from itertools import cycle
from discord import FFmpegPCMAudio
from discord.utils import get
from lxml import html
from xml.dom.minidom import parse, parseString

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
c=0
count=0
players={}
songs = asyncio.Queue()
play_next_song = asyncio.Event()
client = commands.Bot(command_prefix='-')
###################Embed F.A.Q###################
@client.command(name="h")
async def displayembed(ctx):
    embed = discord.Embed(
        title = "Hola, ¿quien soy?",
        description = "Soy SuguBot, un bot desarrollado para satisfascer\n las necesidades en psicologia crew, proximas metas: musica",
        color = discord.Color.dark_blue()
    )
    embed.set_footer(text="El talento muere cuando no se apuesta.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/587446672741892096/91d0ae1c6da214afe46775b39664c4ee.webp")
    embed.add_field(name="Comandos", value="Escribi -help para conocer mis comandos", inline=False)
    embed.add_field(name="Conoceme", value="https://twitter.com/matiassctt\nhttps://www.instagram.com/matiassctt/", inline=True)
    #embed.add_field(name="Test3", value="test3", inline=True)
    await ctx.send(embed=embed)

@client.command(name="perfil")
async def perfil(ctx, member: discord.Member):
    guild=member.guild
    embed = discord.Embed (colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"Informacion de: {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="Nombre dentro del servidor:", value=member.display_name, inline=False)
    embed.add_field(name="Top rol:", value=member.top_role.mention, inline=True)
    embed.add_field(name="Tu cuenta se creo el:", value=member.created_at.strftime("%#d %B %Y a las %I:%M %p UTC"), inline=True)
    embed.add_field(name=f"Te uniste al servidor el:", value=member.joined_at.strftime("%#d %B %Y a las %I:%M %p UTC"), inline=True)
    embed.add_field(name="¿Sabias qué?", value=random.choice(randomfacts), inline=True)

    await ctx.send(embed=embed)
    
###################Database######################

def conectar():
    try:
        mibase=mysql.connector.connect(host="localhost", user="root", password="", database="sugubot")
        return mibase
    except:
        print ("No se pudo conectar")
        
base=conectar()
mycursor=base.cursor()

@client.command(name="inpale")
async def inpale(ctx):
    response = "**Bienvenidos a la International Pajas League, los comandos que podes usar son:**\n"
    response = response + "-listado\n"
    response = response + "-cantidad **nombre** **mes**"
    await ctx.send(response)
@client.command(name="listado")
async def listado(ctx):
    res="SELECT * FROM usuarios"
    mycursor.execute(res)
    fila=mycursor.fetchall()
    response = "**Listado de participantes de la INPALE:**\n"
    for rows in fila:
        idd=rows[0],
        nombre=rows[1],
        idd=str(idd)
        nombre=str(nombre)
        idd=idd.replace("(","")
        idd=idd.replace(")","")
        idd=idd.replace(",","")
        nombre=nombre.replace("(","")
        nombre=nombre.replace(")","")
        nombre=nombre.replace(",","")
        nombre=nombre.replace("'","")
        response = response + idd + " | " + nombre.capitalize() + "\n"
    await ctx.send(response)

@client.command(name="cantidad")
async def cantidad(ctx, usuario, mes):
    res = 'SELECT SUM(cantidad) FROM pjs, usuarios WHERE pjs.id_usuario=usuarios.id_usuario and usuarios.nombre=%s and pjs.mes=%s'
    val=(usuario, mes)
    mycursor.execute(res, val)
    res = mycursor.fetchall()
    res = str(res)
    res=res.replace("[","")
    res=res.replace("]","")
    res=res.replace("Decimal","")
    base.commit()
    response = "La cantidad de pajas de**", usuario.capitalize(), "**en el mes de**", mes, "**es de**", res, "**pajas"
    response = str(response)
    response=response.replace("(","")
    response=response.replace(")","")
    response=response.replace(",","")
    response=response.replace("'","")
    await ctx.send(response)
    
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
gamequotes=[
    "@matiassctt",
    "-help",
    "Musica coming soon!"
]
randomfacts=[
    "El carpincho es el roedor mas grande del mundo llegando a medir entre 1.10 y 1.30 metros.",
    "111,111,111 x 111,111,111 = 12,345,678,987,654,321",
    "El tomate es una fruta",
    "Maste todavía no sabe que ser si no fuera un pendejo",
    "Técnicamente el negro no es un color",
    "Tu pie es tan grande como tu antebrazo",
    "Los patos son los violadores del reino animal",
    "No puedes respirar rapidamente con los ojos volteados",
    "El popó de los wombats es cuadrado",
    "No puedes lamer tu codo",
    "Te quedan dos intentos",
    "Las mujeres con todas putas menos tu mamá y tu abuela",
]
parametros = ()      
###############Vault#####################    
@client.command(name="vaultsave", help="Guarda una imagen, nombre y despues url")
async def vaultsave(ctx, nombre, url):
    img_data = requests.get(url).content
    validacion=str(url)[-3:]
    c=0
    if validacion=="gif":
        nombre=nombre+"gif"
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

@client.command(name="vaultsend", help="Envia una imagen")
async def vaultsend(ctx, nombre):
    validacion=nombre[-3:]
    validacion.lower()
    if validacion=="gif":
        await ctx.send(file=discord.File(nombre+".gif"))
    else:
        await ctx.send(file=discord.File(nombre+".jpg"))

@client.command(name="vaultlist", help="Lista del vault")
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
        #nombre=nombre+"gif"
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

    
@client.command(name='coin', help='Tails or Heads')
async def coin(ctx):
    caracruz = [
        'Yo, el bot de la razón absoluta, elijo **Cara**',
        'Yo, el bot de la razón absoluta, elijo **Cruz**',
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

@client.command(name='8BALL', help='8ball')
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
        await fetch_user_profile(user_id)

#################League of legends##########################

@client.command(name="lol", help="Partida de LoL, solo nombre")
async def lol(ctx, nombre):
    nombre=nombre.lower()
    url="https://porofessor.gg/live/las/"
    nombre.replace(" ", "_")
    response=url+nombre
    await ctx.send(response)

@client.command(name="tier", help="Tierlist de lol, rol")
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

@client.command(name="ugg", help="Champion de lol, nombre")
async def ugg(ctx, nombre):
    nombre=nombre.lower()
    url="https://u.gg/lol/champions/"
    nombre.replace(" ", "_")
    response=url+nombre+"/build"
    await ctx.send(response)

@client.command(name="profile", help="Perfil de lol, nombre y region.")
async def profile(ctx, nombre, region="las"):
    region=region.lower()
    if region=="las":
        url = 'https://las.op.gg/summoner/userName='+nombre
        #url = 'https://las.op.gg/summoner/userName=hyejooist'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(url, headers=headers)

        tree = html.fromstring(result.content)
        #Revisa si esta ingame
        liga = tree.xpath('//div[@class="TierRank"]/text()')
        unranked = tree.xpath('//div[@class="TierRank unranked"]/text()')
        puntos = tree.xpath('//span[@class="LeaguePoints"]/text()')
        wins = tree.xpath('//span[@class="wins"]/text()')
        losses = tree.xpath('//span[@class="losses"]/text()')
        ultimas_partidas = tree.xpath('//span[@class="total"]/text()')
        ultimas_partidas_wins=tree.xpath('//span[@class="win"]/text()')
        ultimas_partidas_losses=tree.xpath('//span[@class="lose"]/text()')
        try:
            liga = liga[0]
        except IndexError:
            liga="asdasd"
        try:
            unranked=unranked[0].strip()
        except IndexError:
            unranked="asdasd"
            print (unranked)
        print (liga)
        if unranked=="Unranked":
            embed = discord.Embed(
                title = f"Perfil de {nombre}",
                description=f"Podes ver mas de tu informacion en {url}",
                color = discord.Color.dark_blue()
            )
            #embed.set_author(name=f"Informacion de: {nombre}")
            embed.set_thumbnail(url="https://i.imgur.com/jrASJI2.png")
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

            embed.add_field(name="Liga", value="Unranked", inline=True)
            embed.add_field(name="Informacion:", value="¡Empeza a rankear para obtener tus estadisticas!", inline=False)
            embed.add_field(name="Ultimas partidas", value=f"Ultimamente jugaste {ultimas_partidas[0]} partidas, ganaste {ultimas_partidas_wins[0]} y perdiste {ultimas_partidas_losses[0]}.", inline=False)
            embed.add_field(name="¿Sabias qué?", value=random.choice(randomfacts), inline=True)

            await ctx.send(embed=embed)
            return
        if unranked!="Unranked":
            if liga.startswith("Silver"):
                imagen="https://i.imgur.com/GHQOcdK.png"
            if liga.startswith("Bronze"):
                imagen="https://i.imgur.com/7AX0K64.png"
            if liga.startswith("Gold"):
                imagen="https://i.imgur.com/XVt1qku.png"
            #if liga.startswith("Platinum"):
            #if liga.startswith("Diamond"):
            #if liga.startswith("Master"):
            #if liga.startswith("Grand"):
            #if liga.startswith("Chall"):
            winrate= tree.xpath('//span[@class="winratio"]/text()')
            winrate=winrate[0]
            winrate=winrate[-3:]
            embed = discord.Embed(
                title = f"Perfil de {nombre}",
                description=f"Podes ver mas de tu informacion en {url}",
                color = discord.Color.dark_blue()
            )
            #embed.set_author(name=f"Informacion de: {nombre}")
            embed.set_thumbnail(url=imagen)
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

            embed.add_field(name="Liga", value=liga, inline=True)
            embed.add_field(name="Puntos", value=puntos[0], inline=True)
            embed.add_field(name="Promos:", value="En arreglo", inline=True)
            embed.add_field(name="Win", value=wins[0], inline=True)
            embed.add_field(name="Losses", value=losses[0], inline=True)
            embed.add_field(name="Winrate", value=winrate, inline=True)
            embed.add_field(name="Ultimas partidas", value=f"Ultimamente jugaste {ultimas_partidas[0]} partidas, ganaste {ultimas_partidas_wins[0]} y perdiste {ultimas_partidas_losses[0]}.", inline=False)
            embed.add_field(name="¿Sabias qué?", value=random.choice(randomfacts), inline=True)

            await ctx.send(embed=embed)
    if region=="lan":
        url="https://lan.op.gg/summoner/userName="
        response=url+nombre
    if region=="br":
        url="https://br.op.gg/summoner/userName="
        response=url+nombre
    if region=="na":
        url="https://na.op.gg/summoner/userName="
        response=url+nombre
    if region=="euw":
        url="https://euw.op.gg/summoner/userName="
        response=url+nombre
    if region!="las" and region!="lan" and region!="br" and region!="na" and region!="euw":
        response="Region incorrecta, proba con LAS, LAN, BR, NA o EUW"
    await ctx.send(response)   
#################Funcionalidades#########################
    
@client.command(name='calc', help='Calculadora: Ejemplo 2 + 2')
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
        title = f" Avatar de {member.name}",
    )
    avatar.set_image(url='{}'.format(member.avatar_url))
    #avatar.set_footer(text=f'Bastante feo e')
    await ctx.send(embed=avatar)

@client.command(name="av", help="Muestra el avatar de un usuario")
async def av(ctx, member: discord.Member):
    avatar=discord.Embed(
        color = discord.Color.dark_blue(),
        title = f" Avatar de {member.name}",
    )
    avatar.set_image(url='{}'.format(member.avatar_url))
    #avatar.set_footer(text=f'Bastante feo e')
    await ctx.send(embed=avatar)

@client.command(name="prune", help="Borra de 1 a 50 mensajes.", pass_context=True)
async def clear(ctx, amount=0):
    if amount==0:
        response="Por favor, selecciona la cantidad de mensajes"
        await ctx.send(response)
    if amount>=1 and amount<=50:
        response=str(amount)+" mensajes borrados"
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(response)
    if amount>=51:
        response="Mas de 50 es mucho, ¿no?"
        await ctx.send(response)
##################Canciones######################################
@client.command(name='tusa', help='tusa')
async def tusa(ctx):
    tusa = [
        "Pero si le ponen la canción (Hmm)\nLe da una depresión tonta\nLlorando lo comienza a llamar\nPero él la dejó en buzón (No\n¿Será porque con otra está (Con otra está)\nFingiendo que a otra se puede amar?\nPero diste todo este llanto por nada\n**AHORA SOY UNA CHICA MALA**"
    ]

    response = random.choice(tusa)
    await ctx.send(response)
@client.command(name="cancion", help="bb")
async def cancion(ctx):
    cancion = [
        "Pensaba que te había olvidao, eh\nPero pusieron la canción, eh, eh, eh\nQue cantamo bien borracho\nQue bailamo bien borracho\nNos besamo bien borracho los dos\nPensaba que te había olvidao, eh\nPero pusieron la canción, eh, eh, eh\nQue cantamo bien borracho\nQue bailamo bien borracho\nNos besamo bien borracho los dos\nPensaba que te había olvidoo\n"
    ]

    response = random.choice(cancion)
    await ctx.send(response)
    
@client.event
async def on_ready():
    #await client.change_presence(activity=discord.Game("Musica comming soon!"))
    await client.change_presence(activity=discord.Game(name='-h, Ayudando a '+str(len(client.guilds))+' servidores | Conectado con '+str(len(set(client.get_all_members())))+' usuarios'))

#################Mensajes#########################
    
@client.event
async def on_message(message):
    channel = message.channel
    if message.content=="XD":
        await channel.send(file=discord.File("xd.mp4"))
        await channel.send(file=discord.File("XD.jpg"))
    else:
        mensaje=message.content
        mensaje=mensaje.lower()
        if message.author == client.user:
            return
        if mensaje == 'la wea del mago':
            await channel.send('LA WEA DEL MAGO')
        if mensaje == "ivan" or mensaje == "iván":
            await channel.send("COGETE A PALU")
        if mensaje == "test":
            response = random.choice(testquotes)
            await channel.send(response)
        await client.process_commands(message)
        if mensaje.startswith("hola bro"):
            await channel.send("Deci hola mi rey")
            def check(m):
                return m.content == "hola" and m.channel==channel
            msg = await client.wait_for("message", check=check)
            await channel.send("Hola {.author}!".format(msg))
        if mensaje.startswith('reaction'):
            await channel.send('Send me that reaction, mate')

            def check(reaction, user):
                return user == message.author and str(reaction.emoji) == 'gun21'

            try:
                reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await channel.send('not piola')
            else:
                await channel.send('piola')

#################Musica#########################

@client.command("play", help="Musica")
async def bb(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("No estas conectado a un chat de voz.")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('1.m4a')
    player = voice.play(source)

@client.command("stop", help="Musica")
async def cc(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("No estas conectado a un chat de voz.")
        return
    await voice.disconnect()
client.run(token)
