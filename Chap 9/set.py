#This program demonstrates various set operations
baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

#Display members of baseball set
print('The following sutends are on the baseball team:')
for name in baseball:
    print(name)

#Display members of basketball set
print()
print('the following students are on the basketball team:')
for name in basketball:
    print(name)

#Intersection
print()
print('The following students play both basketball and baseball:')
for name in baseball.intersection(basketball):
    print(name)

#Union
print()
print('The following students play either baseball or basketball:')
for name in baseball.union(basketball):
    print(name)

#Difference
print()
print('The following students play baseball, but not basketball:')
for name in baseball.difference(basketball):
    print(name)

#Symmetric
print()
print('The following students play one sport, but not both:')
for name in baseball.symmetric_difference(basketball):
    print(name)
    
