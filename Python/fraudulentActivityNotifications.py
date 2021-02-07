def activityNotifications(expenditure, d):
    count = 0
    tempindex = 0
    tempList = expenditure[tempindex:d]
    tempList.sort()
        # tempList.append('*')
    if d % 2 != 0:
        for index in range(len((expenditure[d:]))-1):
            mean = int(len(tempList)/2)
            if (mean*2) < expenditure[d]:
                count += 1
                tempindex += 1
                d += 1
            else:
                tempindex += 1
                d += 1

    else:
        for index in range(len((expenditure[d:]))-1):
            mean = (int(len(tempList)/2) * int(len(tempList)/2) - 1)/2
            if (mean*2) < expenditure[d]:
                count += 1
                tempindex += 1
                d += 1
            else:
                tempindex += 1
                d += 1
    print(count)




activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5)
activityNotifications([10, 20, 30, 40, 50], 3)
activityNotifications([1, 2, 3, 4, 4], 4)
