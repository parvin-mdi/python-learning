number_of_winner = int(input('How many winner you have? '))
winner_list = []
counter = 0
for i in range(number_of_winner):
    counter = input(f'Enter the information of winner {i+1}')
    winner_list.append(counter.split('.'))

list_of_femail = []
list_of_mail = []
for i in range(number_of_winner):
    if winner_list[i][0] == 'f':
        data = winner_list[i][1:]
        data[0] = data[0].capitalize()
        list_of_femail.append(data)

    elif winner_list[i][0] == 'm':
        data = winner_list[i][1:]
        data[0] = data[0].capitalize()
        list_of_mail.append(data)

for i in range(len(list_of_femail)):
    print(f'f {list_of_femail[i][0]} {list_of_femail[i][1]}')

for i in range(len(list_of_mail)):
    print(f'm {list_of_mail[i][0]} {list_of_mail[i][1]}')