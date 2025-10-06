# API Quickstart

The Example API allows you to retrieve user data securely and efficiently.  
This quickstart will help you authenticate, send your first request, and understand the response.

---

## 1. Prerequisites
- Sign up at the [Developer Portal](https://example.com/dev).
- Generate an API key from your dashboard.
- Install `curl` or use a REST client (e.g., Postman).
- Base URL: `https://api.example.com/v1`

---

## 2. Authentication
All requests require an `Authorization` header with your API key:

Authorization: Bearer <API_KEY>

---

## 3. Make Your First Request
```bash

curl -H "Authorization: Bearer <API_KEY>" \
     "https://api.example.com/v1/users?limit=2"

Example Response

json
[
  {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "active": true,
    "created_at": "2025-09-01T12:34:56Z"
  },
  {
    "id": 2,
    "name": "Bob",
    "email": "bob@example.com",
    "active": false,
    "created_at": "2025-09-02T09:21:00Z"
  }
]

```
## 4. Understanding the Response

id → Unique identifier for the user.

name → Full name of the user.

email → Contact email address.

active → Boolean flag showing if the user’s account is active.

created_at → ISO‑8601 timestamp of when the user was created.

## 5. Error Handling

If your request fails, the API returns a JSON error object:

json
{
  "error": "Unauthorized",
  "message": "Missing or invalid API key",
  "status": 401
}
401 Unauthorized → Check your API key.

429 Too Many Requests → You’ve hit the rate limit.

500 Internal Server Error → Temporary issue on our side.

## 6. Next Steps

Explore the API Reference.

Try filtering users with query parameters (?limit=10, ?active=true).

Review Best Practices for production use.

Join the Developer Community Forum for support and tips.

