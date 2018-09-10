#字典
alien_0 = {'color':'green','points':'5'}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_postion'] = 0
alien_0['y_postion'] = 25
print(alien_0)


alien_0['color'] = 'yellow'
alien_0['speed'] = 'medium'
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] =='medium':
	x_increment = 2
else:
	x_increment = 3
alien_0['x_postion'] += x_increment
print(alien_0)

del alien_0['points']
print(alien_0)

favourite_lan = {
	'tom':'python',
	'jack':'C',
	'sam':'java',
	'sari':'ruby',
	'sam':'c++'
}
print(favourite_lan['tom'])

#test
familiar_person = {
	'first_name':'jiang',
	'last_name':'chaomei',
	'age':'25',
	'city':'changzhou'
}
print(familiar_person)

favorite_num = {
	'tom':'1',
	'jack':'2',
	'sam':'3',
	'henry':'4',
	'lisa':'5'
}

print(favorite_num['tom'])

#注意 字典遍历
for key,value in favorite_num.items():
	print('\nKey:' + key)
	print('Value:' + value)

for name,language in favourite_lan.items():
	print('\nName:' + name)
	print('Language:' + language)

for key in favourite_lan.keys():
	print('\nName:' + key.title())

friends = ['tom','jack']
for name in favourite_lan:
	if name in friends:
		print('Hi I see ' + name + ' your favourite language is ' + favourite_lan[name])
	else:
		print('8080')
if 'ame' not in friends:
	print('Ame ,you are not in my favorite friends.\n')

for name in sorted(favourite_lan.keys()):
	print(name.title() + '\'s favourite language is ' + favourite_lan[name] + '.\n')

#用集合set()来去除重复项
for name in set(favourite_lan.keys()):
	print(name.title())

#test 6-2
characters = {
	'C':'the most inside lan',
	'java':'the object-orented lan',
	'C++':'skillful inner-memory operator',
	'python':'java plus with perfect distributions',
	'MVC':'model,viewer,controller'
}
for key,value in characters.items():
	 print(key.title() + ' : ' + value + '\n')

rivers_countries = {
	'Yangtz':'china',
	'nile':'egypt',
	'amazon':'brizil',
	'fuerjia':'russia',
	'henhe':'india'
}
for river,country in rivers_countries.items():
	print('The ' + river.title() + ' runs through ' + country +'.\n')

for river in rivers_countries.keys():
	print(river + '\n')

people = ['sam','jack','wuxi']
for person in favourite_lan.keys():
	if person in people:
		print(person.title() + " Congulations!\n")

alien_0 = {'color':'green','points':'5'}
alien_1 = {'color':'red','points':'6'}
alien_2 = {'color':'blue','points':'7'}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)

for alien_number in range(30):
	new_alien = {'color':'red','points':'23','speed':'medium'}
	aliens.append(new_alien)

print('\n')

for alien in aliens[:5]:
	print(alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['points'] = 'red'
		alien['speed'] ='medium'

print(aliens[0:5])




 













