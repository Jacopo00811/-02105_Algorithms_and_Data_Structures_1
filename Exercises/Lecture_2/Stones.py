N, W = map(int, input().split()) 
List = list(map(int, input().split()))
counter = 0
weight = 0
for w in (sorted(List)):
    if (weight+w) <= W:
        weight += w
        counter += 1
print(counter)


