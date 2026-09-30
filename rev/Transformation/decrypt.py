s = '慣慤敭祻ㄶ形楴獟楮獴㌴摟潦弸強㤰扡㌷敽'

flag = ''
for ch in s:
    n = ord(ch)              # e.g. 0x6163
    hi = n >> 8              # 0x61 -> 'a'
    lo = n & 0xFF            # 0x63 -> 'c'
    flag += chr(hi) + chr(lo)
print(flag)