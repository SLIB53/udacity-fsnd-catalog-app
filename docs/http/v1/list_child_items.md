# List Child Items

## Request

```text
GET /api/v1/category/<category_id>/items
```

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
