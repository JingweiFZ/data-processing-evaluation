# data-processing-evaluation

Simple Python module for evaluating the efficiency of data processing.

## Usage
```python
import data_processing_evaluation


processing_result = [[1, 0, 0, 1, 1],
                     [1, 1, 0, 0, 0],
                     [1, 0, 1, 0, 1],
                     [0, 1, 0, 0, 0],
                     [0, 0, 0, 1, 0]]

ground_truth = [[1, 0, 0, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1]]

result = get_coefficients(processing_data, ground_truth_data)

```

## Input
processing_result - Output data from processing process

ground_truth - Test set

## Ancillary variables
top - Test outcome positive

ton - Test outcome negative

## Output
tpr - True positive rate

tnr - True negative rate

fpr - False positive rate

fnr - False negative rate

ppv - Positive predictive value

npv - Negative predictive value

fdr - False discovery rate

for - False omission rate

acc - Accuracy

pre - Prevalence

f_score - F1 score

mcc - Matthews correlation coefficient

plr - Positive likelihood ratio

nlr - Negative likelihood ratio

dor - Diagnostic odds ratio

## Credits
[https://en.wikipedia.org/wiki/Confusion_matrix](https://en.wikipedia.org/wiki/Confusion_matrix)