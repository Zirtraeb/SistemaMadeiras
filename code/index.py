print('Bem-vindos à madereira de Beatriz Avelar')

print('PIN - Pinho')
print('PER - Peroba')
print('MOG - Mogno')
print('IPE - Ipê')
print('IMB - Imbuia')


def escolha_tipo(): 
  while True:
    tipo = input('Digite as letras indicadas acima para o tipo de madeira desejada: ')

    if(tipo == 'PIN'):
      valor = 150.40
    elif(tipo == 'PER'):
      valor = 170.20
    elif(tipo =='MOG'):
      valor = 190.90
    elif(tipo =='IPE'):
      valor = 210.10
    elif(tipo =='IMB'):
      valor = 220.70
    else:
      print('Inválido. Digite novamente.')
      continue
    return valor


def qtd_toras(): 
  while True:
    try:
      quantidade = int(input('Informe a quantidade de toras desejadas (Máximo 2000): '))
    except:
      print('Apenas números devem ser informados.')
      continue
    if(quantidade < 100):
      desconto = 0
    elif (quantidade >= 100) and (quantidade < 500):
      desconto = 4/100
    elif (quantidade >= 500) and (quantidade < 1000):
      desconto = 9/100
    elif (quantidade >= 1000) and (quantidade <= 2000):
      desconto = 16/100
    else:
      print('Quantidade inválida, digite um número entre 1 e 2000.')
      continue
    return quantidade, desconto


def frete(): 
  while True:
    print('Qual tipo de entrega deseja?')
    print('Digite 1 para transporte rodoviário')
    print('Digite 2 para transporte ferroviário')
    print('Digite 3 para transporte hidroviário')
    transporte = int(input(''))
    if(transporte == 1):
      valor = 1000
    elif(transporte == 2):
      valor = 2000
    elif(transporte == 3):
      valor = 2500
    else:
      print('Digite uma opção válida.')
      continue
    return valor


tipo = escolha_tipo()
quantidade, desconto = qtd_toras()
frete = frete()

total = ((tipo * quantidade) * (1-desconto)) + frete
print(f'Valor de {quantidade} unidades = {tipo * quantidade}')
print(f'Valor do frete = {frete}')
print(f'O valor total do pedido com desconto + frete = R${total}')
