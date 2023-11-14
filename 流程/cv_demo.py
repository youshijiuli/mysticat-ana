from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 1.获取数据
iris = load_iris()


# 2.数据集合划分
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=1
)

# 3.特征工程数据预处理

transfer = StandardScaler()
X_train = transfer.fit_transform(X_train)
X_test = transfer.transform(X_test)


# 4.模型实例化
estimator = KNeighborsClassifier()

param_grid = {"n_neighbors": [1, 3, 5, 7]}
estimator = GridSearchCV(estimator, param_grid=param_grid, cv=5)

estimator.fit(X_train, y_train)


# 5.模型评估
# 5.1 预测值结果输出
y_pre = estimator.predict(X_test)
print("预测值是:\n", y_pre)
print("预测值和真实值的对比是:\n", y_pre == y_test)

# 5.2 准确率计算
score = estimator.score(X_test, y_test)
print("准确率为:\n", score)

# 5.3 查看交叉验证,网格搜索的一些属性
print("在交叉验证中,得到的最好结果是:\n", estimator.best_score_)
print("在交叉验证中,得到的最好的模型是:\n", estimator.best_estimator_)
print("在交叉验证中,得到的模型结果是:\n", estimator.cv_results_)

# 准确率为:
#  1.0
# 在交叉验证中,得到的最好结果是:
#  0.9416666666666668