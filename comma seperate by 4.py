value = []
items=[x for x in raw_input().split(',')]
for p in items:
    print p
    intp = int(p, 2)
    print intp
    if not intp%5:
        value.append(p)

print ','.join(val
