# Briefing

Recursos relacionados ao objeto Briefing.

## GET briefings/

Rota responsável por listar todos os briefings.
Método: `GET`
Parâmetros: `N/A`

### Resposta de sucesso

`200 OK`

```json
[
    {
        "name": "Briefing Name",
        "responsible": "Responsável",
        "retailer": "Retailer #1",
        "category": "Novo Produto",
        "available": 1
    },
    ...
]
```

### Respostas de erro

`400 Bad Request` Requisição inválida
`404 Not Found` Não há briefing disponível
`500 Internal Error` Erro inesperado

## POST briefing/

Rota responsável por criar um briefing.
Método: `PUT`
Parâmetros: `json body`

```json
{
    "name": "New Briefing",
    "responsible": "Responsável",
    "retailer": 1,
    "category": 1,
    "available": 1
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

`400 Bad Request` Objeto Briefing inválido.
`404 Not Found` Caminho inexistente.
`500 Internal Error` Erro inesperado

## GET briefing/{id}/

Rota responsável por retornar detalhes de um briefing por ID.
Método: `GET`
Parâmetros: `id (path)`

### Resposta de sucesso

`200 OK`

```json
{
    "name": "Briefing Name",
    "responsible": "Responsável",
    "retailer": "Retailer #1",
    "category": "Novo Produto",
    "available": 1
}
```

### Respostas de erro

`400 Bad Request` Requisição inválida
`404 Not Found` Briefing não existe

## PUT briefing/{id}/

Rota responsável por atualizar um briefing por ID.
Método: `PUT`
Parâmetros: `id (path)`, `json body`

```json
{
    "name": "Updated Briefing",
    "responsible": "Responsável",
    "retailer": 1,
    "category": 1,
    "available": 1
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

`400 Bad Request` Objeto Briefing inválido.
`404 Not Found` Briefing inexistente.
`500 Internal Error` Erro inesperado
