from math import ceil
# nejprve vytvoř třídu Locality, která označuje lokalitu, kde se nemovitost nachází; Třída bude mít atributy name (název katastru/obce) a locality_coefficient (tzv. místní koeficient, který se používá k výpočtu daně)
class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient
# Vytvoř třídu Property, která bude reprezentovat nějakou nemovitost. Třída bude mít atribut locality (lokalita, kde se pozemek nachází, bude to objekt třídy Locality)
class Property:
    def __init__(self, locality):
        self.locality = locality
# Dále vytvoř třídu Estate, která reprezentuje pozemek a je potomkem třídy Property. 
class Estate(Property):
    # slovník s koeficienty pro jednotlivé typy pozemků
    ESTATE_COEFFICIENTS = {
        "land": 0.85,
        "building site": 9,
        "forrest": 0.35,
        "garden": 2
    }
    #Třída bude mít atributy locality, estate_type (typ pozemku), area (plocha pozemku v metrech čtverečních)
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
    #Dále přidej metodu calculate_tax(), která spočítá výši daně pro pozemek a vrátí hodnotu jak celé číslo (pro zaokrouhlení použij funkci ceil() z modulu math)
    def calculate_tax(self):
        type_coef = Estate.ESTATE_COEFFICIENTS.get(self.estate_type, 1)
        tax = self.area * type_coef * self.locality.locality_coefficient
        return ceil(tax)
    
 #Vytvoř třídu Residence`, která reprezentuje byt, dům či jinou stavbu a je potomkem třídy Property. Třída bude mít atributy locality, area (podlahová plocha bytu nebo domu) a commercial (pravdivostní hodnota, která určuje, zda se jedná o nemovitost používanou k podnikání).
class Residence(Property):
    def __init__(self, locality, area, commercial=False):
            super().__init__(locality)
            self.area = area
            self.commercial = commercial
    #Dále přidej metodu calculate_tax(), která spočítá výši daně pro byt a vrátí hodnotu jako číslo. Daň vypočítej pomocí vzorce: podlahová plocha * koeficient lokality * 15. Pokud je hodnota parametru commercial True, tj. pokud jde o komerční nemovitost, vynásob celou daň číslem 2.
    def calculate_tax(self):
            tax = self.area * self.locality.locality_coefficient * 15
            if self.commercial:
                tax *= 2
            return ceil(tax)
    
# Otestování funkcí
# Zemědělský pozemek o ploše 900 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 900 * 0.85 * 0.8 = 612.
manetin = Locality("Manětín", 0.8)
zemedelsky_pozemek = Estate(manetin, "land", 900)
print(f"Daň z pozemku je {zemedelsky_pozemek.calculate_tax()} Kč.")

#Dům s podlahovou plochou 120 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 120 * 0.8 * 15 = 1440
dum = Residence(manetin, 120, commercial=False)
print(f"Daň z domu je {dum.calculate_tax()} Kč.")

#Kancelář (tj. komerční nemovitost) s podlahovou plochou 90 metrů čtverečních v lokalitě Brno s koeficientem 3. Daň z této nemovitosti je 90 * 3 * 15 * 2 = 8100
brno = Locality("Brno", 3)
kancelar = Residence(brno, 90, commercial=True)
print(f"Daň z kanceláře je {kancelar.calculate_tax()} Kč.")