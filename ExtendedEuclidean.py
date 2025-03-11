
def gcd(r0, r1):
    # r0, r1, r2, r3, ..., rn, 0
    # return rn
    while r1 > 0:
        r2 = r0 % r1 
        r0 = r1
        r1 = r2
    return r0

def eea(r0, r1):
    # (r0, s0, t0), (r1, s1, t1), (r2, s2, t2), (r3, s3, t3), ..., (rn, sn, tn), 0 
    # ri = si*r0 + ti*r1
    s0 = 1
    t0 = 0
    s1 = 0
    t1 = 1
    while True:
        q = r0//r1
        r2 = r0 - q*r1
        if r2 == 0:
            return (r1, s1, t1)
        s2 = s0 - q*s1
        t2 = t0 - q*t1

        r0 = r1
        r1 = r2
        s0 = s1
        s1 = s2
        t0 = t1
        t1 = t2

def inverse(r0, r1):
    # Complete this function
    return 0

def main():
    print(inverse(973, 301))
    print(inverse(973, 300))
    print(inverse(97333333333333, 300000000))
    print(inverse(97333333333333, 5678901234))

if __name__ == "__main__":
    main()
    

