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
import sqlite3
import urllib.parse, urllib.request, re

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
token = "Aca va tu token"
YOUTUBE_API = 'Aca va tu API de yt'
c=0
count=0
client = commands.Bot(command_prefix='/')
client.remove_command('help')
DIR = os.path.dirname(__file__)
db = sqlite3.connect(os.path.join(DIR, "SongTracker.db"))  # connecting to DB if this file is not there it will create it
SQL = db.cursor()
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

###################Embed F.A.Q###################
@client.command(name="h")#Se muestra un Embed con los datos para contactar.
async def displayembed(ctx):
    embed = discord.Embed(
        title = "Hola, ¿quien soy?",
        description = "Soy SuguBot, un bot desarrollado para satisfascer\n las necesidades en psicologia crew, mi meta es expandirme lo mas posible y sacarle el mayor provecho a la API de LoL.",
        color = discord.Color.dark_blue()
    )
    embed.set_footer(text="El talento muere cuando no se apuesta.")
    embed.set_thumbnail(url="https://i.imgur.com/E2jPb6o.png")
    embed.add_field(name="Comandos", value="Podes ver todos mis comandos y sus funcionalidades en https://sugubot.000webhostapp.com/ !", inline=False)
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
    embed.add_field(name="¿Sabias qué?", value=random.choice(facts), inline=True)

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
    "teto21.png",
    "teto22.png",
    "teto23.png",
    "teto24.png",
    "teto25.png",
    "teto26.png",
]
suguquotes=[
    "sugu1.png",
    "sugu2.png",
    "sugu3.png",
    "sugu4.jpg",
    "sugu5.png",
    "sugu6.png",
    "sugu7.jpg",
    "sugu8.jpg",
    "sugu9.png",
    "sugu10.png",
    "sugu11.png",
    "sugu12.png",
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
facts=[
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
dsa=[
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
asd=[
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

@client.command(name="random")
async def randomfacts(ctx):
    response = random.choice(facts)
    await ctx.send(response)
    print ("Comando usado: random")

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
        total=wins+losses
        winr=(wins/total)*100
        embed = discord.Embed(
            title = f"Perfil de {nombre}",
            description=f"Podes ver mas de tu informacion en {url}",
            color = discord.Color.dark_blue()
        )
        #embed.set_author(name=f"Informacion de: {nombre}")
        embed.set_thumbnail(url=imagen)
        embed.set_footer(text=f"Gracias a Riot por prestarme su API.")
        embed.add_field(name="Liga", value=tier+" "+rank, inline=True)
        embed.add_field(name="Puntos", value=lp, inline=True)
        embed.add_field(name="Promos:", value=promo, inline=True)
        embed.add_field(name="Total de partidas", value=total, inline=True)
        embed.add_field(name="Win", value=wins, inline=True)
        embed.add_field(name="Losses", value=losses, inline=True)
        embed.add_field(name="Winrate", value=winr, inline=True)
        embed.add_field(name="Nivel", value=nivel, inline=True)
        embed.add_field(name="Maestrias:", value=acu, inline=True)
        embed.add_field(name="¿Sabias qué?", value=random.choice(facts), inline=False)
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
        embed.add_field(name="¿Sabias qué?", value=random.choice(facts), inline=True)
        
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
            if mensaje == ":mati:":
                await channel.send(":mati:")
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
    url=random.choice(dsa)
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
    url=random.choice(asd)
    avatar.set_image(url='{}'.format(url))
    await ctx.send(embed=avatar)
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
        filelist = [ f for f in os.listdir(mydir) if f.endswith(".mp3") ]
        for f in filelist:
            os.remove(os.path.join(mydir, f))
        await ctx.send("Musica reiniciada")
    else:
        await ctx.send("Este comando solo lo puede usar Mati, tagealo")

@client.command(name="join", pass_context=True, aliases=["j"])
async def join(ctx):

    ##################################################################

    '''
    if you would like to take a look at the database and the table please download: https://sqlitebrowser.org/dl/
    In the first section of the join command we first use SQLite to make us a table in our database that we have connected to above
    we use the statement 'create table if not exists' this creates the table if one by the name specified does not exist
    We create the table Music with columns that we populate right away with when you use the join command in a server
    it gets the Server ID, Sever name, voice channel id, voice channel name, user that used the join command, what postition in the queue we are (starts at one),
    generates queue folder name, and generates the song file name
    then the last thing we do is assign those variables to each column and then create a new row with that info
    then we use db.commit() to write these changes we are making ot the database (basically a save command)
    '''

    SQL.execute('create table if not exists Music('
                '"Num" integer not null primary key autoincrement, '
                '"Server_ID" integer, '
                '"Server_Name" text, '
                '"Voice_ID" integer, '
                '"Voice_Name" text, '
                '"User_Name" text, '
                '"Next_Queue" integer, '
                '"Queue_Name" text, '
                '"Song_Name" text'
                ')')
    server_name = str(ctx.guild)
    server_id = ctx.guild.id
    SQL.execute(f'delete from music where Server_ID ="{server_id}" and Server_Name = "{server_name}"')
    db.commit()
    user_name = str(ctx.message.author)
    queue_name = f"Queue#{server_id}"
    song_name = f"Song#{server_id}"
    channel_id = ctx.message.author.voice.channel.id
    channel_name = str(ctx.message.author.voice.channel)
    queue_num = 1
    SQL.execute('insert into Music(Server_ID, Server_Name, Voice_ID, Voice_Name, User_Name, Next_Queue, Queue_Name, Song_Name) values(?,?,?,?,?,?,?,?)',
                (server_id, server_name, channel_id, channel_name, user_name, queue_num, queue_name, song_name))
    db.commit()

    ##################################################################

    '''
    This is basic join command
    '''

    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice is not None:
        return await voice.move_to(channel)

    await channel.connect()
    channel = str(channel)
    channel = channel.translate(non_bmp_map)

    print(f"The client has joined {channel}")

    await ctx.send(f"Me uni a {channel}")


@client.command(pass_context=True)
async def test(ctx):
    id = ctx.guild
    id_hash = hash(id)
    user_name = str(ctx.message.author)
    print(ctx.guild.id)


@client.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):

    ##################################################################

    '''
    In the first section of the leave command we are setting variables to the server name, server id, voice channel name, and voice channel id
    then we use SQL to look for rows that match all four of those variables and delete it we are doing this because we don't want to
    create multiple rows for one server we want to keep each server to only be able to populate one row in the DB
    '''

    server_name = str(ctx.guild)
    server_id = ctx.guild.id
    channel_id = ctx.message.author.voice.channel.id
    channel_name = str(ctx.message.author.voice.channel)
    SQL.execute(f'delete from music where Server_ID ="{server_id}" and Server_Name = "{server_name}" and Voice_ID="{channel_id}" and Voice_Name="{channel_name}"')
    db.commit()

    ##################################################################

    '''
    This is basic leave 
    '''

    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        channel = str(channel)
        channel = channel.translate(non_bmp_map)
        print(f"The client has left {channel}")
        await ctx.send(f"Me fui de {channel}")
    else:
        print("client was told to leave voice channel, but was not in one")
        await ctx.send("No creo estar en un canal de voz :(")


@client.command(pass_context=True, aliases=['i', 'ini'])
async def init(ctx, *url: str):

    ##################################################################

    '''
    In the first section of the play command
    We are doing like above command setting variables to info about the server the command is used in
    Then we are using SQl to select the generated song file name that matches with the server info so we can keep the song file names different
    name_song = SQL.fetchone() this is used to set the variabe name_song to what the SQL command returns
    This need a try block because if someone uses /play before ever having the client join a voice channel the server will not have a row in the DB
    So it will return an error we use the try block and if that happens we tell the user what went wrong

    '''
    await join(ctx)
    server_name = str(ctx.guild)
    server_id = ctx.guild.id
    channel_id = ctx.message.author.voice.channel.id
    channel_name = str(ctx.message.author.voice.channel)
    try:
        SQL.execute(f'select Song_Name from Music where Server_ID="{server_id}" and Server_Name="{server_name}" and Voice_ID="{channel_id}" and Voice_Name="{channel_name}"')
        name_song = SQL.fetchone()
        SQL.execute(f'select Server_Name from Music where Server_ID="{server_id}" and Server_Name="{server_name}"')
        name_server = SQL.fetchone()
    except:
        await ctx.send("¡Metete a un canal de voz con -j!")
        return

    ##################################################################

    '''
    in the second section of the play command we have the Check queue function changes inside
    '''

    def check_queue():

        ##################################################################

        '''
        Setting variables to info about the server and setting DIR to the current path of the main client path
        and we are getting the name of the queue folder
        '''

        DIR = os.path.dirname(__file__)
        db = sqlite3.connect(os.path.join(DIR, "SongTracker.db"))
        SQL = db.cursor()
        SQL.execute(f'select Queue_Name from Music where Server_ID="{server_id}" and Server_Name="{server_name}"')
        name_queue = SQL.fetchone()
        SQL.execute(f'select Server_Name from Music where Server_ID="{server_id}" and Server_Name="{server_name}"')
        name_server = SQL.fetchone()

        ##################################################################

        '''
        First check to see if there even is a queues folder then we check for a generated queue folder inside of the queues folder
        after that we list that directory getting the first song file inside of it
        '''

        Queue_infile = os.path.isdir("./Queues")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queues"))
            Queue_Main = os.path.join(DIR, name_queue[0])
            length = len(os.listdir(Queue_Main))
            still_q = length - 1
            try:
                first_file = os.listdir(Queue_Main)[0]

                song_num = first_file.split('-')[0]
            except:
                print("No more queued song(s)\n")
                SQL.execute('update Music set Next_Queue = 1 where Server_ID = ? and Server_Name = ?', (server_id, server_name))
                db.commit()
                return

            ##################################################################

            '''
            We are now moving the song file gotten above out of the queues folders and then renaming based on the number at the start of the song file name 
            '''

            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath(Queue_Main) + "\\" + first_file)
            if length != 0:
                print("Song done, playing next queued\n")
                print(f"Songs still in queue: {still_q}")
                song_there = os.path.isfile(f"{name_song[0]}({name_server[0]}).mp3")
                if song_there:
                    os.remove(f"{name_song[0]}({name_server[0]}).mp3")
                shutil.move(song_path, main_location)
                for file in os.listdir("./"):
                    if file == f"{song_num}-{name_song[0]}({name_server[0]}).mp3":
                        os.rename(file, f'{name_song[0]}({name_server[0]}).mp3')

                ##################################################################

                voice.play(discord.FFmpegPCMAudio(f'{name_song[0]}({name_server[0]}).mp3'), after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.25

            else:
                SQL.execute('update Music set Next_Queue = 1 where Server_ID = ? and Server_Name = ?', (server_id, server_name))
                db.commit()
                return

        else:
            SQL.execute('update Music set Next_Queue = 1 where Server_ID = ? and Server_Name = ?', (server_id, server_name))
            db.commit()
            print("No songs were queued before the ending of the last song\n")

    ##################################################################

    '''
    In the third section of the play command
    we check for an old song file with the same name as before and delete it
    '''

    song_there = os.path.isfile(f"{name_song[0]}({name_server[0]}).mp3")
    try:
        if song_there:
            os.remove(f"{name_song[0]}({name_server[0]}).mp3")
            SQL.execute('update Music set Next_Queue = 1 where Server_ID = ? and Server_Name = ?', (server_id, server_name))
            db.commit()
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("¡Ya estas escuchando musica! Pone -p para agregar mas canciones a la queue")
        return

    ##################################################################

    '''
    In the fourth section of the play command
    we check for a queue folder inside of the queues folder with the same name as last time then delete it
    '''

    SQL.execute(f'select Queue_Name from Music where Server_ID="{server_id}" and Server_Name="{server_name}"')
    name_queue = SQL.fetchone()
    queue_infile = os.path.isdir("./Queues")
    if queue_infile is True:
        DIR = os.path.abspath(os.path.realpath("Queues"))
        Queue_Main = os.path.join(DIR, name_queue[0])
        Queue_Main_infile = os.path.isdir(Queue_Main)
        if Queue_Main_infile is True:
            print("Removed old queue folder")
            shutil.rmtree(Queue_Main)

    ##################################################################

    await ctx.send("Amigo, te pido por favor que me esperes porque soy un botsito nuevo y me cuesta una bocha")

    ##################################################################

    '''
    In the sixth section of the play command
    This might look the same, but we have removed the renaming of the file by listing all filse in a folder then looking for one that end with .mp3
    because we will have more than one in there I have changed it to just download and name the song file what we want before anything else very similar top the queue command
    '''
    voice = get(client.voice_clients, guild=ctx.guild)
    song_path = f"./{name_song[0]}({name_server[0]}).mp3"

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': False,
        'outtmpl': song_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    song_search = " ".join(url)

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            info = ydl.extract_info(f"ytsearch1:{song_search}", download=False)
            info_dict = info.get('entries', None)[0]
            print(info_dict)
            video_title = info_dict.get('title', None)
            ydl.download([f"ytsearch1:{song_search}"])

    except:
        print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if spotify URL)")
        c_path = os.path.dirname(os.path.realpath(__file__))
        system(f"spotdl -ff {name_song[0]}({name_server[0]}) -f " + '"' + c_path + '"' + " -s " + song_search)  # make sure there are spaces in the -s

    ##################################################################

    '''
    one thing has changed it's the playing of the song
    '''

    voice.play(discord.FFmpegPCMAudio(f"{name_song[0]}({name_server[0]}).mp3"), after=lambda e: check_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    ##################################################################


    print("playing\n")


@client.command(pass_context=True, aliases=['pa', 'pau'])
async def pause(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music paused")
        voice.pause()
        await ctx.send("Musica pausada")
    else:
        print("Music not playing failed pause")
        await ctx.send("No hay musica para pausar")


@client.command(pass_context=True, aliases=['r', 'res'])
async def resume(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Resumed music")
        voice.resume()
        await ctx.send("Resumiendo...")
    else:
        print("Music is not paused")
        await ctx.send("La musica no esta pausada")


@client.command(pass_context=True, aliases=['st', 'sto'])
async def stop(ctx):

    ##################################################################

    '''
    In the first section of the stop command we are doing like above setting variables to server info the stop command was used in
    '''

    server_name = str(ctx.guild)
    server_id = ctx.guild.id
    SQL.execute('update Music set Next_Queue = 1 where Server_ID = ? and Server_Name = ?', (server_id, server_name))
    db.commit()
    SQL.execute(f'select Queue_Name from Music where Server_ID="{server_id}" and Server_Name="{server_name}"')
    name_queue = SQL.fetchone()

    ##################################################################

    '''
    in the second section of the stop command 
    we have the program check for a folder inside Queues folder to see if these is anything that need to be deleted
    '''

    queue_infile = os.path.isdir("./Queues")
    if queue_infile is True:
        DIR = os.path.abspath(os.path.realpath("Queues"))
        Queue_Main = os.path.join(DIR, name_queue[0])
        Queue_Main_infile = os.path.isdir(Queue_Main)
        if Queue_Main_infile is True:
            shutil.rmtree(Queue_Main)

    ##################################################################

    '''
    basic stuff here
    '''

    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_playing():
        print("Music stopped")
        voice.stop()
        await ctx.send("Stopped")
    else:
        print("No music playing failed to stop")
        await ctx.send("No hay musica para stopear")


@client.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, *url: str):
    try:
        url.startswith("https://www.youtube.com/")
        url=url
    except:
        query_string = urllib.parse.urlencode({
            "search_query":url
        })
        htm_content=urllib.request.urlopen(
            "http://www.youtube.com/results?"+query_string
        )
        search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
        url='http://www.youtube.com/watch?v=' + search_results[0]
    ##################################################################

    '''
    In the first section of the queue command we are doing like above setting variables to server info the queue command was used in
    also like above we have a try block for the same reasons
    but instead of just getting the generated song name we also get the generated queue name as well as the next queue number
    '''

    server_name = str(ctx.guild)
    server_id = ctx.guild.id
    try:
        SQL.execute(f'select Queue_Name from Music where Server_ID="{server_id}" and Server_Name="{server_name}"')
        name_queue = SQL.fetchone()
        SQL.execute(f'select Song_Name from Music where Server_ID="{server_id}" and Server_Name="{server_name}"')
        name_song = SQL.fetchone()
        SQL.execute(f'select Next_Queue from Music where Server_ID="{server_id}" and Server_Name="{server_name}"')
        q_num = SQL.fetchone()
    except:
        await ctx.send("¡Metete a un canal de voz con -j!")
        return

    ##################################################################

    '''
    In the second section of the queue command we have also made some changes
    instead of like before where we just have one queue folder then download songs to that folder we make a queues folder
    then we make a folder with the name generated in the join command inside of the queue folder
    this is how we separate the queues
    '''

    Queue_infile = os.path.isdir("./Queues")
    print (Queue_infile)
    if Queue_infile is False:
        os.mkdir("Queues")
    DIR = os.path.abspath(os.path.realpath("Queues"))
    Queue_Main = os.path.join(DIR, name_queue[0])
    print (Queue_Main)
    Queue_Main_infile = os.path.isdir(Queue_Main)
    print (Queue_Main_infile)
    if Queue_Main_infile is False:
        os.mkdir(Queue_Main)

    ##################################################################

    '''
    In the Third section of the queue command it's basically the same 
    with some minor changes for the name of the song file within the queue folders
    '''
    SQL.execute(f'select Server_Name from Music where Server_ID="{server_id}" and Server_Name="{server_name}"')
    name_server = SQL.fetchone()
    queue_path = os.path.abspath(os.path.realpath(Queue_Main) + f"\\{q_num[0]}-{name_song[0]}({name_server[0]}).mp3")

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': False,
        'outtmpl': queue_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    song_search = " ".join(url)

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            # print("Downloading audio now\n")
            ydl.download([f"ytsearch1:{song_search}"])
            info = ydl.extract_info(f"ytsearch1:{song_search}", download=False)
            info_dict = info.get('entries', None)[0]
            video_title = info_dict.get('title', None)
    except:
        print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if spotify URL)")
        # q_path = os.path.abspath(os.path.realpath("Queue"))
        Q_DIR = os.path.abspath(os.path.realpath("Queues"))
        Queue_Path = os.path.join(Q_DIR, name_queue[0])
        system(f"spotdl -ff {q_num[0]}-{name_song[0]}({name_server[0]}) -f " + '"' + Queue_Path + '"' + " -s " + song_search)

    ##################################################################

    '''
    inside the fourth section of the queue command we do basically the same stuff with one add on
    we use SQl to add one the Next queue number so we can keep the song file names separate inside of the queue folder 
    EX:
    1song#48297234638927438.mp3
    2song#48297234638927438.mp3
    3song#48297234638927438.mp3
    4song#48297234638927438.mp3
    '''

    await ctx.send(f"Temazo agregado a la queue")

    SQL.execute('update Music set Next_Queue = Next_Queue + 1 where Server_ID = ? and Server_Name = ?', (server_id, server_name))
    db.commit()

    print(f"added to queue\n")


@client.command(pass_context=True, aliases=['s', 'ski'])
async def skip(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Playing next song")
        voice.stop()
        await ctx.send("Mal ahi skippeado...")
    else:
        print("No music playing failed to play next song")
        await ctx.send("No hay musica para skipear")

"""
@client.command(name="play", aliases=['s', 'j', 'i', 'l'])
async def play (ctx):
    await ctx.send("Desactive la musica hasta que me pueda pagar un servidor, posiblemente en un par de dias")
#############Help#############
"""
@client.command(name="help", pass_context=True)
async def help(ctx, a=""):
    a=a.lower()
    if a=="":
        await ctx.send("Para mas informacion escribi -help [nombre del comando]")
        author = ctx.message.author
        embed = discord.Embed(
            title = "¡Mis comandos!",
            color = discord.Color.dark_blue(),
            description = "Podes encontrar informacion mas detallada en https://sugubot.000webhostapp.com/"
        )
        embed.set_thumbnail(url="https://i.imgur.com/E2jPb6o.png")
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="League of Legends:", value="**-lol**, **-ugg**, **-profile**, **-tier** ", inline=False)
        embed.add_field(name="Vault:", value="**-vaultlist**, **-vaultsend**, **-vaultsave**, **-vaultdelete** ", inline=False)
        embed.add_field(name="Musica:", value="**-join**, **-init**, **-play**, **-skip**, **-pause**, **-resume**, **-stop**, **-leave**", inline=False)
        embed.add_field(name="Informacion:", value="**-avatar**, **-perfil**", inline=False)
        embed.add_field(name="Ocio:", value="**-8ball**, **-coin**, **-pick**, **-hug**, **-kiss**, **-calc**, **-tusa**, **-cancion**", inline=False)
        embed.add_field(name="Eventos on_message:", value="**teto**, **sugu**, **test**", inline=False)
        embed.add_field(name="Moderacion:", value="**-prune**, **-kick**, **-ban**", inline=False)
        embed.add_field(name="Mati:", value="**-reset**, **-status**", inline=False)

        await ctx.send(embed=embed)
    elif a=="lol":
        embed=discord.Embed(
            title="League of Legends",
            color= discord.Color.dark_blue(),
            description = "Muestra una partida en vivo de LoL",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Parametros:", value="Nombre de invocador, Region*", inline=False)
        embed.add_field(name="*", value="Automaticamente en LA2, puede ser LA1 o NA.")
        await ctx.send(embed=embed)
    elif a=="ugg":
        embed=discord.Embed(
            title="League of Legends",
            color= discord.Color.dark_blue(),
            description = "Te envio a la informacion del campeon que quieras",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Parametros:", value="Nombre del campeon", inline=False)
        await ctx.send(embed=embed)
    elif a=="tier":
        embed=discord.Embed(
            title="League of Legends",
            color= discord.Color.dark_blue(),
            description = "Te envio un link de los mejores campeones en ese rol",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Parametros:", value="Rol", inline=False)
        await ctx.send(embed=embed)
    elif a=="profile":
        embed=discord.Embed(
            title="League of Legends",
            color= discord.Color.dark_blue(),
            description = "Te muestro el perfil del usuario especificado",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Parametros:", value="Nombre de invocador, Region*", inline=False)
        embed.add_field(name="*", value="Automaticamente en LA2, puede ser LA1 o NA.")
        await ctx.send(embed=embed)
    elif a=="vaultlist":
        embed=discord.Embed(
            title="Vault",
            color= discord.Color.dark_blue(),
            description = "Te muestro una lista de los archivos de tu servidor",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif a=="vaultsend":
        embed=discord.Embed(
            title="Vault",
            color= discord.Color.dark_blue(),
            description = "Envio el archivo a tu servidor",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Parametros:", value="Nombre del archivo", inline=False)
        await ctx.send(embed=embed)
    elif a=="vaultsave":
        embed=discord.Embed(
            title="Vault",
            color= discord.Color.dark_blue(),
            description = "Guardo un archivo en tu servidor*",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Parametros:", value="Nombre del archivo, URL del archivo*", inline=False)
        embed.add_field(name="*", value="Por ahora solo acepto JPG, PNG o GIF.")
        await ctx.send(embed=embed)
    elif a=="vaultdelete":
        embed=discord.Embed(
            title="Vault",
            color= discord.Color.dark_blue(),
            description = "Borro un archivo de tu servidor*",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Parametros:", value="Nombre del archivo", inline=False)
        embed.add_field(name="*", value="No funciona en este momento.")
        await ctx.send(embed=embed)
    elif a=="init" or a=="i":
        embed=discord.Embed(
            title="Musica",
            color= discord.Color.dark_blue(),
            description = "Te pongo una cancion.*",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Parametros:", value="Nombre o URL de la cancion", inline=False)
        embed.add_field(name="*", value="Para seguir poniendo canciones, usa -p.")
        await ctx.send(embed=embed)
    elif a=="play" or a=="p":
        embed=discord.Embed(
            title="Musica",
            color= discord.Color.dark_blue(),
            description = "Te pongo una cancion.*",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Parametros:", value="Nombre o URL de la cancion", inline=False)
        embed.add_field(name="*", value="Para poner canciones por primera vez, usa -i.")
        await ctx.send(embed=embed)
    elif a=="join":
        embed=discord.Embed(
            title="Musica",
            color= discord.Color.dark_blue(),
            description = "Me uno al canal de voz.",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif a=="leave":
        embed=discord.Embed(
            title="Musica",
            color= discord.Color.dark_blue(),
            description = "Me voy del canal de voz.",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif a=="pause":
        embed=discord.Embed(
            title="Musica",
            color= discord.Color.dark_blue(),
            description = "Le pongo pausa a la cancion.",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif a=="resume":
        embed=discord.Embed(
            title="Musica",
            color= discord.Color.dark_blue(),
            description = "Resumo la cancion pausada.",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif a=="stop":
        embed=discord.Embed(
            title="Musica",
            color= discord.Color.dark_blue(),
            description = "Termino con toda la musica del servidor.",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif a=="skip":
        embed=discord.Embed(
            title="Musica",
            color= discord.Color.dark_blue(),
            description = "Pongo la siguiente cancion.",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif a=="perfil":
        embed=discord.Embed(
            title="Informacion",
            color= discord.Color.dark_blue(),
            description = "Te muestro el perfil del usuario.*",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Parametros:", value="Usuario*", inline=False)
        embed.add_field(name="*", value="Si no mencionas a nadie, muestro tu perfil.")
        await ctx.send(embed=embed)
    elif a=="avatar":
        embed=discord.Embed(
            title="Informacion",
            color= discord.Color.dark_blue(),
            description = "Te muestro el avatar del usuario.*",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Parametros:", value="Usuario*", inline=False)
        embed.add_field(name="*", value="Si no mencionas a nadie, muestro tu avatar.")
        await ctx.send(embed=embed)
    elif a=="coin":
        embed=discord.Embed(
            title="Ocio",
            color= discord.Color.dark_blue(),
            description = "Lanzo una moneda, puede ser cara o cruz.",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif a=="8ball":
        embed=discord.Embed(
            title="Ocio",
            color= discord.Color.dark_blue(),
            description = "Respondo a todas tus dudas.",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    elif a=="pick":
        embed=discord.Embed(
            title="Ocio",
            color= discord.Color.dark_blue(),
            description = "Si no sabes a quien elegir, yo lo hago por vos ;).",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Parametros:", value="Parametros que quieras elegir*", inline=False)
        embed.add_field(name="*", value="Los parametros se dividen por espacio", inline=False)
        await ctx.send(embed=embed)
    elif a=="hug":
        embed=discord.Embed(
            title="Ocio",
            color= discord.Color.dark_blue(),
            description = "Abrazas al usuario. <3",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Parametros:", value="Usuario", inline=False)
        await ctx.send(embed=embed)
    elif a=="kiss":
        embed=discord.Embed(
            title="Ocio",
            color= discord.Color.dark_blue(),
            description = "Besas al usuario. <3",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Parametros:", value="Usuario", inline=False)
        await ctx.send(embed=embed)
    elif a=="prune":
        embed=discord.Embed(
            title="Moderacion",
            color= discord.Color.dark_blue(),
            description = "Te borro de 1 a 50 mensajes.*",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Parametros:", value="Cantidad", inline=False)
        embed.add_field(name="*", value="Por seguridad, solo los usuarios que puedan manejar los mensajes pueden usar este comando.", inline=False)
        await ctx.send(embed=embed)
    elif a=="kick":
        embed=discord.Embed(
            title="Moderacion",
            color= discord.Color.dark_blue(),
            description = "Kickeo al usuario.*",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Parametros:", value="Usuario, Razon", inline=False)
        embed.add_field(name="*", value="Solo los usuarios que puedan kickear a otros pueden usar este comando.", inline=False)
        await ctx.send(embed=embed)
    elif a=="ban":
        embed=discord.Embed(
            title="Moderacion",
            color= discord.Color.dark_blue(),
            description = "Baneo al usuario.*",
        )
        embed.set_footer(text=f"Requerido por {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Parametros:", value="Usuario, Razon, Cantidad de días que borro sus mensajes", inline=False)
        embed.add_field(name="*", value="Solo los usuarios que puedan banear a otros pueden usar este comando.", inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Comando no encontrado.")
                       
        

@client.command(name="status")
async def status(ctx, msj="status"):
    if ctx.message.author.id==186955944410742785:
        if msj=="status":
            await client.change_presence(activity=discord.Game(name='-h, Ayudando a '+str(len(client.guilds))+' servidores | Conectado con '+str(len(set(client.get_all_members())))+' usuarios'))
        elif msj!="status":
            msj = msj.replace("_", " ")
            await client.change_presence(activity=discord.Game(name=msj))
    else:
        await ctx.send("Solo Mati puede cambiar el status del bot")
@client.command(name="pruebayt")
async def pruebayt(ctx, *, search):
    query_string = urllib.parse.urlencode({
        "search_query":search
    })
    htm_content=urllib.request.urlopen(
        "http://www.youtube.com/results?"+query_string
    )
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])
@client.event
async def on_command_error(ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("El comando no cuenta con los argumentos requeridos.")
        elif isinstance(error,commands.BadArgument):
            await ctx.send("Error en los argumentos dados.")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("El comando no existe! Usa -help para ver la lista de comandos")
@client.command(name = "kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f"El usuario {member} fue kickeado por {ctx.message.author} por la razon de **{reason}**")
    except:
        await ctx.send("No contas con los permisos necesarios para realizar esta accion")

@client.command(name = "ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member,*,reason=None, delete_message_days=1):
    try:
        await member.ban(reason=reason)
        await ctx.send(f"El usuario {member} fue baneado por {ctx.message.author} por la razon de **{reason}** y se borraron los mensajes de hace {delete_message_days} dias")
    except:
        await ctx.send("No contas con los permisos necesarios para realizar esta accion")


        
@client.command(name="prune", help="Borra de 1 a 50 mensajes.", pass_context=True)
@commands.has_permissions(manage_messages=True)
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
    
client.run(token)
