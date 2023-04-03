sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros

sp = (sp*100)/total
rj = (rj*100)/total
mg = (mg*100)/total
es = (es*100)/total
outros = (outros*100)/total

print(f" O faturamento de São Paulo Soma {sp:.2f}%") 
print(f" O faturamento de Rio de Janeiro Soma {rj:.2f}%") 
print(f" O faturamento de Minas Gerais Soma {mg:.2f}%") 
print(f" O faturamento de Espirito Santo Soma {es:.2f}%") 
print(f" O faturamento de Outros estados Soma {sp:.2f}%") 