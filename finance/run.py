from src.cores.processing import monthly_payment
from src.cores.processing import capital_calculation



print("Здравствуйте, вас приветствует программа, способная рассчитывать сумму кредита, общий капитал и т.п.!\n"
      "Выберете один из интересующих вас вариантов:\n"
      "1. Расчитать долг\n"
      "2. Вычеслить общий капитал\n"
      "3. Выход")

while True:
      response_value = input("\nВыберите интересующую задачу: ")

      try:
            response_value = int(response_value)

      except ValueError:
            print("Пожалуйста, введите корректные числовые значения!")
            continue

      if response_value == 1:
            monthly_payment ()
            continue

      elif response_value == 2:
            capital_calculation ()
            continue

      elif response_value == 3:
            print("До встречи!")
            break

      else:
            print("Неправильный номер операции!")