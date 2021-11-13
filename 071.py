sports = ['Football', 'Hockey', 'Basketball']
print(sports)
favorite = input('Введите ваш людимый спорт:').capitalize()
sports.append(favorite)
sports.sort()
print(sports)