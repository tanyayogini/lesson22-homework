# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, room, population):
        self._room = room
        self._city_population = population

    def get_room(self):
        return self._room

    def get_city_population(self):
        return self._city_population




# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

person = Person(42, 100500)
print(person.get_room(), person.get_city_population())
