tabela = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
          'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
          's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
          '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
          '7': '--...', '8': '---..', '9': '----.'}

print("Programa feito para reescrever um texto para o Código Morse.")
texto = input("\nDigite o texto: ")

symbols = []
for x in range(len(texto)):
    caractere = texto[x].lower()
    if caractere in tabela.keys():
        symbols.append(caractere)

morse = list(map(lambda c: tabela[c], symbols))
conversao = ' '.join(morse)
print(f"\nO texto em Código Morse é:\n{conversao}")