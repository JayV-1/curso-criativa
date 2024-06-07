def main():
    conta = conta_em_float(input("Qual foi o valor da conta? "))
    porcentagem = porcentagem_em_float(input("Qual porcentagem da gorjeta? "))
    gorjeta = conta * porcentagem
    print(f"Valor da gorjeta: ${gorjeta:.2f}")


def conta_em_float(valor):
    valor = float(valor.replace('$', ''))
    
    return (valor)
    


def porcentagem_em_float(p):
    p = float(p.replace('%',''))/100

    return(p)


main()