# Create Child Item

## Request

```text
POST /api/v1/category/<category_id>/item
```

```json
{
    "name": "UTF-8 string",         // required
    "description": "UTF-8 string"   // optional
}
```

## Response

```text
201 Created
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

#### Missing Required Parameter(s)

```text
400 Bad Request
```

```json
{
    "reason": "Body missing required parameter(s)."
}
```
