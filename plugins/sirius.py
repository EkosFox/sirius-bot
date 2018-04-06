from disco.bot import Bot, Plugin
import random
import time
from siriusquotes import quotes
from weather import *

class SirusBot(Plugin):
	@Plugin.command('weather', '<content:str...>')
	def Weather_Trigger(self, event, content):
		event.msg.reply(content)