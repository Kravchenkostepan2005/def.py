import time


def showtime(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'{func.__name__} executed in {t2 - t1} sec')
        return result
    return wrapper


@showtime
def original_func(a, b):
    res = a ** b
    print(res)
    return res

if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    original_func(a, b)
   def withdraw(self, a):
        cash = 5000000
        balance = 10000
        if a < cash:
            return balance + a
        else:
            return "You want to withdraw too much"
    a = int(input("How much do you want to withdraw? "))
    balance = 10000
    balance1 = balance + a
    account_2 = BankAccount('User', 4698346, 6056, balance1)
    print(account_2)

def showtime1(withdraw):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = withdraw(*args, **kwargs)
        t2 = time.time()
        print(f'{withdraw.__name__} executed in {t2 - t1} sec')
        return result
    return wrapper


@showtime1
def original_func1():
    with open("abc1.txt", "w") as f:
        t1 = time.time()
        t2 = time.time()
        f.write(f"{original_func1.__name__} executed in {t2 - t1} sec")
