t1 = (1,2,3,4,5)
t2 = (6,7,8,9,10)

result = tuple(a+b for a,b in zip(t1,t2))

print("Tuples")
print(t1)
print(t2)

print("Sum Of Tuples:")
print(result)