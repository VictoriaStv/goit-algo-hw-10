import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.stats import qmc

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Визначення функції
def f(x):
    return x ** 2

# Визначення меж інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа
n = 10000  # Кількість точок

# Генерація квазірандомних точок всередині прямокутника з використанням послідовності Соболя
x_random = qmc.Sobol(1).random(n)
x_random = a + (b - a) * x_random.flatten()

# Обчислення значення функції в отриманих точках
y_random = f(x_random)

# Обчислення площі під кривою
integral_approx = np.mean(y_random) * (b - a)

print("Значення інтеграла за допомогою методу Монте-Карло:", integral_approx)

# Обчислення значення інтеграла аналітично
integral_analytical, _ = quad(f, a, b)
print("Аналітичне значення інтеграла:", integral_analytical)
