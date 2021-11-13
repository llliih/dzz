party = []

while True:
    party.append(input('Введите имя человека, которого хотите пригласить:'))
    if len(party)>=3:
        mess=input('Хотите продолжить').capitalize()
        if mess == 'Yes':
            continue
        elif mess == 'No':
            break
        else:
            print('ошибка')
print('Приглашено', len(party), 'человек')

