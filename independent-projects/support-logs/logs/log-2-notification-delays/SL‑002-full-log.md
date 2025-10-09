## Log 2: Notification Delivery Delays

- **Ticket Reference:** [ticket‑002-CS](https://github.com/musman-uk/portfolio/blob/main/independent-projects/support-logs/tickets/ticket-002-CS/full-ticket.md) 
- **Reported By:** Customer Support  
- **Date Opened:** 2025-09-22  
- **Environment:** Mobile App v2.1 · iOS 17  
- **Priority:** Critical  
- **Status:** Resolved  

### Report
Customer Support escalated multiple user complaints that push notifications for critical account alerts (e.g., payment failures, password resets, and security warnings) were delayed by up to 15 minutes. These delays undermined the reliability of time‑sensitive communication and created frustration for users who were unable to complete urgent actions. The issue was classified as critical because it directly impacted account security and customer trust.

### Steps to Reproduce
1. Trigger a password reset from the mobile app.  
2. Wait for the push notification.  
3. Measure delivery time.  

**Observed:** Notifications consistently arrived after 10–15 minutes.  
**Expected:** Notifications should be delivered within 30 seconds under normal operating conditions.  

### Diagnosis
- Investigation revealed a backlog in the message broker queue responsible for dispatching push notifications.  
- A misconfigured retry policy applied exponential backoff too aggressively, causing retries to accumulate and overwhelm the queue during peak load.  
- Because monitoring alerts for queue latency and delivery times had not been configured, the issue was not detected until end users reported it.  
- The backlog was reproducible in staging under simulated peak load, confirming the root cause.  

### Resolution
- Retry thresholds were adjusted to prevent runaway exponential backoff and reduce queue congestion.  
- The broker cluster was scaled horizontally to increase throughput and provide additional headroom during peak usage.  
- Monitoring and alerting were added for queue latency, delivery times, and retry rates to ensure early detection of similar issues.  
- Customer Support was provided with updated runbooks to escalate notification delays more quickly in the future.  

### Verification
- Test notifications were delivered consistently within 5–10 seconds across multiple devices and accounts.  
- Monitoring dashboards confirmed queue latency remained within acceptable thresholds during simulated load tests.  
- Customer Support validated the fix with affected users, who confirmed that notifications were once again arriving promptly.  

**Closed:** 2025-09-24
