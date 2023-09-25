import discord
from bot_mantik import *

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('Selam eğlence'):
        await message.channel.send("Selam!")
    elif message.content.startswith('Görüşürüz eğlence'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('Parola Oluştururmusun?'):
        await message.channel.send(sifre_uret(10))
    elif message.content.startswith('Nasilsin Eğlence'):
        await message.channel.send("Iyiyim sen?")
    elif message.content.startswith('Elektrikli araçlar doğaya zararlımı sence'):
        await message.channel.send("Bence elektrikli araçlar doğaya daha zararlı.Çünkü pilleri 4 yıl gidiyor...")
    elif message.content.startswith('Sorunlarin var Eğlence'):
        await message.channel.send("Yapimcima iletebilirsin Yapimcim:.maden_suyu")
    elif message.content.startswith('Eğlence sence fabrikalar egzozlarına filtre takmalımı?'):
        await message.channel.send("Evet.Bence takmalı.Egzozlardan çıkan kara duman doğaya zararlıdır.Ozon tabakasına zarar verebilir.")
    elif message.content.startswith('!help'):
        await message.channel.send("Yardım kanalımıza bağlanmak için aşağıdaki linke tıklayabilirsiniz.")
        await message.channel.send("https://discord.com/channels/1143596366799581194/1153400729084625058")
    elif message.content.startswith('Bana doğa nasıl korulunur içerikli bir video atarmısın?'):
        await message.channel.send("Tabiki!Aşağıdaki linke tıkla!")
        await message.channel.send("https://www.youtube.com/watch?v=Qyq_WDAoI_Q")
    else:
        await message.channel.send(message.content)

client.run("MTE0NTc5Mjc0MzQ4Mjg3MTgzOQ.G8HzKF.EnTTPVOAXih7uzcGA_q0jhhyjd0WpbugLnoIcM")