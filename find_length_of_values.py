def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    # for i,item in enumerate (data):
    #     print(i)
    return data.popitem()
data = {
    "x": "23",
    "3": "y", 
    "z": "5", 
    7:'a'
  }
print(find_length_of_values(data))