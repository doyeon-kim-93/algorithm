# def cruch(size):
#     print(size,'망치로 광석을 뿌시는 중..')
#     if size == 1:
#         print('다부셔버림')
#         return
#     cruch(size-1)
#
# cruch(5)

def cruch(size):
    print(size,'망치로 광석을 뿌시는 중..')
    if size == 1:
        print('다부셔버림')
        return 1
    return cruch(size-1) + size


print(cruch(5))