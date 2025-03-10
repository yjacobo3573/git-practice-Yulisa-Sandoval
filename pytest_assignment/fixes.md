def divide_numbers(a,b)
---
  For this function I discovered a mistake from my test case. The mistake was that there wasn't any error handling for division by 0. So, I simply modified the function to explicitly raise a zero division error with a custom error message which optimized it.

def reverse_string(s)
---
  This function didn't handle non-string input properly, so I decided to add an if statement to verify if the passed in s parameter was a string and if it wasn't I raised a customized type error saying "Input must be a string."


def get_list_element(lst, index):
---
  For this function I discovered two errors from my test cases. The first one was that the else was simply returning "Not found" instead of an actual error. So, I fixed it to return an index error with a customized message. The other error was that there wasn't any checks to make sure the index was an int, so I fixed that by simply adding an if statement to check the type and return a type error saying "Index must be an integer". Another additional bug was the boundary checking, so I modified it to 0 <= index <len(1st) since before it didn't take into account that the user could enter negative numbers.
  




