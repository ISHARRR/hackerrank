def countSwaps(a):
    count = 0
    print (a)
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count = count + 1
    print ('Array is sorted in', count, 'swaps.')
    print ('First Element:', a[0])
    print ('Last Element:', a[-1])

countSwaps([3,2,1])
