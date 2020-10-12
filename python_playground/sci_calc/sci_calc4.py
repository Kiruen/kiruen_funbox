import numpy as np
import pandas as pd

data = pd.Series(range(1, 10, 1), index=(str(chr(c)) for c in range(70, 79)))
print(data)
print(data['M'])
print()

data = pd.Series({'k':3, 'f':66.0, 'a':77, 't':777})
print(data)
print(data['f':'t'])

data1 = pd.Series({3:22, 1:66, 2:77})
print(data)

ages = {'k':1, 'a':22}
heights = {'k':111, 'a':222}
df = pd.DataFrame({'age':ages, 'height':ages})
print(df)
print(df.columns)
print(df['age'])

print( pd.DataFrame(({f'col{2 * i}':i, f'col{2 * i + 1}':i ** 2} for i in range(0, 5))) )

print(pd.DataFrame(np.zeros(3, dtype=[('A','i8'), ('B','f8')])) )

indA = pd.Index([3, 7, 2, 1])
indB = pd.Index([4, 7, 2, 8])
print(indA ^ indB)
print(indA | indB)

