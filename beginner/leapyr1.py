def leapyr(n):
    if n%4==0 and n%100!=0:
        if n%400==0:
            print n, " a leap year"
    elif n%4!=0:
        print n, " not a leap year"
print leapyr(2016)
