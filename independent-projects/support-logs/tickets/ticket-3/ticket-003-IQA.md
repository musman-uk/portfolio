## ticket‑003‑IQA: Authentication Timeout

Opened By: Internal QA  
Date: 2025‑09‑28  
Priority: High  
Environment: API Gateway · Staging Cluster  

### Description  
During scheduled load testing on the staging cluster, the QA team observed intermittent authentication timeouts. The failures occurred when concurrent login attempts exceeded expected thresholds. Approximately 15 to 20 percent of login requests failed to establish a session, returning timeout errors. The behaviour was consistent across multiple test runs, indicating a systemic issue rather than isolated anomalies.  

### Impact  
- QA testing cycles are blocked until authentication stability is confirmed.  
- There is a risk that similar behaviour could occur in production under high load.  
- Test coverage for authentication workflows cannot be completed until this issue is resolved.  

*Linked Log:** [SL-003](https://github.com/musman-uk/portfolio/blob/main/independent-projects/support-logs/logs/log-3/SL-003.md)
