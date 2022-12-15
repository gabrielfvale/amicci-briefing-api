# Category

Recursos relacionados ao objeto Category.

## GET categories/

Rota responsável por listar todos as categorias.
Método: `GET`
Parâmetros: `N/A`

### Resposta de sucesso

`200 OK`

```json
[
    {
        "id": 1,
        "name": "Category Name",
        "description": "Category Description"
    },
    ...
]
```

### Respostas de erro

`400 Bad Request` Requisição inválida
`404 Not Found` Não há categoria disponível
`500 Internal Error` Erro inesperado

## POST category/

Rota responsável por criar uma categoria.
Método: `PUT`
Parâmetros: `json body`

```json
{
    "name": "New Category",
    "description": "Description"
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

`400 Bad Request` Objeto Categoria inválido.
`404 Not Found` Caminho inexistente.
`500 Internal Error` Erro inesperado

## GET category/{id}/

Rota responsável por retornar detalhes de uma categoria por ID.
Método: `GET`
Parâmetros: `id (path)`

### Resposta de sucesso

`200 OK`

```json
{
    "id": 1,
    "name": "Category Name",
    "description": "Category Description"
}
```

### Respostas de erro

`400 Bad Request` Requisição inválida
`404 Not Found` Categoria não existe

## PUT category/{id}/

Rota responsável por atualizar uma categoria por ID.
Método: `PUT`
Parâmetros: `id (path)`, `json body`

```json
{
    "name": "New Category Name",
    "description": "Category Description"
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

`400 Bad Request` Categoria inválida.
`404 Not Found` Objeto Categoria inexistente.
`500 Internal Error` Erro inesperado
