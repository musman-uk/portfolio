# Configuration Guide

## 1. Introduction
The Example Web App can be customised through a configuration file that defines how the application runs in your environment. This guide explains how to create, validate, and maintain a configuration file. It covers default locations, supported options, troubleshooting, and best practices. By the end, you will have a reliable configuration that ensures the application behaves consistently across environments.

---

## 2. Prerequisites
Before configuring, ensure the following:

- **Installation**: Example Web App is installed and running.  
- **Permissions**: You have write access to the configuration directory.  
- **Editor**: A text editor capable of saving UTF‑8 encoded YAML files.  
- **Knowledge**: Basic familiarity with YAML syntax (indentation and key‑value pairs).  

---

## 3. Configuration File Location
The application automatically loads configuration from the following paths:

- **macOS/Linux**: `/etc/example-app/config.yml`  
- **Windows**: `C:\ProgramData\ExampleApp\config.yml`  

You can override the location with the `EXAMPLE_APP_CONFIG` environment variable:
```bash
export EXAMPLE_APP_CONFIG=/custom/path/config.yml
```

---

## 4. Basic Example
```yaml
server:
  port: 8080
  host: localhost
logging:
  level: info
features:
  signup: true
```

This configuration runs the app on port 8080, binds it to localhost, logs at `info` level, and enables the signup feature.

---

## 5. Configuration Options

### 5.1 Server
- **server.port** → Port number the app listens on (default: 8080).  
- **server.host** → Host interface (`localhost` or `0.0.0.0`).  

### 5.2 Logging
- **logging.level** → Verbosity (`debug`, `info`, `warn`, `error`).  

### 5.3 Features
- **features.signup** → Enables or disables user signup.  
- **features.notifications** → Toggles email or desktop notifications.  

### 5.4 Database
```yaml
database:
  url: postgres://user:pass@localhost:5432/example
  pool: 10
```
- **database.url** → Connection string for the database.  
- **database.pool** → Maximum number of connections in the pool.  

---

## 6. Validation
Validate your configuration before restarting the app:

```bash
example-app validate --config /etc/example-app/config.yml
```

If the file is valid, you will see:
```
Configuration valid.
```

If errors exist, the validator will highlight the line number and issue.

---

## 7. Applying Changes
After editing the configuration file, restart the application:

- **Linux/macOS**:
```bash
systemctl restart example-app
```

- **Windows**:
```powershell
Restart-Service ExampleApp
```

---

## 8. Troubleshooting

### 8.1 Common Issues
- **App fails to start** → Check YAML syntax (indentation is critical).  
- **Port already in use** → Choose a different `server.port`.  
- **Database connection errors** → Verify credentials and network access.  
- **Changes not applied** → Ensure you restarted the service after editing.  

### 8.2 Diagnostic Command
Run:
```bash
example-app doctor
```
This checks configuration, database connectivity, and environment variables.

---

## 9. Best Practices
- **Use Comments**: Annotate configuration files to explain non‑obvious values.  
- **Separate Environments**: Maintain different configs for development, staging, and production.  
- **Secure Secrets**: Avoid hard‑coding passwords; use environment variables or a secrets manager.  
- **Version Control**: Store configuration files in a private repository to track changes.  
- **Validation First**: Always run `example-app validate` before restarting in production.  

---

## 10. Advanced Configuration

### 10.1 Environment Overrides
Environment variables can override YAML values:
```bash
export EXAMPLE_APP_SERVER__PORT=9090
```
This sets `server.port` to 9090 without editing the file.

### 10.2 Include Files
Large configurations can be split into multiple files:
```yaml
include:
  - /etc/example-app/logging.yml
  - /etc/example-app/features.yml
```

### 10.3 Conditional Settings
Use profiles to switch between environments:
```yaml
profiles:
  development:
    logging.level: debug
  production:
    logging.level: warn
```

---

## 11. Security Considerations
- Restrict file permissions:  
  - Linux/macOS: `chmod 600 config.yml`  
  - Windows: limit access to Administrators  
- Never commit secrets to public repositories.  
- Rotate database credentials regularly.  

---

## 12. Example: Production Configuration
```yaml
server:
  port: 80
  host: 0.0.0.0
logging:
  level: warn
features:
  signup: false
  notifications: true
database:
  url: postgres://prod_user:secure_pass@db.example.com:5432/example
  pool: 20
```

This configuration runs the app on port 80, binds to all interfaces, logs only warnings and errors, disables signup, enables notifications, and connects to a production database with a larger pool.

---

## 13. Summary
This guide demonstrated how to:

1. Locate and create a configuration file.  
2. Define server, logging, feature, and database options.  
3. Validate and apply changes safely.  
4. Troubleshoot common issues.  
5. Apply best practices for security and maintainability.  
6. Extend configuration with overrides, includes, and profiles.  

By following these steps, you can ensure the Example Web App runs consistently and securely across environments. Professional documentation anticipates your questions, provides annotated examples, and reassures you with validation, troubleshooting, and best practices. This guide is designed to do exactly that.
