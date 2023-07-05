def main(list1,n):
    """
    A list of several elements is given. Return all items from end n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    if n<0:
        return list1[::n]
    else:
        return list1[::(-1*n)]
a = ['a', 1, 'b', 2, 'c', 3, 'd', 4]
n = 2
print(main(a,n))
list1=['a', 'b', 'c', 'd', 'e', 'f']
n = -1
print(main(list1,n))


