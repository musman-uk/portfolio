# API Quickstart

Install the SDK with your package manager:

```bash
npm install example-sdk
```

Then import it and call the client:

```python
import example_sdk
client = example_sdk.Client()
print(client.list())
```

This should return your data. The SDK automatically connects to the service and provides access to the main methods. You can explore additional methods by checking the client object. Most users will start with `list()` to see available items. If you encounter errors, verify your installation and try again. The API key should be set, but details are not included here.
