# Docentendraaiboek · Starten met IoT "van webshop tot datastroom"

*Bij les 2 Klimaatbeheersing, onderdeel 2.3 (slides 43–44). Versie oktober 2026.*

## Structurele Opzet & Bestandsbeheer

De lesomgeving kent twee versies die in de repository beheerd worden:

1. **`docent/notebooks/` (Docentenversie):**
   * **Doel:** Volledige referentie, uitgewerkte code-oplossingen, ingevulde tabellen en **100% voorgevoerde uitvoerblokken** (plots, tabellen, console-logs).
   * **Gebruik:** Voor de docent tijdens het lesgeven of als naslagwerk.
2. **`notebooks/` (Studentenversie):**
   * **Doel:** Actief werkblad voor studenten.
   * **Geïntegreerde Didactiek:** 
     * **Code-oplossingscellen verwijderd:** Codecellen met de tag `tags: ["oplossing"]` zijn gestript. Studenten typen hun eigen Python-code in de daarboven gelegen invulbare studenten-codecellen met `# SCHRIJF HIER JE CODE:`.
     * **Verborgen Markdown-oplossingen behouden:** Inklapbare HTML-secties (`<details><summary><b>Oplossing tonen</b></summary></details>`) voor inhoudelijke/conceptuele vragen blijven behouden in het studentennotebook.
     * **Geen herhaling:** Instructies staan in Markdown, beknopte Hints/Startercode in de `#` comments van de codecel.
     * **Groene Callout-boxen (`background-color: #e8f5e9; color: #1b5e20;`):** Ondersteunen direct onder de uitvoer de interpretatie van netwerkdata, JSON-structuren en grafieken.

---

## Voorbereiding (één keer, ± 30 min)

1. **Repository op GitHub zetten** (publiek of binnen de UGent-organisatie) en de Codespaces-knop in de README testen: *Code ▸ Codespaces ▸ Create codespace*. De eerste build duurt 2–3 min; daarna start een Codespace in ± 30 s.
2. **Klascode kiezen**, bv. `i700301-2026-k7q2` (iets onvoorspelbaars: de broker is publiek). Zet ze in `02_mqtt_live_meekijken.ipynb` (variabele `KLASCODE`), in `04_wokwi_virtuele_sensor.ipynb` en in `wokwi/main.py`, en geef ze op het bord.
3. **Eigen Codespace openen** en alle docentennotebooks (`docent/notebooks/*.ipynb`) één keer doorlopen. Notebook 02, sectie 5 (virtuele S31-CB) laat je tijdens de les in een **apart tabblad** draaien, zodat je zelf ook kunt meekijken met het klasverkeer.
4. Optioneel: de **HiveMQ Websocket Client** (<https://www.hivemq.com/demos/websocket-client/>) in een browsertab open hebben, verbonden met `broker.hivemq.com:8884` (SSL), geabonneerd op `ugent/<klascode>/#`. Handig als "scherm vooraan" om alle groepen te zien.
5. Antratek- en Dragino-pagina's in tabbladen klaarzetten (adressen in README).

---

## Lesverloop (± 2 × 50 min)

| Tijd | Wat | Hoe & Wat er precies gebeurt |
|---|---|---|
| **0–10 min** | **Notebook 00: Start hier** | • Studenten openen hun Codespace en voeren **Notebook 00** uit.<br>• **Pakketcontrole:** Python 3.12, `paho-mqtt`, `requests`, `pandas`, `matplotlib` worden gevalideerd.<br>• **MQTT & HTTP test:** Er wordt een testbericht gestuurd naar HiveMQ en actuele weerdata opgevraagd bij Open-Meteo.<br>• **Didactisch accent:** Eerst wordt de **volledige ruwe JSON** geprint met `json.dumps(indent=2)`, waarna studenten leren hoe ze specifieke sleutels selecteren (`gegevens['current']`). |
| **10–25 min** | **Notebook 01: Stap 1 & 2** *(Webshop & Handleiding)* | • **Jij demonstreert op het scherm:** Antratek webshop ▸ product S31-LB ▸ artikelnummer EU868 ▸ Dragino wiki ▸ handleiding §2.2 (OTAA Join), §2.3 (Payload), §3.3 (AT-commando's).<br>• **Studentenopdracht 1.1 & 2.1:** Studenten vullen in hun notebook het gekozen sensortype in, beschrijven het LED-gedrag bij de Join (5s groen continu) en het AT-commando voor 10 min interval (`AT+TDC=600`). |
| **25–50 min** | **Notebook 01: Stap 3** *(Payload decodering)* | • **Samen binaire bytes ontleden:** 11 bytes byte-voor-byte ontleden op het bord (Big-Endian, Two's complement voor negatieve temperaturen, bitmasking voor alarmvlaggen).<br>• **Opdracht 3.1:** Studenten schrijven hun eigen Python-code in de invulcel om 3 hex-payloads (A, B, C) automatisch te decoderen.<br>• **Stap 3g:** Je toont hoe de officiële JavaScript-decoder van Dragino via Node.js exact dezelfde waarden oplevert. |
| **50–60 min** | **Pauze** | |
| **60–70 min** | **Notebook 01: Stap 4** *(NB-IoT & MQTT)* | • S31-CB (NB-IoT/LTE-M variant) bespreken: AT-commando's (`AT+PRO`, `AT+SERVADDR`), JSON-dataformaat en netwerkvergelijking.<br>• **Opdracht 4.1 & 4.2:** AT-commando reeks samenstellen en netwerkbeperkingen (Duty cycle 868 MHz vs. NB-IoT gelicentieerd spectrum) toelichten. |
| **70–95 min** | **Notebook 02: MQTT Live Meekijken** | • **Jij start de Simulatie:** Start Cel 5 (virtuele S31-CB) in een apart tabblad met `DUUR = 1500`. Drie stalafdelingen zenden nu live MQTT-berichten.<br>• **Studenten:** Abbonneren zich op live topics (`ugent/<klascode>/stal/#`), publiceren eigen statusberichten (`retain=True`), vangen een Pandas DataFrame op met alle klasberichten, en filteren alarmen (`interrupt == 1`). |
| **95–110 min** | **Notebook 03 (of 04)** | • **Keuze Notebook 03:** Echte live data ophalen van 60+ publieke meetstations rond Gent via de HTTP REST API van Sensor.Community (een publiek sensornetwerk van burgers/vrijwilligers). Berekenen van de Temperature-Humidity Index (**THI hittestress**) en analyse van sensorverzadiging op 99.9% RV bij de DHT22.<br>• **Alternatief Notebook 04:** Wokwi ESP32 MicroPython simulatie. Zelf een virtuele DHT22 sensor programmeren en verbinden met MQTT. |
| **110–120 min**| **Afronding** | • **Koppeling naar de theorie (slides 43–44):** Waar zat elk verbindingstype (LoRaWAN vs NB-IoT vs Wi-Fi) en elk protocol (MQTT vs HTTP vs Modbus) in wat we gedaan hebben? |

---

## Oplossingen & Referentiecode

In de studentennotebooks (`notebooks/*.ipynb`) zijn alle code-oplossingscellen gestript. Hieronder vind je de directe referentiecode zoals deze aanwezig is in de docentenversie (`docent/notebooks/*.ipynb`).

### Notebook 00 · Start hier
**Opdracht (Open-Meteo API aanpassen):**
```python
import requests
import json

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 51.05,
    "longitude": 3.72,
    "current": "temperature_2m,relative_humidity_2m"
}

antwoord = requests.get(url, params=params, timeout=10)
gegevens = antwoord.json()

# 1. Eerst volledige JSON afdrukken
print("=== VOLLEDIGE JSON-RESPONS ===")
print(json.dumps(gegevens, indent=2))

# 2. Daarna selectie afdrukken
print("\n=== SELECTIE VAN GEGEVENS ===")
huidig = gegevens["current"]
eenheden = gegevens["current_units"]
print(f"Gent: {huidig['temperature_2m']} {eenheden['temperature_2m']}, {huidig['relative_humidity_2m']} {eenheden['relative_humidity_2m']}")
```

---

### Notebook 01 · Sensor kiezen, verbinden en uitlezen

#### Opdracht 2.1 (Handleiding §2.2 & §3.3.1)
* **Groene LED bij Join:** Na het indrukken van de knop (5 s) knippert de groene LED 5× snel. Bij een geslaagde join brandt de groene LED **5 seconden continu**.
* **AT-commando zendinterval:** `AT+TDC=600` (600 seconden = 10 minuten). Via TTN downlink: `01 00 02 58`.

#### Opdracht 3.1 (Hex Payloads Decoderen)
Opbouw: `[bat 2B][timestamp 4B][vlaggen 1B][temp 2B signed ×10][RV 2B ×10]`, alles Big-Endian.

```python
# Oplossing codecel in docent/notebooks/01_sensor_kiezen_en_verbinden.ipynb
monster_data = {
    "A": "0BC46AD703600000D60278",
    "B": "0AE6696486D800FFCE0393",
    "C": "0B866A4671380101400320"
}

for label, hex_code in monster_data.items():
    resultaat = decodeer_s31lb(hex_code)
    print(f"Sample {label}:", resultaat)
```

**Tabeloverzicht van de uitkomsten:**
| Sample | Payload | Batterij | Tijd (UTC) | Alarm | T (°C) | RV (%) |
|---|---|---|---|---|---|---|
| **Demo** | `0B456AD703600001050197` | 2,885 V | 2026-10-20 06:00:00 | Nee | 26,1 | 40,7 |
| **A** | `0BC46AD703600000D60278` | 3,012 V | 2026-10-20 06:00:00 | Nee | 21,4 | 63,2 |
| **B** | `0AE6696486D800FFCE0393` | 2,790 V | 2026-01-12 05:30:00 | Nee | **−5,0** (`FFCE` = −50) | 91,5 |
| **C** | `0B866A4671380101400320` | 2,950 V | 2026-07-02 14:10:00 | **Ja** (byte 6 = `01`) | 32,0 | 80,0 |

#### Opdracht 4.1 (AT-commando's MQTT)
```text
AT+PRO=3,5
AT+SERVADDR=broker.hivemq.com,1883
AT+CLIENT=s31cb-afdeling3
AT+PUBTOPIC=ugent/i700301/stal/afdeling3
AT+MQOS=1
AT+TDC=600
```

#### Opdracht 4.2 (LoRaWAN vs NB-IoT)
1. **LoRaWAN (868 MHz):** Ongelicentieerd spectrum met wettelijke *duty cycle* van 1% (max. 36 s zendtijd per uur) en TTN Fair-Use Policy (30 s uplink per dag). Elke byte kost zendtijd en batterij.
2. **NB-IoT:** Gelicentieerd 4G/5G-spectrum zonder duty cycle. Je betaalt een vast maandabonnement per simkaart, waardoor JSON- payloads van 300 bytes geen netwerkbeperking vormen.

---

### Notebook 02 · MQTT Live Meekijken

#### Opdracht 4.1 (Retained statusberichten)
```python
status_berichten = luister(f"{BASIS}/groepen/+/status", seconden=5)
for topic, payload, is_retained in status_berichten:
    print(f"Topic: {topic} | Inhoud: {payload} | Retained?: {is_retained}")
```
* **Conclusie:** Berichten komen **onmiddellijk** binnen met `is_retained = True`. De broker bewaart de laatste status op het topic.

#### Sectie 7 (Alarmen filteren & Last Will)
```python
alarm_berichten = [
    (topic.split("/")[-1], json.loads(payload)["temperature"], json.loads(payload)["humidity"])
    for topic, payload, retain in ruwe_berichten
    if json.loads(payload).get("interrupt") == 1
]
print("Aantal alarmen:", len(alarm_berichten))
```
* **Last Will & Testament (LWT):** `client.will_set(topic, payload="offline", qos=1, retain=True)`. Als een stalsensor wegvalt door kabelbreuk of lege batterij, publiceert de broker automatisch het offline-bericht naar de klimaatcomputer.

---

### Notebook 03 · Echte sensoren via HTTP REST API

#### Opdracht 2.1 (Sensorverzadiging op 99.9% RV)
```python
print("Sensortypes op 99.9% RV:")
print(df[df["humidity"] >= 99.9]["type"].value_counts())
```
* **Conclusie:** Vrijwel alle sensoren die op 99.9% RV staan zijn van het goedkope type **DHT22**. Bij hoge luchtvochtigheid (zoals in veestallen) raakt het capacitieve polymeer verzadigd met condens water, waardoor de sensor urenlang op 99.9% blijft steken. Geleidelijke gekalibreerde sensoren (SHT31, BME280) zijn vereist.

#### Sectie 7 (Resampling & THI)
```python
# Binnensensoren vs Buitensensoren
print(df.groupby("binnen")["THI"].describe().round(1))

# Resampling naar 20 min intervallen
df_dag_20min = df_dag.resample("20min", on="timestamp").mean(numeric_only=True)
print(f"Piek THI (2.5 min): {df_dag['THI'].max():.2f} vs (20 min): {df_dag_20min['THI'].max():.2f}")
```
* **Conclusie:** Herbemonsteren naar 20-minuten intervallen vlakt korte extremen en pieken af, waardoor de maximale THI-score licht afneemt.

---

### Notebook 04 · Wokwi Virtuele Sensor (ESP32 MicroPython)
1. **Zendinterval = 600 s:** Batterijduur stijgt drastisch doordat de ESP32 99% van de tijd in `machine.deepsleep()` staat.
2. **Wi-Fi vs LoRaWAN:** Wi-Fi associatie kost 100–200 mA gedurende enkele seconden. LoRaWAN activeert de radio voor slechts enkele milliseconden, wat jaren batterijduur op een knoopcel oplevert.
3. **JSON Flexibiliteit:** Extra velden toevoegen (bijv. `"lichtsterkte": 450`) verstoort bestaande ontvangers niet, mits het afgesproken schema gerespecteerd blijft.

---

## Valkuilen & Practical Tips

* **Publieke HiveMQ Broker:** Iedereen kan meelezen op `broker.hivemq.com`. Gebruik de unieke klascode en herinner studenten eraan dat er geen gevoelige persoonsgegevens verzonden mogen worden.
* **Firewalls & Poort 1883:** In Codespaces werkt poort `1883` altijd direct. Mocht een student lokaal op campus-Wi-Fi werken waar 1883 geblokkeerd is, schakel dan over op WebSockets via poort `8884` (zie tip in Notebook 00).
* **Sensor.Community API:** Bij hevig netwerkverkeer kan de live API van Sensor.Community vertragen. Het notebook beschikt over automatische fallback-mechanismen naar lokale reserve-bestanden in `data/`.
* **Codespaces Beheer:** Herinner studenten eraan om na afloop hun Codespace af te sluiten (*Codespaces ▸ Stop current codespace*) om gratis uren te besparen.
