#2.2.Crea un código que imprima en pantalla la siguiente expresión.
#1  A B C
#2  D E F
#3  G H I
letters = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

for x in range(0, len(letters), 3):
    print(letters[x:x+3])
