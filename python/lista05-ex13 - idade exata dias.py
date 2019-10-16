vividos = int(input('dias vividos:'))
anos = vividos//365
meses = (vividos%365)//30
dias = vividos -anos*365-meses*30
print('foram vividos',anos,'anos,',meses,'meses e',dias,'dias')
