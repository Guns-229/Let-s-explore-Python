
# Setting up Python for machine learning: scikit-learn and IPython Notebook
*From the video series: [Introduction to machine learning with scikit-learn](https://github.com/justmarkham/scikit-learn-videos)*

## Agenda

- What are the benefits and drawbacks of scikit-learn?
- How do I install scikit-learn?
- How do I use the IPython Notebook?
- What are some good resources for learning Python?

![scikit-learn algorithm map](images/02_sklearn_algorithms.png)

## Benefits and drawbacks of scikit-learn

### Benefits:

- **Consistent interface** to machine learning models
- Provides many **tuning parameters** but with **sensible defaults**
- Exceptional **documentation**
- Rich set of functionality for **companion tasks**
- **Active community** for development and support

### Potential drawbacks:

- Harder (than R) to **get started with machine learning**
- Less emphasis (than R) on **model interpretability**

### Further reading:

- Ben Lorica: [Six reasons why I recommend scikit-learn](http://radar.oreilly.com/2013/12/six-reasons-why-i-recommend-scikit-learn.html)
- scikit-learn authors: [API design for machine learning software](http://arxiv.org/pdf/1309.0238v1.pdf)
- Data School: [Should you teach Python or R for data science?](http://www.dataschool.io/python-or-r-for-data-science/)

![scikit-learn logo](images/02_sklearn_logo.png)

## Installing scikit-learn

**Option 1:** [Install scikit-learn library](http://scikit-learn.org/stable/install.html) and dependencies (NumPy and SciPy)

**Option 2:** [Install Anaconda distribution](https://www.continuum.io/downloads) of Python, which includes:

- Hundreds of useful packages (including scikit-learn)
- IPython and IPython Notebook
- conda package manager
- Spyder IDE

![IPython header](images/02_ipython_header.png)

## Using the IPython Notebook

### Components:

- **IPython interpreter:** enhanced version of the standard Python interpreter
- **Browser-based notebook interface:** weave together code, formatted text, and plots

### Installation:

- **Option 1:** Install [IPython](http://ipython.org/install.html) and the [notebook](https://jupyter.readthedocs.io/en/latest/install.html)
- **Option 2:** Included with the Anaconda distribution

### Launching the Notebook:

- Type **ipython notebook** at the command line to open the dashboard
- Don't close the command line window while the Notebook is running

### Keyboard shortcuts:

**Command mode** (gray border)

- Create new cells above (**a**) or below (**b**) the current cell
- Navigate using the **up arrow** and **down arrow**
- Convert the cell type to Markdown (**m**) or code (**y**)
- See keyboard shortcuts using **h**
- Switch to Edit mode using **Enter**

**Edit mode** (green border)

- **Ctrl+Enter** to run a cell
- Switch to Command mode using **Esc**

### IPython and Markdown resources:

- [nbviewer](http://nbviewer.jupyter.org/): view notebooks online as static documents
- [IPython documentation](http://ipython.readthedocs.io/en/stable/): focuses on the interpreter
- [IPython Notebook tutorials](http://jupyter.readthedocs.io/en/latest/content-quickstart.html): in-depth introduction
- [GitHub's Mastering Markdown](https://guides.github.com/features/mastering-markdown/): short guide with lots of examples

## Resources for learning Python

- [Codecademy's Python course](https://www.codecademy.com/learn/python): browser-based, tons of exercises
- [DataQuest](https://www.dataquest.io/): browser-based, teaches Python in the context of data science
- [Google's Python class](https://developers.google.com/edu/python/): slightly more advanced, includes videos and downloadable exercises (with solutions)
- [Python for Informatics](http://www.pythonlearn.com/): beginner-oriented book, includes slides and videos

## Comments or Questions?

- Email: <kevin@dataschool.io>
- Website: http://dataschool.io
- Twitter: [@justmarkham](https://twitter.com/justmarkham)


```python
from IPython.core.display import HTML
def css_styling():
    styles = open("styles/custom.css", "r").read()
    return HTML(styles)
css_styling()
```




<style>
    @font-face {
        font-family: "Computer Modern";
        src: url('http://mirrors.ctan.org/fonts/cm-unicode/fonts/otf/cmunss.otf');
    }
    div.cell{
        width: 90%;
/*        margin-left:auto;*/
/*        margin-right:auto;*/
    }
    ul {
        line-height: 145%;
        font-size: 90%;
    }
    li {
        margin-bottom: 1em;
    }
    h1 {
        font-family: Helvetica, serif;
    }
    h4{
        margin-top: 12px;
        margin-bottom: 3px;
       }
    div.text_cell_render{
        font-family: Computer Modern, "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;
        line-height: 145%;
        font-size: 130%;
        width: 90%;
        margin-left:auto;
        margin-right:auto;
    }
    .CodeMirror{
            font-family: "Source Code Pro", source-code-pro,Consolas, monospace;
    }
/*    .prompt{
        display: None;
    }*/
    .text_cell_render h5 {
        font-weight: 300;
        font-size: 16pt;
        color: #4057A1;
        font-style: italic;
        margin-bottom: 0.5em;
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


