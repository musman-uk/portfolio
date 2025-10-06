# CLI Tool

## 1. Introduction
The `example-tool` command‑line interface (CLI) provides a fast and consistent way to manage tasks directly from your terminal. This guide walks you through installation, verification, and common commands, and then expands into workflows, troubleshooting, and best practices. By the end, you will be able to confidently use `example-tool` for everyday task management and integrate it into your scripts or automation pipelines.

---

## 2. Prerequisites
Before installing,  please ensure the following are in place:

- **Operating System**: macOS, Linux, or Windows 10+  
- **Terminal Access**: Bash, Zsh, or PowerShell  
- **Permissions**: Ability to install binaries and modify PATH  
- **Network Access**: Outbound HTTPS enabled  

---

## 3. Installation

### 3.1 macOS/Linux
Install using the official script:
```bash
curl -sSL https://example.com/install.sh | bash
```

### 3.2 Windows (PowerShell)
```powershell
iwr -useb https://example.com/install.ps1 | iex
```

### 3.3 Verification
Confirm installation:
```bash
example-tool --version
```
Expected output:
```
example-tool version 1.2.0
```

If the version number appears, installation was successful.

---

## 4. Basic Usage

### 4.1 Listing Tasks
```bash
example-tool list
```
Output:
```
1. Buy milk
2. Finish report
```

### 4.2 Adding a Task
```bash
example-tool add "Book dentist appointment"
```

### 4.3 Removing a Task
```bash
example-tool remove 2
```

---

## 5. Global Options
- `--help` → Show usage information  
- `--version` → Display version number  
- `--config <path>` → Use a custom configuration file  
- `--verbose` → Print detailed logs  

Global options can be combined with any command:
```bash
example-tool list --verbose
```

---

## 6. Workflows

### 6.1 Daily Tasks
List only today’s tasks:
```bash
example-tool list --today
```

### 6.2 Batch Add
Add multiple tasks from a file:
```bash
cat tasks.txt | xargs -n1 example-tool add
```

### 6.3 Automation
Schedule recurring commands with cron (Linux/macOS):
```bash
0 9 * * * example-tool list --today >> ~/daily_tasks.log
```

On Windows, use Task Scheduler with:
```powershell
example-tool list --today >> C:\logs\daily_tasks.txt
```

---

## 7. Configuration
By default, `example-tool` reads configuration from:

- macOS/Linux: `~/.example-tool/config.yml`  
- Windows: `%USERPROFILE%\.example-tool\config.yml`  

### 7.1 Example Configuration
```yaml
default_list: work
notifications: true
sync:
  enabled: true
  interval: 15
```

### 7.2 Explanation
- **default_list** → sets the default task list  
- **notifications** → enables desktop notifications  
- **sync.enabled** → toggles background sync  
- **sync.interval** → sets sync frequency in minutes  

Restart the tool after editing the configuration file.

---

## 8. Troubleshooting

### 8.1 Common Issues
- **Command not found** → Ensure the binary is in your PATH.  
- **Permission denied** → Run with `sudo` or adjust file permissions.  
- **Windows errors** → Use PowerShell 5.1+ or Windows Terminal.  
- **Config not applied** → Verify YAML syntax and restart the tool.  

### 8.2 Diagnostic Command
Run:
```bash
example-tool doctor
```
This checks installation, configuration, and environment variables.

---

## 9. Best Practices
- **Use Config Files**: Store defaults in `config.yml` to avoid repeating flags.  
- **Separate Contexts**: Use `--config` to maintain different files for work and personal tasks.  
- **Script Automation**: Combine with shell scripts for recurring workflows.  
- **Error Handling**: Always check exit codes (`$?` in Bash, `$LASTEXITCODE` in PowerShell).  
- **Cross‑Platform Consistency**: Test scripts on both Linux and Windows if sharing with a team.  

---

## 10. Advanced Features

### 10.1 Filtering
```bash
example-tool list --status open
```

### 10.2 Exporting
```bash
example-tool export --format json > tasks.json
```

### 10.3 Importing
```bash
example-tool import tasks.json
```

---

## 11. Security Notes
- Avoid storing sensitive data in plain text configuration files.  
- Use environment variables for secrets.  
- Rotate credentials regularly if the tool integrates with external services.  

---

## 12. Summary
This guide covered:

1. Installing `example-tool` across platforms  
2. Running basic commands (list, add, remove)  
3. Using global options and workflows  
4. Configuring defaults with YAML  
5. Troubleshooting common issues  
6. Applying best practices and advanced features  

By following these steps, you now have a reliable, cross‑platform CLI for managing tasks. Professional documentation anticipates your needs, provides runnable examples, and reassures you with troubleshooting and best practices. `example-tool` is designed to integrate seamlessly into your daily workflow, whether you are managing personal tasks or automating team processes.
