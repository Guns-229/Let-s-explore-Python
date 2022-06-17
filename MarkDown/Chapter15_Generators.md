
Chapter 15: Generators
=============================
_____________________________
The functions generally follow the conventional process flow, return values ​​and quit. Generators work similarly, but remember the state of the processing between calls, staying in memory and returning the next item expected when activated.

The generators have several advantages over conventional functions:

+ *Lazy Evaluation*: generators are only processed when it is really needed, saving processing resources. 
+ They reduce the need to create lists.
+ They allow to work with unlimited sequences of elements.

Generators are usually called through a *for* loop. The  syntax is similar to the traditional function, just the *yield* instruction substitutes *return*. In each new iteraction, *yield* returns the next value.

Exemple:


```python
def gen_pares():
    """
    Generates even numbers from 0 to 20
    """
    i = 0

    while i <= 20:
        yield i
        i += 2

# Shows each number and goes to the next
for n in gen_pares():
    print (n)
```

    0
    2
    4
    6
    8
    10
    12
    14
    16
    18
    20
    

Another example:


```python
import os

# Finds files recursively
def find(path='.'):

    for item in os.listdir(path):
        fn = os.path.normpath(os.path.join(path, item))

        if os.path.isdir(fn):

            for f in find(fn):
                yield f
        else:
            yield fn

# At each interaction, the generator yeld a new file name
for fn in find():
    print (fn)
```

    .ipynb_checkpoints\Chapter15_Generators-checkpoint.ipynb
    Chapter15_Generators.ipynb
    


```python

```




<style>
    @font-face {
        font-family: "Computer Modern";
        src: url('http://mirrors.ctan.org/fonts/cm-unicode/fonts/otf/cmunss.otf');
    }
    div.cell{
        width:800px;
        margin-left:16% !important;
        margin-right:auto;
    }
    h1 {
        font-family: Helvetica, serif;
    }
    h4{
        margin-top:12px;
        margin-bottom: 3px;
       }
    div.text_cell_render{
        font-family: Computer Modern, "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;
        line-height: 145%;
        font-size: 130%;
        width:800px;
        margin-left:auto;
        margin-right:auto;
    }
    .CodeMirror{
            font-family: "Source Code Pro", source-code-pro,Consolas, monospace;
    }
    .note{
            border-bottom: 1px black dotted;
    }
    .prompt{
        display: None;
    }
    .text_cell_render h5 {
        font-weight: 300;
        font-size: 16pt;
        color: #4057A1;
        font-style: italic;
        margin-bottom: .5em;
        margin-top: 0.5em;
        display: block;
    }
    
    .warning{
        color: rgb( 240, 20, 20 )
        }  
</style>
<script>
    MathJax.Hub.Config({
                        TeX: {
                           extensions: ["AMSmath.js"]
                           },
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\[","\\]"] ]
                },
                displayAlign: 'center', // Change this to 'center' to center equations.
                "HTML-CSS": {
                    styles: {'.MathJax_Display': {"margin": 4}}
                }
        });
</script>


