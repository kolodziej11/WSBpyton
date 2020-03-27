from random import randrange

def main():
    lista = []
    for i in range(10):
        n = randrange(1, 50)
        lista.append(n)
    print(lista)
    
    print(list(
        filter(lambda arg: pierwsza(arg), lista)
    ))
    print([k for k in lista if pierwsza(k)])
    
def pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    first = int(n**0.5) + 1
    for dzielnik in range(3, first, 2):
        if n % dzielnik == 0:
            return False
    return True

    print(list(
        filter(lambda arg: pierwsza(arg), lista)
    ))
    print([k for k in lista if pierwsza(k)])


if __name__ == '__main__':
     main()