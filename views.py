from model import Crud, db


def inserir_cliente():
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    endereco = input('Endereço: ')

    inserir_dados = Crud(nome, telefone, endereco)
    db.insert(inserir_dados.as_dict())


def buscar_cliente():
    busca = input('Qual cliente deseja buscar: ')
    resultado = db.search(Crud.CrudQuery.nome.search(busca))
    print(resultado)


def update_cliente():
    key = input('Nome da chave que deseja mudar (nome, telefone ou endereco): ')
    valor = input('Qual valor deseja colocar: ')
    b_id = int(input('Qual o id do cliente que deseja atualizar: '))
    db.update({f'{key}': f'{valor}'}, doc_ids=[b_id])
    print('\nCliente atualizado com sucesso.')


def delete_cliente():
    b_id = int(input('ID do cliente que deseja excluir.'))
    db.remove(doc_ids=[b_id])
