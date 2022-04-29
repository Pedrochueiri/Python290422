credito = float(input("Seu Credito: "))
total = 0

quero_comprar = input("Gostaria de comprar? s-n:")
if quero_comprar == "s":
    while True:
        preco = float(input("Preço do produto: "))
        if preco <= credito:
            print("Compra aprovada!")
            total += preco
            credito -= preco
            print(f"Total: R$ {total:.2f} \nCredito: R$ {credito:.2f}")
            continua = input("continuar? s ou n")
            if continua != "s": #!= diferente
                break
            else:
                continue
        else:
            print("Compra não aprovada!")
            print(f"Total: R$ {total:.2f} \nCredito: R$ {credito:.2f}")
            continue
else:
    print("OK... obrigado!")
    print(f"Total: R$ {total:.2f} \nCredito: R$ {credito:.2f}")

if total > 0:
    print(f"Total: R$ {total:.2f}") #f - format