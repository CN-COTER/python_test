class animal():
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def eat(self, food):
        printf(self.name+"eat"+food)

        a = animal('chicken', 'female', '11')
        b = animal('dog', 'male', '20')
        c = animal('bird', 'male', '30')
        printf(a.name, b.name, c.name)
