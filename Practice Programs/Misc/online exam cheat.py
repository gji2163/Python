from io import BytesIO
import base64
import firebase_admin
from firebase_admin import db
from PIL import Image as Im
import discord
import io

TOKEN = 'ODQ2NzA2MjA1MDgyNTE3NTA1.YKzamg.lXLtjvSLeSvHLwVOnjDEFqaaPos'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)




cred = firebase_admin.credentials.Certificate('bot.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bot-world.firebaseio.com/',
    'databaseAuthVariableOverride': {
        'uid': 'my-service-worker'
    }
})

var=0
d={}

async with aiohttp.ClientSession() as session:
    async with session.get(my_url) as resp:
        if resp.status != 200:
            return await channel.send('Could not download file...')
        data = io.BytesIO(await resp.read())
        await channel.send(file=discord.File(data, 'cool_image.png'))

def display(event):
    global var,d
    exec("x=io.BytesIO(base64.decodebytes(b'"+list(event.data.values())[0]+"'))")
    var+=1
    #await channel.send(file=discord.File(x))
    #x.save(str(var)+'_'+event.path+'.png')

ref = db.reference('/Bot/').listen(display)
