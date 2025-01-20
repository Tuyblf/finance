def credits_sum (loan_sum, loan_term, apr):

    """
    Функция для расчета ежемесячного платежа по кредиту.

    :param loan_sum: Сумма кредита (основной долг)
    :param apr: Годовая процентная ставка (в процентах)
    :param loan_term: Срок кредита в годах
    :return: Ежемесячный платеж
    """

    monthly_rate = apr / 100 / 12  # Преобразуем годовую ставку в месячную
    number_of_payments = loan_term * 12  # Общее количество платежей

    # Формула для расчета ежемесячного платежа
    monthly_payment = (loan_sum * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments)

    return monthly_payment