## Log 1: Data Export Corruption

- **Ticket Reference:** [ticket‑001-FT](https://github.com/musman-uk/portfolio/blob/main/independent-projects/support-logs/tickets/ticket-001-FT/full-ticket.md)  
- **Reported By:** Finance Team  
- **Date Opened:** 2025-09-14  
- **Environment:** Web App v3.4 · Windows 11 · Chrome 118  
- **Priority:** High  
- **Status:** Resolved  

### Report
During the September month‑end close, Finance users reported that CSV exports from the reporting dashboard were unusable. Exported files were missing header rows, and several columns were shifted out of alignment. This broke downstream reconciliation processes and prevented automated scripts from ingesting the data. The issue was raised as urgent because it directly impacted regulatory reporting deadlines and created significant manual rework for the Finance Team.

### Steps to Reproduce
1. Log in as a Finance role user.  
2. Navigate to **Reports → Monthly Summary**.  
3. Select **Export → CSV**.  
4. Open the exported file in Excel or Google Sheets.  

**Observed:** Header row missing, column alignment corrupted, data shifted into incorrect fields.  
**Expected:** Properly formatted CSV with headers and aligned data across all locales.  

### Diagnosis
- Root cause traced to a recent update of the CSV serialization library introduced in Web App v3.4.  
- UTF‑8 characters in header labels were not handled correctly, causing the serializer to misalign columns.  
- The regression was not detected during pre‑release testing because test data sets did not include non‑ASCII characters.  
- The issue was reproducible across multiple browsers and operating systems, confirming it was not environment‑specific.  

### Resolution
- Rolled back to the stable library version (2.8.1) pending a permanent fix.  
- Added regression tests specifically targeting CSV export formatting, including UTF‑8 header scenarios.  
- Implemented automated validation of exported files in the CI pipeline to catch malformed outputs before release.  
- Coordinated with Finance to re‑export and validate all affected reports to ensure business continuity.  

### Verification
- Finance team confirmed that exports now open correctly in both Excel and Google Sheets without manual adjustment.  
- Regression tests passed across all supported locales and character sets.  
- Monitoring was added to flag anomalies in export jobs, ensuring early detection of similar issues in future releases.  

**Closed:** 2025-09-16
