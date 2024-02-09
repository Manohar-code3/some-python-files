import sys

def getDataFromUser():
    print("Enter data word (binary): ", end="")
    return input()

def getCRCgenerator():
    print("Enter CRC generator (binary): ", end="")
    return input()

def findDividend(dataword, crcGenerator):
    dividend = dataword
    crcLength = len(crcGenerator)
    for i in range(crcLength - 1):
        dividend += "0"
    return dividend

def division(dividend, crcGenerator):
    remainder = dividend
    for i in range(len(remainder) - len(crcGenerator) + 1):
        if remainder[i] == '1':
            for j in range(len(crcGenerator)):
                remainder = remainder[:i + j] + ('0' if remainder[i + j] == crcGenerator[j] else '1') + remainder[i + j + 1:]
    return remainder[len(remainder) - len(crcGenerator) + 1:]

dataword = getDataFromUser()
crcGenerator = getCRCgenerator()
dividend