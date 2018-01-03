# Create Category

## Request

```text
POST /api/v1/category
```

```json
{
    "name": "UTF-8 string"  // required
}
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

#### Missing Required Parameter(s)

```text
400 Bad Request
```

```json
{
    "reason": "Body missing required parameter(s)."
}
```
