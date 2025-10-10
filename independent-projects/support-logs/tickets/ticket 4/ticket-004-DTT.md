## ticket‑004‑DTT: Rate‑Limit Misconfiguration

**Opened:** 2025‑10‑01  
**Reported By:** Developer Tools Team  
**Environment:** 3rd‑Party API Integration  
**Status:** Planned  
**Severity:** Low  

### Summary  
API requests to a third‑party integration are being throttled prematurely. Investigation indicates that incorrect header values are being sent, which causes the external service to apply stricter rate limits than intended.  

### Steps to Reproduce  
1. Send a batch of requests to the third‑party API using the current integration.  
2. Monitor response headers for rate‑limit values.  
3. Observe throttling after fewer requests than documented by the provider.  

### Expected Behaviour  
The integration should respect the documented rate‑limit thresholds of the third‑party API.  

### Actual Behaviour  
Requests are throttled earlier than expected, resulting in unnecessary delays.  

### Impact  
- Development teams experience slower feedback loops when testing integrations.  
- There is no direct impact on production users at this stage.  

### Planned Action  
- Correct header configuration in the integration layer.  
- Validate changes against the provider documentation.  
- Add monitoring to ensure rate‑limit behaviour aligns with expectations.  
