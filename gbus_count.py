# This code is the solution of the GBus_Count problem of the KickStart 2022 Practice Session #3
# by Aitsaid Azzedine

# The most important function
def find_number_of_gbuses_per_city(gbus_list, cities):
  bus_count_lst = []
  for n in range(len(cities)):
    count = 0
    for gbus in gbus_list:
        if (gbus[0] <= cities[n] <= gbus[1]):
            count += 1
    bus_count_lst.append(count)
  return bus_count_lst


def main():
  # Get number of test cases
  test_cases = int(input())

  for test_case in range(1, test_cases + 1):
    # Get gbuses
    num_gbuses = int(input())
    # Put gbus cities into a list of tuples of [start, end]
    gbus_list = input().split()
    gbus_list = [(int(gbus_list[i]), int(gbus_list[i + 1]))
                        for i in range(len(gbus_list))
                        if i % 2 == 0]
    # Get cities
    num_cities_to_return = int(input())
    cities_list = []
    for i in range(num_cities_to_return):
      cities_list.append(int(input()))

    ans = find_number_of_gbuses_per_city(gbus_list, cities_list)
    print("Case #%d:" % (test_case), end=" ")
    for i in range(len(ans)):
      print("%d" % ans[i], end=" ")
    print("") # print new line after each case.

    # blank line between test cases
    if test_case != test_cases:
      _ = input()



if __name__ == "__main__":
  main()
