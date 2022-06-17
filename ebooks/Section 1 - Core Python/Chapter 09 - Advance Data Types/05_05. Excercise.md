
## Excercise 

1. Write a Python script to add key to a dictionary. 
> Sample Dictionary : {0: 10, 1: 20}
> Expected Result : {0: 10, 1: 20, 2: 30}
2. Write a Python script to concatenate following dictionaries to create a new one. 
> Sample Dictionary :
> dic1={1:10, 2:20}
> dic2={3:30, 4:40}
> dic3={5:50,6:60}
> Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
3. Write a python script to print the data type of the given variable without using `type`. 
4. Write a Python script to check if a given key already exists in a dictionary. 
5. Write a Python program to iterate over dictionaries using for loops. 
6. Write a Python script to generate and print a dictionary that contains number (between 1 and n) in the form (x, x*x). 
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

8. Write a Python script to merge two Python dictionaries. 
9. Write a Python script to sort (ascending and descending) a dictionary by value. 
10. Write a Python program to sum all the items in a dictionary. 
11. Write a Python program to multiply all the items in a dictionary. 
12. Write a Python program to remove a key from a dictionary. 
13. Write a Python program to map two lists into a dictionary. 
14. Write a Python program to sort a dictionary by key. 
15. Write a Python program to get the maximum and minimum value in a dictionary. 
16. ** TODO: Write a Python program to get a dictionary from an object's fields. ** 
17. Write a Python program to remove duplicates (in terms of value) from Dictionary. 
18. Write a Python program to check a dictionary is empty or not.
1. What will be the output of the following code snippets?

a. 
```python
a=[1,2,3,4,5,6,7,8,9]
print(a[::2])
```
b. 
```python
a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50,60
print(a)
```
c.
```python
a=[1,2,3,4,5]
print(a[3:0:-1])
```
d.
```python
arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
for i in range(0, 4):
    print(arr[i].pop())
```
e.
```python
arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6): 
    print(arr[i], end = " ")
```
f. 
```python
nums = set([1,1,2,3,3,3,4])
print len(nums)
```
g.
```python
numbers = [1, 2, 3, 4]

numbers.append([5,6,7,8])

print len(numbers)
```
h.
```python
names1 = ['Amir', 'Barry', 'Chales', 'Dao']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10

print(sum)
```

i.
```python
names1 = ['Amir', 'Barry', 'Chales', 'Dao']

loc = names1.index("Edward")

print (loc)
```

j.
```python
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

print len(list1 + list2)
```

k.
```python
list1 = [1, 2, 3, 8, 4]
list2 = [5, 6, 7, 8, 2]

print len(set(list1 + list2))
```
