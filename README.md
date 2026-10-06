# Resposta questões
1. Veiculo, Contrato de locação, Cliente, Condutor e Manutenção

2.
- Veículo
Atributos: Placa, Modelo e Ano.
Métodos: Manutenções e imprimir histórico de manutenções 
- Cliente
Atributos: Nome, documento e telefone de contato
Métodos: Cadastrar e alugar
- Contrato de locação
Atributos: Data de inicio, data de término prevista e valor total
- Condutor
Atributos: Nome, documento, telefone de contato e CNH
- Manutenção
Atributos: Data, tipo de serviço e custo

3.
Superclasse/Generalização: Cliente
Subclasses/Especializações: Pessoa Física e Pessoa Jurídica

4.
- Veículo e Contrato
Agregação
O veículo possui um contrato, onde o veículo é o todo, e o contrato é a parte, e mesmo se um for excluído o outro vai continuar a existir

- Veículo e Condutor
Associação
Um condutor pode ter vários veículos, e um veículo pode existir sem um condutor

- Veículo e Manutenção
Associação
O veículo é associado a manutenção que é feita nele

- Cliente e Contrato
Agregação
O cliente através do método alugar faz o contrato e possui ele, porém os dois não tem uma dependência forte

- Cliente e Condutor
Herança
A classe condutor possui os atributos da classe cliente, sendo como uma classe filha da classe cliente

- Contrato e Condutor
Composição
Como na relação se o contrato for apagado o condutor também é apagado, existe uma dependência do condutor com o contrato
