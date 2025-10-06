# API Quickstart

This API lets you get a list of users.

## Prerequisites
- You need an API key (find it in your account dashboard).
- Works with curl or Postman.

## Example Request
```bash
curl -H "Authorization: Bearer <API_KEY>" \
     https://api.example.com/v1/users

Example Response
json
[
  { "id": 1, "name": "Alice" },
  { "id": 2, "name": "Bob" }
]

```
Notes
Only tested with a few accounts so far.

Error codes not covered yet.

More details will be added later.
