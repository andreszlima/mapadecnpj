# Mapa de CNPJs

## Objetivo

O objetivo deste projeto é criar um mapa de CNPJs, com o objetivo de facilitar a visualização de empresas e suas relações.

## Como funciona

O projeto é dividido em três partes:

1. Coleta e atualização de dados - Python e PostgreSQL
2. Servidor para obtenção dos dados tratados - Node.js e PostgreSQL
3. Front-end para visualização dos dados - React.js (esta parte terá seu próprio repositório)

### Coleta e atualização de dados

A coleta de dados é feita utilizando Python, com o download dos dados brutos fornecidos pela receita federal do Brasil. Posteriormente estes dados são tratados para que estejam consistentes e são posteriormente inseridos no banco de dados PostgreSQL. Como os dados são atualizados mensalmente pela receita federal, o processo de atualização é feito mensalmente. Para que isso seja feito com segurança, são utilizados dois bancos de dados. Um é o mapadecnpj_prod, que é o banco de dados utilizado pelo servidor para obtenção dos dados tratados. O outro é o mapadecnpj_dev, que é utilizado para a coleta e tratamento dos dados. Após a coleta e tratamento dos dados, eles são inseridos no banco de dados mapadecnpj_prod, que é o banco de dados utilizado pelo servidor.

### Servidor para obtenção dos dados tratados

O servidor é feito utilizando Node.js, com o framework Express.js. O servidor é responsável por obter os dados tratados do banco de dados PostgreSQL e fornecê-los para o front-end. O servidor também é responsável por fornecer os dados para a API.

### Front-end para visualização dos dados

O front-end é feito utilizando React.js. O front-end é responsável por obter os dados do servidor e exibi-los para o usuário. O front-end também é responsável por fornecer uma interface para a API.

## Como executar

