salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
months_for_answer=months

while months > 0 :
    money_capital += (spend)
    money_capital -= (salary)
    spend *= (1 + increase)
    if money_capital > 0:
        months -= 1

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months_for_answer} месяцев без долгов:", int(money_capital))
