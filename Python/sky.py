import datetime

#
# def solution(S, K):
#     # write your code in Python 3.6
#     days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#
#     for d in days:
#         if d == S:
#             i = days.index(S)
#             newdate = (i + K)
#             if newdate <= 6:
#                 print( days[newdate])
#             else:
#                 print( days[((i + K) % 7)])
#
# solution('Sat', 23)



def solution(A):
    newArray = [e for e in A if e >= 0 and e < 10]
    newArray.sort(reverse=True)
    print(newArray[0])
solution([-1,-3,2,4,45,])
