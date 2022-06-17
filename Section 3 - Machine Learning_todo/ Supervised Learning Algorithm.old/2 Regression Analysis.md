
# 2 Regression Analysis

## Linear Regression

Linear regression is an modeling approach to describe the relationship between a **scalar dependent variable** Y and one or more **explanatory variables** (or **independent variables**) denoted X. 

In **simple linear regression** only one explanatory variable is present. In **multiple linear regression** more than one explanatory variable are present. 

In **linear regression**, the relationships are modeled using linear predictor functions whose unknown model parameters are estimated from the data and are called **linear models**. 

Example of linear regression

![Linear_regression.svg.png](attachment:Linear_regression.svg.png)

##  Why use linear regression?

* widely used
* runs fast
* easy to use (not a lot of tuning required)
* highly interpretable
* basis for many other methods

## Libraries

- Sciket-learn


We are going to use sciket for our examples. Please download the following modules using `conda` or `pip`:

> conda install pandas

> conda install scikit

> conda install scikit-learn

> conda install matplotlib

Sample datasets are  present in sklearn and we are going to use them in our learning. 

In the below example we will try to predict the cost of the house in boston based on features. 

### Predicting Prices of Boston Housing Values


```python
%matplotlib inline

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn 
import seaborn as sns

from matplotlib import rcParams
sns.set_style("whitegrid")
sns.set_context("poster")
```


```python
from sklearn.datasets import load_boston
```

### Load and Asess the Boston Housing data set from sklearn


```python
boston = load_boston()
boston.keys()
```




    dict_keys(['data', 'target', 'feature_names', 'DESCR'])




```python
print(boston.data.shape)
```

    (506, 13)


The boston dataset contains the following features 


```python
print(boston.feature_names)
```

    ['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO'
     'B' 'LSTAT']


Now, lets convert boston.data into pandas data frame


```python
bos = pd.DataFrame(boston.data)
bos.columns = boston.feature_names
bos.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CRIM</th>
      <th>ZN</th>
      <th>INDUS</th>
      <th>CHAS</th>
      <th>NOX</th>
      <th>RM</th>
      <th>AGE</th>
      <th>DIS</th>
      <th>RAD</th>
      <th>TAX</th>
      <th>PTRATIO</th>
      <th>B</th>
      <th>LSTAT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00632</td>
      <td>18.0</td>
      <td>2.31</td>
      <td>0.0</td>
      <td>0.538</td>
      <td>6.575</td>
      <td>65.2</td>
      <td>4.0900</td>
      <td>1.0</td>
      <td>296.0</td>
      <td>15.3</td>
      <td>396.90</td>
      <td>4.98</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.02731</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0.0</td>
      <td>0.469</td>
      <td>6.421</td>
      <td>78.9</td>
      <td>4.9671</td>
      <td>2.0</td>
      <td>242.0</td>
      <td>17.8</td>
      <td>396.90</td>
      <td>9.14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.02729</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0.0</td>
      <td>0.469</td>
      <td>7.185</td>
      <td>61.1</td>
      <td>4.9671</td>
      <td>2.0</td>
      <td>242.0</td>
      <td>17.8</td>
      <td>392.83</td>
      <td>4.03</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.03237</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0.0</td>
      <td>0.458</td>
      <td>6.998</td>
      <td>45.8</td>
      <td>6.0622</td>
      <td>3.0</td>
      <td>222.0</td>
      <td>18.7</td>
      <td>394.63</td>
      <td>2.94</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.06905</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0.0</td>
      <td>0.458</td>
      <td>7.147</td>
      <td>54.2</td>
      <td>6.0622</td>
      <td>3.0</td>
      <td>222.0</td>
      <td>18.7</td>
      <td>396.90</td>
      <td>5.33</td>
    </tr>
  </tbody>
</table>
</div>



## Describing the Data Set


```python
print(boston.DESCR)
```

    Boston House Prices dataset
    ===========================
    
    Notes
    ------
    Data Set Characteristics:  
    
        :Number of Instances: 506 
    
        :Number of Attributes: 13 numeric/categorical predictive
        
        :Median Value (attribute 14) is usually the target
    
        :Attribute Information (in order):
            - CRIM     per capita crime rate by town
            - ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
            - INDUS    proportion of non-retail business acres per town
            - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
            - NOX      nitric oxides concentration (parts per 10 million)
            - RM       average number of rooms per dwelling
            - AGE      proportion of owner-occupied units built prior to 1940
            - DIS      weighted distances to five Boston employment centres
            - RAD      index of accessibility to radial highways
            - TAX      full-value property-tax rate per $10,000
            - PTRATIO  pupil-teacher ratio by town
            - B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
            - LSTAT    % lower status of the population
            - MEDV     Median value of owner-occupied homes in $1000's
    
        :Missing Attribute Values: None
    
        :Creator: Harrison, D. and Rubinfeld, D.L.
    
    This is a copy of UCI ML housing dataset.
    http://archive.ics.uci.edu/ml/datasets/Housing
    
    
    This dataset was taken from the StatLib library which is maintained at Carnegie Mellon University.
    
    The Boston house-price data of Harrison, D. and Rubinfeld, D.L. 'Hedonic
    prices and the demand for clean air', J. Environ. Economics & Management,
    vol.5, 81-102, 1978.   Used in Belsley, Kuh & Welsch, 'Regression diagnostics
    ...', Wiley, 1980.   N.B. Various transformations are used in the table on
    pages 244-261 of the latter.
    
    The Boston house-price data has been used in many machine learning papers that address regression
    problems.   
         
    **References**
    
       - Belsley, Kuh & Welsch, 'Regression diagnostics: Identifying Influential Data and Sources of Collinearity', Wiley, 1980. 244-261.
       - Quinlan,R. (1993). Combining Instance-Based and Model-Based Learning. In Proceedings on the Tenth International Conference of Machine Learning, 236-243, University of Massachusetts, Amherst. Morgan Kaufmann.
       - many more! (see http://archive.ics.uci.edu/ml/datasets/Housing)
    


boston.target contains the housing prices 

## Setting up our Housing Data for Linear Regression Analysis

Create a variable called PRICE which will contain the prices.
This information is contained in the target data, what we want to predict using the linear model.


```python
bos['PRICE'] = boston.target
bos.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CRIM</th>
      <th>ZN</th>
      <th>INDUS</th>
      <th>CHAS</th>
      <th>NOX</th>
      <th>RM</th>
      <th>AGE</th>
      <th>DIS</th>
      <th>RAD</th>
      <th>TAX</th>
      <th>PTRATIO</th>
      <th>B</th>
      <th>LSTAT</th>
      <th>PRICE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00632</td>
      <td>18.0</td>
      <td>2.31</td>
      <td>0.0</td>
      <td>0.538</td>
      <td>6.575</td>
      <td>65.2</td>
      <td>4.0900</td>
      <td>1.0</td>
      <td>296.0</td>
      <td>15.3</td>
      <td>396.90</td>
      <td>4.98</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.02731</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0.0</td>
      <td>0.469</td>
      <td>6.421</td>
      <td>78.9</td>
      <td>4.9671</td>
      <td>2.0</td>
      <td>242.0</td>
      <td>17.8</td>
      <td>396.90</td>
      <td>9.14</td>
      <td>21.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.02729</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0.0</td>
      <td>0.469</td>
      <td>7.185</td>
      <td>61.1</td>
      <td>4.9671</td>
      <td>2.0</td>
      <td>242.0</td>
      <td>17.8</td>
      <td>392.83</td>
      <td>4.03</td>
      <td>34.7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.03237</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0.0</td>
      <td>0.458</td>
      <td>6.998</td>
      <td>45.8</td>
      <td>6.0622</td>
      <td>3.0</td>
      <td>222.0</td>
      <td>18.7</td>
      <td>394.63</td>
      <td>2.94</td>
      <td>33.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.06905</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0.0</td>
      <td>0.458</td>
      <td>7.147</td>
      <td>54.2</td>
      <td>6.0622</td>
      <td>3.0</td>
      <td>222.0</td>
      <td>18.7</td>
      <td>396.90</td>
      <td>5.33</td>
      <td>36.2</td>
    </tr>
  </tbody>
</table>
</div>




```python
bos.head(10)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CRIM</th>
      <th>ZN</th>
      <th>INDUS</th>
      <th>CHAS</th>
      <th>NOX</th>
      <th>RM</th>
      <th>AGE</th>
      <th>DIS</th>
      <th>RAD</th>
      <th>TAX</th>
      <th>PTRATIO</th>
      <th>B</th>
      <th>LSTAT</th>
      <th>PRICE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00632</td>
      <td>18.0</td>
      <td>2.31</td>
      <td>0.0</td>
      <td>0.538</td>
      <td>6.575</td>
      <td>65.2</td>
      <td>4.0900</td>
      <td>1.0</td>
      <td>296.0</td>
      <td>15.3</td>
      <td>396.90</td>
      <td>4.98</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.02731</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0.0</td>
      <td>0.469</td>
      <td>6.421</td>
      <td>78.9</td>
      <td>4.9671</td>
      <td>2.0</td>
      <td>242.0</td>
      <td>17.8</td>
      <td>396.90</td>
      <td>9.14</td>
      <td>21.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.02729</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0.0</td>
      <td>0.469</td>
      <td>7.185</td>
      <td>61.1</td>
      <td>4.9671</td>
      <td>2.0</td>
      <td>242.0</td>
      <td>17.8</td>
      <td>392.83</td>
      <td>4.03</td>
      <td>34.7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.03237</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0.0</td>
      <td>0.458</td>
      <td>6.998</td>
      <td>45.8</td>
      <td>6.0622</td>
      <td>3.0</td>
      <td>222.0</td>
      <td>18.7</td>
      <td>394.63</td>
      <td>2.94</td>
      <td>33.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.06905</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0.0</td>
      <td>0.458</td>
      <td>7.147</td>
      <td>54.2</td>
      <td>6.0622</td>
      <td>3.0</td>
      <td>222.0</td>
      <td>18.7</td>
      <td>396.90</td>
      <td>5.33</td>
      <td>36.2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.02985</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0.0</td>
      <td>0.458</td>
      <td>6.430</td>
      <td>58.7</td>
      <td>6.0622</td>
      <td>3.0</td>
      <td>222.0</td>
      <td>18.7</td>
      <td>394.12</td>
      <td>5.21</td>
      <td>28.7</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.08829</td>
      <td>12.5</td>
      <td>7.87</td>
      <td>0.0</td>
      <td>0.524</td>
      <td>6.012</td>
      <td>66.6</td>
      <td>5.5605</td>
      <td>5.0</td>
      <td>311.0</td>
      <td>15.2</td>
      <td>395.60</td>
      <td>12.43</td>
      <td>22.9</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.14455</td>
      <td>12.5</td>
      <td>7.87</td>
      <td>0.0</td>
      <td>0.524</td>
      <td>6.172</td>
      <td>96.1</td>
      <td>5.9505</td>
      <td>5.0</td>
      <td>311.0</td>
      <td>15.2</td>
      <td>396.90</td>
      <td>19.15</td>
      <td>27.1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.21124</td>
      <td>12.5</td>
      <td>7.87</td>
      <td>0.0</td>
      <td>0.524</td>
      <td>5.631</td>
      <td>100.0</td>
      <td>6.0821</td>
      <td>5.0</td>
      <td>311.0</td>
      <td>15.2</td>
      <td>386.63</td>
      <td>29.93</td>
      <td>16.5</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.17004</td>
      <td>12.5</td>
      <td>7.87</td>
      <td>0.0</td>
      <td>0.524</td>
      <td>6.004</td>
      <td>85.9</td>
      <td>6.5921</td>
      <td>5.0</td>
      <td>311.0</td>
      <td>15.2</td>
      <td>386.71</td>
      <td>17.10</td>
      <td>18.9</td>
    </tr>
  </tbody>
</table>
</div>



Exploring this data set. First, use describe() to get basic summary statistics for each of the columns.


```python
bos.describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CRIM</th>
      <th>ZN</th>
      <th>INDUS</th>
      <th>CHAS</th>
      <th>NOX</th>
      <th>RM</th>
      <th>AGE</th>
      <th>DIS</th>
      <th>RAD</th>
      <th>TAX</th>
      <th>PTRATIO</th>
      <th>B</th>
      <th>LSTAT</th>
      <th>PRICE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3.593761</td>
      <td>11.363636</td>
      <td>11.136779</td>
      <td>0.069170</td>
      <td>0.554695</td>
      <td>6.284634</td>
      <td>68.574901</td>
      <td>3.795043</td>
      <td>9.549407</td>
      <td>408.237154</td>
      <td>18.455534</td>
      <td>356.674032</td>
      <td>12.653063</td>
      <td>22.532806</td>
    </tr>
    <tr>
      <th>std</th>
      <td>8.596783</td>
      <td>23.322453</td>
      <td>6.860353</td>
      <td>0.253994</td>
      <td>0.115878</td>
      <td>0.702617</td>
      <td>28.148861</td>
      <td>2.105710</td>
      <td>8.707259</td>
      <td>168.537116</td>
      <td>2.164946</td>
      <td>91.294864</td>
      <td>7.141062</td>
      <td>9.197104</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.006320</td>
      <td>0.000000</td>
      <td>0.460000</td>
      <td>0.000000</td>
      <td>0.385000</td>
      <td>3.561000</td>
      <td>2.900000</td>
      <td>1.129600</td>
      <td>1.000000</td>
      <td>187.000000</td>
      <td>12.600000</td>
      <td>0.320000</td>
      <td>1.730000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.082045</td>
      <td>0.000000</td>
      <td>5.190000</td>
      <td>0.000000</td>
      <td>0.449000</td>
      <td>5.885500</td>
      <td>45.025000</td>
      <td>2.100175</td>
      <td>4.000000</td>
      <td>279.000000</td>
      <td>17.400000</td>
      <td>375.377500</td>
      <td>6.950000</td>
      <td>17.025000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.256510</td>
      <td>0.000000</td>
      <td>9.690000</td>
      <td>0.000000</td>
      <td>0.538000</td>
      <td>6.208500</td>
      <td>77.500000</td>
      <td>3.207450</td>
      <td>5.000000</td>
      <td>330.000000</td>
      <td>19.050000</td>
      <td>391.440000</td>
      <td>11.360000</td>
      <td>21.200000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>3.647423</td>
      <td>12.500000</td>
      <td>18.100000</td>
      <td>0.000000</td>
      <td>0.624000</td>
      <td>6.623500</td>
      <td>94.075000</td>
      <td>5.188425</td>
      <td>24.000000</td>
      <td>666.000000</td>
      <td>20.200000</td>
      <td>396.225000</td>
      <td>16.955000</td>
      <td>25.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>88.976200</td>
      <td>100.000000</td>
      <td>27.740000</td>
      <td>1.000000</td>
      <td>0.871000</td>
      <td>8.780000</td>
      <td>100.000000</td>
      <td>12.126500</td>
      <td>24.000000</td>
      <td>711.000000</td>
      <td>22.000000</td>
      <td>396.900000</td>
      <td>37.970000</td>
      <td>50.000000</td>
    </tr>
  </tbody>
</table>
</div>



## Building the Regression Model

In this section we are going to select a model which will suite our problem/solution.



### Step 1: Checking for Linearity - Scatterplots

We are going to use Scatter plots to find the best match. 

Using scatter plots, let's take a look into the relationships between the variables and price. In order to create a linear model, the predictors or features that we use must have a linear relationship to price.


```python
for b in bos:
    xaxis = "PRICE"
    if(xaxis != b):
        sns.lmplot(y=b, x="PRICE", data=bos, fit_reg = True)
        plt.title("Relationship between %s and Price" %b)
```


![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_32_0.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_32_1.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_32_2.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_32_3.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_32_4.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_32_5.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_32_6.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_32_7.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_32_8.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_32_9.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_32_10.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_32_11.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_32_12.png)


Based on the above graphs, we can club the features in two category, 
- Strong Possible Predictors:
- Weaker Possible Predictors:

#### Strong Possible Predictors:

These features have string relationships to price exemplified by a small, tight distribution of data around the line of best fit extimated by the plot.

- Number of Rooms (RM)
- % of Lower Status Population (LSTAT)
- Nitrus Oxide Concentration (in parts per 10 million) (NOX)
- Weighted Distance from 5 Major Employment Centers (DIS)


```python
# Number of Rooms 
sns.regplot(y="PRICE", x="RM", data=bos, fit_reg = True)
plt.title("Relationship between RM and Price")
```




    <matplotlib.text.Text at 0x1589ce443c8>




![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_36_1.png)



```python
# % of Lower Status Population
sns.regplot(y="PRICE", x="LSTAT", data=bos, fit_reg = True)
plt.title("Relationship between LSTAT and Price")
```




    <matplotlib.text.Text at 0x1589cfdc908>




![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_37_1.png)



```python
# Nitrus Oxide Concentration (in parts per 10 million)
sns.regplot(y="PRICE", x="NOX", data=bos, fit_reg = True)
plt.title("Relationship between NOX and Price")
```




    <matplotlib.text.Text at 0x1589cb3a9b0>




![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_38_1.png)



```python
# Weighted Distance from 5 Major Employment Centers
# Strong positive coorelation, the closer/further the town is from employment centers, the higher/lower the housing price.
sns.regplot(y="PRICE", x="DIS", data=bos, fit_reg = True)
plt.title("Relationship between DIS and Price")
```




    <matplotlib.text.Text at 0x1589ba29198>




![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_39_1.png)


### Weaker (still decent) Possible Predictors:

These features have string relationships to price exemplified by a small, tight distribution of data around the line of best fit extimated by the plot.


```python
# Pupil Teacher Ratio in schools/college
sns.regplot(y="PRICE", x="PTRATIO", data=bos, fit_reg = True)
plt.title("Relationship between PTRATIO and Price")
```




    <matplotlib.text.Text at 0x1589d00ada0>




![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_42_1.png)



```python
# Crime Rate
sns.regplot(y="PRICE", x="CRIM", data=bos, fit_reg = True)
plt.title("Relationship between Crime Rate and Price")
```




    <matplotlib.text.Text at 0x1589b9d1d30>




![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_43_1.png)


## Step 2: Checking for Normality: Histograms

We have now found most common possible variables which can impact the price. Now lets normalize any variable to make its values normally distributed along with line.

In the above graphs we found that relationship between crime rate and price is not normalised. Logging of the data helps in normalizing it and eliminates any skew in the distribution to make patterns more visible and data more interprettable.

### Adjusting the Crime Rate Feature


When we look at our Crime Rate and Price graph, we see it exhibits exponential decay. This can be coorected by taking it's log so that it has a linear relationship with price.


```python
# Crime Rate
sns.regplot(y="PRICE", x="CRIM", data=bos, fit_reg = True)
plt.title("Relationship between Crime Rate and Price")
```




    <matplotlib.text.Text at 0x1589cc97fd0>




![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_48_1.png)



```python
x = np.log(bos.CRIM)
plt.scatter(x, bos.PRICE)

plt.xlabel("Log of Crime Rate")
plt.ylabel("Housing Price")
plt.title("Adjusted Crime Rate vs. Original Prices")
```




    <matplotlib.text.Text at 0x1589cd4f358>




![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_49_1.png)


#### update dataframe

Lets update the dataframe with our findings from normalization


```python
bos1 = bos
bos1['CRIM'] = np.log(bos['CRIM'])
```

    c:\apps\miniconda3\lib\site-packages\ipykernel_launcher.py:2: RuntimeWarning: invalid value encountered in log
      



```python
for b in bos1:
    xaxis = "PRICE"
    if(xaxis != b):
        sns.lmplot(y=b, x="PRICE", data=bos1, fit_reg = True)
        plt.title("Relationship between %s and Price" %b)
```


![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_52_0.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_52_1.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_52_2.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_52_3.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_52_4.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_52_5.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_52_6.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_52_7.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_52_8.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_52_9.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_52_10.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_52_11.png)



![png](2%20Regression%20Analysis_files/2%20Regression%20Analysis_52_12.png)



```python
from sklearn.linear_model import LinearRegression
# X = bos1.drop("PRICE", axis = 1)
lr = LinearRegression()
print(lr)
```

    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)


## Part 3: Checking for coorelation between our Features- Coorelation Matrix


```python
df = bos1.iloc[:, [0,4,5,7,10,12]]
df.corr()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CRIM</th>
      <th>NOX</th>
      <th>RM</th>
      <th>DIS</th>
      <th>PTRATIO</th>
      <th>LSTAT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>CRIM</th>
      <td>1.000000</td>
      <td>0.138597</td>
      <td>-0.111418</td>
      <td>-0.485705</td>
      <td>0.371048</td>
      <td>0.346300</td>
    </tr>
    <tr>
      <th>NOX</th>
      <td>0.138597</td>
      <td>1.000000</td>
      <td>-0.302188</td>
      <td>-0.769230</td>
      <td>0.188933</td>
      <td>0.590879</td>
    </tr>
    <tr>
      <th>RM</th>
      <td>-0.111418</td>
      <td>-0.302188</td>
      <td>1.000000</td>
      <td>0.205246</td>
      <td>-0.355501</td>
      <td>-0.613808</td>
    </tr>
    <tr>
      <th>DIS</th>
      <td>-0.485705</td>
      <td>-0.769230</td>
      <td>0.205246</td>
      <td>1.000000</td>
      <td>-0.232471</td>
      <td>-0.496996</td>
    </tr>
    <tr>
      <th>PTRATIO</th>
      <td>0.371048</td>
      <td>0.188933</td>
      <td>-0.355501</td>
      <td>-0.232471</td>
      <td>1.000000</td>
      <td>0.374044</td>
    </tr>
    <tr>
      <th>LSTAT</th>
      <td>0.346300</td>
      <td>0.590879</td>
      <td>-0.613808</td>
      <td>-0.496996</td>
      <td>0.374044</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
from statsmodels import api as sm
from statsmodels.formula.api import ols
```


```python
bos1 = bos
bos1['CRIM'] = np.log(bos1['CRIM'])
```


```python
m = ols('PRICE ~ PTRATIO + NOX + RM + LSTAT + DIS ',bos1).fit()
print(m.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                  PRICE   R-squared:                       0.708
    Model:                            OLS   Adj. R-squared:                  0.705
    Method:                 Least Squares   F-statistic:                     242.6
    Date:                Mon, 08 May 2017   Prob (F-statistic):          3.67e-131
    Time:                        20:04:54   Log-Likelihood:                -1528.7
    No. Observations:                 506   AIC:                             3069.
    Df Residuals:                     500   BIC:                             3095.
    Df Model:                           5                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    Intercept     37.4992      4.613      8.129      0.000      28.436      46.562
    PTRATIO       -1.0458      0.114     -9.212      0.000      -1.269      -0.823
    NOX          -17.9966      3.261     -5.519      0.000     -24.403     -11.590
    RM             4.1633      0.412     10.104      0.000       3.354       4.973
    LSTAT         -0.5811      0.048    -12.122      0.000      -0.675      -0.487
    DIS           -1.1847      0.168     -7.034      0.000      -1.516      -0.854
    ==============================================================================
    Omnibus:                      187.456   Durbin-Watson:                   0.971
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):              885.498
    Skew:                           1.584   Prob(JB):                    5.21e-193
    Kurtosis:                       8.654   Cond. No.                         545.
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.


### Interpreting coefficients

There is a ton of information in this output.We concentrate on the coefficient table (middle table).

* We begin interpretting the coefficients by first noticing that the p-value (under P>|t|) is so small, basically zero. This means that our selected features are a statistically significant predictor of PRICE.

<p><strong>In general, the $\hat{\beta_i}, i > 0$ can be interpreted as the following: "A one unit increase in $x_i$ is associated with, on average, a $\hat{\beta_i}$ increase/decrease in $y$ net of all other variables."</strong></p>
<p><strong>On the other hand, the interpretation for the intercept, $\hat{\beta}_0$ is the average of $y$ given that all of the independent variables $x_i$ are 0. Our $\hat{\beta}_0$ is $\$23,000$.</strong></p>
<p><strong>Lets look at our three most significant regression coefficients:</strong></p>
On the other hand, the interpretation for the intercept,  β^0β^0  is the average of  yy  given that all of the independent variables  xixi  are 0. Our  β^0β^0  is  $23,000$23,000 .

Lets look at our three most significant regression coefficients:

* The LARGEST regression coefficient is for RM of 4.2933 means that on average, each additional room is associated with an increase of  $4,300$4,300  in house price net of the other variables. The confidence interval gives us a range of plausible values for this average change, about ( $3,400,$5,128$3,400,$5,128 ). That's a lot of money for each additional room!

* Another significant feature, indicated by a high regression coefficient, is PTRATIO's of -.9256. This means that on average, each point increase in PTRATIO is associated with an decrease of  $925$925  in house price net of the other variables. The confidence interval gives us a range of plausible values for this average change, about ( $692,$1,159$692,$1,159 ).

* Our third most significant feature, is DIS's of -.6926. This means that on average, each increase in DIS is associated with an decrease of  $692$692  in house price net of the other variables. The confidence interval gives us a range of plausible values for this average change, about ( $398,$998$398,$998 ).

### Predicting Prices

Now we have found all the main features which We are going to find the prices using `lr.predict`.


```python
print(lr.predict(X)[0:6])
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-23-5c9f04bd0644> in <module>()
    ----> 1 print(lr.predict(X)[0:6])
    

    NameError: name 'X' is not defined


lets find the difference between actual price and prediction using a graph


```python
plt.scatter(bos.PRICE, lr.predict(X))
plt.xlabel("Actual Price: $Y_i$")
plt.ylabel("My Predicted price: $\hat{Y}_i$")
plt.title("Actual Vs Predicted proces")
```


```python
mseTotal = np.mean((bos.PRICE - lr.predict(X)) **2)
print(mseTotal)
```


```python
lr = LinearRegression()
lr.fit(X[['PTRATIO']], bos.PRICE)
```


```python
msePTR = np.mean((bos.PRICE - lr.predict(X[['PTRATIO']])) **2)
print(msePTR)
```

### Training and validation data sets

We are going to split the data sets into training and test data sets in order to train our model on training data and check its performance against test data. 


```python
X_train = X[:-50]
X_test = X[-50:]
Y_train = bos.PRICE[:-50]
Y_test = bos.PRICE[-50:]
print(X_train.shape)
```


```python
print(sklearn.datasets)
```


```python
from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt

lr = linear_model.LinearRegression()
boston = datasets.load_boston()
y = boston.target

# cross_val_predict returns an array of the same size as `y` where each entry
# is a prediction obtained by cross validation:
predicted = cross_val_predict(lr, boston.data, y, cv=10)

fig, ax = plt.subplots()
ax.scatter(y, predicted)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
```
