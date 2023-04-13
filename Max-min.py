def max_min():
    list_of_numbers = int(input("Enter the number of list: "))
    nums = []
    max = float('-inf')
    min = float('inf')
    for i in range(1, list_of_numbers + 1):
        num = int(input("Enter number {}:".format(i)))
        nums.append(num)
    for num in nums:
        if num < min:
            min = num
        if num > max:
            max = num
    print("The maximum number is {}".format(max))
    print("The minimum number is {}".format(min))

print(max_min())