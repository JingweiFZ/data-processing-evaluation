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

result = method(processing_result, ground_truth)

```