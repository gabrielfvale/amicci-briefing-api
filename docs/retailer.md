# Retailer

Recursos relacionados ao objeto Retailer.

## GET retailers/

Rota responsável por listar todos os retailers.
Método: `GET`
Parâmetros: `N/A`

### Resposta de sucesso

`200 OK`

```json
[
    {
        "id": 1,
        "name": "Retailer Name",
        "vendors": ["Vendor 1", "Vendor 2"],
    },
    ...
]
```

### Respostas de erro

`400 Bad Request` Requisição inválida
`404 Not Found` Não há varejista disponível
`500 Internal Error` Erro inesperado

## POST retailer/

Rota responsável por criar um retailer.
Método: `PUT`
Parâmetros: `json body`

```json
{
    "name": "New Retailer",
    "vendors": [1, 2]
}
```

### Resposta de sucesso

`200 OK`

```json
{
    "id": {id}
}
```

### Respostas de erro

`400 Bad Request` Objeto Varejista inválido.
`404 Not Found` Caminho inexistente.
`500 Internal Error` Erro inesperado

## GET retailer/{id}/

Rota responsável por retornar detalhes de um retailer por ID.
Método: `GET`
Parâmetros: `id (path)`

### Resposta de sucesso

`200 OK`

```json
{
    "id": 1,
    "name": "Retailer Name",
    "vendors": ["Vendor 1"]
}
```

### Respostas de erro

`400 Bad Request` Requisição inválida
`404 Not Found` Varejista não existe

## PUT retailer/{id}/

Rota responsável por atualizar um retailer por ID.
Método: `PUT`
Parâmetros: `id (path)`, `json body`

```json
{
    "name": "New Retailer Name",
    "vendors": [1, 2, 3]
}
```

### Resposta de sucesso

`200 OK`

```json
{
    "id": {id}
}
```

### Respostas de erro

`400 Bad Request` Varejista inválido.
`404 Not Found` Objeto Varejista inexistente.
`500 Internal Error` Erro inesperado
