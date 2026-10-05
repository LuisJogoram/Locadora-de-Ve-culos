from classes import cliente

opcao = 1
while opcao != 0:
    print('Escolha uma opção')
    print('1 - Criar um cliente')
    print('2 - Criar um contrato')
    # Está escrito "criar", mas ele só edita, se não houver um existente ele cria, mas se já existir um ele edita
    print('3 - Visualizar informações de um condutor')
    print('4 - Visualizar informações de um contrato')
    print('0 - Sair')
    opcao = int(input())

    match opcao:
        case 1:
            erro = False # A existência da variável erro é para fazer a verificação, se essa variável ficar como "True" ele não altera as informações do cliente
            nome = str(input('Informe o nome/razão social do cliente: '))
            if nome.strip() != '':
                tipodocumento = str(input('O documento do cliente é CPF ou CNPJ?: '))
                if tipodocumento.upper() == 'CPF':
                    documento = str(input('Informe o CPF do cliente (coloque apenas números): '))
                    if len(documento) == 11 and documento.isdigit() == True:
                        dval = True
                    else:
                        print('CPF inválido')
                        dval = False
                elif tipodocumento.upper() == 'CNPJ':
                    documento = str(input('Informe o CNPJ do cliente (coloque apenas números): '))
                    if len(documento) == 14 and documento.isdigit() == True:
                        dval = True
                    else:
                        print('CNPJ inválido')
                        dval = False
                else:
                    print('O documento deve ser CPF ou CNPJ')
                    dval = False
                    erro = True
                if dval == True:
                    cnh = str(input('Informe a CNH do cliente: '))
                    if len(cnh) == 11 and cnh.isdigit() == True: # A CNH possui dois números, o número que fica na vertical que tem 10 dígitos e o número de registro que tem 11, não entendi bem qual era pra colocar então deixei o número de registro
                        telefone = str(input('Informe o telefone com DDD do cliente: '))
                        if len(telefone) == 10 and telefone.isdigit() == True:
                            pass
                        else:
                            print('Telefone inválido')
                    else:
                        print('CNH inválida')
                        erro = True
                else:
                    erro = True
            else:
                print('Nome inválido')
                erro = True
            if erro == False: # Criação/Edição do objeto cliente1
                cliente1 = cliente(nome, documento, cnh, telefone)
                print('Cliente atualizado com as seguintes informações: ')
                print('Nome/Razão social:', cliente1.nome)
                if tipodocumento.upper() == 'CPF':
                    print(f'CPF: {cliente1.documento[:3]}.{cliente1.documento[3:6]}.{cliente1.documento[6:9]}-{cliente1.documento[9:]}')
                elif tipodocumento.upper() == 'CNPJ':
                    print(f'CNPJ: {cliente1.documento[:2]}.{cliente1.documento[2:5]}.{cliente1.documento[5:8]}/{cliente1.documento[8:12]}-{cliente1.documento[12:]}')
                print('CNH:', cliente1.cnh)
                print(f'Telefone: ({cliente1.telefone[:2]}){cliente1.telefone[2:6]}-{cliente1.telefone[6:]}')
        
        case 2:
            erro = False # A existência da variável erro é para fazer a verificação, se essa variável ficar como "True" ele não altera as informações do cliente
            dataInicio = str(input('Digite a data de início do contrato: '))
            if len(dataInicio) == 8 and dataInicio.isdigit() == True:
                dataTermino = str(input('Digite a data de término do contrato: '))
                if len(dataInicio) == 8 and dataInicio.isdigit() == True:
                    valor = float(input('Digite o valor total do contrato: '))
                    status = str(input('Digite o status do contrato (ativo, finalizado ou cancelado): '))
                    if status.lower() == 'ativo' or 'finalizado' or 'cancelado':
                        pass
                    else:
                        print('Status inválido')
                        erro = True
                else:
                    print('Data inválida')
                    erro = True
            else:
                print('Data inválida')
                erro = True
            if erro == False: # Criação/Edição do contrato do cliente1
                cliente1.aluguel(dataInicio, dataTermino, valor, status)
                print('Aluguel feito com as seguintes informações: ')
                print(f'Data de início: {cliente1.contrato.dataInicio[:2]}/{cliente1.contrato.dataInicio[2:4]}/{cliente1.contrato.dataInicio[4:]}')
                print(f'Data de término: {cliente1.contrato.dataTermino[:2]}/{cliente1.contrato.dataTermino[2:4]}/{cliente1.contrato.dataTermino[4:]}')
                print(f'Valor total: R${cliente1.contrato.valor:.2f}')
                print('Status:', cliente1.contrato.status)
        
        case 3:
            print('Nome/Razão social:', cliente1.nome)
            if tipodocumento.upper() == 'CPF':
                print(f'CPF: {cliente1.documento[:3]}.{cliente1.documento[3:6]}.{cliente1.documento[6:9]}-{cliente1.documento[9:]}')
            elif tipodocumento.upper() == 'CNPJ':
                print(f'CNPJ: {cliente1.documento[:2]}.{cliente1.documento[2:5]}.{cliente1.documento[5:8]}/{cliente1.documento[8:12]}-{cliente1.documento[12:]}')
            print('CNH:', cliente1.cnh)
            print(f'Telefone: ({cliente1.telefone[:2]}){cliente1.telefone[2:6]}-{cliente1.telefone[6:]}')
        
        case 4:
            print(f'Data de início: {cliente1.contrato.dataInicio[:2]}/{cliente1.contrato.dataInicio[2:4]}/{cliente1.contrato.dataInicio[4:]}')
            print(f'Data de término: {cliente1.contrato.dataTermino[:2]}/{cliente1.contrato.dataTermino[2:4]}/{cliente1.contrato.dataTermino[4:]}')
            print(f'Valor total: R${cliente1.contrato.valor:.2f}')
            print('Status:', cliente1.contrato.status)
        
        case _:
            print('Opção inválida')