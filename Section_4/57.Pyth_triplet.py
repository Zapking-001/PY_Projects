"""
Docstring for 57.Pyth_triplet: 

            Efficiency : Time complexity:  O(m•n)
                         Space complexity: Depends on number of triples found.

"""
n = int(input("Enter the range: "))

# Method - 1
def triples_efficient(limit):
    result = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            c_sq = a**2 + b**2
            c = int(c_sq**0.5)
            if c <= limit and c*c == c_sq:
                result.append((a, b, c))
    return result
print(triples_efficient(n))

# Method - 2
def triples_shortest(n):
    return [(a, b, int((a*a + b*b)**.5)) for a in range(1, n+1) for b in range(a, n+1) if (a*a + b*b)**.5 % 1 == 0 and (a*a + b*b)**.5 <= n]

print(triples_shortest(n))

# Method - 3
def triples_mathematical(limit):
    triples_list = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            sum_sq = a*a + b*b
            # Find integer square root without imports
            for c in range(b, limit + 1):
                if c * c == sum_sq:
                    triples_list.append((a, b, c))
                    break
                if c * c > sum_sq:
                    break
    return triples_list

print(triples_mathematical(n))