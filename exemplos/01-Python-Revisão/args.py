def soma(*num):
    total = 0
    for n in num:
        total += n
    return total

print(soma(1,2,3,4,5,6,7,8))