# Static and Dynamic Code Analysis Report

## Static Analysis

**Pylint**:

- Line 5: Missing function or method docstring (missing-function-docstring)
- Line 12: Missing function or method docstring (missing-function-docstring) 
- Line 19: Missing function or method docstring (missing-function-docstring) 
- Line 26: Missing function or method docstring (missing-function-docstring) 
- Line 28: Unused variable 'output' (unused-variable)
- Line 1: Unused import math (unused-import)
- Line 2: Unused import random (unused-import)

**Flake8**
- Line 6: line too long (93 > 79 characters)

### Fix Summary 

**Pylint**

- Added a newline after the end of the code.
- Added a docstring to the first line of the program explaining the code.
- Added docstring to expensive_op function
- Added docstring to the slow_func function
- Added docstring to unused_function
- Added docstring to main 
- Decided to print output for testing purposes
- Got rid of imports, they were unused 

**Flake8**
- I shortened the line characters.

## Line profiler
### Bottleneck found in:
- ‘Expensive_op’ was very time-consuming somewhere around 122764899.1 microseconds for the line “ total += i*n “.
- ‘Slow_func’ was overly slow as well.

### Fixes:

**Def expensive_op(n):**

I optimized this function by replacing it with an arithmetic series formula, using cache, and it shortened the time spent. Previously, it was 122764899.1 microseconds for the line “ total += i*n “ and now the time is 948.8 microseconds for the whole function.

**Def slow_func(lst):**

I optimized this function by using a list comprehension instead and that greatly improved the time in the line profiler chart.

**Def unused_function():**

I optimized this function by getting rid of unnecessary variables and that made it more efficient. 


## Code Coverage
Coverage before: 92%
Coverage after: 100%

### Fix
- ‘unused_function()’ not covered, so I removed it, and for testing purposes, I used the other functions in main otherwise, they wouldn’t have been covered either.






