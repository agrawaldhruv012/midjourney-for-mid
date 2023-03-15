import discord
import asyncio

client = discord.Client()

#5
async def midjourney(message):
    await message.channel.send('Please enter your input:')
    try:
        input_message = await client.wait_for('message', timeout=30.0, check=lambda m: m.author == message.author and m.channel == message.channel)
    except asyncio.TimeoutError:
        await message.channel.send('Input timed out.')
        return
    output_message = 'Some code to send input to midjourney bot and get response'
    await message.channel.send(output_message)


#6
@client.event
async def on_message(message):
    if message.channel.id == 1081912696850632836 and message.author != client.user:
        await midjourney(message)


#7
async def send_output(output_message):
    channel = client.get_channel(1082513043281416234)
    await channel.send(output_message)


#8
async def midjourney(message):
    await message.channel.send('Please enter your input:')
    try:
        input_message = await client.wait_for('message', timeout=30.0, check=lambda m: m.author == message.author and m.channel == message.channel)
    except asyncio.TimeoutError:
        await message.channel.send('Input timed out.')
        return
    output_message = 'Some code to send input to midjourney bot and get response'
    await send_output(output_message)
    await message.channel.send(output_message)


#9
client.run('MTA4NTM0OTExMDQxNDA1MzQ2Ng.GdPOXd.Vnt_zS08Dw0fGLsfg7a13bVzkK2p-mmKn7Gld4')
