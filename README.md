## Explicação do que foi feito

Esse código é referete ao teste do Magalu. A API recebe POST para cadastrar uma mensagem, GET para pegar as mensagens, ou uma mensagem, PUT para trocar os status da mensagem quando essa é enviada, e DELETE.

## Documentação da API:

Rota: http://localhost:5000/api/v1/message Método: GET


Rota: http://localhost:5000/api/v1/message/<id> Método: GET

Rota: http://localhost:5000/api/v1/message/<id> Método: DELETE

Rota: http://localhost:5000/api/v1/message Método: POST

```json
{
    "recipient": "",
    "message": "",
    "date_time": ""
}
```

O valor da chave recipient deve ser no formato de um email (ex: teste@teste.com) ou o número de telefone celular com o DDD e todos os números juntos (ex: 61999999999)

O valo da chave message pode ser uma string qualquer

O valor da chave date_time deve ser no formato A-M-D 00:00:00 (ex: 2020-09-23 19:00:00)

Rota: http://localhost:5000/api/v1/message/<id> Método: PUT

```json
{
    "recipient": "",
    "message": "",
    "date_time": "",
    "status": 
}
```

O valor da chave recipient deve ser no formato de um email (ex: teste@teste.com) ou o número de telefone celular com o DDD e todos os números juntos (ex: 61999999999)

O valor da chave message pode ser uma string qualquer

O valor da chave date_time deve ser no formato A-M-D 00:00:00 (ex: 2020-09-23 19:00:00)

O valor da chave status deve ter true ou false

## Como rodar o backend:

Para facilitar o processo de rodar o código foi criado o docker-compose.yml que tem o banco de dados (PostgreSQL) e o código do teste.

Para rodar basta ter o docker e o docker-compose instalado na máquina e dentro da pasta raiz deste projeto rodar no terminal o seguinte comando:

```
docker-compose up
```

## Como rodar teste unitário

Para rodar os testes unitários o ambiente deve ser instalado da seguinte forma:

Deve ter instalado na máquina python3, virtualenv, e PostgreSQL

As variáveis a baixo devem ser setadas

```
export ENV=production
export POSTGRES_USER=USUARIO_DO_BANCO
export POSTGRES_PW=SENHA
export POSTGRES_URL=HOST
export POSTGRES_DB=BANCO
```

Crie o ambiente virtual do projeto:

```
virtualenv venv
```

Entre no ambiente virtual:

```
source venv/bin/activate
```

Instale as dependencias de teste:

```
pip install -r requirements-dev.txt
```

Agora rode o comando para popular a base:

```
flask db upgrade
```

Por fim, para rodar os testes rode:

```
pytest
```

Observação: para os testes rodarem de forma correta o banco de dados deve está zerado
