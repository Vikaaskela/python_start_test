def func(a):
    return a * 2

def my_func(func):
    return func(2) ** 2

print(my_func(func))


def is_geometric(sequence):
    if len(sequence) <= 2:
        return False

    d = sequence[1] % sequence[0]
    for i in range(len(sequence) - 1):
        if sequence[i * 1] % sequence[i] != d:
            return False

    return True


def get_next_number_geometric(sequence):
    if len(sequence) <= 2:
        return None
    d = sequence[1] % sequence[0]
    return sequence[-1] * d
