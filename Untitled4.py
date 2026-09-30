# задание 6
import numpy as np, matplotlib.pyplot as plt
f = lambda x: (x - 3) ** 2
df = lambda x: 2 * (x - 3)
x, lr, path = 10.0, 0.1, []
for i in range(30):
    path.append(x); x = x - lr * df(x)
print(x)
xs = np.linspace(-2, 12, 100); plt.plot(xs, f(xs)); plt.scatter(path, [f(p) for p in path], c='r'); plt.show()

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, lr in zip(axes, [0.01, 0.1, 1.1]):
    x, path = 10.0, []
    for i in range(30):
        path.append(x)
        x = x - lr * df(x)
    xs = np.linspace(-2, 12, 100)
    ax.plot(xs, f(xs))
    ax.scatter(path, [f(p) for p in path], c='r', s=20)
    ax.set_title(f'lr = {lr}')
plt.show()

rng = np.random.default_rng(0)
X = rng.uniform(0, 5, 50)
y = 2 * X + 1 + rng.normal(0, 0.5, 50)
plt.scatter(X, y); plt.show()

def loss(w, b): return np.mean((w * X + b - y) ** 2)
def grads(w, b):
    p = w * X + b
    return np.mean(2 * (p - y) * X), np.mean(2 * (p - y))

w, b, lr, hist = 0.0, 0.0, 0.05, []
for i in range(200):
    dw, db = grads(w, b); w -= lr * dw; b -= lr * db; hist.append(loss(w, b))
print(w, b)
plt.plot(hist); plt.show()
plt.scatter(X, y); plt.plot(X, w * X + b, 'r'); plt.show()

from sklearn.linear_model import LinearRegression
lr_sk = LinearRegression().fit(X.reshape(-1, 1), y)
print("sklearn:", lr_sk.coef_[0], lr_sk.intercept_)
print("наш GD: ", w, b)

# повторение
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Генерируем данные: y = 2x² - 3x + 1 + шум
rng = np.random.default_rng(0)
X = rng.uniform(-3, 3, 100)
y = 2 * X**2 - 3 * X + 1 + rng.normal(0, 1, 100)

plt.scatter(X, y, s=15)
plt.title('Данные: парабола + шум')
plt.show()

# 2. Loss и градиенты для p = a·x² + b·x + c
def loss(a, b, c):
    p = a * X**2 + b * X + c
    return np.mean((p - y) ** 2)

def grads(a, b, c):
    p = a * X**2 + b * X + c
    err = 2 * (p - y)
    da = np.mean(err * X**2)
    db = np.mean(err * X)
    dc = np.mean(err)
    return da, db, dc

# 3. Обучение
a, b, c = 0.0, 0.0, 0.0
lr = 0.01
hist = []

for i in range(2000):
    da, db, dc = grads(a, b, c)
    a -= lr * da
    b -= lr * db
    c -= lr * dc
    hist.append(loss(a, b, c))

print(f"Наши параметры:  a={a:.3f}, b={b:.3f}, c={c:.3f}")

# 4. График loss
plt.plot(hist)
plt.xlabel('шаг'); plt.ylabel('loss')
plt.title('Loss падает')
plt.show()

# 5. Прямая поверх точек
xs = np.linspace(-3, 3, 100)
plt.scatter(X, y, s=15, label='данные')
plt.plot(xs, a * xs**2 + b * xs + c, 'r', label='наша парабола')
plt.legend()
plt.show()

# 6. Сверка со sklearn (полиномиальные признаки)
X_poly = np.column_stack([X**2, X])
lr_sk = LinearRegression().fit(X_poly, y)
print(f"sklearn:         a={lr_sk.coef_[0]:.3f}, b={lr_sk.coef_[1]:.3f}, c={lr_sk.intercept_:.3f}")