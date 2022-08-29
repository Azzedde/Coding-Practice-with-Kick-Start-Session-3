# This code is the solution of the Record Breaker problem of the KickStart 2022 Practice Session #3
# by Aitsaid Azzedine

def number_of_record_breaking_days(number_of_days, vistors):
  record_breaking_days = 0
  biggest = -1 
  for n in range(number_of_days):
        condition1 = vistors[n] > biggest
        if (n+1 < number_of_days):
            condition2 = vistors[n] > vistors[n+1]
       
        else:
            condition2 = True
                
        if condition1 & condition2:
            record_breaking_days += 1
        if condition1:
            biggest = vistors[n]        
  return record_breaking_days

def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1, 1):
    number_of_days = int(input())
    vistors = list(map(int, input().split()))

    ans = number_of_record_breaking_days(number_of_days, vistors)

    print("Case #{}: {}".format(test_case, ans))

if __name__ == "__main__":
  main()
