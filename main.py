# THE random sentence generator.
import random

from words.nouns import nouns
from words.verbs import verbs
from words.adjectives import adjectives

i = 0
while True:
	print(f'[{str(i)}] The {random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(nouns)}.')
	input()
	i += 1
