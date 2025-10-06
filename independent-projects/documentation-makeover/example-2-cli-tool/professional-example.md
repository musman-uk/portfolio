# CLI Tool

The `mytool` CLI helps you manage tasks quickly and consistently across environments.  
This guide covers installation, common commands, global options, and troubleshooting.

---

## 1. Installation
### macOS / Linux

```bash

curl -sSL https://example.com/install.sh | bash
```
### Windows (PowerShell)
```powershell 
iwr -useb https://example.com/install.ps1 | iex
````
### Verify installation:

```bash
mytool --version

```
## 2. Basic Commands

List Tasks
```bash
mytool list
```

Example Output
```Code
1. Buy milk
2. Finish report
```

Add a Task
``` bash
mytool add "Book dentist appointment"
```
Remove a Task
```bash
mytool remove 2
```

## 3. Global Options
`--help` → Show usage information.

`--version` → Display current version.

`--config <path>` → Use a custom configuration file.

## 4. Configuration
You can set defaults in a config file (~/.mytool/config.yml):

```yaml
default_list: personal
notifications: true
```

## 5. Troubleshooting
`Command not found` → Ensure the binary is in your PATH.

`Permission denied` → Try running with `sudo` or adjust file permissions.

Windows issues → Use PowerShell 5.1+ or Windows Terminal.

## 6. Next Steps
Explore advanced commands in the Full CLI Reference.

Configure defaults with mytool config.

Join the Community Forum for tips and support.
