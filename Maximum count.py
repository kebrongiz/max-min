def get_max_count():
    nums = []

    curr_num = 1

    while curr_num != 0:
        curr_num = int(input("Enter a number(0 for end): "))
        nums.append(curr_num)

    max = nums[0]
    count = 1
    for num in nums[1:]:
        if num > max:
            max = num
            count = 1
        elif num == max:
            count += 1

    print("The largest number is {}".format(max))
    print("The occurrence count of the largest number is {}".format(count))


get_max_count()
