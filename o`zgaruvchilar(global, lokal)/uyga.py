import time

#1- masala
def timedomer(funksiya):
    def wrapper(*args, **kwargs):
        bosh_vaqt = time.time()  # Funksiya bajarilishidan oldingi vaqt
        result = funksiya(*args, **kwargs)  # Funksiyani bajarish
        tug_vaqt = time.time()  # Funksiya bajarilishidan keyingi vaqt
        print(f"Funksiya bajarish vaqti: {tug_vaqt - bosh_vaqt} soniya")
        return result

    return wrapper


@timedomer
def misol_funksiya():
    for _ in range(1000000):
        pass


misol_funksiya()




# 2 - masala
def fibonacci(n):
    def wrapper(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
    return list(wrapper(n))

n = 10
print(fibonacci(n))

