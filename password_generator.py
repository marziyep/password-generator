import random
import pandas as pd

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
alphabets_capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
alphabets_lowercase = [i.lower() for i in alphabets_capital]
dice = [1, 2, 3]


def generator():
    password = ''
    for i in range(9):
        chance = random.choice(dice)
        if chance == 1:
            char1 = random.choice(numbers)
            password = password + char1
        elif chance == 2:
            char2 = random.choice(alphabets_capital)
            password = password + char2
        else:
            char3 = random.choice(alphabets_lowercase)
            password = password + char3
    return password

amount = int(input('how many passwords would you like to produced: '))
my_set = set()

while len(my_set) != amount:
        for i in range(amount):
            my_set.add(generator())

mylist = list(my_set)
my_dictionary = {'passwords': mylist}
my_dataframe = pd.DataFrame(my_dictionary )
name = input('how would you like to name your file?')
my_dataframe.to_excel(f'{name}.xlsx')
print(f'ur passwords have been saved in a file named {name}')





