print("Добрый день! Мы будем рады видеть вас на нашей онлайн-конференции 20 марта!")
print("\nСтоимость билетов на мероприятие по тарифам:")
print('\n"Детский" до 18 лет - бесплатно')
print('"Молодёжный" от 18 до 25 лет - 990 рублей')
print('"Взрослый" от 25 лет - 1390 рублей')
print("\n!!!При покупке 3-х билетов и более предоставляется скидка 10% от стоимости заказа!!!")

tickets = int(input("Пожалуйста, введите количество билетов, которое вы хотите приобрести на мероприятие:"))
S = 0
price = 0
for price in range(1, tickets + 1 ):
    age = int(input("Введите, пожалуйста, возраст посетителя конференции для выписки билета:"))
    if 0 <= age <= 18:
        price = 0
    elif 18 <= age <= 25:
        price = 990
    elif 25 <= age <= 99:
        price = 1390
    else:
        print("Пожалуйста, введите корректный возраст посетителя!:")
    if tickets >= 3:
        S = S + price * 0.9
    else:
        S = S + price
print("Общая стоимость к оплате составила:", S)
