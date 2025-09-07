number_of_people = int(input('Please enter the number of people: '))
print('Now type the name of each person with their interest.')
print('choose between these type: Horror, Romance, Comedy, History , Adventure , Action')

each_person = []
for i in range(number_of_people):
    information = input(f'enter the person number {i}')
    each_person.append(information)


answer = []
for i in each_person:
    answer.append(i.split(' '))
    # answer.pop(0)


print(each_person)
print(answer)

# test = [['a', 'b'], ['c', 'd']]
# # print(test)
# for i in range(2):
#     test.append(test[i][i])
# print(test)