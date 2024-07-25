import numpy as np
import pandas as pd
import wooldridge

import pandas as pd
from sklearn import linear_model

# 导入数据
df = wooldridge.data('wage1')
df = df[['wage','educ','exper','tenure']]

# 建立线性回归模型
X = df[['exper','tenure']]  # 保持自变量为二维数组
y = df['educ']
model = linear_model.LinearRegression().fit(X, y)

# 输出模型参数
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)

# 输出模型评估指标
r_squared = model.score(X, y)
print("R-squared:", r_squared)
print("n:",len(df))

# 获取模型预测值
y_pred = model.predict(X)

# 计算残差
residuals = y - y_pred

# 将残差添加到DataFrame中
df['r1'] = residuals
# 建立线性回归模型
X = df[['r1']]  # 保持自变量为二维数组
y = df['wage']
y = np.log(y)
model = linear_model.LinearRegression().fit(X, y)

# 输出模型参数
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)

# 输出模型评估指标
r_squared = model.score(X, y)
print("R-squared:", r_squared)
print("n:",len(df))