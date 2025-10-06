# API Quickstart

The Example API allows you to retrieve user data securely and efficiently.  
This quickstart guides you through authentication, your first request, and interpreting responses.

## 1. Prerequisites
- Sign up at the [Developer Portal](https://example.com/dev).
- Generate an API key from your dashboard.
- Install `curl` or use a REST client (e.g., Postman).

## 2. Make Your First Request
```bash
curl -H "Authorization: Bearer <API_KEY>" \
     "https://api.example.com/v1/users?limit=2"

Example Response
json
[
  { "id": 1, "name": "Alice", "email": "alice@example.com", "active": true },
  { "id": 2, "name": "Bob", "email": "bob@example.com", "active": false }
]

```
## 3. Understanding the Response
id → Unique identifier for the user.

name → Full name of the user.

email → Contact email address.

active → Boolean flag showing if the user’s account is active.

## 4. Error Handling
If your request fails, the API returns a JSON error object:

json
{
  "error": "Unauthorized",
  "message": "Missing or invalid API key"
}
401 Unauthorized → Check your API key.

429 Too Many Requests → You’ve hit the rate limit.

## 5. Next Steps
Explore the API Reference.

Try filtering users with query parameters (?limit=10, ?active=true).

Review Best Practices for production use.
