from itertools import combinations, permutations
a = input("Enter the first word: ").upper()
b = input("Enter the second word: ").upper()
c = input("Enter the result word: ").upper()
all_letters = set(a + b + c)
for comb in combinations(range(10), len(all_letters)):
    for perm in permutations(comb):
        d = dict(zip(all_letters, perm))
        f = lambda x: sum(d[e] * 10**i for i, e in enumerate(x[::-1]))
        if f(a) + f(b) == f(c):
            print ("{} + {} = {}".format(f(a), f(b), f(c)))
