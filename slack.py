from slackclient import SlackClient
import os
import time
from ConfigParser import SafeConfigParser
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

def main():
	nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/chatnlu')
	agent = Agent.load('./models/dialogue', interpreter=nlu_interpreter)
	if sc.rtm_connect():
		while True:
			for slack_message in sc.rtm_read():
				message = slack_message.get("text")
				user = slack_message.get("user")
				channel = slack_message.get("channel")
				if not message or not user or user == "Insulter":
					continue
				message = unicode(message)
				response = agent.handle_message(message)[0]
				sc.rtm_send_message(channel, "{text}".format(text=response))

			time.sleep(1)

		else:
			print "Connection failed"

if __name__ == "__main__":
	parser = SafeConfigParser()
	parser.read("config.ini")
	SLACK_API_TOKEN = parser.get("slack", "API_TOKEN")
	sc = SlackClient(SLACK_API_TOKEN)
	main()
