# Configuration Guide

The Example App can be configured with a YAML file. Place the file in the default location:

- Linux/macOS: `/etc/example-app/config.yml`  
- Windows: `C:\ProgramData\ExampleApp\config.yml`  

Example:

```yaml
server:
  port: 8080
logging:
  level: info
```

The application will read this file automatically when it starts. You can change the values to suit your environment. Most users will only need to adjust the port or logging level. Restart the app after making changes. Other options may be available but are not listed here.
