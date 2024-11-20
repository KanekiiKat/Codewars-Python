def move_zeros(lst):
    for num in lst:
        if num == 0:
            lst.remove()
            lst.append(0)
    return lst
