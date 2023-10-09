# Processando e Transformando Dados com Power BI

### DESCRIÇÃO
Neste desafio será a sua vez de aplicar as etapas de coleta, obtenção e transformação de dados com Power BI e MySQL na Azure.

### INSTRUÇÕES
#### Descrição do desafio módulo 3 – Processamento de Dados Simplificado com Power BI
1. Configurar o setup de banco de dados na Azure.
2. Popular o servidor com script fornecido.
3. Integre o MySQL com Power Bi.
4. Realize as transformações indicadas.
#### Diretrizes para transformação dos dados
1. Verifique os cabeçalhos e tipos de dados.
2. Modifique os valores monetários para o tipo double preciso.
3. Verifique a existência dos nulos e analise a remoção.
4. Os employees com nulos em Super_ssn podem ser os gerentes. Verifique se há algum colaborador sem gerente.
5. Verifique se há algum departamento sem gerente.
6. Se houver departamento sem gerente, suponha que você possui os dados e preencha as lacunas.
7. Verifique o número de horas dos projetos.
8. Separar colunas complexas.
9. Mesclar consultas employee e departament para criar uma tabela employee com o nome dos departamentos associados aos colaboradores. A mescla terá como base a tabela employee. Fique atento, essa informação influencia no tipo de junção.
10. Neste processo elimine as colunas desnecessárias.
11. Realize a junção dos colaboradores e respectivos nomes dos gerentes. Isso pode ser feito com consulta SQL ou pela mescla de tabelas com Power BI. Caso utilize SQL, especifique no README a query utilizada no processo.
12. Mescle as colunas de Nome e Sobrenome para ter apenas uma coluna definindo os nomes dos colaboradores.
13. Mescle os nomes de departamentos e localização. Isso fará que cada combinação departamento-local seja único. Isso irá auxiliar na criação do modelo estrela em um módulo futuro.
14. Explique por que, neste caso supracitado, podemos apenas utilizar o mesclar e não o atribuir.
15. Agrupe os dados a fim de saber quantos colaboradores existem por gerente.
16. Elimine as colunas desnecessárias, que não serão usadas no relatório, de cada tabela.


## RELATORIO - Envio do Problema
##### Descrição do desafio módulo 3 – Processamento de Dados Simplificado com Power BI
1. A instância SQL foi criada com sucesso e configurada corretamente.
2. O banco de dados foi criado e os dados foram inseridos utilizando o MySQL.
3. A conexão foi estabelecida com sucesso.
##### Diretrizes para transformação dos dados
1. Cabeçalhos e tipos de dados mudados
2. "Valores monetários encontrados em Salario.Funcionario foram modificados para o tipo double preciso.
3. Foi encontrado um valor nulo em IDgerente.Funcionario com o nome do colaborador James. Foi analisada a possibilidade de remoção.
4. Ao analisar esse dado, foi identificado que James é um gerente, portanto, não foi necessária a sua remoção.
5.
6. Foi verificado que não existem departamentos sem gerente.
7. Numero de horas verificado.
8. Colunas complexas localizadas em Endereco.Funcionario foram separadas, nomes corrigidos e formatados.
9. A junção dos dados de Employee e Department foi realizada com sucesso, utilizando IdGerente como base.
10. Foram analisadas as colunas que poderiam ser excluídas e estas foram removidas, resultando na relação de funcionários associados aos departamentos.
11. Foi utilizada uma query SQL para realizar a junção dos colaboradores com os respectivos nomes dos gerentes.
    ##### SELECT e.Fname as Employee_FirstName, e.Lname as Employee_LastName, 
    ##### m.Fname as Manager_FirstName, m.Lname as Manager_LastName
    ##### FROM employee e
    ##### LEFT JOIN employee m ON e.Super_ssn = m.Ssn;
12. As colunas de Nome e Sobrenome foram mescladas em uma única coluna para definir os nomes dos colaboradores.
13. Departamento com a coluna Local foi mesclado.
14. No caso mencionado, apenas a operação de mesclar foi necessária em vez de atribuir, porque a mescla envolve a combinação de dados de duas fontes diferentes com base em uma condição específica, enquanto atribuir geralmente se refere a dar um valor a uma variável ou objeto em programação. Neste contexto de manipulação de dados, a mescla é a operação mais apropriada para combinar informações de diferentes fontes de dados.
15. Os dados foram agrupados para determinar quantos colaboradores existem por gerente.
16. Foram removidas as colunas desnecessárias, que não serão utilizadas no relatório, de cada tabela.

https://app.powerbi.com/groups/me/reports/04ec6c16-442f-463e-92b5-57361dd83381/ReportSection?experience=power-bi