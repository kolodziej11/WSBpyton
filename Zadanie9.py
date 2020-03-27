def main():

plik = open("C:\wsb.txt", "rt")
data = plik.read()
slowa = data.split()

print('Liczba słów w pliku:', len(words))

if __name__ == '__main__':
    main()