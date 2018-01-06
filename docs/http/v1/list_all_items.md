# List All Items

## Request

```text
GET /api/v1/items
```

### Query Parameters

Parameter   |   Valid Arguments     |   Default Value
------------|-----------------------|-----------------------
`order_by`  |   `id`, `age`         |   `id`
`order`     |   `asc`, `desc`       |   `asc`
`limit`     |   _integer_           |   10

## Response

```text
200 OK
```

```json
[
    {
        "id": 0,
        "name": "UTF-8 string",
        "description": "UTF-8 string",
        "created_at": 0,    // UNIX time
        "modified_at": 0    // UNIX time
    },
    {
        "id": 1,
        "name": "UTF-8 string",
        "description": "UTF-8 string",
        "created_at": 1,    // UNIX time
        "modified_at": 1    // UNIX time
    },
]
```
