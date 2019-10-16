valorhora = float(input('informe o valor da hora trabalhada:'))
qhoras = float(input('informe a quantidade de horas tralhadas no mês:'))
salario = valorhora*qhoras
ir = salario*0.11
inss = salario*0.08
sindicato = salario*0.05
liquido = salario-ir-inss-sindicato
print('salario bruto',salario,'reais')
print('IR', ir,'reais')
print('INSS',inss,'reais')
print('sindicato',sindicato,'reais')
print('liquido',liquido, 'reais')
input('.')