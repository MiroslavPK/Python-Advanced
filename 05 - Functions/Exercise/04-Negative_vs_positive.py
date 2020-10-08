def neg_vs_pos(nums):
    negatives = sum(num for num in nums if num < 0)
    positives = sum(num for num in nums if num >= 0)

    print(negatives)
    print(positives)
    if abs(negatives) > positives:
        print('The negatives are stronger than the positives')
    else:
        print('The positives are stronger than the negatives')


nums = list(map(int, input().split()))
neg_vs_pos(nums)
