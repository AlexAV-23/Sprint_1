
def digit_root(num:int):
    if num > 10000000:
        print(f'Ошибка: число {num} превышает 10 000 000')
        return None
    amount = 0
    while num:
        amount += num % 10
        num //= 10
        if not (amount // 10) and not num:
            return amount
        if not num:
            num = amount
            amount = 0
    
print(digit_root(4851))
print(digit_root(97569))
print(digit_root(889987))
print(digit_root(10000001))