def countingValleys(n, s):
    count = 0
    vally = 0
    for i in s:
        if i == 'U':
            count = count + 1
            if count == 0:
                vally = vally + 1
        else:
            count = count - 1
    print vally

countingValleys(8, ['U','D','D','D','U','D','U','U'])
