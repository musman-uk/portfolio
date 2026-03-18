# API Quickstart

This guide explains how to install the Example SDK and make a basic request. It assumes you already have an API key.

## Installation
Install the SDK using your package manager:

```bash
npm install example-sdk
```

or

```bash
pip install example-sdk
```

Verify installation by importing the package:

```bash
python -c "import example_sdk"
```

## Authentication
Set your API key as an environment variable:

```bash
export EXAMPLE_API_KEY="your_api_key_here"
```

On Windows:

```powershell
setx EXAMPLE_API_KEY "your_api_key_here"
```

## First Request
The following example retrieves tasks:

```python
from example_sdk import Client
import os

client = Client(api_key=os.getenv("EXAMPLE_API_KEY"))
tasks = client.tasks.list()
print(tasks)
```

## Example Response
```json
{
  "tasks": [
    {"id": 1, "title": "Buy milk"},
    {"id": 2, "title": "Finish report"}
  ]
}
```

This confirms the SDK is working. You can now explore other methods such as `tasks.create()` or `tasks.delete()`.

## Notes
- Ensure your API key is valid.  
- The SDK requires Python 3.10+ or Node.js 18+.  
- For more details, see the API reference.  
