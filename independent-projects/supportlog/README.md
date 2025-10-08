## 📋 SupportLog

SupportLog is a mock technical support dashboard. It demonstrates how structured issue tracking communicates clearly, builds trust, and reduces friction. Each log captures the report, environment, diagnosis, and resolution in a format that mirrors real support workflows.

---

### Log 1: Data Export Corruption
- **Reported By:** Finance Team  
- **Environment:** Web App v3.4, Windows 11, Chrome 118  
- **Status:** Resolved  
- **Summary:** CSV exports from the reporting dashboard produced malformed files, with missing headers and shifted columns.  
- **Diagnosis:** Root cause traced to a recent update in the CSV serialization library that mishandled UTF‑8 characters.  
- **Resolution:** Rolled back to stable library version, added regression tests for export formatting.  
[Full Log](logs/log-1-data-export/ISSUE.md)

---

### Log 2: Notification Delivery Delays
- **Reported By:** Customer Support  
- **Environment:** Mobile App v2.1, iOS 17  
- **Status:** Resolved  
- **Summary:** Push notifications for critical account alerts were delayed by up to 15 minutes, impacting time‑sensitive user actions.  
- **Diagnosis:** Queue backlog caused by misconfigured retry policy in the message broker.  
- **Resolution:** Adjusted retry thresholds, scaled broker cluster, and added monitoring alerts for queue latency.  
[Full Log](logs/log-2-notification-delays/ISSUE.md)
