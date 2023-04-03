num = int(input("Digite o número a ser verficado:"))
num_atual = 1
prox_num = 0
num_anterior = 0

while num > prox_num:
    
    prox_num = num_anterior + num_atual
    num_anterior = num_atual
    num_atual = prox_num
    
    print(num_atual)
    
if num_atual == num:
    print("O número ",num," faz parte da sequencia logica de Fibonacci")
else:
     print("O número ",num," não faz parte da sequencia logica de Fibonacci")
