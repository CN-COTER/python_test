#if语句
cars = ['BMW','BENZ','AUDI','BUICK','TOYATA','NISSAN','HONDA']
for car in cars:
	if car == 'BMW':
		print(car.title())
	else:
		print(car)

requested_topping = 'mushroom'
if requested_topping != 'mushroom':
	print('It is wrong!')
 

#and / or / in / not in
age_0 = 1
age_1 = 2
if age_0 >= 20 or age_1 <21:
	print('false')

if 'BMW' in cars:
	print('11')
if 'MBS' not in cars:
	print('djfb')

#布尔表达式
game_active = True
is_edit = False



age =  18
if age == 18:
	print('My age is 18!')
if age > 19:
	print('Too old!')
elif age < 19:
	print('Too young!')
else:
	print('Yes!')

age = 66
if age <19:
	print('Too old!')
elif age >65:
	print('Too young!')

#test
#V1
alien_color = 'green'
if alien_color =='green':
	print("U get five points")
#V2
if alien_color == 'red':
	print('Sorry')

if alien_color == 'green':
	print('U get 5 points')
else:
	print('U get 10 points')

request_toppings = ['mushroom','green peppers','extra cheese']
for request_topping in request_toppings:
	if request_topping =='green peppers':
		print('Green peppers is consumed！')
	else:
		print('Add ' + request_topping +'.')
print('Finish making a pizza!')

request_toppings = []
if request_toppings:
	for request_topping in request_toppings:
		print('Add ' + request_topping +'.')
else:
	print('There is nothing in request_toppings!')

avilable_toppings = ['mushroom','olives','green peppers','pineapple','cheese']
request_toppings = ['mushroom','green peppers','extra cheese']
for request_topping in request_toppings:
	if request_topping in avilable_toppings:
		print('Add ' + request_topping +'.')
	else:
		print('Sorry,we donnot have ' + request_topping + '.')
print('\nFinished making a pizza.')

#test 
users = ['admin','Davide','Jobs','Albert']
if users:
	for user in users:
		if user =='admin':
			print('Hello, ' + user.title() + 'would you like to see a status report.')
		else:
			print('Hello ' + user + 'thank you for logging in again')
else:
	print('We need to find some users.')

current_users = ['admin','Davide','Jobs','Abert','Luxun']
new_users = ['admin','Davide','AAAA','BBB','CCCCC']
for new_user in new_users:
	if new_user in current_users or new_user.lower() in current_users:
		print('The name has been registered')
	else:
		print('The name can be used.')

number = [1,2,3,4,5,6,7,8,9]
for num in number:
 	if num == 1:
 		print('1st')
 	elif num == 2:
 	 	print('2nd')
 	elif num == 3:
 	 	print('3rd')
 	else:
 	 	print(str(num) + 'th')







