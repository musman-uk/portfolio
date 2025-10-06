# CLI Tool

The `example-tool` command‑line interface helps you manage tasks from the terminal. This guide covers installation and basic usage.

## Installation
Download the installer for your platform:

- **macOS/Linux**  
```bash
curl -sSL https://example.com/install.sh | bash
```

- **Windows (PowerShell)**  
```powershell
iwr -useb https://example.com/install.ps1 | iex
```

Verify installation:

```bash
example-tool --version
```

## Basic Commands
### List Tasks
```bash
example-tool list
```

Example output:
```
1. Buy milk
2. Finish report
```

### Add a Task
```bash
example-tool add "Book dentist appointment"
```

### Remove a Task
```bash
example-tool remove 2
```

## Options
- `--help` → Show usage information  
- `--version` → Display version  

## Notes
The tool reads configuration from `~/.example-tool/config.yml` if present. Most users can run commands without additional setup. If you encounter errors, reinstall or check your environment. For more commands, run:

```bash
example-tool --help
```

This will display a list of available subcommands and options.  
