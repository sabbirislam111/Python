day1 = [23, 17, 34, 12, 5]
day2 = [34, 23, 54, 11, 9]
day3 = [76, 45, 75, 29, 3]
day4 = [16, 17, 89, 78, 2]
day5 = [11, 10, 71, 32, 8]
day6 = [33, 10, 99, 36, 6]
day7 = [18, 17, 34, 19, 9]

index_wise = [day1, day2, day3, day4, day5, day6, day7]

final_list = []
for i in index_wise:
    final_list += i

print(f'Min = {min(final_list)}\nmax = {max(final_list)}')


