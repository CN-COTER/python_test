class car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def run(self):
        print(self.model)

class Battery():
    def __init__(self, battery_size = '70'):
        self.battery_size = battery_size;

    def describe(self):
        print(self.battery_size)


class Elecar(car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        #添加自己的特有属性
        self.battery = Battery()

    def run2(self):
        print(self.make + "电池容量" + self.battery.battery_size)

    def run(self):
        if (self.battery.battery_size == '70'):
            print(self.model)


mytesla = Elecar('ford', '911', 2018)
mytesla.run()


