# In Python, you can write numbers in binary format by starting the number with 0b
print 0b0,    #0
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7

print 0b1 + 0b11
print 0b11 * 0b11

shift_right = 0b1100
shift_left = 0b1

shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right) # 0b11
print bin(shift_left)  # 0b100

# binary operator AND (&)
#0 & 0 = 0
# 0 & 1 = 0
# 1 & 0 = 0
# 1 & 1 = 1
print bin(0b1110 & 0b101) # 0b100

# binary operator OR (|)
# 0 | 0 = 0
# 0 | 1 = 1
# 1 | 0 = 1
# 1 | 1 = 1
print bin(0b1110 | 0b101) # 0b1111

# binary operator XOR (^)
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0
print bin(0b1110 ^ 0b101) # 0b1011

# binary operator NOT (~)
a = 0b111100 # a = 60 before "flipping"
a = ~a
print bin(a) # -0b111101
print a #-61

# check if the fourth bit from the right is on
def check_bit4(input_bit):
    mask = 0b1000
    desired = input_bit & mask
    if desired > 0:
        return "on"
    else:
        return "off"
print check_bit4(0b1100)

# turn third bit on in a
a = 0b10111011
mask = 0b100
a = a | mask
print bin(a) # 0b10111111

# flip every bit
a = 0b11101110
print bin(a ^ 0b11111111) # 0b10001

# function to flip nth bit
def flip_bit(number, n):
    mask = 0b1 << n-1
    result = number ^ mask
    return bin(result)
print flip_bit(0b10100100101, 4) # 0b10100101101
