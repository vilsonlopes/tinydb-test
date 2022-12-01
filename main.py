from views import inserir_cliente, buscar_cliente, update_cliente, delete_cliente

print('______Programa CRUD TinyDB_______\n')
print('Use as opções abaixo para usar o Programa')

while True:
    print('''\n-Digite 1 para inserir.
-Digite 2 para ver um cliente.
-Digite 3 para editar.
-Digite 4 para excluir.
-Digite 0 para encerrar.''')

    print('\nDigite uma opção: ')

    opcao = int(input())

    if opcao == 0:
        break

    if opcao == 1:
        inserir_cliente()

    if opcao == 2:
        buscar_cliente()

    if opcao == 3:
        update_cliente()

    if opcao == 4:
        delete_cliente()

    else:
        print('Digite uma opção válida.')
