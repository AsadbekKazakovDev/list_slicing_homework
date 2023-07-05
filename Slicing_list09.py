def main(list1,n):
    """
    A list of several elements is given. Return all items except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    return list1[n:]
list1 = ['a', 1, 'b', 2, 'c', 3, 'd', 4]
n = 2
print(main(list1,n))