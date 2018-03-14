from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

from PhraseGenerator import generatePhrase

class ActionInsult(Action):
	def name(self):
		return 'action_insult'

	def run(self, dispatcher, tracker, domain):

		name = tracker.get_slot('name')
		insult = generatePhrase(True)
		if (name):
			response = """{} is a {}""".format(name, insult)
		else:
			response = """You are a {}""".format(insult)

		dispatcher.utter_message(response)
		return [SlotSet('name', None)]


class ActionCompliment(Action):
	def name(self):
		return 'action_compliment'

	def run(self, dispatcher, tracker, domain):
		name = tracker.get_slot('name')
		compliment = generatePhrase(False)
		if (name):
			response = """{} is a {}""".format(name, compliment)
		else:
			response = """You are a {}""".format(compliment)

		dispatcher.utter_message(response)
		return [SlotSet('name', None)]

