import datetime

def get_day_of_week(day, month, year):
    date = datetime.date(year, month, day)
    days = ["Понедельник", "Вторник", "Среда", "Четверг",
            "Пятница", "Суббота", "Воскресенье"]
    return days[date.weekday()]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_age(day, month, year):
    today = datetime.date.today()
    birth = datetime.date(year, month, day)
    age = today.year - birth.year
    if (today.month, today.day) < (birth.month, birth.day):
        age -= 1
    return age

# Шаблоны цифр 5x5 из звёздочек
DIGITS = {
    '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
    '1': ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
    '2': [" *** ", "*   *", "   * ", "  *  ", "*****"],
    '3': [" *** ", "*   *", "  ** ", "*   *", " *** "],
    '4': ["*   *", "*   *", "*****", "    *", "    *"],
    '5': ["*****", "*    ", "**** ", "    *", "**** "],
    '6': [" *** ", "*    ", "**** ", "*   *", " *** "],
    '7': ["*****", "    *", "   * ", "  *  ", " *   "],
    '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
    '9': [" *** ", "*   *", " ****", "    *", " *** "],
    '.': ["     ", "     ", "     ", "     ", "  *  "],
    ' ': ["     ", "     ", "     ", "     ", "     "],
}

def print_stars_date(day, month, year):
    text = f"{day:02d} {month:02d} {year:04d}"
    for row in range(5):
        line = "  ".join(DIGITS[ch][row] for ch in text)
        print(line)

def main():
    day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))
    year = int(input("Введите год рождения: "))

    print(f"\nДень недели: {get_day_of_week(day, month, year)}")
    print(f"Високосный год: {'Да' if is_leap_year(year) else 'Нет'}")
    print(f"Возраст: {calculate_age(day, month, year)}")
    print("\nДата рождения на табло:")
    print_stars_date(day, month, year)

if __name__ == "__main__":
    main()