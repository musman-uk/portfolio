## 📋 Support Logs

Support Logs is a mock technical support dashboard. It demonstrates how structured issue tracking communicates clearly, builds trust, and reduces friction. Each log captures the **report, environment, status, diagnosis, and resolution** in a format that mirrors real support workflows.

---

## 📓 Logbook

### Log 1: Data Export Corruption (ID: SL‑001, Opened: 2025‑09‑14)
💼 **Reported By:** Finance Team  
🖥️ **Environment:** Web App v3.4 · Windows 11 · Chrome 118  
✔️ **Status:** Resolved  

- **Summary:** CSV exports from the reporting dashboard produced malformed files, with missing headers and shifted columns.  
- **Impact:** Month‑end reporting was disrupted, creating stress and manual rework for Finance.  
- **Diagnosis:** Root cause traced to a recent update in the CSV serialization library that mishandled UTF‑8 characters.  
- **Resolution:** Rolled back to stable library version and added regression tests for export formatting.  

 → [View Full Log](logs/log-1-data-export/ISSUE.md)

---

### Log 2: Notification Delivery Delays (ID: SL‑002, Opened: 2025‑09‑22)
🎧 **Reported By:** Customer Support  
📱 **Environment:** Mobile App v2.1 · iOS 17  
✔️ **Status:** Resolved  

- **Summary:** Push notifications for critical account alerts were delayed by up to 15 minutes.  
- **Impact:** Customers missed time‑sensitive updates, leading to frustration and increased support tickets.  
- **Diagnosis:** Queue backlog caused by a misconfigured retry policy in the message broker.  
- **Resolution:** Adjusted retry thresholds, scaled broker cluster, and added monitoring alerts for queue latency.  

→ [View Full Log](logs/log-2-notification-delays/ISSUE.md)

---

### Log 3: Authentication Timeout (ID: SL‑003, Planned)
🔍 **Reported By:** Internal QA  
🌐 **Environment:** API Gateway · Staging Cluster  
✔️ **Status:** Planned  

- **Summary:** Users intermittently experience timeouts during login under high load.  
- **Impact:** Authentication failures block access to core services, creating frustration and potential security concerns.  
- **Planned Action:** Stress‑test gateway under simulated peak load, optimise session handling, and add retry logic.  

---

### Log 4: Rate‑Limit Misconfiguration (ID: SL‑004, Planned)
🗃️ **Reported By:** Developer Tools Team  
🔌 **Environment:** 3rd‑Party API Integration  
✔️ **Status:** Planned  

- **Summary:** API requests are being throttled prematurely due to incorrect rate‑limit headers.  
- **Impact:** Downstream services fail to fetch required data, causing degraded user experience.  
- **Planned Action:** Align rate‑limit configs with provider documentation, add monitoring for quota thresholds, and implement graceful fallback.  

---

## 🗺️ Roadmap

- Add Log 5: Analytics Accuracy Issues (mismatched metrics across dashboards)  
- Add Log 6: Multi‑Region Deployment Latency (failover testing)  
- Introduce severity levels (🟢🟡🔴) and timeline view for issue lifecycle
