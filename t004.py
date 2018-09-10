brands = ['Benz','BMW','Audi','Honda','Toyota','Nissan','Mazada']
names = ['j1','j2','j3','j4','j5','j6']
print(brands)
print(brands[2])
print(brands[1].upper())
print(brands[0].lower())
#访问倒数第一个，倒数第二个。
print(brands[-1])
print(brands[-2])


print('my'.title() + ' first car is ' + str(brands[2]) )
brands[1] = 'Volvo'
print(brands)
brands.append('BMW')
print(brands)
brands.insert(0,'BYD')
print(brands)
del brands[1]
print(brands)
del brands[0]
print(brands)
pop_brand = brands.pop()
print(pop_brand)
print(brands)
first_brand = brands.pop(0)




