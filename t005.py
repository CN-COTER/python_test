#接t004.py列表学习
brands = ['Benz','BMW','Audi','Honda','Toyota','Nissan','Mazada']
brands.remove('Benz')
print(brands)	
too_expensive = 'BMW'
brands.remove(too_expensive)
print(brands)
print("\nA " + too_expensive.title() + " is too expensive")
print('--------------------------------------------------------')
#练习
people = ['aa','bb','cc','dd','ee']
print('Welcome ' + people[0] + ',' + people[2] +',' + people[3] + ' to take part in our party.')
people[1] = 'AA'
print('aa is busy with his homework,so '+ people[1] + ' comes.')
print(people)
people.insert(0,'BB')
people.insert(3,'CC')
people.append('EE')
print(people)
print("I just be able to invite two  of you to take part in my party")
people1 = people.pop();
print("I am sorry to inform " + people1 +" that you are forbided to come.")
del people[0]
del people[1]
print(people)