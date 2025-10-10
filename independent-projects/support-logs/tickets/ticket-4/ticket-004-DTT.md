## ticket‑004‑DTT: Rate‑Limit Misconfiguration

Opened By: Developer Tools Team  
Date: 2025‑10‑01  
Priority: Low  
Environment: 3rd‑Party API Integration  

### Description  
The Developer Tools Team identified that API requests to a third‑party integration are being throttled earlier than expected. Investigation shows that incorrect header values are being sent, which causes the external service to apply stricter rate limits than documented. The throttling occurs after fewer requests than the provider specifies, resulting in unnecessary delays during integration testing.  

### Impact  
- Development teams experience slower feedback loops when testing integrations.  
- There is no direct impact on production users at this stage.  
- If left unresolved, the misconfiguration could affect future production deployments that rely on this integration.  

*Linked Log:** [SL-004](https://github.com/musman-uk/portfolio/blob/main/independent-projects/support-logs/logs/log-4/SL--004.md)

