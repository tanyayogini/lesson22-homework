# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, unit_type, speed=1):
        self._unit_type = unit_type
        self._speed = speed

    def _get_speed(self):
        if self._unit_type == 'is_fly':
            return self._speed * 1.2
        elif self._unit_type == 'crawl':
            return self._speed * 0.5
        else:
            return self._speed

    def move(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(x=self.x, y=self.y + speed, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(x=self.x, y=self.y - speed, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(x=self.x - speed, y=self.y, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(x=self.x + speed, y=self.y, unit=self)

#     ...
