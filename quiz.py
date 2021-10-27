import random
from colours import Colour

with open('vocabulary.txt') as f:
	lines = f.readlines()

correct = 0
total = 0

while True:
	question_number = random.randint(0, len(lines))
	question = lines[question_number].split(' ')
	print(Colour.question(question[0] + ' ' + question[1]))
	i = input("ANSWER: ").upper()
	if i:
		i = i.split()
		total += 1
	else:
		if total > 0:
			print(Colour.question(str(correct) + '/' + str(total) + '  ' + str(int(correct*100/total)) + '%'))
		break	
	if i[0] == question[3].upper() and i[1] == question[4].upper():
		print(Colour.correct(question[3] + ' ' + question[4]))
		correct += 1
	else:
		print(Colour.error(question[3] + ' ' + question[4]))
	input()




