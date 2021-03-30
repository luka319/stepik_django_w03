>>> d = {}
>>> a = ['kk', 'kk', 's']
>>> for z in a:
...     d.setdefault(z, 0)
...     d[z] = d[z]+1
...
0
1
0
>>> d
{'kk': 2, 's': 1}
