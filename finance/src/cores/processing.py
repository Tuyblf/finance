from src.cores.functions.credit import credits_sum
from src.cores.functions.capital import capital_sum



def monthly_payment ():
    principal_amount = int(input("Введите сумму долга: "))  # Сумма кредита
    annual_interest_rate = int(input("Введите годовую процентную ставку: "))  # Годовая процентная ставка
    loan_term_years = int(input("Введите срок кредита в годах: "))  # Срок кредита в годах

    monthly_payment = credits_sum(principal_amount, annual_interest_rate, loan_term_years)
    print(f"\nЕжемесячный платеж: {monthly_payment:.2f} рублей")



def capital_calculation ():
    income = int(input("Введите вашу зарплату (в месяц): "))
    debts = int(input("Введите общую сумму долгов: "))
    assets = int(input("Введите общую сумму активов: "))
    savings_rate = float(input("Введите процент от зарплаты, который вы откладываете (например, 0.2 для 20%): "))
    monthly_expenses = int(input("Введите ваши ежемесячные расходы: "))
    saving_period = int(input("Введите период накоплений в месяцах: "))

    net_worth, annual_savings, total_savings = capital_sum(
        income,
        debts,
        assets,
        savings_rate,
        monthly_expenses,
        saving_period
     )

    print(f"\nВаш капитал составляет: {net_worth} валюты.")
    print(f"Ваши годовые сбережения составляют: {annual_savings:.2f} рублей.")
    print(f"Ваши сбережения за {saving_period} месяцев составляют: {total_savings:.2f} рублей.")