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

# ------------------------------- Task 2-------------------------------------
rand_num = random.randint(1, 5)
number_particip = (int(input(f"Hello. Welcome to the car races.\n"
                f"You can create your own car and take part in this competition.\n"
                f"However, first of all you need to name the number of participants. ")))
cars_particip = (f"Well {number_particip} participants will take part in this race.\n"
                 f"Now every participant can create his own car.\n"
                 f"So, you can create any car using available engines, wheels and car types.\n"
                 f"Available car types: passenger, jeep, cargo.\n"
                 f"Available engine types: v6, v8, v10.\n"
                 f"Available wheel: simple - 15 kilos\n"
                 f"So, your car were chosen! Let's start the race!")
print(cars_particip)


print('\n -------------------------------------------------------')
print('Ready...')
time.sleep(3)
print('Go!')
time.sleep(1)
print('*')
time.sleep(1)
print('***')
time.sleep(1)
print('*****')
print('The first participant is ahead!')
time.sleep(1)
print('*******')
time.sleep(1)
print('********')
print(f"Wow! It is surprise. The {rand_num} participant was overtaken!")
time.sleep(1)
print('**********')
time.sleep(1)
print('**************')
print(f"Halfway was gone by participant under the number {rand_num}!")
time.sleep(1)
print('*****************')
print('Other participants is overtaking others!')
time.sleep(1)
print('***********************')
print('The first participant has overtaken everyone!')
time.sleep(1)
print('***************************')
time.sleep(2)
print('*************************************')
time.sleep(2)
print('*********************************************')
time.sleep(2)
print('Each participant have a chance to win!')
print('*******************************************************')
time.sleep(2)
print('*************************************************************************')
time.sleep(2)
print('Who will win? We will see soon')
print('********************************************************************************')
time.sleep(3)
print('*************************************************************************************************()FINISH!!!!!()')
random_num = random.randint(1, 5)
print(f"Incredibly! The {random_num} participant successfully completed the race! You're a winner!\n"
      f"You can try again if other participants don't mind.")

