# lplus obfuscator

## Beschreibung

Zur datenschutzkonformen Verarbeitung von LPLUS-Prüfungsdaten werden die personenbezogenen Daten der REST-Abfragen mithilfe dieses Moduls anonymisiert. Dabei kommt der SHA256-Algorithmus zum Einsatz.
Es wird die Funktion obfuscate() als Wrapper um die Abfrage gelegt und produziert dann den anonymisierten Datensatz.

### Beispiel:<br>
Originalantwort bei Abfrage eines Kandidaten:<br>
```
response = requests.get("https://fub.lplus-teststudio.de/publicapi/v1/candidates/179922", headers=headers)
response = {"userLicences":[{"licenceId":995,"locationId":23}],"examinationParts":[{"userDetailId":179922,"examinationPartId":2268,"examinationPartName":"Demoprüfung","examinationPartPosition":1,"licenceId":995,"licenceName":"_test_bug","locationId":23,"locationName":"99999_Miri_Test","numberOfTries":0}],"uasOperatorContext":null,"id":179922,"userName":"TEST_jondoe","password":null,"userState":1,"gender":3,"salutation":null,"salutationLocalizationKey":null,"title":0}
```
Anonymisierte Datenstruktur nach Nutzung von obfuscate():<br>
```
from lplus_obfuscator import obfuscate

response_anonym = obfuscate(response)
response_anonym = {'userLicences': [{'licenceId': 995, 'locationId': 23}], 'examinationParts': [{'userDetailId': 179922, 'examinationPartId': 2268, 'examinationPartName': 'Demoprüfung', 'examinationPartPosition': 1, 'licenceId': 995, 'licenceName': '_test_bug', 'locationId': 23, 'locationName': '99999_Miri_Test', 'numberOfTries': 0}], 'uasOperatorContext': None, 'id': 179922, 'userName': '593900fd750256457086968d880c75412759725bd191048594ac898161d72c9f', 'password': None, 'userState': 1, 'gender': '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce', 'salutation': None, 'salutationLocalizationKey': None, 'title': '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'}
```
Personenbezogene Daten wie Username oder Geschlecht wurden durch einen gehashten Wert ersetzt, welcher nicht mehr zurückführbar ist. Die weitere Verarbeitung der Daten erfolgt dann mit anonymisierten Nutzer:innen-Daten.

Das Modul kann entweder aus dem Repo geklont oder per pip installiert werden (https://pypi.org/project/lplus-obfuscator/): 
```
pip install lplus-obfuscator
```

und dann wie gewohnt importiert werden
```
from lplus_obfuscator import obfuscate
```
