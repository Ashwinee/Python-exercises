no = range(0,11,1)
Square = []
for n in no:
    Square.append(n*n)

print no
print Square

print('{0:>10} {1:>10}').format("Number","Square")
for n in no:
    print("{0:>10d} {1:>10d}".format(n,Square[n]))
    print

