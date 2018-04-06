import discord
import asyncio
import config
import random
import time
from weather import *
from log import *
allowed = ["EkosFox#0860"]
quotes = [
"Besides, the world isn't split into good people and Death Eaters. We've all got both light and dark inside us. What matters is the part we choose to act on. That's who we really are.",
"This is how it is — this is why you're not in the Order — you don't understand — there are things worth dying for!",
"Why would I go looking for someone I know wants to kill me?!",
"Quelli che ci amano non ci lasciano mai veramente.",
"I want to commit the murder I was imprisoned for.",
"If you want to know what a man’s like, take a good look at how he treats his inferiors, not his equals.",
"You think the dead we loved ever truly leave us?",
"Well, bad times like that bring out the best in some people and the worst in others.",
"What's life without a little risk?",
"The world isn't split into good people and Death Eaters."
]
purge = []
client = discord.Client(status="=>")

@client.event
async def on_ready():
	info("Bot " + client.user.name + "(" + client.user.id + ")" + " has been logged in!")
	await client.change_presence(game=discord.Game(name='with code'))

@client.event
async def on_message(message):
	global purge
	def is_mod(m):
		return str(m.author) in allowed
	
	def purgeCheck(m):
		return str(m.author) in purge
		
		
	msg = message.content
	
	if msg.startswith('!sirius'):
		await client.send_message(message.channel, 'Working!')
		
	elif msg.startswith('!ping'):
		await client.send_message(message.channel, 'Pong')
		
	elif msg.startswith('!purgeall'):
		await client.purge_from(message.channel)
	
	elif msg.startswith('!quote'):
		rint = random.randint(0,len(quotes)-1)
		await client.send_message(message.channel,"*\"" + quotes[rint] + "\"*")
	
	elif msg.startswith('!purge'):
		for i in msg.split(" "):
			if i != "!purge":
				purge.append(i)
				
		if len(purge) > 0:
			deleted = await client.purge_from(message.channel, check=purgeCheck)
			await client.send_message(message.channel, 'Deleted {} message(s) from #{}'.format(len(deleted),str(message.channel)))
		purge = []
	
	elif msg.startswith('!weather'):
		if str(message.author) in allowed:
			wsm = msg.split(" ")
			if not ["zip","coordinates"] in wsm:
				if len(wsm) != 2 and "tomorrow" not in wsm:
					await client.send_message(message.channel, "!ERROR! : Wrong Syntax!")
				else:
					addH = str()
					a = data_organizer(data_fetch(url_builder(wsm[1])))
					ii = 0
					for i in a:
						if ii == 0:
							await client.send_message(discord.Object(id=431235681042432020), "Weather Forecast for " + i + "\n---------------------------------------\n")
						if ii % 2 == 0 and ii != 0:
							# addH += str(i) + "\n"
							await client.send_message(discord.Object(id=431235681042432020),"Date: " + str(i[0]) + "\nMin: " + str(i[1]) + " \xb0" + "C\nMax: " + str(i[2]) + " \xb0" + "C\nDescription: " + str(i[3]) + "\n---------------------------------------\n" )
							await asyncio.sleep(1)
						ii += 1
						if ii > 8:
							break
				await client.send_message(discord.Object(id=431235681042432020),"Requested by " + message.author.mention)
		
		#if message.content.find('tomorrow')

client.run(config.token)