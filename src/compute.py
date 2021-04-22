def add_sub(a, b):  # 加法和减法
    return a ^ b


def mul(a, b, poly=0b100011011):  # 乘法
    ans = 0
    while b > 0:
        if b & 0x01 == 0x01:
            ans ^= a
        a <<= 1
        if a & 0x100 == 0x100:
            a ^= poly
        a &= 0xff
        b >>= 1
    return ans


def divide(a, b):  # 除法
    if b == 1:
        return a
    ans = 0
    while len(bin(a)) >= len(bin(b)):
        rec = len(bin(a)) - len(bin(b))
        a ^= (b << rec)
        ans ^= (1 << rec)
    return ans


def mod(a, b):  # 模运算
    temp_a = a
    temp_b = b
    ans = 0
    if temp_b == 1:
        return 0
    rec = len(bin(temp_a)) - len(bin(temp_b))
    if rec < 0:
        return temp_a
    elif rec == 0:
        return temp_a ^ temp_b
    elif rec > 0:
        while len(bin(temp_a)) >= len(bin(temp_b)):
            temp_a ^= (temp_b << (len(bin(temp_a))) - len(bin(temp_b)))
        return temp_a
    return -1


def fast_pow(x, n, m=0b100011011):  # 快速幂
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = mod(mul(result, x), m)
        x = mod(mul(x, x), m)
        n //= 2
    result = mod(result, m)
    return result


def main():
    print("0x89 +/- 0x4d=%s" % (hex((add_sub(0x89, 0x4d)))))
    print("0xaf +/- 0x3b=%s" % (hex((add_sub(0xaf, 0x3b)))))
    print("0x35 +/- 0xc6=%s" % (hex((add_sub(0x35, 0xc6)))))
    print("0xce * 0xf1=%s" % (hex((mul(0xce, 0xf1)))))
    print("0x70 * 0x99=%s" % (hex((mul(0x70, 0x99)))))
    print("0x00 * 0xa4=%s" % (hex((mul(0x00, 0xa4)))))
    print("0xde / 0xc6=%s ... %s" %
          (hex(divide(0xde, 0xc6)), hex(mod(0xde, 0xc6))))
    print("0x8c / 0x0a=%s ... %s" %
          (hex(divide(0x8c, 0x0a)), hex(mod(0x8c, 0x0a))))
    print("0x3e / 0xa4=%s ... %s" %
          (hex(divide(0x3e, 0xa4)), hex(mod(0x3e, 0xa4))))
    print("0x89^18829=%s" % (hex(fast_pow(0x89, 18829))))
    print("0x3e^28928=%s" % (hex(fast_pow(0x3e, 28928))))
    print("0x19^26460=%s" % (hex(fast_pow(0x19, 26460))))
    print("0xba^13563=%s" % (hex(fast_pow(0xba, 13563))))


if __name__ == "__main__":
    main()
