import json

with open('dados.json') as tmp:
    data = json.load(tmp)
    
data_num = len(data) - 1

while data_num >= 0:
    if data[data_num]['valor'] == 0:
        data.pop(data_num)
    data_num -= 1
    
media = 0
faturamento = []
i = 0
for datas in data:
    valor = datas['valor']
    faturamento.insert(i, valor)
    i+=1
    media = media + valor

data_num = len(data) - 1
print('o valor medio de faturamento diario é de ',round(media/(data_num+1),2))
while data_num >= 0:
    if data[data_num]['valor'] == min(faturamento):
        print('o dia de menos faturamento foi ',data[data_num]['dia'],' com o valor de R$',round(data[data_num]['valor'],2))
    if data[data_num]['valor'] == max(faturamento):
        print('o dia de Maior faturamento foi ',data[data_num]['dia'],' com o valor de R$',round(data[data_num]['valor'],2))                                                                            
    data_num -= 1