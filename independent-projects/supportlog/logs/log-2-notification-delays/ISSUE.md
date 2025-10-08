## Log 2: Notification Delivery Delays

- **Reported By:** Customer Support  
- **Date Opened:** 2025-09-22  
- **Environment:** Mobile App v2.1, iOS 17  
- **Priority:** Critical  
- **Status:** Resolved  

### Report
Users reported that push notifications for critical account alerts (e.g., payment failures, security warnings) were delayed by up to 15 minutes. This impacted time‑sensitive actions such as password resets.

### Steps to Reproduce
1. Trigger a password reset from the mobile app.  
2. Wait for push notification.  
3. Observe delivery time.  

**Observed:** Notifications arrive after 10–15 minutes.  
**Expected:** Notifications delivered within 30 seconds.  

### Diagnosis
- Queue backlog identified in the message broker.  
- Misconfigured retry policy caused exponential backoff to overwhelm the queue.  
- Monitoring alerts were not configured for queue latency.  

### Resolution
- Adjusted retry thresholds to prevent runaway backoff.  
- Scaled broker cluster to handle peak load.  
- Added monitoring alerts for queue latency and delivery times.  

### Verification
- Test notifications delivered consistently within 5–10 seconds.  
- Customer Support confirmed resolution with affected users.  

**Closed:** 2025-09-24
