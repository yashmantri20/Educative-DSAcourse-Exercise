
# Convert Decimal Integer to Binary

def convert_int_to_bin(dec_num):
    s = []
    ans = ''
    while(dec_num != 0):
        s.append(dec_num%2)
        dec_num = dec_num//2
    while(len(s)):
        ans += str(s.pop())
    return ans

