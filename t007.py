brands = ['coco','nike','anta','puma','spider','audi']
for brand in brands:
	print(brand)
for brand in brands:
	print(brand.title() + ' produces great goods.')
	print('I cannot wait to buy ' + brand.title() + '.\n')
print("Thanks for your goods!")
print('--------------------------------------------------')
for brand in brands:
	print(brand.lower())
print('---------------------------------------------------')
ladies = ['fanbb','zhaow','zhangzy','gongl']
for lady in ladies:
	print('I like '+ lady.title() +'.')
print('I really love zhangzy')
print('---------------------------------------------------\n')
animals = ['dog','cat','snake','bird']
for animal in animals:
	print(animal.title())
	print('A '+animal.title()+' would make a good pet.')
print('All of these animals make a great pet.') 
print("-----------------------------------------------\n")





#range(a,b,c) list()制作列表
for num in range(1,5):
	print(num)
print('\n')

numbers = list(range(2,8,3))
print(numbers)
squres = []
for value in range(1,11):
	squre=value**2
	squres.append(squre)
print(squres)
print('-----------------------------------')
squares = []
for value in range(1,50,5):
	squares.append(value**3)
print(squares)



#min() max() sum()
print(min(squares))
print(max(squares))
print(sum(squares))


#列表解析来生成列表
squres = [value*2 for value in squares] 
print(squres)

#test
print('\n\n')
for num in range(1,21):
	print(num)

list1 = list(range(1,1000001))
print(min(list1))
print(max(list1))
print(sum(list1))

for value in range(1,21,2):
	print(value)

list2 = [value for value in range(3,31,3)]
print(list2)
list3 = [value**3 for value in range(1,11,1)]
print(list3)
print('------------------------------------------------')

#截取列表切片
nums = ['aa','bb','cc','dd','ee','ff']
print(nums[1:3])
print(nums[:3])
print(nums[1:])
print(nums[-3:])#列表最后三个数字

for value in nums[:3]:
	print(value.title())


#利用切片来复制数据（产生副本），而不是直接赋值
foods = ['pizza','sandwich','hot-dog','milk']
friends_foods = foods[:]
foods.append('rice')
friends_foods.append('source')
print(foods)
print(friends_foods)


#test
print('The first three items in the list are: ')
for item in foods[:3]:
	print(item.title())
print('The items from the middle of the list are: ')
for item in foods[1:4]:
	print(item.title())
print('The item from the last of the list are: ')
for item in foods[-3:]:
	print(item.title())
pizza = ['aa','bb','cc','dd','ee']
friends_pizza =pizza[:]
pizza.append('ff')
friends_pizza.append('gg')
print(pizza)
print(friends_pizza)
for item in foods:
	print(item.title())
for item in pizza:
	print(item.title())
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')




#不可更改的列表称为元组（）
dimensions = (200,21212,888)
print(dimensions[0])
for dimension in dimensions:
	print(dimension)

#test
foods = ('rice','milk','hotdog','cake','sandwich')
for food in foods:
	print(food.title())
foods = ('rice','milk','hotdog','rice','pizza')
for food in foods:
	print(food.title())



