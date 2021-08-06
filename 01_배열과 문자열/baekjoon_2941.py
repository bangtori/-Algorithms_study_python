str = input()
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in a :
  str = str.replace(i, '.')

print(len(str))