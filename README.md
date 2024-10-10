# Automação de Registro de Produtos

Este projeto faz parte da **Jornada Python** da **Hashtag Treinamentos**. O objetivo deste script é automatizar o processo de login e cadastro de produtos em uma plataforma web. Ele utiliza bibliotecas como **PyAutoGUI** para interação com a interface do usuário e **Pandas** para manipulação da base de dados de produtos.

## Funcionalidades

- **Abertura Automática do Google Chrome**: O script abre o navegador e acessa o link da plataforma de cadastro de produtos.
- **Login Automático**: Após acessar a plataforma, o script realiza o login automaticamente com um email e senha fornecidos no código.
- **Importação de Base de Dados**: Utiliza um arquivo CSV para obter os dados dos produtos, incluindo código, marca, tipo, categoria, preço unitário, custo e observações.
- **Cadastro Automático de Produtos**: A partir da base de dados, o script preenche automaticamente o formulário de cadastro de produtos e submete as informações para cada item na tabela.
- **Controle de Fluxo**: Pausas programadas (usando `time.sleep`) garantem que o site tenha tempo suficiente para carregar as páginas antes de realizar as ações.
- **Interações Flexíveis**: Caso algum campo não tenha valor (por exemplo, campo de observações), o script pula esse campo automaticamente.

## Tecnologias Utilizadas

- **Python 3.x**
- **PyAutoGUI**: Usada para simular ações de teclado e mouse.
- **Pandas**: Usada para ler o arquivo CSV e manipular dados.
- **Time**: Para pausar o script e garantir que o site tenha tempo de carregar.



## Exemplo de Base de Dados (produtos.csv)

Seu arquivo CSV deve conter as seguintes colunas:

| codigo | marca     | tipo   | categoria | preco_unitario | custo | obs            |
|--------|-----------|--------|-----------|----------------|-------|----------------|
| 12345  | Marca X   | Tipo A | Cat 1     | 49.99          | 35.00 | Nenhuma        |
| 67890  | Marca Y   | Tipo B | Cat 2     | 79.99          | 60.00 | Produto novo   |
| ...    | ...       | ...    | ...       | ...            | ...   | ...            |

