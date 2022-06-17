import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.cross_validation import train_test_split

from sklearn.datasets import load_boston
bos = load_boston()
print(bos)

df_x = pd.DataFrame(bos.data, columns=bos.feature_names)
df_y = pd.DataFrame(bos.target)

print(df_x)
print(df_y)

reg=linear_model.LinearRegression()

x_train,x_test,y_train,y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)
reg.fit(x_train, y_train)
reg.coef_
a = reg.predict(x_test)
print("*"*10)
print(a[0])
print(y_test)

# mean square error - To find the error 

print(np.mean((a-y_test)**2))