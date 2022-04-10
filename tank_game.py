import random
from typing import Sequence

class Gun():
    """
    Создается пушка. Предлагается ввести калибр пушки и и длину ствола.
    Обладает методом, с помощью которого можно узнать попал ли снаряд в цель.
    """
    def __init__(self, caliber: int, barrel_length: int) -> None:
        self.caliber = caliber
        self.barrel_length = barrel_length

    def is_on_target(self, dice=(random.randint(1, 6))) -> bool:
        if self.caliber * dice > 100:
            print('You hit the target!')
            return True
        else:
            print("You didn't hit the target!")
            return False


class Ammo():
    """
    Создается снаряд. Выбирается тип снаряда, тип пушки, принимается объект пушки.
    Обладает методом, который подсчитывает наносимый урон.
    """
    types_ammo = {1: 'high-explosive',
                   2: 'cumulative',
                   3: 'subcaliber'
    }

    def __init__(self, gun: Gun, type: int) -> None:
        self.gun = gun
        self.am_type = self.types_ammo[type]

    def get_damage(self):
        formula = self.gun.caliber * 3
        return formula

    def get_penetration(self):
        return self.gun.caliber


class HECatridge(Ammo):
    """Обладает собственным методом, который позволяет уничтожить вражеский танк
    с определенным порогом очков защиты, т.е. толщины брони."""
    def __init__(self, gun, type) -> None:
        super().__init__(gun, type)
        self.gun = gun
        self.type = type

    def get_damage(self):
        formula = self.gun.caliber * 3
        return formula

    def finish_off_stricken_enemy(self, coordinate_1: int, coordinate_2: int, thickness: int) -> None:
        print(f"Shoot at the enemy's stricken tank to finish it off\n"
              f"but you can only do this if the armor is pierced.\n"
              f"First of all you need to enter coordinates\n"
              f"You coordinates: {coordinate_1}, {coordinate_2} were received")
        chance = random.randint(1, 3)
        shoot = input(f"Enter 'yes' if you wanna shoot: ")
        if shoot == 'yes':
            if thickness > 100:
                print("You can't destroy the enemy if his armor more than 100!")
            elif chance == 1:
                 print('Your target was hit!')
            else:
                print("Your target wasn't pierced! Try again!")


class HEATCatridge(Ammo):
    """Обладает собственным методом, который позволяет выстрелить танку
    на короткой дистанции (меньше 5 километров), повышает эффективность выстрела.
    """
    def __init__(self, gun, type) -> None:
        super().__init__(gun, type)
        self.gun = gun
        self.type = type

    def get_damage(self):
        formula = (self.gun.caliber * 3) * 0.6
        return formula

    def take_shot_if_short_distance(self, distance: int) -> None:
        # Kilometres
        if distance > 5:
            print("You can't shoot if the distance is more than 5 kilometers!")
        else:
            print(f"You took a shoot!"
                  f"Your target was destroyed!")


class APCatridge(Ammo):
    """Обладает собственным методом, который позволяет выстрелить
     по среднебронированному танку, что повышает эффективность снаряда."""
    def __init__(self, gun, type) -> None:
        super().__init__(gun, type)
        self.gun = gun
        self.type = type

    def get_damage(self):
        formula = (self.gun.caliber * 3) * 0.3
        return formula

    def shot_medium_armored_tank(self, thickness):
        print('As you know subcaliber can destroy armor')
        input("Enter 'yes' if you want to shoot"
              f"but if armor of tank > 200 but less than 100 you won't shoot")
        # Привязать к броне как и все остальные методы.
        if thickness > 100 and thickness < 200:
            print('You target was destroyed!')
        else:
            print("You can't destroy this tank!")


class Armour():
    """
    Класс брони танка, имеет два поля, толщина и тип. Метод is_penetrated
    определяет пробита броня или нет.
    """
    def __init__(self, thickness: int, type: str) -> None:
        self.thickness = thickness
        self.type = type

    def is_penetrated(self, projectile: [HEATCatridge, HECatridge, APCatridge]) -> bool:
        if projectile.get_damage() > self.thickness:
            print('The armor was pierced!')
            return True
        else:
            print("The armor wasn't pierced!")
            return False


class HArmour(Armour):
    """
    Обладает методом который определяет пробита броня или нет.
    """
    def __init__(self, thickness, type: str) -> None:
        super().__init__(thickness, type)

    def is_penetrated(self, projectile: [HEATCatridge, HECatridge, APCatridge]):
        if projectile == HECatridge:
            if projectile.get_damage() > self.thickness * 1.2:
                print('The armor was pierced!')
        if projectile == HEATCatridge:
            if projectile.get_damage() > self.thickness * 1:
                print('The armor was pierced!')
        if projectile != HEATCatridge and HECatridge:
            if projectile.get_damage() > self.thickness * 0.7:
                print('The armor was pierced!')
            else:
                print("The armor wasn't pierced!")
        else:
            print("The armor wasn't pierced!")


if __name__ == '__main__':
    # my_projectile = HECatridge(Gun(100, 100), 1)
    # print(my_projectile.get_damage())
    # armor = HArmour(100, 'harmor')
    # armor.is_penetrated(HECatridge(Gun(10, 100), 1))
    # my_am = HECatridge(Gun(38, 50), 1)
    # my_am.finish_off_stricken_enemy(39, 49, 99)
