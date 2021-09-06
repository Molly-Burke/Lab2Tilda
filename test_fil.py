from array import array
#from ArrayQ import ArrayQ

test_array = array('i', [8, 45, 33, 90, 67, 28, 3])

print(test_array.tolist())


test_array.insert(2, 44)
print("\nArray after insert(2, 44): ", test_array.tolist())

test_array.remove(90)
print("\nArray after remove(90): ", test_array.tolist())

test_array.append(5)
print("\nArray after append(5): ", test_array.tolist())

print("\nPop without index gives the value: ", test_array.pop())
print("\nArray after pop(): ", test_array.tolist())

print("\npop(1) gives: ", test_array.pop(1))
print("\nArray after pop(1): ", test_array.tolist())

test_array.append(11)
print("\nArray after append(11): ", test_array.tolist())

print(len(test_array))
print("\n\n\n")


"""
q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
print(q.size())
x = q.dequeue()
print("x =", x)
y = q.dequeue()
print("Y =", y)
print(q.size())

if x == 1 and y == 2:
    print("OK")
else:
    print("FAILED")
