def inverse(mod, number):
    r = [mod, number, mod % number]
    q = [0, mod // number]
    s = [1, 0]
    t = [0, 1]

    num = 2
    while r[num] != 0:
        q.append(r[num - 1] // r[num])
        s.append((s[num - 2]) - s[num - 1] * (q[num - 1]))
        t.append((t[num - 2]) - t[num - 1] * (q[num - 1]))
        r.append(r[num - 1] % r[num])
        num += 1

    result = t[len(t) - 1]
    if result > 0:
        return result
    else:
        return result + mod
