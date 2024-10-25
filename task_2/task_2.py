import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt


# Функція, яку потрібно інтегрувати
def f(x):
    return x**2


# Межі інтегрування
a = 0  # нижня межа
b = 2  # верхня межа

# Кількість випадкових точок для методу Монте-Карло
N = 10000

# Метод Монте-Карло для обчислення інтегралу
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, max(f(x_random)), N)
under_curve = y_random < f(x_random)
monte_carlo_area = (b - a) * max(f(x_random)) * np.sum(under_curve) / N

# Перевірка точності за допомогою функції quad
result_quad, error = spi.quad(f, a, b)

# Візуалізація
x = np.linspace(a, b, 400)
y = f(x)

fig, ax = plt.subplots()

# Графік функції
ax.plot(x, y, "r", linewidth=2)
ax.fill_between(x, 0, y, color="gray", alpha=0.3, label="Аналітичний інтеграл")

# Випадкові точки для методу Монте-Карло
ax.scatter(x_random, y_random, s=1, color="blue", alpha=0.5, label="Випадкові точки")

# Налаштування графіка
ax.set_xlim([a - 0.5, b + 0.5])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Метод Монте-Карло для обчислення інтегралу f(x) = x^2 від 0 до 2")
ax.legend()
plt.grid()
plt.show()

print(f"Метод Монте-Карло : {monte_carlo_area}")
print(f"Аналітичне обчислення : {result_quad}")
print(f"Похибка : {error}")
