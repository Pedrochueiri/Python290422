from tkinter.messagebox import YESNO


credito = float(input("Seu Credito: "))
total = 0 #variavel acumuladora 
preco = float(input("Preço do produto: "))
while credito >= preco:
    total += preco 
    credito -= preco 
    if preco >= credito:
        print("Credito insuficiente")
        break
    print(f"Total: R$ {total:.2f} \nCredito: R$ {credito:.2f}")
    x = int(input("Deseja continuar comprando? \n1-Sim \n2-Não"))
    if x == 1:
        preco = float(input("Preço do produto: "))
        continue
    else:
        print("Total da compra: ", total)
        break
print(f"Total: R$ {total: .2f}")
print(f"Credito restante: R$ {credito:.2f}")

