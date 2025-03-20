import random


when = ['Some time ago', 'Earlier today', 'In the past', 'Not long ago', 'On a chilly night']
who = ['a dragon', 'a fox', 'a koala', 'a lion', 'a squirrel']
name = ['Zara', 'Finn', 'Juno', 'Luca', 'Cleo']
residence = ['Tokyo', 'Paris', 'Australia', 'New York', 'Cairo']
went = ['to a concert', 'on a journey', 'to a park', 'to a party', 'on a road trip']
happened = ['discovered a hidden treasure', 'learned a new dance', 'baked a cake', 'rescued a friend', 'invented a gadget']


story = f"{random.choice(name)} was {random.choice(who)} living in {random.choice(residence)}. {random.choice(when)}, they went {random.choice(went)} and {random.choice(happened)}."

print(story)
