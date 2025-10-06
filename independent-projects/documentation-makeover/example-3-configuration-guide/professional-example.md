# Configuration Guide

The tool can be customized using a YAML configuration file.  
By default, the config file is located at:

- **Linux/macOS**: `~/.config/example-tool/config.yml`  
- **Windows**: `%APPDATA%\example-tool\config.yml`

---

## 1. Example Configuration

```yaml

# Enable verbose logging for troubleshooting
`debug: false`

# Port the server will listen on
`port: 8080`

# Default task list to load on startup
`default_list: personal`

# Enable or disable desktop notifications
notifications: true

# Set log file path (optional)
log_file: /var/log/example-tool.log

```


## 2. Supported Options
| Key            | Type      | Default   | Description                                    |
|----------------|-----------|-----------|------------------------------------------------|
| `debug`        | boolean   | `false`   | Enables verbose logging for troubleshooting.   |
| `port`         | integer   | `3000`    | Port number the server listens on.             |
| `default_list` | string    | `inbox`   | Name of the list to load on startup.           |
| `notifications`| boolean   | `false`   | Show desktop notifications.                    |
| `log_file`     | string    | *(none)*  | Path to a log file for persistent logging.     |

---

## 3. Validation
Validate your configuration before starting the tool:

``` bash
example-tool validate-config
```

If the config is invalid, the validator will return an error message with the line number.

---

## 4. Troubleshooting
- **Config not found** → Ensure the file is in the correct path for your OS.  
- **Invalid YAML** → Use a YAML linter or run `example-tool validate-config`.  
- **Port already in use** → Choose a different port in the config.  
- **Permission denied writing logs** → Update `log_file` path or adjust permissions.  

---

## 5. Best Practices
- Keep sensitive values (like API keys) in environment variables, not in the config file.  
- Use comments in your YAML to document team‑specific conventions.  
- Version‑control your config file if it’s shared across environments.  

---

## 6. Next Steps
- Explore advanced options in the [Full Configuration Reference](https://example.com/docs/config).  
- Learn about [Environment Variable Overrides](https://example.com/docs/env-vars).  
- Join the [Community Forum](https://community.example.com) for tips and support.

