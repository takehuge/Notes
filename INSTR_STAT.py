dev01 = "a"
dev02 = {}
dev02['sex'] = "male"

"""The permutations"""
def dev(word):
    def permutations(items):
        n = len(items)
        if n == 0:
            yield []
        else:
            for i in range(len(items)):
                for cc in permutations(items[:i] + items[i + 1:]):
                    yield [items[i]] + cc

    possibility = []
    for p in permutations(list(word)):
        possibility.append(''.join(p))

    return possibility
