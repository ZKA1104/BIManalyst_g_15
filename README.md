# BIManalyst group 15
# Window Rule Checker using IFCOpenShell

## Use Case
Dette script bruges til at tjekke IFC-modeller for at identificere og validere vinduers egenskaber som højde, bredde, areal, og karmhøjde. Det samlede vinduesareal beregnes også. Scriptet er skrevet i Python og kan køres fra en hvilken som helst Python-kompatibel IDE, såsom Visual Studio Code.

## Sådan fungerer scriptet
1. **Indlæsning af IFC-model:**
   IFC-filen indlæses ved hjælp af `ifcopenshell.open()`, som gør det muligt at åbne og læse IFC-modellen.
   
2. **Tjek af vinduer:**
   Scriptet anvender en regeldefineret funktion fra `windowRule` for at tjekke egenskaberne af vinduer i modellen. Funktionen `windowRule.checkRule(model)` gennemgår IFC-modellen og returnerer et resultat, der opsummerer de fundne vinduers data.

3. **Udskrift af resultat:**
   Efter at have kørt reglen, bliver resultatet af vinduestjekket printet ud i konsollen.

## Kodeeksempel
Her er et kodeudsnit fra scriptet:

```python
import ifcopenshell
from rules import windowRule

# Åbner IFC-filen
model = ifcopenshell.open("C:\\Users\\mikae\\OneDrive\\Dokumenter\\DTU BYGNINGSDESIGN\\3.semster\\41934 Advanced Building Information Modeling\\CES_BLD_24_06_ARC.IFC")

# Tjekker vinduerne ved hjælp af windowRule
windowResult = windowRule.checkRule(model)

# Printer resultatet af tjekket
print("Window result:", windowResult)

