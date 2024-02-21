import discord , random, os
from discord.ext import commands
from bot_logic import coins 
from bot_logic import gen_pass
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def flipcoin(ctx):
    await ctx.send(coins(1))

@bot.command()
async def createpass(ctx):
    await ctx.send(gen_pass(8))

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open (f'images/{img_name}','rb') as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file = picture)

@bot.command()
async def idesampah(ctx):
    img_name = random.choice(os.listdir('kerajinan'))
    with open (f'kerajinan/{img_name}','rb') as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file = picture)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            await file.save(f'./{file.filename}')
            await ctx.send(f'FILE BERHASIL DISIMPAN DENGAN NAMA {file.filename}')
            hasil = get_class('keras_model.h5', 'labels.txt', file.filename)
            
            if hasil[0] == "rabbit\n" and hasil[1] >=0.7 :
                await ctx.send("ini adalah kelinci")
                await ctx.send("kelinci makannya wortel, jerami, rumput kering dll")
                await ctx.send("nama ilmiah kelinci adalah Oryctolagus cuniculus")
                await ctx.send("kelinci memiliki tubuh sekitar 25-55 cm")
                await ctx.send("Persentase kemiripan {:,.1f}%".format(hasil[1]*100))
            elif hasil[0] == "marmut\n" and hasil[1] >=0.7 :
                await ctx.send("ini adalah marmut")
                await ctx.send("marmut makannya paprika merah, brokoli dll")
                await ctx.send("nama ilmiah marmut adalah Marmota")
                await ctx.send("marmut memiliki tubuh sekitar 42-54 cm")
                await ctx.send("Persentase kemiripan {:,.1f}%".format(hasil[1]*100))
    else:
        await ctx.send('ANDA lUPA MENGIRIM GAMBAR!!!')

bot.run("ur token")
 
