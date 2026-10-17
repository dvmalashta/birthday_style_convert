from datetime import date

# Шаблоны цифр в стиле «электронного табло» 
DIGIT_PATTERNS = {
    '0': [
        " *** ",
        "*   *",
        "*   *",
        "*   *",
        "*   *",
        "*   *",
        " *** "
    ],
    '1': [
        "  *  ",
        " **  ",
        "  *  ",
        "  *  ",
        "  *  ",
        "  *  ",
        " *** ",
    ],
    '2': [
        " ***  ",
        "*   * ",
        "    * ",
        "  **  ",
        " *    ",
        "*     ",
        "****  "
    ],
    '3': [
        " ***  ",
        "*   * ",
        "    * ",
        "  *** ",
        "    * ",
        "*   * ",
        " ***  "
    ],
    '4': [
        "*   * ",
        "*   * ",
        "*   * ",
        "***** ",
        "    * ",
        "    * ",
        "    * "
    ],
    '5': [
        "***** ",
        "*     ",
        "*     ",
        " ***  ",
        "    * ",
        "*   * ",
        " ***  "
    ],
    '6': [
        " ***  ",
        "*     ",
        "*     ",
        "****  ",
        "*   * ",
        "*   * ",
        " ***  "
    ],
    '7': [
        "***** ",
        "    * ",
        "   *  ",
        "  *   ",
        " *    ",
        "*     ",
        "*     "
    ],
    '8': [
        " ***  ",
        "*   * ",
        "*   * ",
        " ***  ",
        "*   * ",
        "*   * ",
        " ***  "
    ],
    '9': [
        " ***  ",
        "*   * ",
        "*   * ",
        " **** ",
        "    * ",
        "    * ",
        " ***  "
    ]
}

# Шаблон точки
DOT_PATTERN = [
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    "*"
]

def is_leap_year(year: int) -> bool:
    """Определяет, високосный ли год."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_day_of_week(day: int, month: int, year: int) -> str:
    """Возвращает день недели для указанной даты."""
    d = date(year, month, day)
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[d.weekday()]

def calculate_age(day: int, month: int, year: int) -> int:
    """Вычисляет возраст пользователя на сегодня."""
    today = date.today()
    age = today.year - year
    if (month, day) > (today.month, today.day):
        age -= 1
    return age

def draw_date_with_stars(day: int, month: int, year: int) -> None:
    """Рисует дату в формате дд.мм.гггг символами * с точками между группами."""
    d_str = f"{day:02d}"
    m_str = f"{month:02d}"
    y_str = str(year)

    for row in range(7):
        line_parts = []

        # День (2 цифры)
        for ch in d_str:
            line_parts.append(DIGIT_PATTERNS[ch][row])

        # Точка после дня (пробел + точка + пробел)
        line_parts.append(" ")
        line_parts.append(DOT_PATTERN[row])
        line_parts.append(" ")

        # Месяц (2 цифры)
        for ch in m_str:
            line_parts.append(DIGIT_PATTERNS[ch][row])

        # Точка после месяца (пробел + точка + пробел)
        line_parts.append(" ")
        line_parts.append(DOT_PATTERN[row])
        line_parts.append(" ")

        # Год (4 цифры)
        for ch in y_str:
            line_parts.append(DIGIT_PATTERNS[ch][row])

        print("".join(line_parts))

def main():
    print("Программа расчёта данных о дате рождения и стилизации даты.")

    while True:
        try:
            day = int(input("Введите день рождения (1–31): "))
            month = int(input("Введите месяц рождения (1–12): "))
            year = int(input("Введите год рождения (например, 1990): "))

            if not (1 <= day <= 31) or not (1 <= month <= 12) or year < 1900:
                print("Пожалуйста, введите корректные значения (день 1–31, месяц 1–12, год >= 1900).")
                continue

            try:
                _ = date(year, month, day)
            except ValueError:
                print("Такая дата не существует (например, 30 февраля). Попробуйте ещё раз.")
                continue

            break
        except ValueError:
            print("Вводите только целые числа.")

    day_of_week = get_day_of_week(day, month, year)
    leap = is_leap_year(year)
    age = calculate_age(day, month, year)

    print(f"\nДата: {day:02d}.{month:02d}.{year}")
    print(f"День недели: {day_of_week}")
    print(f"Год был {'високосным' if leap else 'не високосным'}.")
    print(f"Ваш возраст: {age} лет.")
    print("\nДата в стиле электронного табло:")
    draw_date_with_stars(day, month, year)

    input("\nНажмите Enter, чтобы закрыть программу...")

if __name__ == "__main__":
    main()
