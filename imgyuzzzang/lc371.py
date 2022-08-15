# 371. Sum of Two Integers

def plusOneUnit(a, b):
    if a ^ b:
        return (0,1)
    if a & b:
        return (1,0)
    return (0,0)

def getSum(a: int, b: int) -> int:
    binary_a = bin(a)[2:]
    binary_b = bin(b)[2:]
    res = ''
    print(bin(a))

    maxLength = max(len(binary_a), len(binary_b))
    binary_a = binary_a.zfill(maxLength)
    binary_b = binary_b.zfill(maxLength)

    next = 0
    for unit_a, unit_b in zip(binary_a[::-1], binary_b[::-1]):
        next1, now1 = plusOneUnit(int(unit_a), int(unit_b))
        next2, now2 = plusOneUnit(now1, next)
        next = max(next1, next2)
        res += str(now2)
    
    if next:
        res += '1'

    return int(res[::-1], 2)
        
    
print(getSum(-1,2))
        
# 마이너스 생각 못하고 구현 실패~!~! 우항항