def divide_numbers(a,b)
  For this function I created 3 test cases. The second one was an edge case where I checked if dividing by zero raised a Zero Division Error and it did by default. So, I simply modified the function to explicitly raise a zero division error with a custom error message which optimized it.

def reverse_string(s)
  This function didn't handle non-string input properly, so I decided to add an if statement to verify if the passed in s parameter was a string and if it wasn't I raised a customized type error saying "Input must be a string."


def get_list_element(lst, index):
  For this function I discovered two errors from my test cases. The first one was that the else was simply returning "Not found" instead of an actual error. So, I fixed it to return a index error with a customized message. The other error was that there wasn't any checks to make sure the index was a number and not a string.
  




