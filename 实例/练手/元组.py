atuple = (1, 2, 3, 'one', 'two', 'three')
ctuple = (1,) # 若元组只有一个元素，要保留一个逗号

# atuple.append('four') 报错

print(1 in atuple)
print('two' in atuple)
print('four' in atuple)

btuple = atuple + atuple
print(btuple)
print(btuple[-1])

print(list(atuple))