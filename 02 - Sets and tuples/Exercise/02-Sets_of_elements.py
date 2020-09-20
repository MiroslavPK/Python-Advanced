n, m = map(int, input().split())

n_set = set()
m_set = set()

for i in range(n+m):
    if i < n:
        n_set.add(input())
    else:
        m_set.add(input())

intersection = n_set & m_set

print('\n'.join(intersection))
