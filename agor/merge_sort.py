# coding: utf-8
import copy

# O(n*log(n))


def merge(nums=None, start=None, end=None, mid=None):
    tmp = []
    i = start
    j = mid + 1

    while i <= mid and j <= end:
        if nums[i] > nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1

    if i <= mid:
        tmp.extend(nums[i:mid+1])

    if j <= end:
        tmp.extend(nums[j:end+1])
    nums[start:end+1] = tmp[:]


def merge_sort(nums, start, end):
    if start < end:
        mid = (start + end) / 2
        merge_sort(nums, start, mid)
        merge_sort(nums, mid+1, end)
        merge(nums, start, end, mid)


def main():
    test_nums = [23, 34, 1, 34, 2]
    tn = copy.deepcopy(test_nums)

    if not tn:
        return []

    merge_sort(tn, 0, len(tn) - 1)
    print tn


if __name__ == "__main__":
    main()
