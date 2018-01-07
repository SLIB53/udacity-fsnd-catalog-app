# Update Item

## Request

```text
PUT /api/v1/item/<item_id>
```

```json
{
    "name": "UTF-8 string",         // optional
    "description": "UTF-8 string"   // optional
}
```

## Response

```text
204 No Content
```

### Errors

#### Not Found

```text
404 Not Found
```
