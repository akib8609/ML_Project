import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle



from sklearn.tree import DecisionTreeRegressor



'''
def main():
    run_app()


if _name_ == "_main_":
    main()
'''
df = sns.load_dataset('mpg')

df.isnull().sum()
df.dropna(inplace= True)

x = df[['displacement', 'horsepower', 'weight','acceleration']]
y = df.mpg

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=42)

model = LinearRegression()   #odinary least square
model.fit(X_train,y_train)


filename = 'mpg_regression.sav'
pickle.dump(model, open(filename, 'wb'))
