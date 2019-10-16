temp=[]
mes=['janeiro','fevereiro','março','abril','maio','junho','julho',\
     'agosto','setembro','outubro','novembro','dezembro']

for x in range(12):
    t=float(input('informe a temperatura do mês {}: '.format(mes[x])))
    temp.append(t)

media=sum(temp)/len(temp)

for x in range(len(temp)):
    if temp[x]>media:
        print ('{} - {}'.format((temp[x]),mes[x]))