"""
Problem Link : https://leetcode.com/problems/number-complement/
"""

"""
Approach 1 : Brute Force
    Convert the given integer into binary and then flip each of the binary number and convert it 
    back to integer again.

Approach 2 : Get the nearest 2 power value which is greater than the given number and subtract 1 from the 
    number which is obtained and store it in some variable "a".
    Then subtract the given number from  "a" so as to get the complement of given number.
"""


def findComplement1(num):
    binary = bin(num)[2:]
    res = ""
    for ch in binary:
        if ch == "1":
            res += "0"
        else:
            res += "1"
    return int(res, 2)


def findComplement2(num):
    if num == 0:
        return 1

    temp = 1
    while temp <= num:
        temp <<= 1
    return (temp - 1) - num


print(findComplement1(1024))
print(findComplement2(1024))