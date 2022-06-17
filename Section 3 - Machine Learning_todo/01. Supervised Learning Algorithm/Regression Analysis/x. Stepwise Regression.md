
# Stepwise Regression

This regression is used when multiple independed variables are present, The selection of indepedent variables is done using automated process. 
{## TODO ## how its different from multi linear regression}.

The automated selection is achived by observing statistical values like R-square, t-stat, AIC & BIC metric to discern significant variables. 

It basically fits the regression model by adding & dropping co-variables based on defined criteria. 

## Common stepwise approaches

### Forward Selection

it involves starting with no variables in the model, testing the addition of each variable using a chosen model fit criterion, adding the variable (if any) whose inclusion given the most statistacally significant improvement of the fit, and repeating this process until non improves the model to a statically significant improvement of the fit, and repeating this process until non improves the model to a statistically significant extent. 

### Backword elimination

It involves starting with all candidate variables, testing the deletion of each variable using a chosen model fit criteria, deleting the variable (if any) whose loss gives the most statistically insignificant deterioration of the model fit, and repeating this process until no further variables can be deleted without a statistically significant loss of fit.

### Bi-directional elimination

In this a combination of above approaches are employed, testign at each step for variables to be included or excluded. 


```python
import statsmodels.formula.api as smf 
```


```python
def forward_selected(data, response):
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = 0.0, 0.0
    while remaining and current_score == best_new_score:
        scores_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {} + 1".format(response,
                                          ' + '.join(selected + [candidate]))
            score = smf.ols(formula, data).fit().rsquared_adj
            scores_with_candidates.append((score, candidate))
        scores_with_candidates.sort()
        best_new_score, best_candidate = scores_with_candidates.pop()
        if current_score < best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
    formula = "{} ~ {} + 1".format(response,
                                          ' + '.join(selected))
    model = smf.ols(formula, data).fit()
    return model
            
```


```python
import pandas as pd
```


```python
url = "../files/salary.dat"
data = pd.read_csv(url, sep="\\s+")
model = forward_selected(data, "sl")
print(model.model.formula)
print(model.rsquared_adj)
```

    sl ~ rk + yr + 1
    0.835190760538

