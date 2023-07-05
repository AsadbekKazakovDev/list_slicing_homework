def main(list1,n):
    """
    A list of several elements is given. Return all items from the beginning in n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    return list1[::n]
list1=['a', 'b', 'c', 'd', 'e', 'f']
n = -1
print(main(list1,n))