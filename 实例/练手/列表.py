alist = [1, 2, 3, 'one', 'two', 'three']

alist.append('four')
print(alist)

alist.pop()
print(alist)

alist.insert(3,4)
print(alist)

alist.remove(4)
print(alist)

alist.reverse()
print(alist)

print(tuple(alist))