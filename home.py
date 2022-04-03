import random
import time

# ----------------------------- Task 1-------------------------------------
class Engine():
    def __init__(self, engine_type):
        self.engine_type = engine_type
        self.horse_power = 50
        self.flag_active = True
        self.flag_off = False
        self.power = 0.8

    def generate_power(self):
        if self.engine_type == 'v6':
            return self.horse_power * 0.2 / self.power
        if self.engine_type == 'v8':
            return self.horse_power * 0.4 / self.power
        if self.engine_type == 'v10':
            return self.horse_power * 0.6 / self.power


engine_v6 = Engine('v6')
engine_v6.horse_power = 75
print(engine_v6.generate_power())
engine_v8 = Engine('v8')
engine_v10 = Engine('v10')
engine_v10.horse_power = 90


class Wheel():
    def __init__(self, wheel_weigh, wheel_diameter):
       self.wheel_diameter = wheel_diameter
       if self.wheel_diameter in range(16, 22):
           print('The diameter is true!')
       else:
           print('Diameter 16-21. Enter the number using this diameter!')
       self.wheel_weigh = wheel_weigh


wheel_1 = Wheel(10, 17)
wheel_2 = Wheel(12, 21)
wheel_3 = Wheel(14, 19)
wheel_4 = Wheel(15, 18)

class Car(Engine, Wheel):
    def __init__(self, engine_type, car_type):
        super().__init__(engine_type)
        self.car_type = car_type
        self.passenger_weigh = 1200
        self.jeep_weigh = 1500
        self.cargo_weigh = 1800
        self.object = engine_v6
        self.objects = [wheel_1, wheel_2, wheel_3, wheel_4]


    def start_engine(self):
        engine = random.randint(1, 3)
        if engine != 1:
            print('The engine is not started')
        else:
            print('The engine is started')

    def move(self):
        # 100 = 100 kilometres. Check-in length
        if self.car_type == 'passenger':
            formula = (self.passenger_weigh + wheel_1.wheel_weigh) / self.generate_power() * 100
            print(formula)
        if self.car_type == 'jeep':
            formula = (self.jeep_weigh + wheel_3.wheel_weigh) / self.generate_power() * 100
            print(formula)
        if self.car_type == 'cargo':
            formula = (self.cargo_weigh + wheel_4.wheel_weigh) / self.generate_power() * 100
            print(formula)


car_1 = Car('v6', 'passenger')
car_1.start_engine()
car_1.move()
car_2 = Car('v8', 'jeep')
car_2.move()
car_3 = Car('v10', 'cargo')
car_3.move()