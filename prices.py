import math

def knapsackProblemHelper(giftList, giftCardPrice, best = (math.inf, None)):
    # Base case
    if len(giftList) == 0:
        if best[1] is None:
            print('Not possible')
            return
        return '%s %s' % (best[1][0], best[1][1])
    else:
        # By reducing the size of the list through each iteration,
        # we only check the pairs we have not checked already
        firstTry = giftList.pop()
        for i in giftList:
            newPrice = giftCardPrice - firstTry[1] - i[1]
            if newPrice >= 0 and newPrice < best[0]:
                best = (newPrice, (firstTry, i))
        return knapsackProblemHelper(giftList, giftCardPrice, best)

def knapsackProblem(giftList, giftCardPrice):
    # parse the .txt file
    with open(giftList, 'r') as f:
        data = f.readlines()
    parsedData = [(i.split(',')[0], int(i.split(',')[1]))  for i in data]
    return knapsackProblemHelper(parsedData, giftCardPrice)

# The complexity is between O(n) and O(n^2)
# As the amount of gifts allowed grows, a dynamic programming solution would be quicker
