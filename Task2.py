import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

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
n = 100000  # Кількість точок

# Генерація випадкових точок всередині прямокутника
x_random = np.random.uniform(a, b, n)
y_random = np.random.uniform(0, f(b), n)

# Обчислення кількості точок, які потрапили під криву
count_under_curve = np.sum(y_random < f(x_random))

# Обчислення відношення площі під кривою до площі прямокутника
integral_approx = count_under_curve / n * (b - a) * f(b)

print("Значення інтеграла за допомогою методу Монте-Карло:", integral_approx)

# Обчислення значення інтеграла аналітично
integral_analytical, _ = quad(f, a, b)
print("Аналітичне значення інтеграла:", integral_analytical)
