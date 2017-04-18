# coding: utf-8


def partial(nums, lo, hi):
    i = lo
    j = hi

    while True:

        while nums[i] < nums[lo]:
            # 独立循环找到一个比 nums[lo] 大的数
            i += 1
            if i == hi:
                break

        while nums[j] > nums[lo]:
            j -= 1
            if j == lo:
                break

        if i >= j:
            break

        nums[i], nums[j] = nums[j],nums[i]
    nums[j], nums[lo] = nums[lo], nums[j]
    return j


def sort(nums, lo, hi):
    if lo < hi:
        j = partial(nums, lo, hi)
        sort(nums, lo, j)
        sort(nums, j + 1, hi)


nums = [1, 4, 2, 34, 11]

sort(nums, 0, len(nums) - 1)
print nums


