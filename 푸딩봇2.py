import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("그루밍")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!야옹"):
        await message.channel.send("야옹야옹")

    if message.content.startswith("!갈배"):
            await message.channel.send("장문작뷘")

    if message.content.startswith("!두유"):
        await message.channel.send("인성 썩었다냥")

    if message.content.startswith("!hyun"):
            await message.channel.send("회장님 이다냥")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
