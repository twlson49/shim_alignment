x = lambda a, b, c, d: ((a + b) / c*d-a)/2
print('fshim=',x(18, 5, 5, 7))
y = lambda a, b, c, d: ((a + b) / c*d-a)/2
print('bshim=',y(18, 5, 5, 17))