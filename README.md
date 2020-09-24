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

