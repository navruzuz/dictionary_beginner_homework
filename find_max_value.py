def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    return data.popitem()
data = {
    'a': 'abc',
    'b': 'def', 
    'c': 'ghi'
  }
print(find_max_value(data))