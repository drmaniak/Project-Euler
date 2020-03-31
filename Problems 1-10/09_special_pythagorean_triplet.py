s = 1000
for a in range(1, s):
    for b in range(a+1, s):
        c = 1000 - a - b
        if ((a**2 + b**2) == c**2):
            print(f"a: {a}\nb: {b}\nc: {c}")
            print(a*b*c)

    