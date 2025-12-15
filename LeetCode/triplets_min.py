import sys
from bisect import bisect_left

def nC3(n):
    if n < 3:
        return 0
    return (n * (n-1) * (n-2)) // 6

def solve_from_lists(A, queries):
    # queries : list of integer K (1-indexed positions)
    from collections import Counter
    freq = Counter(A)
    # unique values sorted ascending
    vals = sorted(freq.keys())
    m = len(vals)
    # build suffix counts: for each value v, cnt_ge[v] = number of elements >= v
    # compute list cnt_ge aligned with vals (ascending), where cnt_ge[i] = sum freq[vals[i]:]
    counts = [freq[v] for v in vals]
    # suffix sums: start from right
    cnt_ge = [0] * m
    s = 0
    for i in range(m-1, -1, -1):
        s += counts[i]
        cnt_ge[i] = s

    # compute number of triplets whose min == vals[i]
    trip_counts = [0] * m
    for i in range(m):
        c_ge = cnt_ge[i]
        c_next = cnt_ge[i+1] if i+1 < m else 0
        trip_counts[i] = nC3(c_ge) - nC3(c_next)

    # build prefix sums (cumulative counts) in ascending order of minima
    cum = []
    running = 0
    for t in trip_counts:
        running += t
        cum.append(running)

    total_triplets = cum[-1] if cum else 0

    # answer queries: find smallest index i where cum[i] >= K
    answers = []
    for K in queries:
        if K < 1 or K > total_triplets:
            answers.append(-1)
            continue
        idx = bisect_left(cum, K)  # idx in [0, m-1]
        answers.append(vals[idx])
    return answers

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    try:
        n = int(next(it))
    except StopIteration:
        return
    A = []
    for _ in range(n):
        A.append(int(next(it)))
    try:
        q = int(next(it))
    except StopIteration:
        q = 0
    queries = []
    for _ in range(q):
        try:
            queries.append(int(next(it)))
        except StopIteration:
            break

    results = solve_from_lists(A, queries)
    out = '\n'.join(str(x) for x in results)
    print(out)

if __name__ == "__main__":
    main()
