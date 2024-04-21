# Определение класса Phone
class Phone:
    def __init__(self, name, brand, year, price, features, stars):
        self.name = name
        self.brand = brand
        self.year = year
        self.price = price
        self.features = features
        self.stars = stars

    def __str__(self):
        return f"{self.name}, {self.brand}, ({self.year}), Цена: {self.price}$, Характеристики: {self.features}, Рейтинг: {self.stars}"

def filter_by_brand(phones, brand):
    filtered_phones = [phone for phone in phones if phone.brand == brand]
    return filtered_phones

def sort_by_price(phones):
    sorted_phones = sorted(phones, key=lambda phone: phone.price)
    return sorted_phones

def sort_by_year(phones):
    sorted_phones = sorted(phones, key=lambda phone: phone.year)
    return sorted_phones

def main(phones):
    print("\nТелефоны с высоким рейтингом:")
    for phone in phones:
        if phone.stars >= 4:
            print(phone)
    brand = input('Введите название компании для сортировки: ')
    filtered_phones = filter_by_brand(phones, brand)
    print(f"\nТелефоны компании {brand}:")
    if filtered_phones:
        for phone in filtered_phones:
            print(phone)
    else:
        print("Телефонов данной компании не найдено.")

    sorted_phones = sort_by_price(phones)
    print("\nТелефоны, отсортированные по цене:")
    if sorted_phones:
        for phone in sorted_phones:
            print(phone)
    else:
        print("Телефонов не найдено.")

    sorted_phones_by_year = sort_by_year(phones)
    print("\nТелефоны, отсортированные по году выпуска:")
    if sorted_phones_by_year:
        for phone in sorted_phones_by_year:
            print(phone)
    else:
        print("Телефонов не найдено.")

if __name__ == "__main__":
    phones = [
        Phone("Galaxy S23", "Samsung", 2021, 999, "120Hz display Exynos 2100 Chipset", 5),
        Phone("iPhone 12", "Apple", 2020, 799, "5G OLED display A14 Bionic Chip", 4.5),
        Phone("Xiaomi 12", "OnePlus", 2021, 969, "Fluid AMOLED display Snapdragon 888", 3),
        Phone("Galaxy S21", "Samsung", 2021, 999, "120Hz display Exynos 2100 Chipset", 4.5),
        Phone("OnePlus 9 Pro", "OnePlus", 2021, 969, "Fluid AMOLED display Snapdragon 888", 4),
        Phone("iPhone 13", "Apple", 2022, 999, "5G OLED display A14 Bionic Chip", 5)
    ]
    main(phones)