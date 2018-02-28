# Get Category

## Request

```text
GET /api/v1/category/<category_id>
```

## Response

```text
200 OK
```

```json
{
    "id": 0,
    "name": "UTF-8 string",
    "created_at": 0,    // UNIX time
    "modified_at": 0    // UNIX time
}
```

### Errors

#### Not Found

```text
404 Not Found
```
