def maximumToys(prices, k):
    prices.sort()
    i = 0
    count = 0

    while k >= prices[i]:
        k -= prices[i]
        i += 1
        count += 1

    print (count)


maximumToys([1,12,5,111,200,1000,10],50)
maximumToys([1,2,3,4],7)
maximumToys([3,7,2,9,4],15)
