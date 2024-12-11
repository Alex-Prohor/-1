import doctest

class CarFuelTank:
    def __init__(self, tank_capacity: float, current_fuel: float):
        """
        Создание и подготовка к работе объекта "Бак автомобиля"

        :param tank_capacity: Общая вместимость бака в литрах
        :param current_fuel: Текущее количество топлива в литрах

        :raise TypeError: если параметры не типа int или float
        :raise ValueError: если вместимость или топливо отрицательные, или топливо превышает вместимость

        Примеры:
        >>> tank = CarFuelTank(50, 20)  # инициализация экземпляра класса
        """
        if not isinstance(tank_capacity, (int, float)):
            raise TypeError("Вместимость бака должна быть типа int или float")
        if tank_capacity <= 0:
            raise ValueError("Вместимость бака должна быть положительным числом")

        if not isinstance(current_fuel, (int, float)):
            raise TypeError("Количество топлива должно быть типа int или float")
        if current_fuel < 0:
            raise ValueError("Количество топлива не может быть отрицательным числом")
        if current_fuel > tank_capacity:
            raise ValueError("Текущее топливо не может превышать вместимость бака")

        self.tank_capacity = tank_capacity
        self.current_fuel = current_fuel

    def is_tank_empty(self) -> bool:
        """
        Проверка, пуст ли бак автомобиля.

        :return: True, если бак пуст; иначе False.

        Примеры:
        >>> tank = CarFuelTank(50, 0)
        >>> tank.is_tank_empty()
        True
        """
        return self.current_fuel == 0

    def add_fuel(self, fuel_amount: float) -> None:
        """
        Добавление топлива в бак автомобиля.

        :param fuel_amount: Объем добавляемого топлива в литрах
        :raise ValueError: Если добавляемое топливо превышает свободное место в баке или является отрицательным числом.

        Примеры:
        >>> tank = CarFuelTank(50, 30)
        >>> tank.add_fuel(15)
        >>> tank.current_fuel
        45
        """
        if not isinstance(fuel_amount, (int, float)):
            raise TypeError("Добавляемое топливо должно быть типа int или float")
        if fuel_amount <= 0:
            raise ValueError("Добавляемое топливо должно быть положительным числом")
        if self.current_fuel + fuel_amount > self.tank_capacity:
            raise ValueError("Добавляемое топливо превышает вместимость бака")

        self.current_fuel += fuel_amount

    def use_fuel(self, fuel_amount: float) -> float:
        """
        Использование топлива из бака автомобиля.

        :param fuel_amount: Объем используемого топлива в литрах
        :raise ValueError: Если используемое топливо больше, чем есть в баке или отрицательно.
        :return: Объем реально использованного топлива

        Примеры:
        >>> tank = CarFuelTank(50, 20)
        >>> tank.use_fuel(10)
        10
        >>> tank.current_fuel
        10
        """
        if not isinstance(fuel_amount, (int, float)):
            raise TypeError("Используемое топливо должно быть типа int или float")
        if fuel_amount <= 0:
            raise ValueError("Используемое топливо должно быть положительным числом")
        if fuel_amount > self.current_fuel:
            raise ValueError("Нельзя использовать больше топлива, чем есть в баке")

        self.current_fuel -= fuel_amount
        return fuel_amount


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

    if __name__ == "__main__":
        # Создаем экземпляр бака с объемом 50 литров и 20 литрами топлива
        tank = CarFuelTank(50, 20)

        # Проверяем, пуст ли бак
        print("Бак пустой?", tank.is_tank_empty())  # Ожидаем False

        # Добавляем 10 литров топлива
        tank.add_fuel(10)
        print("Текущий объем топлива:", tank.current_fuel)  # Ожидаем 30

        # Используем 5 литров топлива
        tank.use_fuel(5)
        print("Остаток топлива:", tank.current_fuel)  # Ожидаем 25