#Создайте кортедж с названиями пяти стран.Выведите все содержимое кортеджа.Предложите пользователю
name = ['Belarus', 'Rissia', 'Ukraine', 'Polish', 'China']
for item in name:
    print(item)
#ввести название одной из этих стран и выведете индекс
UserItem = input('введите страну').capitalize()
try:
    print(name.index(UserItem))
except ValueError:
    print('Not found')


