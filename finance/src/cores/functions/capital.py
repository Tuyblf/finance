def capital_sum (income, debts, assets, savings_rate, monthly_expenses, saving_period):

    """
    Вычисляет капитал человека, учитывая зарплату, долги, активы и расходы.

    :param income: Зарплата или другие доходы (в месяц)
    :param debts: Общая сумма долгов
    :param assets: Общая сумма активов
    :param savings_rate: Процент от зарплаты, который человек откладывает (в виде десятичной дроби)
    :param monthly_expenses: Общие ежемесячные расходы
    :param saving_period: Период накоплений в месяцах
    :return: Чистая стоимость (капитал), годовые сбережения и сбережения за указанный период
    """

    # Расчет годовых сбережений
    monthly_savings = income * savings_rate - monthly_expenses
    if monthly_savings < 0:
        monthly_savings = 0  # Нельзя откладывать отрицательную сумму

    annual_savings = monthly_savings * 12
    total_savings = monthly_savings * saving_period

    # Чистая стоимость = Активы - Долги
    net_worth = assets - debts

    return net_worth, annual_savings, total_savings