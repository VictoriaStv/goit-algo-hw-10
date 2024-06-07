from pulp import *

# Ініціалізуємо змінні
limonad = LpVariable("Limonad_units", lowBound=0, cat='Integer')
fruit_juice = LpVariable("Fruit_Juice_units", lowBound=0, cat='Integer')

# Ініціалізуємо задачу максимізації
prob = LpProblem("Maximize_Production", LpMaximize)

# Обмеження на ресурси
prob += 2 * limonad + fruit_juice <= 100  # обмеження на воду
prob += limonad + fruit_juice <= 50       # обмеження на цукор
prob += limonad <= 30                     # обмеження на лимонний сік
prob += 2 * fruit_juice <= 40             # обмеження на фруктове пюре

# Функція максимізації
prob += limonad + fruit_juice

# Вирішуємо задачу
prob.solve()

# Виводимо результати
print("Кількість одиниць Лимонаду потрібно виробити для максимізації загальної кількості продуктів: ", value(limonad))
print("Кількість одиниць Фруктового соку потрібно виробити для максимізації загальної кількості продуктів: ", value(fruit_juice))
print("Загальна кількість вироблених напоїв: ", value(limonad) + value(fruit_juice))