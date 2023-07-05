def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    k = list1[::-1]
    m = list1 + k
    return m
list1  = [1,2,3,4,5]
print(main(list1))