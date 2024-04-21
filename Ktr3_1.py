# Определение класса Phone
class Phone:
    def __init__(self, name, brand, year, price, features, stars):
        self.name = name
        self.brand = brand
        self.year = year
        self.price = price
        self.features = features
        self.stars = stars


def input_phones():
    phones = []
    print("Введите данные телефонов")
    for i in range(3):
        data = input(
            f"Введите данные телефона {i + 1} (модель, производитель, год выпуска, цена, характеристики, рейтинг через запятую): ")
        name, brand, year, price, features, stars = data.split(",")
        year = int(year)
        price = float(price)
        stars = float(stars)
        phones.append(Phone(name.strip(), brand.strip(), year, price, features.strip(), stars))
    phones.sort(key=lambda phone: phone.name)
    return phones


def print_highly_rated_phones(phones):
    found = False
    print("Телефоны с высоким рейтингом:")
    for phone in phones:
        if phone.stars >= 4:
            print(
                f"{phone.name}, {phone.brand}, ({phone.year}), Цена: {phone.price}$, Характеристики: {phone.features}, Рейтинг: {phone.stars}")
            found = True
    if not found:
        print("Телефонов с высоким рейтингом не найдено.")

def filter_by_brand(phones, brand):
    filtered_phones = [phone for phone in phones if phone.brand == brand]
    return filtered_phones

def sort_by_price(phones):
    sorted_phones = sorted(phones, key=lambda phone: phone.price)
    return sorted_phones

def print_brand_filtered_phones(phones):
    brand = input('Введите название компании для сортировки: ')
    filtered_phones = filter_by_brand(phones, brand)
    print(f"Телефоны компании {brand}:")
    if filtered_phones:
        for phone in filtered_phones:
            print(phone.name)
    else:
        print("Телефонов данной компании не найдено.")

def print_sorted_by_price(phones):
    sorted_phones = sort_by_price(phones)
    print("\nТелефоны, отсортированные по цене:")
    if sorted_phones:
        for phone in sorted_phones:
            print(f"{phone.name}: {phone.price}$")
    else:
        print("Телефонов не найдено.")

def main():
    phones = input_phones()
    print_highly_rated_phones(phones)
    print_brand_filtered_phones(phones)
    print_sorted_by_price(phones)


if __name__ == "__main__":
    main()


# Заполнение экземпляров класса Phone
# "Galaxy S23", "Samsung", 2021, 999, "120Hz display Exynos 2100 Chipset", 5
# "iPhone 12", "Apple", 2020, 799, "5G OLED display A14 Bionic Chip", 4.5
# "Xiaomi 12", "OnePlus", 2021, 969, "Fluid AMOLED display Snapdragon 888", 3
#
# "Galaxy S21", "Samsung", 2021, 999, "120Hz display Exynos 2100 Chipset", 4.5)
# "OnePlus 9 Pro", "OnePlus", 2021, 969, "Fluid AMOLED display Snapdragon 888", 4
# "iPhone 13", "Apple", 2022, 999, "5G OLED display A14 Bionic Chip", 5
