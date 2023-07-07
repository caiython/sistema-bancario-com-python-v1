# Sistema Bancário V1 - Caiython

<p style="font-size: 12px">Repositório dedicado à entrega do desafio "Criando um Sistema Bancário com Python" do Bootcamp de Data Science da DIO em parceria com a potência tech.</p>

## Proposta Inicial 

Criar um sistema bancário utilizando a linguagem python que seja capaz de realizar as operações de depósito, saque, verificar extrato e sair conforme a seguinte tabela:

|Operação|Funcionamento|Condições|
|--------|-------------|---------|
|Depósito|O usuário digita um valor numérico e o valor é adicionado ao saldo de sua conta.|O usuário não deve ser capaz de inserir um valor inferior a zero.
|Saque|O usuário digita um valor numérico e o valor é subtraído do saldo de sua conta.|O usuário possui um limite diário de 3 saques. O valor do saque deve ser inferior ou igual ao valor disponível em sua conta. O valor do saque não deve ser superior a 500.
|Extrato|O extrato exibe todas as operações realizadas na conta do usuário.|N/A|
|Sair|Finaliza o programa.|N/A|

## Solução Desenvolvida

- O script do sistema bancário foi desenvolvido sob todas as condições da proposta inicial.
- Além do que foi solicitado, foi adicionado um contador de operações para ajudar o usuário a identificar cada operação ao exibir o extrato.

## Problemas Conhecidos

Foi identificado uma possível interrupção no script onde, ao ser solicitado para digitar o valor do depósito ou do saque, o usuário é capaz de digitar algum valor que não seja numérico, causando um <b>ValueError</b> na função de conversão do valor digitado para float. Apesar disso, é um problema de fácil resolução, porém não será abordado nessa versão inicial do sistema.