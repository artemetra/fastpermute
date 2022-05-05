# A simple way to find the nth term of a permutation

Example:
```
>>> generate_nth_term([1, 2, 3], 4, 7)
[1, 1, 3, 2]
```

Explanation:
If we generate a sequence of permutations with length=4 we'll
get this list:
```
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
```

where the seventh element is the permutation we looked for.