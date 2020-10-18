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
df = pd.DataFrame({'age':ages, 'height':heights})
print(df)
print(df.columns)
print(df['age'])
print(df.height)

print( pd.DataFrame(({f'col{2 * i}':i, f'col{2 * i + 1}':i ** 2} for i in range(0, 5))) )

print(pd.DataFrame(np.zeros(3, dtype=[('A','i8'), ('B','f8')])) )

indA = pd.Index([3, 7, 2, 1])
indB = pd.Index([4, 7, 2, 8])
print(indA ^ indB)
print(indA | indB)

data = pd.Series([1,2,3,4], ['a','b','c','c'])
print(data['c'])

df['growth_velocity'] = df['height'] / df['age']
print(df.growth_velocity)
print(df.values)
print(df.T)
print(df.values[0])
print(df.age)


area = pd.Series({'California': 423967, 'Texas': 695662,
                          'New York': 141297, 'Florida': 170312,
                          'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                         'New York': 19651127, 'Florida': 19552860,
                         'Illinois': 12882135})
df = pd.DataFrame({'area':area, 'pop':pop})
df['density'] = df['pop'] / df['area']

print(df.iloc[:3, :1])  # 'pop'

df.iloc[:3, 1] = 1000
print(df['pop'])

print(df.values[[1,3]])
print(df.values[[1,3], 1])  # 取子矩阵的列1，看上去像个行向量

print(df['pop'])
# print(df.iloc[:, 'pop'])
# print(df['Texas'])
print(df['Texas':'Florida'])

print(df[df.density > 100])

print("人口的开方：")
print(np.sqrt(df['pop']))
print("人口的圆面积：")
print(np.pi * df['pop'] ** 2)


area = pd.Series({'Texas': 695662,'New York': 141297,
                'Florida': 170312, 'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                         'New York': 19651127,})
print(area / pop)
print(area.index | pop.index)
print(area.add(pop, fill_value=0))


A = pd.DataFrame(np.random.randint(0, 20, (5, 2)), columns=list('AB'))
B = pd.DataFrame(np.random.randint(0, 20, (7, 3)), columns=list('BAC'))
# B = pd.DataFrame(np.random.randint(0, 20, (3, 3)), columns=list('BAC'))  # 为什么有的地方不填充？？因为A的广播，只会向B大 维度 扩展
# print(A.add(B, fill_value=A.stack().mean()))
print(A)
print(B)
print(A.add(B, fill_value=A.stack().mean()))
