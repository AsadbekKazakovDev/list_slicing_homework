def main(list1):
    """
    A list of several elements is given. Return the three elements from the beginning.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    return list1[:3]
list1 = [1,2,3,4,5]
print(main(list1))