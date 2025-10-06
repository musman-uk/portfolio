# Configuration Guide
This tool uses a YAML configuration file located at `~/.config/tool/config.yml`.

## Example Config
`yaml debug: true port: 8080 # Configuration Guide

The Example Web App can be customised through a configuration file. This guide explains how to create a basic configuration so the application runs with your preferred defaults.

## Location
The configuration file is read automatically from the following paths:

- macOS/Linux: `/etc/example-app/config.yml`  
- Windows: `C:\ProgramData\ExampleApp\config.yml`  

If the file is not present, the application will use built‑in defaults.

## Example Configuration
```yaml
server:
  port: 8080
  host: localhost
logging:
  level: info
features:
  signup: true
```

## Explanation
- **server.port** → sets the port the application listens on  
- **server.host** → defines the host interface  
- **logging.level** → controls log verbosity (`debug`, `info`, `warn`, `error`)  
- **features.signup** → enables or disables the user signup feature  

## Usage
Once the configuration file is created, restart the application to apply the settings. For example:

```bash
systemctl restart example-app
```

The application will now run on the specified port and host, with logging and features adjusted according to the file.

## Notes
- The configuration must be valid YAML. Invalid syntax may prevent the application from starting.  
- Only a limited set of options are supported. The example above covers the most common ones.  
- If you need to change settings, edit the file and restart the application.  

## Example
```yaml
server:
  port: 9090
  host: 0.0.0.0
logging:
  level: debug
features:
  signup: false
```

This runs the app on port 9090, makes it accessible externally, increases log detail, and disables signup.  


## Notes
Only `debug` and `port` are supported right now.

Defaults: `debug = false`, `port = 3000`.

Config file must be valid YAML.
