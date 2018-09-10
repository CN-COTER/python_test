# 类与对象
class Dog():

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		print(self.name.title() + "is sitting")

	def roll_over(self):
		print(self.name.title() + "is rolling over")

my_dog = Dog('willie', 6)
print("my dog is " + my_dog.name)
