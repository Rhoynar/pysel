names = [
    'John',
    'Mary',
    'Joe',
    'Matt',
    'David',
    'Matt',
    'John'
]

results = []

for name in names:
    if name in results:
        continue
    results.append(name)

print(results)