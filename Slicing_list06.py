def main(list1):
    """A list of several elements is given. Return all items from the beginning in three steps.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    return list1[:len(list1):3]
list1=['a', 'b', 'c', 'd', 'e', 'f']
print(main(list1))