## ticket‑003‑IQA: Authentication Timeout

**Opened:** 2025‑09‑28  
**Reported By:** Internal QA  
**Environment:** API Gateway · Staging Cluster  
**Status:** Planned  
**Severity:** High  

### Summary  
During load testing on the staging cluster, users experienced intermittent authentication timeouts. The issue was observed when concurrent login attempts exceeded expected thresholds.  

### Steps to Reproduce  
1. Initiate 200 or more concurrent login requests against the staging API Gateway.  
2. Observe session establishment times.  
3. Note that approximately 15 to 20 percent of requests fail with timeout errors.  

### Expected Behaviour  
All login requests should complete within the configured session timeout window, even under high load.  

### Actual Behaviour  
A subset of login requests fail to establish a session, returning timeout errors.  

### Impact  
- QA testing cycles are blocked until authentication stability is confirmed.  
- There is a risk of similar behaviour in production if not addressed.  

### Planned Action  
- Conduct targeted stress tests to replicate and measure failure rates.  
- Review session management configuration and optimise timeout thresholds.  
- Coordinate with infrastructure to validate load balancing behaviour.  

