# This code is the solution of the Wiggle_Walk problem of the KickStart 2022 Practice Session #3
# by Aitsaid Azzedine

def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    N, R, C, Sr, Sc = map(int, input().split())
    instructions = input()

    final_r, final_c = end_position(N, R, C, Sr, Sc, instructions)
    print(f'Case #{test_case}: {final_r} {final_c}')

def end_position(N, R, C, Sr, Sc, instructions):
  path = [(Sr, Sc)]
  for n in range(N):
    last=()
    if instructions[n] == 'N':
      last=(path[-1][0] -1 , path[-1][1])
      while(last in path):
        last=(last[0] -1 , last[1])
      path.append(last)

    if instructions[n] == 'E':
      last = (path[-1][0] , path[-1][1] + 1)
      while(last in path):
        last=(last[0] , last[1] + 1)
      path.append(last)

    if instructions[n] == 'W':
      last = (path[-1][0], path[-1][1] - 1)
      while(last in path):
        last=(last[0], last[1] - 1)
      path.append(last)

    if instructions[n] == 'S':
      last = (path[-1][0] + 1, path[-1][1])
      while(last in path):
        last=(last[0] + 1, last[1])
      path.append(last)

    
  final_r, final_c = path[-1]
  
  return final_r, final_c

if __name__ == '__main__':
  main()
