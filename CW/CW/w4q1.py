def complement(sum, m):
    bits = list(sum)
    for i in range(m):
        if bits[i] == '1':
            bits[i] = '0'
        else:
            bits[i] = '1'
    return ''.join(bits)

def calcheck(data, k, m):
    a = int(data[0], 2)
    b = 0
    c = 0
    for i in range(1, k):
        b = int(data[i], 2)
        c = a + b
        temp = bin(c)[2:]
        if len(temp) > m:
            temp = temp[1:]
            c = int(temp, 2)
            c = c + 1
        a = c
    sum = bin(c)[2:]
    t = sum
    if len(sum) < m:
        dif = m - len(sum)
        for i in range(dif):
            t = '0' + t
    sum = t
    return sum

k = int(input("Enter how many segments: "))
m = int(input("How many bits per segment: "))
data = []
for i in range(k):
    segment = input("Enter segment " + str(i+1) + ": ")
    data.append(segment)
checksum = complement(calcheck(data, k, m), m)
print("Check sum Generated is: " + checksum)
