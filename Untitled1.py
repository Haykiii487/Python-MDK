x = 5
name = 'Аня'
nums = [3, 1, 4, 1, 5]
person = {'name': 'Аня', 'age': 19}
print(type(x), type(name), type(nums), type(person))
print(nums[0], nums[-1], len(nums), sum(nums) / len(nums))
print(person['name'])

def mean(lst):
    total = 0
    for v in lst:
        total += v
    return total / len(lst)
 
def minmax(lst):
    lo, hi = lst[0], lst[0]
    for v in lst:
        if v < lo: lo = v
        if v > hi: hi = v
    return lo, hi

def mediana(lst):
 s = sorted(lst) # сортровка копии списка
 n = len(s) # длина
 mid = n // 2 # середина
 if n % 2 == 1: # проверяет кол во чисел в списке
    return s[mid] # возврат элемента списка по индексу 
 return (s[mid-1]+ s[mid]) / 2 # возвращает медиану 






 
print(mean([3, 1, 4]), minmax([3, 1, 4])), print(mediana([3, 1, 4]))

with open('titanic.csv', encoding='utf-8') as f:
    header = f.readline().strip().split(',')
    rows = [line.strip().split(',') for line in f]
print(header)
print(len(rows), 'строк')
print(rows[0])

cols = {h: [] for h in header}
for r in rows:
    for h, v in zip(header, r):
        if v == '':
            continue
        try:
            cols[h].append(float(v))
        except ValueError:
            cols[h].append(v)
print(cols['age'][:10])

for h, vals in cols.items():
    if not vals:
        continue
    if isinstance(vals[0], float):
        lo, hi = minmax(vals)
        print(f'{h:12s} n={len(vals):4d} mean={mean(vals):8.2f} min={lo:6.1f} max={hi:6.1f}')
    else:
        print(f'{h:12s} n={len(vals):4d} unique={len(set(vals))}')

        print("median =", mediana(cols['age'])) # выводит медиану 
# 3 Задание NumPy
        import numpy as np
a = np.array([3, 1, 4, 1, 5])
print(a * 2, a + 10, a ** 2)
print(a.mean(), a.min(), a.max(), a.sum())

M = np.arange(12).reshape(3, 4)
print(M, M.shape)
print('строка 0:', M[0]); print('столбец 1:', M[:, 1]); print('элемент:', M[2, 3])
print(M.T.shape)

print(M.mean(axis=0))  # 4 числа
print(M.mean(axis=1))  # 3 числа

A = np.array([[1, 2, 3], [4, 5, 6]])  # (2, 3)
w = np.array([[1], [0], [-1]])          # (3, 1)
print(A @ w)                            # (2, 1)
print(A + np.array([10, 20, 30]))

rng = np.random.default_rng(0)
X = rng.normal(size=(100, 5))
w = np.array([0.5, -1.0, 2.0, 0.0, 1.5]); b = 0.3
y = X @ w + b
print(X.shape, w.shape, y.shape, y[:5])

ages = np.array(cols['age'])  # Превращаем столбец в numpy-массив

# Считаем все три метрики одной строкой
mean_age, min_age, max_age = ages.mean(), ages.min(), ages.max()

print(f"Mean: {mean_age}, Min: {min_age}, Max: {max_age}")