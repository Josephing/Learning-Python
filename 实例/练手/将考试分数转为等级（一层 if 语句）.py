score = float(input(":"))
degree = 'DCBAAE'
index = (score - 60)//10
if index >= 0:
  return degree[index]
else:
  return degree[-1]
