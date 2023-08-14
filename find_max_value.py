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
    "x": "23",
    "3": "y", 
    "z": "5", 
    7:'a'
  }
print(find_max_value(data))