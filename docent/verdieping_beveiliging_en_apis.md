# Verdieping & Toekomstige Uitbreidingen: Beveiliging, Eigen API's & Hardware

Dit document bundelt achtergrondinformatie, netwerkarchitecturen en ideeën voor toekomstige praktijkuitbreidingen van het IoT-practicum. Het dient als naslagwerk voor docenten die het practicum willen verdiepen met eigen API-servers, beveiligde MQTT-brokers of geavanceerde hardwareopstellingen.

---

## 1. Een Dataset Aanbieden via een Eigen HTTP REST API

In het basispracticum leren studenten hoe ze datasets **uitlezen (consumeren)** van externe REST API's (zoals Open-Meteo of Sensor.Community). Om zelf een dataset vanaf een lokale computer aan derden aan te bieden via het internet, zijn twee onderdelen nodig: de API-code in Python en een netwerktunnel/cloudhost.

### A. Python Code: Een API bouwen op een SQL-dataset (FastAPI + SQLite)
Met het populaire Python-framework **FastAPI** koppel je in enkele regels code een lokale SQL-database (zoals SQLite of PostgreSQL) aan een interactieve HTTP REST API:

```python
# app.py - Een eenvoudige FastAPI server op een SQLite dataset
from fastapi import FastAPI
import sqlite3

app = FastAPI(title="Mijn Stal-Klimaat API")

def lees_dataset_uit_sql():
    conn = sqlite3.connect("klimaat_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, afdeling, temperatuur, luchtvochtigheid FROM metingen ORDER BY id DESC LIMIT 100")
    rijen = cursor.fetchall()
    conn.close()
    return [
        {"timestamp": r[0], "afdeling": r[1], "temperatuur": r[2], "luchtvochtigheid": r[3]}
        for r in rijen
    ]

@app.get("/")
def home():
    return {"bericht": "Welkom bij de Stal-Klimaat API"}

@app.get("/api/v1/klimaat")
def geef_klimaat_data():
    """Geef de laatste 100 metingen uit de SQL-database terug als JSON."""
    return lees_dataset_uit_sql()
```

### B. De Uitdaging: Een Lokale PC Bereikbaar Maken via het Internet
Een lokale computer zit achter een thuis- of campusrouter (NAT/Firewall) en heeft geen vast publiek IP-adres. Om de API vanaf de eigen PC toch beschikbaar te stellen aan anderen over het internet, zijn er twee methoden:

1. **Lokale Tunneling (Ideaal voor demonstraties):**
   * **`ngrok`** of **`Cloudflare Tunnels`**: Deze tools maken een beveiligde uitgaande tunnel vanaf jouw PC naar het internet.
   * *Commando:* `ngrok http 8000`
   * *Resultaat:* Je krijgt een publieke URL (bijv. `https://a1b2-34-89-10.ngrok-free.app/api/v1/klimaat`) die verzoeken van over de hele wereld direct doorstuurt naar jouw lokale Python-server.
2. **Cloud Hosting (Permanente oplossing):**
   * Bied de Python-code en SQL-database aan op een gratis/goedkope cloud-dienst zoals **Render.com**, **Railway.app** of **Fly.io**.

---

## 2. Beveiliging van MQTT-Datastromen (Afschermen van Sensordata)

In het practicum gebruiken we de openbare testbroker `broker.hivemq.com` zonder wachtwoord. Voor industriële toepassingen moet sensordata uiteraard afgeschermd worden.

### De 3 Beveiligingslagen in MQTT

1. **Authenticatie (Gebruikersnaam & Wachtwoord):**
   * Elke sensor of gebruiker moet inloggen bij de broker.
   * *In Python (`paho-mqtt`):*
     ```python
     client.username_pw_set("stal_boer_1", "GeheimWachtwoord123")
     ```
   * *Op een industriële sensor (zoals Dragino S31-CB via AT-commando's):*
     ```text
     AT+UNAME=stal_boer_1
     AT+PWD=GeheimWachtwoord123
     ```
2. **Autorisatie / ACL's (Access Control Lists per Topic):**
   * De broker bepaalt welke gebruiker op welk topic mag lezen (*subscribe*) of schrijven (*publish*).
   * *Voorbeeld:* Boer Jan mag alleen luisteren op `boerderij/stal1/#`, terwijl een onderhoudsmonteur alleen toegang heeft tot `boerderij/stal1/onderhoud`.
3. **TLS/SSL Versleuteling (Dataprivacy over de lijn):**
   * Zorgt ervoor dat wachtwoorden en sensordata op de netwerkkabel onleesbaar zijn voor kwaadwillenden. Je verbindt via poort `8883` (of `8884` voor WebSockets) in plaats van de onversleutelde poort `1883`.

### Vergelijking Broker-Opties (Gratis vs. Betalend)

| Broker / Oplossing | Beveiliging & Eigenschappen | Kostenmodel |
|---|---|---|
| **HiveMQ Cloud (Serverless Free)** | Volledige TLS-versleuteling verplicht, ingebouwde gebruikers/wachtwoordbeheer en ACL's. Zeer eenvoudig in te stellen. | **Gratis** (tot 100 apparaten / 10 GB data per maand). |
| **EMQX Cloud** | Professionele, schaalbare cloudbroker met gratis starter-tier. | **Gratis proef/starter** / daarna per verbruik. |
| **Eigen Mosquitto Server (VPS)** | Installeer de open-source Mosquitto broker op een eigen virtuele server (bijv. DigitalOcean, Hetzner, AWS EC2). Volledige controle over wachtwoorden en SSL-certificaten (via Let's Encrypt). | **€ 4 – € 6 per maand** voor een kleine VPS. |
| **AWS IoT Core / Azure IoT Hub** | Industrieel niveau. Werkt met unieke **X.509-certificaten** per individuele sensor in plaats van wachtwoorden. | Pay-per-message (zeer goedkoop voor enkele sensoren, centenwerk). |

---

## 3. Concrete Ideeën voor Toekomstige Uitgewerkte Practica

Hieronder staan drie concrete ideeën die als vervolgmodule of verdiepingsopdracht uitgewerkt kunnen worden:

### Idee 1: Lokale SQL Dataset via REST API aanbieden
* **Concept:** Studenten maken een lokale SQLite database aan met historische klimaatdata van de faculteit of proefhoeve. Met FastAPI schrijven ze een GET-endpoint om dag-gemiddelden op te vragen en maken dit via `ngrok` live beschikbaar voor hun medestudenten.
* **Leerdoel:** Het begrijpen van de serverzijde van HTTP, JSON-serialisatie en netwerktunnels.

### Idee 2: GSM als Live IoT-Sensor (Smartphone Streaming)
* **Concept:** In plaats van een fysieke hardware-sensor te kopen, gebruiken studenten hun eigen smartphone als IoT-node met gratis apps zoals **Phyphox** of **Sensor Logger**.
* **Werking:** De app leest de ingebouwde sensoren van de smartphone uit (accelerometer, GPS, lichtsensor, temperatuur/druk) en streamt deze data live via HTTP POST of MQTT naar een centrale broker of Python-script.
* **Leerdoel:** Live datastromen visualisaties maken met bewegings- of locatiegegevens zonder extra hardware aan te schaffen.

### Idee 3: Echte LoRaWAN Sensor met 4G Gateway Opstelling
* **Concept:** Een demonstratieset opbouwen met een echte **Dragino S31-LB (LoRaWAN)** klimaat- en bodemsensor en een **4G Outdoor LoRaWAN Gateway** (bijv. Dragino DLOS8-EC25).
* **Dataketen:**
  1. **Sensor** verstuurt 11 binaire bytes via 868 MHz radio.
  2. **4G Gateway** vangt het radiosignaal op en stuurt het via het 4G mobiele netwerk door naar **The Things Network (TTN)**.
  3. **TTN Network Server** voert de JavaScript payload-decoder uit.
  4. De gedecodeerde JSON-data wordt via een **MQTT Integratie** of **Webhook** doorgestuurd naar een Python dashboard of platform zoals **Datacake** of **ThingsBoard**.
* **Leerdoel:** Het demonstreren van een volledig autonoom, netonafhankelijk IoT-systeem in de landbouw zonder afhankelijkheid van lokale Wi-Fi.

---

> 💡 **Meer ideeën & lesmodules:** Raadpleeg ook het bestand **`docent/ideeen.md`** voor een uitgebreide lijst met uitgewerkte didactische concepten (API-documentatie opdrachten, LoRaWAN vs. NB-IoT SIM-kostenvergelijking, cross-over data-sharing tussen medestudenten, live hardware-demos en IP-camera video streaming met Neurale Netwerken).

