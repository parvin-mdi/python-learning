number_of_people = int(input('Please enter the number of people: '))
print('Now type the name of each person with their interest.')
print('choose between these type: Horror, Romance, Comedy, History , Adventure , Action')

each_person = []
for i in range(number_of_people):
    information = input(f'enter the person number {i}')
    each_person.append(information.split(' '))

for i in range(len(each_person)):
    each_person[i].pop(0)

Horror = 0
Romance = 0
Comedy = 0
History = 0
Adventure = 0
Action = 0
for i in range(len(each_person)):
    for j in range(len(each_person[i])):
        if each_person[i][j] == 'Horror':
            Horror = Horror + 1
        elif each_person[i][j] == 'Romance':
            Romance = Romance + 1
        elif each_person[i][j] == 'Comedy':
            Comedy = Comedy + 1
        elif each_person[i][j] == 'History':
            History = History + 1
        elif each_person[i][j] == 'Adventure':
            Adventure = Adventure + 1
        elif each_person[i][j] == 'Action':
            Action = Action + 1

genre = {}
genre['Action'] = Action
genre['Comedy'] = Comedy
genre['History'] = History
genre['Horror'] = Horror
genre['Romance'] = Romance
genre['Adventure'] = Adventure

sorted_genre = sorted(genre.items(), key=lambda x: (-x[1], x[0]))

for key,value in sorted_genre:
    print(f'{key}: {value}')
