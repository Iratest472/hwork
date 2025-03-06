def month_to_season(month_if):
    if month_if in [1, 2, 12]:
        return "Зима"
    elif month_if in [3, 4, 5]:
        return "Весна"
    elif month_if in [6, 7, 8]:
        return "Лето"
    elif month_if in [9, 10, 11]:
        return "Осень"


month = int(input("Введите номер месяца:"))
season = month_to_season(month)
print("Сезон:", season)
