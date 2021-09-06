from array import array

test_array = array('i', [])

print(test_array.tolist())
test_array.insert(2, 44)
print("\nAfter insertion of 44 at index = 2 ", test_array.tolist())
print("\nPop without index gives the value: ", test_array.pop())
print("\nArray after pop(): ", test_array.tolist())
print("\npop(1) gives: ", test_array.pop(1))
print("\nArray after pop(1): ", test_array.tolist())
print("\npop(2) gives: ", test_array.pop(2))
print("\nArray after pop(2): ", test_array.tolist())
test_array.reverse()
print("\nReverse of array: ", test_array.tolist())
print("\ncount(6) gives: ", test_array.count(6))
print(test_array.tolist())
del test_array[0]
print("\nArray after deletion of test_array[0]: ", test_array.tolist())
