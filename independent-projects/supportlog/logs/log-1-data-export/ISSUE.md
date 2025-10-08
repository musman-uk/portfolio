## Log 1: Data Export Corruption

- **Reported By:** Finance Team  
- **Date Opened:** 2025-09-14  
- **Environment:** Web App v3.4, Windows 11, Chrome 118  
- **Priority:** High  
- **Status:** Resolved  

### Report
Finance users reported that CSV exports from the reporting dashboard were unusable. Headers were missing, and several columns were shifted, breaking downstream reconciliation processes.

### Steps to Reproduce
1. Log in as a Finance role user.  
2. Navigate to **Reports → Monthly Summary**.  
3. Select **Export → CSV**.  
4. Open the exported file in Excel.  

**Observed:** Header row missing, column alignment corrupted.  
**Expected:** Properly formatted CSV with headers and aligned data.  

### Diagnosis
- Issue traced to a recent update of the CSV serialization library.  
- UTF‑8 characters in header labels caused the serializer to misalign columns.  
- Regression introduced in v3.4 release.  

### Resolution
- Rolled back to stable library version (2.8.1).  
- Added regression tests for CSV export formatting.  
- Implemented automated validation of exported files in CI pipeline.  

### Verification
- Finance team confirmed exports now open correctly in Excel and Google Sheets.  
- Regression tests passed across all supported locales.  

**Closed:** 2025-09-16
