## Librerias#################
import os
import os.path
import random
import discord
import requests
import youtube_dl
import asyncio
import itertools
import mysql.connector
import xml.dom.minidom
import requests as rq
import pycurl
import json
import sys
import traceback
import shutil

from os import path
from os import system
from discord.ext import commands
from dotenv import load_dotenv
from itertools import cycle
from lxml import html
from xml.dom.minidom import parse, parseString
from io import BytesIO
from discord import FFmpegPCMAudio
from discord.utils import get
from discord import opus
from async_timeout import timeout
from functools import partial
from youtube_dl import YoutubeDL

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
YOUTUBE_API = 'AIzaSyAXdLROaC5iXsY5297_wNfDoWtNLfL77Lk'
c=0
count=0
client = commands.Bot(command_prefix='-')
client.remove_command('help')
###################Embed F.A.Q###################
@client.command(name="h")#Se muestra un Embed con los datos para contactar.
async def displayembed(ctx):
    embed = discord.Embed(
        title = "Hola, ¿quien soy?",
        description = "Soy SuguBot, un bot desarrollado para satisfascer\n las necesidades en psicologia crew, mi meta es expandirme lo mas posible y sacarle el mayor provecho a la API de LoL.",
        color = discord.Color.dark_blue()
    )
    embed.set_footer(text="El talento muere cuando no se apuesta.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/587446672741892096/91d0ae1c6da214afe46775b39664c4ee.webp")
    embed.add_field(name="Comandos", value="Escribi -help para conocer mis comandos", inline=False)
    embed.add_field(name="Conoceme", value="https://twitter.com/matiassctt\nhttps://www.instagram.com/matiassctt/", inline=True)
    #embed.add_field(name="Test3", value="test3", inline=True)
    await ctx.send(embed=embed)
    print ("Comando usado: -h")

@client.command(name="perfil")#Se muestra un Embed con los datos del usuario.
async def perfil(ctx, member: discord.Member = None):#Tomas como parametro la tag del usuario
    if member is None:
        member=ctx.message.author
    guild=member.guild#Conseguir el objeto guild
    embed = discord.Embed (colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"Informacion de: {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="Nombre dentro del servidor:", value=member.display_name, inline=False)
    embed.add_field(name="Top rol:", value=member.top_role.mention, inline=True)
    embed.add_field(name="Tu cuenta se creo el:", value=member.created_at.strftime("%#d %B %Y a las %I:%M %p UTC"), inline=True)
    embed.add_field(name=f"Te uniste al servidor el:", value=member.joined_at.strftime("%#d %B %Y a las %I:%M %p UTC"), inline=True)
    embed.add_field(name="¿Sabias qué?", value=random.choice(randomfacts), inline=True)

    await ctx.send(embed=embed)
    print ("Comando usado: Perfil")
###################Database######################


#@client.command(name="inpale")
#async def inpale(ctx):
#    response = "**Bienvenidos a la International Pajas League, los comandos que podes usar son:**\n"
#    response = response + "-listado\n"
#    response = response + "-cantidad **nombre** **mes**"
#    await ctx.send(response)
#@client.command(name="listado")
#async def listado(ctx):
#    res="SELECT * FROM usuarios"
#    mycursor.execute(res)
#    fila=mycursor.fetchall()
#    response = "**Listado de participantes de la INPALE:**\n"
#   for rows in fila:
#        idd=rows[0],
#        nombre=rows[1],
#       idd=str(idd)
#        nombre=str(nombre)
#        idd=idd.replace("(","")
#        idd=idd.replace(")","")
#        idd=idd.replace(",","")
#        nombre=nombre.replace("(","")
#        nombre=nombre.replace(")","")
#        nombre=nombre.replace(",","")
#        nombre=nombre.replace("'","")
#        response = response + idd + " | " + nombre.capitalize() + "\n"
#    await ctx.send(response)

#@client.command(name="cantidad")
#async def cantidad(ctx, usuario, mes):
#    res = 'SELECT SUM(cantidad) FROM pjs, usuarios WHERE pjs.id_usuario=usuarios.id_usuario and usuarios.nombre=%s and pjs.mes=%s'
#    val=(usuario, mes)
#    mycursor.execute(res, val)
#    res = mycursor.fetchall()
#    res = str(res)
#    res=res.replace("[","")
#    res=res.replace("]","")
#    res=res.replace("Decimal","")
#    base.commit()
#    response = "La cantidad de pajas de**", usuario.capitalize(), "**en el mes de**", mes, "**es de**", res, "**pajas"
#    response = str(response)
#    response=response.replace("(","")
#    response=response.replace(")","")
#    response=response.replace(",","")
#    response=response.replace("'","")
#    await ctx.send(response)
    
###################Diccionarios y listas#########################
tetoquotes=[
    "teto.mp4",
    "teto1.jpg",
    "teto2.png",
    "teto3.png",
    "teto4.jpg",
    "teto5.jpg",
    "teto6.jpg",
    "teto7.jpg",
    "teto8.jpg",
    "teto9.jpg",
    "teto10.png",
    "teto11.png",
    "teto12.png",
    "teto13.png",
    "teto14.png",
    "teto15.png",
    "teto16.png",
    "teto17.png",
    "teto18.png",
    "teto19.png",
    "teto20.png",
]
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
    "No puedes lamer tu codo",
    "Te quedan dos intentos",
    "Las mujeres son todas putas menos tu mamá y tu abuela",
]
hug=[
    "https://i.imgur.com/AJqQ98J.gif",
    "https://i.imgur.com/5YSjLqh.gif",
    "https://i.imgur.com/ZqlC168.gif",
    "https://i.imgur.com/rNTB8dI.gif",
    "https://i.imgur.com/Epq7tQp.gif",
    "https://i.imgur.com/c3foH1y.gif",
    "https://i.imgur.com/9BXEODj.gif",
    "https://i.imgur.com/EoxM6xm.gif",
    "https://i.imgur.com/ijn7mSM.gif",
    "https://i.imgur.com/a8aZKqx.gif",
    "https://i.imgur.com/Ci8G0VW.gif",
    "https://i.imgur.com/3HgexQE.gif",
    "https://i.imgur.com/gEMyapQ.gif",
    ]
kiss=[
    "https://i.imgur.com/mT80Tyw.gif",
    "https://i.imgur.com/rEubBR5.gif",
    "https://i.imgur.com/9NU8ee3.gif",
    "https://i.imgur.com/TFIkiML.gif",
    "https://i.imgur.com/LCbPBVK.gif",
    "https://i.imgur.com/1Pgbtxa.gif",
    "https://i.imgur.com/64k6Xqy.gif",
    "https://i.imgur.com/67X3eWE.gif",
    "https://i.imgur.com/NpBXnXR.gif",
    ]
kill=[
    ]
diccionarioRunas={8100: "Dominación", 8112: "Electrocutar", 8124: "Depredador", 8128: "Cosecha Oscura", 9923: "Lluvia de Espadas",#Key rojas
                  8300: "Inspiración", 8351: "Aumento Glacial", 8360: "Libros de Hechizos Abierto", 8358: "Omniruna",#Key celestes
                  8000: "Precisión", 8005: "Estrategia Ofensiva", 8008: "Cadencia Letal", 8021: "Sobre la Marcha", 8010: "Conquistador", #Key amarillas
                  8400: "Valor", 8437: "Agarre del Perpetuo", 8439: "Réplica", 8465: "Guardián",#Key verdes
                  8200: "Brujería", 8214: "Invocacíon: Aery", 8229: "Cometa Arcano", 8230: "Fase Veloz"#key Azules
                  }

diccionarioHechizos={21: "Barrera", 1: "Purificación", 14: "Ignición", 3: "Extenuación", 4: "Destello", 6: "Fantasma", 7: "Curación", 13: "Claridad", 11: "Castigo", 12: "Teleportación",#Normales
                     30: "¡Por el Rey!", 31: "Disporo", 39: "Marca", 32: "Marca"#Gamemodes
                     }

diccionarioCampeones={266: "Aatrox", 103: "Ahri", 84: "Akali", 12: "Alistar", 32: "Amumu", 34: "Anivia", 1: "Annie", 523: "Aphelios", 22: "Ashe", 136: "Aurelion Sol",
                      268: "Azir", 432: "Bardo", 53: "Blitzcrank", 63: "Brand", 201: "Braum", 51: "Caitlyn", 164: "Camille", 69: "Cassiopeia", 31: "Cho'Gath",
                      42: "Corki", 122: "Darius", 131: "Diana", 119: "Draven", 36: "Dr. Mundo", 245: "Ekko", 60: "Elise", 28: "Evelynn", 81: "Ezreal", 9: "Fiddlestick",
                      114: "Fiora", 105: "Fizz", 3: "Galio", 41: "Gangplank", 86: "Garen", 150: "Gnar", 79: "Gragas", 104: "Graves", 120: "Hecarim", 74: "Heimerdinger",
                      420: "Illaoi", 39: "Irelia", 427: "Ivern", 40: "Janna", 59: "Jarvan IV", 24: "Jax", 126: "Jayce", 202: "Jhin", 222: "Jinx", 38: "Kassasin", 145: "Kai'sa",
                      429: "Kalista", 43: "Karma", 30: "Karthus", 55: "Katarina", 10: "Kayle", 141: "Kayn", 85: "Kennen", 121: "Kha'Zix", 203: "Kindred", 240: "Kled",
                      96: "Kog'Maw", 7: "LeBlanc", 64: "Lee Sin", 89: "Leona", 127: "Lissandra", 236: "Lucian", 117: "Lulu", 99: "Lux", 54: "Malphite", 90: "Malzahar",
                      57: "Maokai", 11: "Maestro Yi", 21: "Miss Fortune", 62: "Wukong", 82: "Mordekaiser", 25: "Morgana", 267: "Nami", 75: "Nasus", 111: "Nautilus",
                      518: "Neeko", 76: "Nidalee", 56: "Noctune", 20: "Nunu y Willump", 2: "Olaf", 61: "Orianna", 516: "Ornn", 80: "Pantheon", 78: "Poppy", 555: "Pyke",
                      246: "Qiyana", 133: "Quinn", 497: "Rakan", 33: "Rammus", 421: "Rek'Sai", 58: "Renekton", 107: "Rengar", 92: "Riven", 68: "Rumble", 13: "Ryze",
                      113: "Sejuani", 235: "Senna", 875: "Sett", 35: "Shaco", 98: "Shen", 102: "Shyvana", 27: "Singed", 14: "Sion", 15: "Sivir", 72: "Skarner", 37: "Sona",
                      16: "Soraka", 50: "Swain", 517: "Sylas", 134: "Syndra", 223: "Tahm Kench", 163: "Taliyah", 91: "Talon", 44: "Taric", 17: "Teemo", 412: "Thresh",
                      18: "Tristana", 48: "Trundle", 23: "Tryndamere", 4: "Twisted Fate", 29: "Twitch", 77: "Udyr", 6: "Urgot", 110: "Varus", 67: "Vayne", 45: "Veigar",
                      161: "Vel'Koz", 254: "Vi", 112: "Viktor", 8: "Vladimir", 106: "Volibear", 19: "Warwick", 498: "Xayah", 101: "Xerath", 5: "Xin Zhao", 157: "Yasuo",
                      83: "Yorick", 350: "Yuumi", 154: "Zac", 238: "Zed", 115: "Ziggs", 26: "Zilean", 142: "Zoe", 143: "Zyra"
                    }
parametros = ()      
###############Vault#####################    
@client.command(name="vaultsave", help="Guarda una imagen, nombre y despues url")
async def vaultsave(ctx, nombre, url):
    directorio = str(ctx.guild.id)
    img_data = requests.get(url).content
    validacion=str(url)[-3:]
    c=0
    verify = str(path.isdir(directorio))
    if verify=="True":
        if validacion=="gif":
            nombre=nombre+"gif"
            a = open(directorio+"/"+"gif.txt", "r")
            for x in a:
                x=x.strip()
                if nombre==x:
                      c=c+1
            if c>=1:
                response="El nombre de esa imagen ya existe, usa otro o mira la lista, pelotudo."
                await ctx.send(response)
            else:         
                with open(directorio+"/"+nombre+".gif", 'wb') as handler:
                    handler.write(img_data)
                    g = open(directorio+"/"+"gif.txt","a+")
                    g.write(nombre+"\n")
                    g.close()
                    response="Registro agregado correctamente"
                await ctx.send(response)
        if validacion=="jpg" or validacion=="png" or validacion=="jpeg":
            b = open(directorio+"/"+"imagenes.txt", "r")
            for x in b:
                x=x.strip()
                if nombre==x:
                      c=c+1
            if c>=1:
                response="El nombre de esa imagen ya existe, usa otro o mira la lista, pelotudo."
                await ctx.send(response)
            else:         
                with open(directorio+"/"+nombre+".jpg", 'wb') as handler:
                    handler.write(img_data)
                    f = open(directorio+"/"+"imagenes.txt","a+")
                    f.write(nombre+"\n")
                    f.close()
                    response="Registro agregado correctamente"
                await ctx.send(response)
    if verify=="False":
        os.mkdir(directorio)
        file = open(directorio+"/"+"imagenes.txt", "w")
        file.close()
        file = open(directorio+"/"+"gif.txt", "w")
        file.close()
        response = "Parece que es la primera vez que tu servidor usaba nuestro Vault! Por eso tuvimos que usar esta primera vez para crear un directorio para que tus imagenes no se pierdan, por favor volve a subir tu primera imagen o gif :)"
        await ctx.send(response)

    print ("Comando usado: Vaultsave")
@client.command(name="vaultsend", help="Envia una imagen")
async def vaultsend(ctx, nombre):
    directorio = ctx.guild.id
    validacion=nombre[-3:]
    validacion.lower()
    if validacion=="gif":
        await ctx.send(file=discord.File(str(directorio)+"/"+nombre+".gif"))
    else:
        await ctx.send(file=discord.File(str(directorio)+"/"+nombre+".jpg"))
    print ("Comando usado: Vaultsend")

@client.command(name="vaultlist", help="Lista del vault")
async def vaultlist(ctx):
    directorio = ctx.guild.id
    nombre = ctx.guild
    f = open(str(directorio)+"/"+"imagenes.txt","r")
    contents = "**Listado de archivos para "+str(nombre)+"**\n"
    contents = contents + "**Listado de imagenes:\n**"
    d = f.readlines()
    for i in d:
        i=i.replace("\n", "")
        if i!=" " or h!="":
            i=i+"\n"
            contents = contents + i
    f.close()
    g = open(str(directorio)+"/"+"gif.txt", "r")
    contentsG = "\n**Listado de gifs:\n**"
    j = g.readlines()
    for h in j:
        h=h.replace("\n", "")
        if h!=" " or h!="":
            h=h+"\n"
            contentsG = contentsG + h
    contents = contents + contentsG
    await ctx.send(contents)
    print ("Comando usado: Vaultlist")

@client.command(name="vaultdelete", help="Borra una imagen")
async def vaultdelete(ctx): #agregar nombre cuando vuelva a funcionar
    quote = [
    'El delete ahora mismo no está funcionando, llamalo a Mati para que borre la imagen manualmente'
    ]

    response = random.choice(quote)
    await ctx.send(response)
    print ("Comando usado: Vaultdelete")
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
    print ("Comando usado: Coin")

@client.command(name='8ball', help='8ball')
async def ball(ctx):
    caracruz = [
        'Yo, el bot de la razón absoluta, te digo que **sí**',
        'Yo, el bot de la razón absoluta, te digo que **no**',
    ]

    response = random.choice(caracruz)
    await ctx.send(response)
    print ("Comando usado: 8ball")
    
@client.command(name='8BALL', help='8ball')
async def ball(ctx):
    caracruz = [
        'Yo, el bot de la razón absoluta, te digo que **sí**',
        'Yo, el bot de la razón absoluta, te digo que **no**',
    ]

    response = random.choice(caracruz)
    await ctx.send(response)
    print ("Comando usado: 8ball")
    
@client.command(name="pick", help="Pick")
async def pick(ctx, *parametros):
    lista=[]
    lista.clear()
    for x in (str(len(parametros))):
        lista.append(parametros)
    response = random.choice(parametros)
    response="Yo, el bot de la razon absoluta elijo a **"+response+"**"
    await ctx.send(response)
    print ("Comando usado: Pick")
"""
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
    print ("Comando usado: Select")
"""
#################League of legends##########################

@client.command(name="lol", help="Partida de LoL, solo nombre")
async def lol(ctx, nombre, region="la2"):
    info=conseguir_info_usuario(nombre)
    idd=info["id"]
    body = llamar_curl("https://"+region+".api.riotgames.com/lol/spectator/v4/active-games/by-summoner/"+idd)
    body = json.loads(body)
    acu=""
    try:
        body = body["status"]["status_code"]
    except:
        body = body

    if body==404:
        acu = "El usuario no se encuentra en partida :("
    else:
        acu = "Partida del usuario: **"+ nombre+"**\n\n"
        for x in range (0, 10):
            if body["participants"][x]["teamId"]==100:
                equipo = "Azul"
            else:
                equipo = "Rojo"
                
            nombres = body["participants"][x]["summonerName"]
            campeon = body["participants"][x]["championId"]
            spell1 = body["participants"][x]["spell2Id"]
            spell2 = body["participants"][x]["spell1Id"]
            for k,v in diccionarioRunas.items():
                if body["participants"][x]["perks"]["perkSubStyle"]==k:
                    runasecundarias = v
                if body["participants"][x]["perks"]["perkIds"][0]==k:
                    keyrune = v
            for s, n in diccionarioHechizos.items():
                if spell1==s:
                    spell1=n
                if spell2==s:
                    spell2=n
            for a, b in diccionarioCampeones.items():
                if campeon==a:
                    campeon=b
                #if banned==a:
                    #banned=b
            if x==5:
                xd = "\n"+equipo+" | "+str(nombres)+" | "+str(campeon)+" | "+str(spell1)+" y "+str(spell2)+" | "+str(keyrune)+" con "+str(runasecundarias)+"\n"
                acu = acu+xd
            else:
                xd = equipo+" | "+str(nombres)+" | "+str(campeon)+" | "+str(spell1)+" y "+str(spell2)+" | "+str(keyrune)+" con "+str(runasecundarias)+"\n"
                acu = acu+xd
        url="https://porofessor.gg/live/las/"+nombre
        acu=acu + "\nPodes ver mas de la partida en: " + url
    await ctx.send(acu)
    print ("Comando usado: LoL")

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
    print ("Comando usado: Loltier")

@client.command(name="ugg", help="Champion de lol, nombre")
async def ugg(ctx, nombre):
    nombre=nombre.lower()
    url="https://u.gg/lol/champions/"
    nombre.replace(" ", "_")
    response=url+nombre+"/build"
    await ctx.send(response)
    print ("Comando usado: Ugg")

@client.command(name="profile", help="Perfil de lol, nombre y region.")
async def profile(ctx, nombre, region="la2"):
    if region=="na1":
        url="https://na.op.gg/summoner/userName="+nombre
    if region=="la1":
        url="https://lan.op.gg/summoner/userName="+nombre
    if region=="la2":
        url="https://las.op.gg/summoner/userName="+nombre
    if region!="na1" and region!="la1" and region !="la2":
        await ctx.send("Lo siento :( las unicas regiones programadas son na1, la1 y la2")
        return 
    info=info_ligas(nombre, region)
    infousuario=conseguir_info_usuario(nombre, region)
    icon=infousuario["profileIconId"]
    nivel=infousuario["summonerLevel"]
    acu=""
    maestrias=conseguir_maestrias(nombre)
    imagen="https://ddragon.leagueoflegends.com/cdn/10.4.1/img/profileicon/"+str(icon)+".png"
    for x in range (0,3):
        puntos=maestrias[x]["championPoints"]
        campeon=maestrias[x]["championId"]
        nivelm=maestrias[x]["championLevel"]
        for a, b in diccionarioCampeones.items():
            if campeon==a:
                campeon=b
        xd = str(campeon) + " | " + str(puntos) + " | Nivel: " + str(nivelm)+"\n"
        acu = acu + xd
    try:
        queue=info[0]["queueType"]
        c=0
        for x in info:
            if info[c]["queueType"]!="RANKED_FLEX_5x5":
                wins = info[c]["wins"]
                losses = info[c]["losses"]
                tier = info[c]["tier"]
                lp = info[c]["leaguePoints"]
                rank = info[c]["rank"]
                try:
                    promo = info[c]["miniSeries"]["progress"]
                except:
                    promo = "Este jugador no esta en promo"
            c=c+1
        embed = discord.Embed(
            title = f"Perfil de {nombre}",
            description=f"Podes ver mas de tu informacion en {url}",
            color = discord.Color.dark_blue()
        )
        #embed.set_author(name=f"Informacion de: {nombre}")
        embed.set_thumbnail(url=imagen)
        embed.set_footer(text=f"Gracias a Riot por prestarme su API.")
        total=wins+losses
        winr=(wins/total)*100
        embed.add_field(name="Liga", value=tier+" "+rank, inline=True)
        embed.add_field(name="Puntos", value=lp, inline=True)
        embed.add_field(name="Promos:", value=promo, inline=True)
        embed.add_field(name="Total de partidas", value=total, inline=True)
        embed.add_field(name="Win", value=wins, inline=True)
        embed.add_field(name="Losses", value=losses, inline=True)
        embed.add_field(name="Winrate", value=winr, inline=True)
        embed.add_field(name="Nivel", value=nivel, inline=True)
        embed.add_field(name="Maestrias:", value=acu, inline=True)
        embed.add_field(name="¿Sabias qué?", value=random.choice(randomfacts), inline=False)
    except:
        embed = discord.Embed(
            title = f"Perfil de {nombre}",
            description=f"Podes ver mas de tu informacion en {url}",
            color = discord.Color.dark_blue()
        )
        #embed.set_author(name=f"Informacion de: {nombre}")
        embed.set_thumbnail(url=imagen)
        embed.set_footer(text=f"Gracias a Riot por prestarme su API.")

        embed.add_field(name="Liga", value="Este usuario es unranked", inline=True)
        embed.add_field(name="Nivel", value=nivel, inline=True)
        embed.add_field(name="Maestrias:", value=acu, inline=False)
        embed.add_field(name="¿Sabias qué?", value=random.choice(randomfacts), inline=True)
        
    await ctx.send(embed=embed)
    print ("Comando usado: Profile")


def conseguir_maestria(nombre="ramirorat",campeon="Aatrox", region="la2"):#championPoints, championLevel
    info=conseguir_info_usuario(nombre)
    idd=info["id"]
    for campeonid, campeonnombre in diccionarioCampeones.items():
        if campeonnombre==campeon:
            body = llamar_curl('https://'+region+'.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/'+idd+'/by-champion/'+str(campeonid))
    body = json.loads(body)
    return body

def conseguir_maestrias(nombre="hyejooist", region="la2"):
    info=conseguir_info_usuario(nombre)
    idd=info["id"]
    body = llamar_curl('https://'+region+'.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/'+idd)
    body = json.loads(body)
    return body
def info_ligas(nombre="Hyejooist", region="la2"):#tier, rank, queueType, leaguePoints, wins, losses, miniSeries
    info=conseguir_info_usuario(nombre)
    idd=info["id"]
    body = llamar_curl("https://"+region+".api.riotgames.com/lol/league/v4/entries/by-summoner/"+idd)
    body = json.loads(body)
    return body

def llamar_curl(url):
    
    b_obj = BytesIO() 
    curl = pycurl.Curl()
    
    api="?api_key=RGAPI-ec5c4b44-5d4e-4e66-a93b-35ab7f761815"
    
    curl.setopt(curl.URL, url+api)
    curl.setopt(curl.WRITEDATA, b_obj)
    curl.setopt(curl.SSL_VERIFYPEER, 0) 
    curl.perform() 
    curl.close()
     
    get_body = b_obj.getvalue()

    return get_body

def conseguir_info_usuario(nombre="Equus", region="la2"):#id, accountId, puuid, profileIconId, summonerLevel
    nombre = nombre.replace(" ", "_")
    body = llamar_curl("https://"+region+".api.riotgames.com/lol/summoner/v4/summoners/by-name/"+nombre)
    body = json.loads(body)
    return body
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
    print ("Comando usado: Calc")



@client.command(name="avatar", help="Muestra el avatar de un usuario", aliases=["av", "a"])
async def avatar(ctx, member: discord.Member = None):
    if member is None:
        member=ctx.message.author
    avatar=discord.Embed(
        colour=member.color,
        title = f" Avatar de {member.name}",
    )
    avatar.set_image(url='{}'.format(member.avatar_url))
    #avatar.set_footer(text=f'Bastante feo e')
    await ctx.send(embed=avatar)
    print ("Comando usado: Avatar")


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
    mensaje = message.content
    if channel.guild.id==186958407264108544:
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
            if mensaje == "eze":
                await channel.send("COGETE A PABLI")
    if mensaje == "test":
        response = random.choice(testquotes)
        await channel.send(response)
    if mensaje == "teto":
        response=random.choice(tetoquotes)
        await channel.send(file=discord.File("teto/"+response))
    if mensaje == "sugu":
        response=random.choice(suguquotes)
        await channel.send(file=discord.File("sugu/"+response))
    await client.process_commands(message)
        #if mensaje.startswith("hola bro"):
            #await channel.send("Deci hola mi rey")
            #def check(m):
                #return m.content == "hola" and m.channel==channel
            #msg =# await client.wait_for("message", check=check)
            #await channel.send("Hola {.author}!".format(msg))
        #if mensaje.startswith('reaction'):
        #    await channel.send('Send me that reaction, mate')
        #
        #    def check(reaction, user):
        #        return user == message.author and str(reaction.emoji) == 'gun21'
        #
        #   try:
        #        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        #    except asyncio.TimeoutError:
        #        await channel.send('not piola')
        #    else:
        #        await channel.send('piola')

#################Mariconadas#########################
@client.command(name="hug")
async def hug(ctx, member: discord.Member = None):
    if member is None:
        await (ctx.send("¡Menciona a alguien para abrazarlo!"))
        return
    avatar=discord.Embed(
        colour=member.color,
        title = f" {ctx.message.author.name.capitalize()} abrazo a {member.name.capitalize()}",
    )
    url=random.choice(hug)
    avatar.set_image(url='{}'.format(url))
    await (ctx.send(embed=avatar))
    print ("Comando usado: hug")
    
@client.command(name="kiss")
async def kiss(ctx, member: discord.Member = None):
    if member is None:
        await (ctx.send("¡Menciona a alguien para besarlo!"))
        return
    avatar=discord.Embed(
        colour=member.color,
        title = f" {ctx.message.author.name.capitalize()} beso a {member.name.capitalize()}",
    )
    url=random.choice(kiss)
    avatar.set_image(url='{}'.format(url))
    await (ctx.send(embed=avatar))
    print ("Comando usado: kiss")

#################Musica#########################
#OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll','libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

#def load_opus_lib(opus_libs=OPUS_LIBS):
#    if opus.is_loaded():
#        print ("a")
#        return True
#        
#
#    for opus_lib in opus_libs:
#            try:
#                opus.load_opus(opus_lib)
#                print ("aa")
#                return
#            except OSError:
#                print ("bb")
#                pass

#    raise RuntimeError('Could not load an opus lib. Tried %s' %(', '.join(opus_libs)))
#load_opus_lib()

@client.command(name="reset")
async def reset(ctx):
    if ctx.message.author.id==186955944410742785:
        os.remove("song.mp3")
        await ctx.send("Musica reiniciada")
    else:
        await ctx.send("Este comando solo lo puede usar Mati, tagealo")
@client.command(name="join", pass_context=True, aliases=["j"])
async def join(ctx):
	global voice
	channel = ctx.message.author.voice.channel
	voice = get (client.voice_clients, guild=ctx.guild)

	if voice and voice.is_connected():
	    await voice.move_to(channel)
	else:
	    voice = await channel.connect()

	await ctx.send(f"Unido a {channel}")

@client.command(name="leave", pass_context=True, aliases=["l"])
async def leave(ctx):
	channel = ctx.message.author.voice.channel
	voice= get(client.voice_clients, guild=ctx.guild)

	if voice and voice.is_connected():
		await voice.disconnect()
		await ctx.send(f"Me fui de {channel}")
	else:
		await ctx.send("No creo estar en un canal de voz :(")

@client.command(name="init", pass_context=True, aliases=['i', 'ini'])
async def play(ctx, url: str):
    await join(ctx)
    def check_queue():
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_q = length - 1
            try:
                first_file = os.listdir(DIR)[0]
            except:
                print("No more queued song(s)\n")
                queues.clear()
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
            if length != 0:
                print("Song done, playing next queued\n")
                print(f"Songs still in queue: {still_q}")
                song_there = os.path.isfile("song.mp3")
                if song_there:
                    os.remove("song.mp3")
                shutil.move(song_path, main_location)
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, 'song.mp3')

                voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.07

            else:
                queues.clear()
                return

        else:
            queues.clear()
            print("No songs were queued before the ending of the last song\n")



    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            queues.clear()
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("Bro..ya tengo musica en otro server :( pero si sos del mismo server tirame mas temazos con -q!")
        return


    Queue_infile = os.path.isdir("./Queue")
    try:
        Queue_folder = "./Queue"
        if Queue_infile is True:
            print("Removed old Queue Folder")
            shutil.rmtree(Queue_folder)
    except:
        print("No old Queue folder")

    await ctx.send("Amigo, te pido por favor que me esperes porque soy un botsito nuevo y me cuesta una bocha")

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([url])
    except:
        print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
        c_path = os.path.dirname(os.path.realpath(__file__))
        system("spotdl -f " + '"' + c_path + '"' + " -s " + url)

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07
    print("playing\n")


@client.command(name="pause", pass_context=True, aliases=['pa', 'pau'])
async def pause(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music paused")
        voice.pause()
        await ctx.send("Musica pausada mis reyes")
    else:
        print("Music not playing failed pause")
        await ctx.send("No tenemos musica p pausar :(")


@client.command(name="resume", pass_context=True, aliases=['r', 'res'])
async def resume(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Resumed music")
        voice.resume()
        await ctx.send("R E S U M I D AAAAAAAA")
    else:
        print("Music is not paused")
        await ctx.send("La musica no esta pausada")


@client.command(name="stop", pass_context=True, aliases=['sto'])
async def stop(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music stopped")
        voice.stop()
        await ctx.send("Stopeadoscu")
    else:
        print("No music playing failed to stop")
        await ctx.send("No hay musica para stoppear")

queues = {}

@client.command(name="play", pass_context=True, aliases=['p', 'pla'])
async def queue(ctx, url: str):
    Queue_infile = os.path.isdir("./Queue")
    if Queue_infile is False:
        os.mkdir("Queue")
    DIR = os.path.abspath(os.path.realpath("Queue"))
    q_num = len(os.listdir(DIR))
    q_num += 1
    add_queue = True
    while add_queue:
        if q_num in queues:
            q_num += 1
        else:
            add_queue = False
            queues[q_num] = q_num

    queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song{q_num}.%(ext)s")

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'outtmpl': queue_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([url])
    except:
        print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
        q_path = os.path.abspath(os.path.realpath("Queue"))
        system(f"spotdl -ff song{q_num} -f " + '"' + q_path + '"' + " -s " + url)


    await ctx.send("Agregado ese temazo a la queue")
    print (queues)
    print("Song added to queue\n")



@client.command(name="skip", pass_context=True, aliases=['s', 'sk'])
async def next(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Playing Next Song")
        voice.stop()
        await ctx.send("Mal ahi salteando")
    else:
        print("No music playing")
        await ctx.send("No hay musica p skipear")
#############Help#############
@client.command(name="help", pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        title = "¡Mis comandos!",
        color = discord.Color.dark_blue(),
        description = "Podes encontrar informacion mas detallada en {ponermipaginaaca}"
    )
    embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="League of Legends:", value="**-lol**, **-ugg**, **-profile**, **-loltier** ", inline=False)
    embed.add_field(name="Vault:", value="**-vaultlist**, **-vaultsend**, **-vaultsave**, **-vaultdelete** ", inline=False)
    embed.add_field(name="Musica:", value="**-join**, **-init**, **-play**, **-skip**, **-pause**, **-resume**, **-stop**, **-leave**", inline=False)
    embed.add_field(name="Informacion:", value="**-avatar**, **-perfil**", inline=False)
    embed.add_field(name="Ocio:", value="**-8ball**, **-coin**, **-pick**, **-hug**, **-kill**, **-kiss**, **-calc**, **-tusa**, **-cancion**", inline=False)
    embed.add_field(name="Eventos on_message:", value="**teto**", inline=False)
    embed.add_field(name="Moderacion:", value="**-prune**", inline=False)
    embed.add_field(name="Mati:", value="**-reset**, **-status**", inline=False)

    await ctx.send(embed=embed)

@client.command(name="status")
async def status(ctx, msj="status"):
    if ctx.message.author.id==186955944410742785:
        if msj=="status":
            await client.change_presence(activity=discord.Game(name='-h, Ayudando a '+str(len(client.guilds))+' servidores | Conectado con '+str(len(set(client.get_all_members())))+' usuarios'))
        elif msj!="status":
            await client.change_presence(activity=discord.Game(name=msj))
    else:
        await ctx.send("Solo Mati puede cambiar el status del bot")
            
client.run(token)
