def fill_jug_with_cups(N, cups, L):
    cups.sort(reverse=True)  # Sort cups in descending order to use larger cups first
    frequencies = [0] * N
    remaining_capacity = L

    while remaining_capacity > 0:
        used_cup = -1
        max_distinct_cups = 0

        for i in range(N):
            if cups[i] <= remaining_capacity and frequencies[i] < cups.count(cups[i]):
                distinct_cups = len(set([cups[j] for j in range(N) if cups[j] <= remaining_capacity]))
                
                if distinct_cups > max_distinct_cups:
                    max_distinct_cups = distinct_cups
                    used_cup = i

        if used_cup == -1:
            break  # No cup can be used further

        remaining_capacity -= cups[used_cup]
        frequencies[used_cup] += 1

    return frequencies

# Input
N = int(input())
cups = list(map(int, input().split()))
L = int(input())

frequencies = fill_jug_with_cups(N, cups, L)

# Output
for cup in cups:
    print(cup, end=' ')
print()

for frequency in frequencies:
    print(frequency, end=' ')
print()
