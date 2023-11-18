def calculate_water_mass(radius, height):
    # Плотность воды (приблизительно 1 кг/литр)
    density_water = 1000.0
    # Объем цилиндра
    volume = 3.14159 * radius**2 * height
    # Масса воды
    mass = volume * density_water / 1000.0  
    # Переводим объем из кубических сантиметров в литры
    return round(mass, 2)
# Пример использования
radius_cylinder = 2.0
height_cylinder = 5.0
water_mass = calculate_water_mass(radius_cylinder, height_cylinder)
print("Масса воды в цилиндре:", water_mass, "кг")