from numpy.random import choice

names_file = open('names.txt', 'r')
people = names_file.read().split(',\n')

draw = choice(people, 2)
print(*draw, sep=', ')
