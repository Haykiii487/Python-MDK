# задание 5
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
X, y = load_iris(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=.25, random_state=0)
knn = KNeighborsClassifier(3).fit(X_tr, y_tr)
pred = knn.predict(X_te)
print(pred[:5], y_te[:5], 'accuracy:', accuracy_score(y_te, pred))

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

X, y = load_iris(return_X_y=True)
X_vis = X[:, [2, 3]]  # длина и ширина лепестка

# Обучаем kNN на этих двух признаках
knn = KNeighborsClassifier(3).fit(X_vis, y)

# Новая точка и её 3 соседа
new = [[4.5, 1.5]]
dist, idx = knn.kneighbors(new)
print("Классы соседей:", y[idx[0]], "→ предсказание:", knn.predict(new)[0])

# Рисуем
plt.scatter(X_vis[:, 0], X_vis[:, 1], c=y, cmap='viridis', edgecolor='k')
plt.scatter(new[0][0], new[0][1], c='red', marker='*', s=300)
plt.scatter(X_vis[idx[0], 0], X_vis[idx[0], 1], s=200, facecolors='none', edgecolors='red', linewidths=2)
plt.xlabel('Длина лепестка'); plt.ylabel('Ширина лепестка')
plt.show()

import pandas as pd
from sklearn.linear_model import LogisticRegression
df = pd.read_csv('clean.csv')
feats = ['pclass', 'age', 'fare', 'family', 'sex_num']
X_tr, X_te, y_tr, y_te = train_test_split(df[feats], df['survived'], test_size=.25, random_state=0)
lr = LogisticRegression(max_iter=1000).fit(X_tr, y_tr)
print('accuracy:', lr.score(X_te, y_te), 'baseline:', (y_te == 0).mean())

from sklearn.metrics import confusion_matrix, classification_report
print(confusion_matrix(y_te, lr.predict(X_te)))
print(classification_report(y_te, lr.predict(X_te)))

new = pd.DataFrame([[1, 25, 80, 0, 1]], columns=feats)
print(lr.predict(new), lr.predict_proba(new))

# повторение
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=.25, random_state=0)

for k in [1, 5, 15]:
    knn = KNeighborsClassifier(k).fit(X_tr, y_tr)
    acc = accuracy_score(y_te, knn.predict(X_te))
    print(f"k={k}: accuracy = {acc:.4f}")