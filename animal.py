class animal():
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def eat(self, food):
        printf(self.name+"eat"+food)


a = animal('cat', 'male', '30')
b = animal('dog', 'male', '20')
c = animal('bird', 'male', '30')
print(a.name, b.name, c.name)
