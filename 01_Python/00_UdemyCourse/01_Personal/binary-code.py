inta = int(input())

def binaryNum(num):
    result = []
    while num != 0:
        result.append(num%2)
        num = num // 2
        result.reverse()
    return result

num_output = binaryNum(inta)
print(num_output)

