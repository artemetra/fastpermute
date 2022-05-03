def generate_nth_term(options: list, length: int, n: int, *, cycle=False) -> list:
    """Generates the nth term of a permutation sequence.
    Example:
    >>> generate_nth_term([1, 2, 3], 4, 7)
    [1, 1, 3, 2]
    Explanation:
    If we generate a sequence of permutations with length=4 we'll
    get this list:
    0: 1 1 1 1
    1: 1 1 1 2
    2: 1 1 1 3
    3: 1 1 2 1
    4: 1 1 2 2
    5: 1 1 2 3
    6: 1 1 3 1
    7: 1 1 3 2
    8: 1 1 3 3
        ...

    `generate_nth_term` won't generate the entire sequence but will
    just use some basic maths to figure out the term

    :param list options: list of elements to be used in permutations
    :param int length: length of permutation
    :param int n: nth term
    :param bool cycle: cycle if `n` is out of bounds, defaults to False
    :raises ValueError: if `n` is out of bounds and cycle=False
    :return list:
    """
    term = []
    _len = len(options)
    _bound = (_len ** (length)) - 1
    if not cycle and n > _bound:
        raise ValueError(f"The Nth term is out of bounds [{_bound}]")
    n %= _bound  # even if `cycle` is false, it won't change anything
    for i in range(length - 1, -1, -1):
        idx = (n // _len**i) % _len
        term.append(options[idx])
    return term
