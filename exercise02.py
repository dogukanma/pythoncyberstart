grades = [15, 29, 93, 84, 65, 47]
print(grades[1:3])
print(grades[1:])
grades[0] = 25
print(grades[0])
print("len(grades) = " + str(len(grades)))
grades.append(111)
print(grades)
grades.insert(1, 444)
print(grades)
grades.extend([100, 200, 300])
print(grades)

# ilk gördüğünü siler 
grades.remove(111)
print(grades)
grades.extend([1,1,11])
print(grades.count(1))

arr = ["1", "5", "2", "-4", "a", "b", "e", "c"]
arr.sort()
print(arr)