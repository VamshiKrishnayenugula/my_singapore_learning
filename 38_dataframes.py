#the easiest way to create a dataframe from two lists is by using pandas

"""we have two lists , we have to use the zip() function to combine the lists
"""

import pandas as pd 

list1 = ['Tesla', 'Ford', 'Fiat']
models = ['X', 'Focus', 'Doblo']

col = ['brands','model']
df = pd.DataFrame(list(zip(list1, models)),index = [1,2,3],columns = col)

print(df)

print('add col to this dataframe')

df['age'] = [34,54,56]

print('latest dataframe is ')

print()

print(df)

print('drop method ')

"""inplace = True means we want the change to be made on the original dataframe
on  a dataframe , axis 1 means columns , os when we pass 1 to the azis parameter , we are dropping a column
"""

df.drop('brands',inplace=True, axis= 1)
print(df)