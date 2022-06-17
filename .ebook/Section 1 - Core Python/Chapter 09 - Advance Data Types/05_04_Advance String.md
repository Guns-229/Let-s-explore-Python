
### `maketrans` & `translate`

This `static` method returns a translation table usable for `str.translate()` based on the parameters passed to it.

If only one argument is provided then, it must be a dictionary mapping Unicode ordinals (integers) or characters (strings of length 1) to Unicode ordinals, strings (of arbitrary lengths) or None. Character keys will then be converted to ordinals.

If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to None in the result.

```python
static str.maketrans(x[, y[, z]])
```

where

- If only one argument is present then, 
    - it must be a dictionary. and 
    - it should contain 1-to-1 mapping from a single character string to its translation OR an Unicode ordinals (97 for 'a') to its translation.
- If two arguments (`x` & `y`) are present then, 
    - they both are strings of equal length. 
    - Each character in the first string is a replacement to its corresponding index in the second string.
- z: If all three arguments (`x`, `y` & `z`) are present 
    - `z` should also be a string
    - Each character in the third argument is mapped to None.

```python
str.translate(map)
```


#### `maketrans` with one parameter

We need to pass a dictionary with both properties details above


```python
dis = {
    'a': 'boss ',
    'b': 'good ',
    'c': 'A '
}

trans = str.maketrans(dis)

print("Translated string:", "cba\b.".translate(trans))
```

    Translated string: A good boss .



```python
dis = {
    'a': '63',
    'b': '64',
    'c': '65'
}

trans = str.maketrans(dis)

print("Translated string:", "cba.".translate(trans))
```

    Translated string: 656463.


You can see that text "abc." got transformed to "A good boss .". Note, `.` at the end of the string, as it was not present in the translation dictionary thus it was not converted and remained as it is.

#### `maketrans` with two parameters

We need two equal size strings as parameters


```python
firstString = "abc"
secondString = "ॐༀੴ"
translation = str.maketrans(firstString, secondString)

print("Translated string:", "c. b".translate(translation))
```

    Translated string: ੴ. ༀ


#### `maketrans` with three parameters


```python
firstString = "abc"
secondString = "xyz"
thirdString = "ab"

string = "abcd"
print("Original string:", string)

translation = str.maketrans(firstString, secondString, thirdString)

# translate string
print("Translated string:", string.translate(translation))
```

    Original string: abcd
    Translated string: zd



```python

```
