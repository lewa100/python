import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

#print(pd.get_dummies(data['whoAmI']))

data['robot'] = False
data['human'] = False

data.loc[data['whoAmI'] == 'robot', 'robot'] = True
data.loc[data['whoAmI'] == 'human', 'human'] = True
print(data)