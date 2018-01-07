# Get Item

## Request

```text
GET /api/v1/item/<item_id>
```

## Response

```text
200 OK
```

```json
{
    "id": 0,
    "name": "UTF-8 string",
    "description": "UTF-8 string",
    "created_at": 0,    // UNIX time
    "modified_at": 0    // UNIX time
}
```

### Errors

#### Not Found

```text
404 Not Found
```
