from smartphone import Smartphone

catalog = [
    Smartphone("Sony", "AX", "+79001122334"),
    Smartphone("Samsung", "Note10", "+79001122333"),
    Smartphone("Nokia", "i900", "+79005522333"),
    Smartphone("Samsung", "x224", "+79005555555"),
    Smartphone("Nokia", "i700", "+79005522222")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.sub_number}.")
