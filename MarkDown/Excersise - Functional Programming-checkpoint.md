
# Excercise - Functional Programming


**Q: ** Try rewriting the code below as a map. It takes a list of real names and replaces them with code names produced using a more robust strategy.


```python
names = ["Aalok", "Chandu", "Roshan", "Manish"]

for i in range(len(names)):
    names[i] = hash(names[i])
print(names)
```

    [-1525715610743626849, 1864234633280094006, -6034146732772895475, -2026123989043073386]
    

Ans: 


```python
secret_names = map(hash, names)
print(secret_names)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-1-9dd45e7450d5> in <module>()
    ----> 1 secret_names = map(hash, names)
          2 print(secret_names)
    

    NameError: name 'names' is not defined


1. Write a function called generate_matrix that takes two positional arguments – m and n – and a keyword argument default that specifies the value for each position. It should use a nested list comprehension to generate a list of lists with the given dimensions. If default is provided, each position should have the given value, otherwise the matrix should be populated with zeroes.

2. Write a function called initcap that replicates the functionality of the string.title method, except better. Given a string, it should split the string on whitespace, capitalize each element of the resulting list and join them back into a string. Your implementation should use a list comprehension.

3. Write a function called make_mapping that takes two lists of equal length and returns a dictionary that maps the values in the first list to the values in the second. The function should also take an optional keyword argument called exclude, which expects a list. Values in the list passed as exclude should be omitted as keys in the resulting dictionary.

4. Write a function called compress_dict_keys that takes a dictionary with string keys and returns a new dictionary with the vowels removed from the keys. For instance, the dictionary {"foo": 1, "bar": 2} should be transformed into {"f": 1, "br": 2}. The function should use a list comprehension nested inside a dict comprehension.

5. Write a function called dedup_surnames that takes a list of surnames names and returns a set of surnames with the case normalized to uppercase. For instance, the list ["smith", "Jones", "Smith", "BROWN"] should be transformed into the set {"SMITH", "JONES", "BROWN"}.
