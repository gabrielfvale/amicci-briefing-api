# Vendor

Recursos relacionados ao objeto Vendor.

## GET vendors/

Rota responsável por listar todos os vendors.
Método: `GET`
Parâmetros: `N/A`

### Resposta de sucesso

`200 OK`

```json
[
    {
        "id": 1,
        "name": "Vendor Name",
    },
    ...
]
```

### Respostas de erro

`400 Bad Request` Requisição inválida
`404 Not Found` Não há fornecedor disponível
`500 Internal Error` Erro inesperado

## POST vendor/

Rota responsável por criar um vendor.
Método: `PUT`
Parâmetros: `json body`

```json
{
    "name": "New Vendor",
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

`400 Bad Request` Objeto Fornecedor inválido.
`404 Not Found` Caminho inexistente.
`500 Internal Error` Erro inesperado

## GET vendor/{id}/

Rota responsável por retornar detalhes de um vendor por ID.
Método: `GET`
Parâmetros: `id (path)`

### Resposta de sucesso

`200 OK`

```json
{
    "id": 1,
    "name": "Vendor Name",
}
```

### Respostas de erro

`400 Bad Request` Requisição inválida
`404 Not Found` Categoria não existe

## PUT vendor/{id}/

Rota responsável por atualizar um vendor por ID.
Método: `PUT`
Parâmetros: `id (path)`, `json body`

```json
{
    "name": "New Vendor Name",
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

`400 Bad Request` Objeto fornecedor inválido.
`404 Not Found` Fornecedor inexistente.
`500 Internal Error` Erro inesperado
