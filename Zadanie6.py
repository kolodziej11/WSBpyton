def main():
    liczba = int(input('Podaj liczbę:'))
    def fib(n):
        if n < 2:
            return n
        return fib(n - 2) + fib(n - 1)

    print([fib(el) for el in range(liczba) if el != 0 and el != 1 and el != 2])

if __name__ == '__main__':
    main()