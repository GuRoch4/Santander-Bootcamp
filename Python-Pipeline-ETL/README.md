# Explorando IA Generativa em um Pipeline de ETL com Python

## DESCRIÇÂO
Prepare-se para uma jornada prática pelo mundo da Ciência de Dados neste vídeo! Vamos construir um pipeline ETL (Extração, Transformação e Carregamento), demonstrando a relação entre dados, Inteligência Artificial (IA) e APIs. Extração: A aventura começa com uma planilha simples, de onde extrairemos os IDs dos usuários. Depois, usaremos esses IDs para acessar a API da 'Santander Dev Week 2023' e obter dados mais detalhados, um processo que evidencia a versatilidade na coleta de informações em Ciência de Dados. Transformação: Adentraremos o universo da IA com o GPT-4 da OpenAI, transformando esses dados em mensagens personalizadas de marketing. Veremos como a IA pode ser empregada de maneira inovadora e prática! Carregamento: Finalizaremos o processo enviando essas mensagens de volta para a API da 'Santander Dev Week 2023'. Este passo ilustra como dados transformados são reintegrados em sistemas, completando o ciclo de um pipeline ETL.

#### Python REST OpenAI API ChatGPT ETL

## Objetivos do Projeto
Contexto: Você é um cientista de dados no Santander e recebeu a tarefa de envolver seus clientes de maneira mais personalizada. Seu objetivo é usar o poder da IA Generativa para criar mensagens de marketing personalizadas que serão entregues a cada cliente. Condições do Problema:

1- Você recebeu uma planilha simples, em formato CSV ('SDW2023.csv'), com uma lista de IDs de usuário do banco:

2- Seu trabalho é consumir o endpoint GET https://sdw-2023-prd.up.railway.app/users/%7Bid%7D (API da Santander Dev Week 2023) para obter os dados de cada cliente.

3- Depois de obter os dados dos clientes, você vai usar a API do ChatGPT (OpenAI) para gerar uma mensagem de marketing personalizada para cada cliente. Essa mensagem deve enfatizar a importância dos investimentos.

4- Uma vez que a mensagem para cada cliente esteja pronta, você vai enviar essas informações de volta para a API, atualizando a lista de "news" de cada usuário usando o endpoint PUT https://sdw-2023-prd.up.railway.app/users/%7Bid%7D.

# Resumo do Projeto - Envio do Problema

Este projeto representa a realização bem-sucedida de uma jornada prática pela Ciência de Dados, onde construímos um Pipeline de ETL (Extração, Transformação e Carregamento) usando Python, IA e APIs.

Durante esta jornada, extraímos com sucesso os IDs dos usuários de uma planilha e os utilizamos para acessar a API da 'Santander Dev Week 2023', demonstrando a versatilidade na coleta de informações em Ciência de Dados. Além disso, adentramos no mundo da IA com o GPT-4 da OpenAI, transformando os dados em mensagens personalizadas de marketing, revelando maneiras inovadoras de aplicar a IA de forma prática.

Por fim, finalizamos o processo enviando essas mensagens de volta para a API da 'Santander Dev Week 2023', ilustrando como dados transformados são reintegrados em sistemas, completando o ciclo de um pipeline ETL de forma eficaz.

Este projeto é um testemunho do poder do Python, da IA e da integração de APIs em Ciência de Dados, proporcionando resultados impactantes.