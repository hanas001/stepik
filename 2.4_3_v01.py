ln = input('')

countall = len(ln)
g = ln.count('g')
c = ln.count('c')
print (countall)
print (type(countall))
print (g)
print (type(g))
print (c)
print (type(c))
res = int (float((g + c)) / countall * 100)
print (res)