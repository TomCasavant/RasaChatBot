import random 
import os
import yaml
import json


def generatePhrase(insult=True):
	if (insult):
		filepath = '/insults.yml'
	else:
		filepath = '/compliments.yml'
	config = yaml.load(open(os.path.dirname(__file__) + filepath))

	col1 = random.choice(config['column1'])

	col2 = random.choice(config['column2'])

	col3 = random.choice(config['column3'])

	# print generated insult for the 'user' 
	return (col1 + ' ' + col2 + ' ' + col3 + '.' )

