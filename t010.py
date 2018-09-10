#继续t009.py里面的字典
pizza = {
	'crust':'thick',
	'toppings':['mushroom','extra cheese']
}

for topping in pizza['toppings']:
	print('You ordered the toppings that:' + topping)

users = {
	'aa':{
	'first_name':'xiao a',
	'second_name':'da a',
	'name':'aa',
	},
	'bb':{
	'first_name':'xiao b',
	'second_name':'da b',
	'name':'bb',
	},
}
for user,user_name in users.items():
	print('User is ' + user)
	full_name = user_name['first_name'] + ' ' + user_name['second_name']
	print(full_name)

#用户输入
message = input('Tell me something,and I will repeat it back to you.')
print(message)
name = input('Please enter your name: ')
print('hello , ' + name)
age = int(input('How old are you?'))
if age >= 18:
	print('Audlt')
else:
	print('Non Audlt')
 
number = int(input('Enter a number:'))
if number%2 ==0:
	print('The number ' + str(number) + 'is even')
else:
	print('The number ' + str(number) + 'is odd')
number = input('输入一个数字：')
if int(number) % 2 ==0:
	print('\nThe number ' + str(number) + ' is even ')
else:
	print('\nThe number ' + str(number) + ' is odd.')

current_number = 1
while current_number <=5:
	print(current_number)
	current_number += 1

message = input('Enter a character: ')
while message != 'q':
	print('Continue enter')
	message = input('Enter a character:')

active = True
while active:
	message = input("continue:")
	if message =='quit':
		break
	else:
		print(message)

current_number = 0
while current_number<10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)
print('\n')

x = 1
while x <=5:
	print(x)
	x += 1



# message = input("Enter a topping:")
# toppings = []
# while message != 'quit':
# 	print("we have added the " + message.title())
# 	toppings.append(message)
# 	message =input("Enter a topping:")
# print('End')
# print(toppings)


i = 10
while i >= 0:
	num = int(input("Enter a number:"))
	if num < 3:
		print("The price is free.")
		i-=1
	elif num >= 3 and num <=12:
		print("The price is $10")
		i-=1
	elif num > 12:
		print("The price is $15")
		i-=1
	else:
		print('Enter a correct number:')
		i-=1
print('Thanks for use.')

