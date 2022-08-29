# This code is the solution of the Sherlock and Watson Gym Secrets problem of the KickStart 2022 Practice Session #3
# by Aitsaid Azzedine
import itertools

# Complete the count_pairs function
def count_pairs(a, b, n, k):
  pairs = 0
  # TODO: Add logic to count the number of pairs modulo 10^9+7 (1000000007)
  l = range(1, n+1)
  all_pairs = list(itertools.permutations(l,2))
  for pair in all_pairs:
    if(((pair[0] ** a)+(pair[1] ** b)) % k == 0):
        pairs += 1
  return (pairs % (10 ** 9 + 7 * 1000000007))

if __name__ == '__main__':
  # Read number of test cases
  num_cases = int(input())

  for tc in range(1, num_cases + 1):
    a, b, n, k = map(int, input().split())

    print("Case #%d: %d" % (tc, count_pairs(a, b, n, k)))
