from pulp import LpProblem, LpVariable, LpMaximize, LpStatus, value

# Створюємо задачу лінійного програмування для максимізації виробництва
model = LpProblem("Optimization_of_Production", LpMaximize)

# Змінні: кількість вироблених Лимонаду (x1) і Фруктового соку (x2)
x1 = LpVariable("Lemonade", lowBound=0, cat="Continuous")
x2 = LpVariable("Fruit_Juice", lowBound=0, cat="Continuous")

# Цільова функція: максимізувати загальну кількість вироблених одиниць
model += x1 + x2, "Total_Production"

# Обмеження ресурсів
# Вода: 2 * x1 (для лимонаду) + 1 * x2 (для фруктового соку) <= 100
model += 2 * x1 + 1 * x2 <= 100, "Water_Constraint"

# Цукор: 1 * x1 <= 50
model += 1 * x1 <= 50, "Sugar_Constraint"

# Лимонний сік: 1 * x1 <= 30
model += 1 * x1 <= 30, "Lemon_Juice_Constraint"

# Фруктове пюре: 2 * x2 <= 40
model += 2 * x2 <= 40, "Fruit_Puree_Constraint"

# Розв'язання задачі
model.solve()

# Результати
results = {
    "Status": LpStatus[model.status],
    "Lemonade": x1.varValue,
    "Fruit_Juice": x2.varValue,
    "Total Production": value(model.objective),
}

print(results)
