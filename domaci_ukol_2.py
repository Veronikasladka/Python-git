# 1. část domacího úkolu
import requests

# získání IČO od uživatele
ico = input("Zadej IČO subjektu: ")

# sestavení URL adresy
url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"

# odeslání GET požadavku
response = requests.get(url)

# převedení odpovědi na JSON
data = response.json()

# získání požadovaných údajů
obchodni_jmeno = data.get("obchodniJmeno")
adresa = data.get("sidlo", {}).get("textovaAdresa")
print("Obchodní jméno:", obchodni_jmeno)
print("Adresa sídla:", adresa)

# 2. část domácího úkolu
import requests

# získání názvu subjektu od uživatele
nazev = input("Zadej název subjektu (nebo jeho část): ")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = f'{{"obchodniJmeno": "{nazev}"}}'

# odeslání POST requestu
response = requests.post(
    "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat",
    headers=headers,
    data=data
)

# převedení odpovědi na JSON
result = response.json()

# získání počtu a seznamu subjektů
pocet = result.get("pocetCelkem", 0)
subjekty = result.get("ekonomickeSubjekty", [])
print(f"Nalezeno subjektů: {pocet}")

for subjekt in subjekty:
    jmeno = subjekt.get("obchodniJmeno")
    ico = subjekt.get("ico")
    print(f"{jmeno}, {ico}")

