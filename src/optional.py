import compute


def ex_gcd(a, b=0b100011011):  # 采用书上的递归方法
    if b == 0:
        return a, 1, 0
    else:
        gcd, x_temp, y_temp = ex_gcd(b, compute.mod(a, b))
        x = y_temp
        y = x_temp ^ compute.mul(y_temp, compute.divide(a, b))

        return [gcd, x, y]


def inv(a, b=0b100011011):  # 求逆元
    return compute.fast_pow(a, 254, b)  # 由于poly^255=1，只要求出poly^254就是逆元


def irr_poly(n):
    irr = [0b10, 0b11]
    result = []
    for i in range(0b100, 2 ** (n + 1)):  # 逐个完成检查
        flag = 1
        for poly in irr:
            gcd, x, y = ex_gcd(i, poly)  # 仅需要对之前的不可约多项式进行因子检查
            if gcd != 1:
                flag = 0
        if flag == 1:
            irr.append(i)
            if i > 0b100000000:  # 输出x^8以上的多项式
                result.append(i)
    return result


def pri_poly(n):
    irr = irr_poly(n)  # 求不可约多项式
    m = 2 ** n - 1
    result = []
    check_m = 1 << m
    for poly in irr:
        flag = 1  # 检查通过的flag
        if compute.mod(check_m+1, poly) != 0:  # 检查x^m+1
            flag = 0
        else:
            for q in range(8, m):
                check_q = 1 << q
                if compute.mod(check_q+1, poly) == 0:  # 检查 x^q+1
                    flag = 0
        if flag == 1:
            result.append(poly)
    return result


def main():
    gcd, x, y = ex_gcd(0x75, 0x35)
    print(hex(x), hex(y), hex(gcd))
    gcd, x, y = ex_gcd(0xac, 0x59)
    print(hex(x), hex(y), hex(gcd))
    gcd, x, y = ex_gcd(0xf8, 0x2e)
    print(hex(x), hex(y), hex(gcd))
    gcd, x, y = ex_gcd(0x48, 0x99)
    print(hex(x), hex(y), hex(gcd))
    print(hex(inv(0x8c)))
    print(hex(inv(0xbe)))
    print(hex(inv(0x01)))
    print(hex(inv(0x2d)))
    ls = pri_poly(8)
    for poly in ls:
        print(bin(poly))
    print(ls)
    # a = int(input('a='), 16)
    # ex_gcd(a)


if __name__ == '__main__':
    main()
