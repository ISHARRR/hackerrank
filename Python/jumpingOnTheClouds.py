
def jumpingOnClouds(c):

    jumps = 0
    i = 0
    while i < (len(c)-1):
        if c[i] == 1:
            i = i + 1
            jumps = jumps + 1
            print (c,jumps, '1')

        else:
            i = i + 2
            jumps = jumps + 1
            print (c,jumps, '2')

    print (jumps)

# def jumpingOnClouds(c):
#     c.append('*')
#     jumps = 0
#     i = 0
#     while i < len(c):
#         if c[i] == 0 and c[i+1] == 0 and c[i+2] == 1:
#             i = i + 2
#
#         elif c[i] == 1 and c[i+1] == 0 and c[i+2] == 0:
#             i = i + 2
#
#         elif c[i] == 0 and c[i+1] == 0 and c[i+2] == '*':
#             i = i + 1
#
#         elif c[i] == 0 and c[i+1] == 0 and c[i+2] == 0:
#             c.pop(i)
#
#         elif c[i] == 0 and c[i+1] == 1:
#             i = i + 1
#
#         elif c[i] == 1 and c[i+1] == 0:
#             i = i + 1
#
#         elif c[i] == 0 and c[i+1] == '*':
#             break
#
#     for i in c:
#         if i == 0:
#             jumps = jumps + 1
#     return (jumps - 1)





jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])
jumpingOnClouds([0, 0, 0, 1, 0, 0])
