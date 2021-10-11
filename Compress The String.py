import itertools as it
print(*[(len(list(group)), int(key)) for key, group in it.groupby(input())])