def count_users_with_age(data:list, age:int) -> int:
    """
    Return the number of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        int: The number of users with the given age
    """
    count=0
    for i in data:
        if i['job']=='Student':
            count+=1
    return count
data = [
  {
    'name': 'John',
    'job': 'Barber'
  }, 
  {
    'name': 'Mary',
    'job': 'Developer'
  },
  {
    'name': 'Ann', 
    'job': 'Teacher'
  }
  ]
print(count_users_with_age(data,'Student'))