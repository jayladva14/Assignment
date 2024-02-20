def findErrorNums(nums):
    n = len(nums)
    sum_nums = sum(nums)
    sum_sq_nums = sum(x * x for x in nums)

    S = n * (n + 1) // 2
    S_sq = n * (n + 1) * (2 * n + 1) // 6

    diff = S - sum_nums
    diff_sq = S_sq - sum_sq_nums

    y = (diff_sq // diff - diff) // 2
    x = diff + y

    return [y, x]

def userInput():
    input_string = input()
    userNums = [int(x) for x in input_string.split()]

    if len(userNums) < 2:
        print()
        return

    result = findErrorNums(userNums)
    print(result)
userInput()