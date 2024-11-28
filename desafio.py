def main():
    nome = input("Qual o nome do heroi? ")  
    xp = int(input("Qual o seu xp? "))
    classificator = get_class(xp)
    print(f"O Herói de nome {nome} está no nível de {classificator}")

   
def get_class(xp):
    if xp <= 1000:
        return "ferro"
    elif xp <= 2000:
        return "bronze"
    elif xp <= 5000:
        return "prata"
    elif xp <= 7000:
        return "ouro"
    elif xp <= 8000:
        return "platina"
    elif xp <= 9000:
        return "ascendente"
    elif xp <= 10000:
        return "imortal"
    else:
        return "radiante"


main()
    