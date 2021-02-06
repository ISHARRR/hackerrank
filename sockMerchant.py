# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    ar.sort()
    ar.append('*')

    while i<n:
        if ar[i] == ar[i+1]:
            i += 2
            pairs = pairs + 1
        else:
            i += 1
    return pairs

sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
