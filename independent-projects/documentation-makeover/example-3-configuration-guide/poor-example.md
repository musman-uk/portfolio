# Configuration Guide

Create a file called `config.yml` in your home directory:

```yaml
enabled: true
path: /data
```

The tool will read this file automatically when it starts. You can change the values to suit your environment. Most users will only need to adjust the path. The configuration format is YAML, and the tool expects valid syntax. If the file is missing, defaults will be used. No detailed explanation of the options is provided here. The example above should be enough to get started. For additional settings, you may need to experiment or look at the source code.
