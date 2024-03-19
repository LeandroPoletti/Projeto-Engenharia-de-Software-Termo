from random import randrange
palavras = ['amar', 'comer', 'partir']

def selecionarPalavra(lista : list) -> str:
    numero = randrange(len(lista))
    return(lista[numero])

def verificarEntrada(entrada: str, correto: str) -> list:
    entrada = entrada.lower()
    correto = correto.lower()
    
    
    while(len(entrada)>len(correto)):
        print("Mais quantidade de letras q a palavra certa")
        entrada = input("Insira novamente: ").lower()
    
    while(len(entrada)<len(correto)):
        print("Mais quantidade de letras q a palavra certa")
        entrada = input("Insira novamente: ").lower()
    
    existe = ['Não'] * len(entrada)
    
    for letra in range(len(entrada)):
        if entrada[letra] in correto:
            if entrada[letra] == correto[letra]:
                existe[letra] = "pos certa"
            else:
                existe[letra] = 'existe mas pos errada'
        
    
    return existe

a = selecionarPalavra(palavras)
print(a)
b = input("AAAAAAAAAAAA")
resultado = verificarEntrada(b, a)
print(resultado)