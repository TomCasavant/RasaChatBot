from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/chatnlu')
agent = Agent.load('./models/dialogue', interpreter=nlu_interpreter)


while True:
	statement = unicode(raw_input("User: "))
	print ("bot: " +  agent.handle_message(statement)[0])
