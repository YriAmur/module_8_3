class Car:
    def __init__(self, model, vin_number, numbers):
        if self.__is_valid_vin(vin_number) and self.__is_valid_numbers(numbers):
            self.model = model
            self.__vin = vin_number
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int) is False:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin_number not in range(1000000, 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str) is False:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True

    def say_info(self):
        return ('Марка модели: %s, vin: %s, номер: %s' %(self.model, self.__vin, self.__numbers))

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
    print(f'{first.model} успешно создан')
    #print(f'Инфо: {first.say_info()}')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')
    #print(f'Инфо: {second.say_info()}')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
    #print(f'Инфо: {third.say_info()}')