# API Quickstart

## 1. Introduction
This Quickstart is designed to help you install the Example API SDK, authenticate securely, and make your first request. By the end, you will have a working environment, a successful API call, and the confidence to explore more advanced features. The guide assumes no prior experience with the SDK and is structured to anticipate common questions and pitfalls.

---

## 2. Prerequisites
Before you begin, ensure the following are in place:

- **Runtime**: Node.js 18+ or Python 3.10+  
- **Account**: A registered account on the Example Developer Portal  
- **API Key**: Generated from your account dashboard  
- **Network Access**: Outbound HTTPS enabled  
- **Editor/Terminal**: Any environment where you can run code and commands  

If you are missing any of these, visit the [Getting Started](#) page on the portal.

---

## 3. Installation
The SDK is available for both Node.js and Python. Choose the environment that suits your workflow.

### 3.1 Node.js
```bash
npm install example-sdk
```

### 3.2 Python
```bash
pip install example-sdk
```

### 3.3 Verification
Confirm installation by importing the package:

```bash
node -e "require('example-sdk')"
# or
python -c "import example_sdk"
```

If no errors appear, the SDK is installed correctly.

---

## 4. Authentication
All requests require an API key. The recommended approach is to store it as an environment variable.

### 4.1 macOS / Linux
```bash
export EXAMPLE_API_KEY="your_api_key_here"
```

### 4.2 Windows (PowerShell)
```powershell
setx EXAMPLE_API_KEY "your_api_key_here"
```

### 4.3 Best Practice
Avoid hard‑coding API keys in your source code. Use environment variables or a secrets manager to reduce the risk of accidental exposure.

---

## 5. First Request
The following example retrieves a list of tasks from the API.

### 5.1 Node.js
```javascript
const { Client } = require("example-sdk");

const client = new Client({ apiKey: process.env.EXAMPLE_API_KEY });

async function main() {
  try {
    const tasks = await client.tasks.list();
    console.log(tasks);
  } catch (err) {
    console.error("Request failed:", err.message);
  }
}

main();
```

### 5.2 Python
```python
from example_sdk import Client
import os

client = Client(api_key=os.getenv("EXAMPLE_API_KEY"))

try:
    tasks = client.tasks.list()
    print(tasks)
except Exception as e:
    print("Request failed:", e)
```

---

## 6. Example Response
```json
{
  "tasks": [
    {"id": 1, "title": "Buy milk", "status": "open"},
    {"id": 2, "title": "Finish report", "status": "in_progress"}
  ]
}
```

### 6.1 Response Fields
- **id** → Unique identifier for the task  
- **title** → Human‑readable description of the task  
- **status** → Current state (`open`, `in_progress`, `done`)  

---

## 7. Error Handling
The API uses standard HTTP status codes. Common cases include:

- **401 Unauthorized** → API key missing or invalid  
- **404 Not Found** → Endpoint path incorrect  
- **429 Too Many Requests** → Rate limit exceeded; retry after delay  

### 7.1 Example Error Response
```json
{
  "error": {
    "code": 401,
    "message": "Invalid API key"
  }
}
```

### 7.2 Handling Errors
- Always log the error code and message.  
- For 401 errors, confirm your API key is set correctly.  
- For 429 errors, implement exponential backoff before retrying.  

---

## 8. Troubleshooting
- **Command not found** → Ensure Node.js or Python is installed and on your PATH.  
- **Module not found** → Verify the SDK was installed with `npm install` or `pip install`.  
- **Invalid API key** → Regenerate the key from the developer portal and update your environment variable.  
- **SSL errors** → Confirm your system clock is correct and HTTPS traffic is allowed.  

---

## 9. Next Steps
Now that you have made your first request, you can:

- Explore filtering tasks with query parameters (`?status=open`).  
- Create new tasks using the `tasks.create()` method.  
- Review the [Tasks API Reference](#) for advanced usage.  
- Learn about pagination, error codes, and webhooks in the [Advanced Guides](#).  

---

## 10. Best Practices
- **Security**: Rotate API keys regularly and avoid committing them to version control.  
- **Error Handling**: Always check for error codes and provide user‑friendly messages.  
- **Performance**: Use pagination for large datasets to avoid timeouts.  
- **Testing**: Validate your integration in a sandbox environment before moving to production.  

---

## 11. Summary
This Quickstart demonstrated how to:

1. Install the Example SDK  
2. Authenticate with an API key  
3. Make your first request  
4. Interpret the response  
5. Handle common errors  
6. Apply best practices for security and performance  

By following these steps, you now have a working environment and a clear path to deeper exploration. Professional documentation anticipates your questions, provides runnable examples, and reassures you with troubleshooting and next steps. This guide is designed to do exactly that.
