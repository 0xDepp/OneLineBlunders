(lambda xxx: print("\n".join(list(map(str, list(filter(lambda v: v!=-1, [xx if sum(xx) == 100 else -1 for xx in (__import__("itertools")).combinations(xxx, 7)]))[0])))))([int(input()) for _ in range(9)])