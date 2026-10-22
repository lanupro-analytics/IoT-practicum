# 🌐 Starten met IoT: van webshop tot datastroom

Welkom bij het practicum **Starten met IoT (Internet of Things)** van de opleiding **Precisielandbouw – toepassingen voor plant en dier** (UGent, les *Klimaatbeheersing in de veehouderij*, onderdeel 2.3).

In dit practicum ga je stapsgewijs aan de slag met echte draadloze klimaatsensoren, datadecoderingsketens, MQTT-netwerken en HTTP REST API's — **volledig in je browser, zonder dat je fysieke apparaten hoeft aan te kopen of op je eigen PC hoeft te installeren!**

---

## 🚀 Snelstartgids voor Studenten (In 4 eenvoudige stappen)

Heb je nog nooit met GitHub of Python gewerkt? Geen zorgen! Volg de 4 stappen hieronder om in enkele minuten aan de slag te gaan.

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ 1. GitHub       │ ──> │ 2. Start        │ ──> │ 3. Voer uit in  │ ──> │ 4. Sluit af     │
│    Inloggen     │     │    Codespaces   │     │    Notebooks    │     │    na de les    │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
```

### Stap 1: Inloggen op GitHub
1. Zorg dat je bent ingelogd op je [GitHub.com](https://github.com) account.
2. *Heb je nog geen account?* Maak gratis een account aan via [github.com/signup](https://github.com/signup) met je UGent e-mailadres.

---

### Stap 2: Je virtuele werkplek openen (GitHub Codespaces)
Met **GitHub Codespaces** start je een volledige virtuele computer in je internetbrowser waarin alle software (Python 3.12, Jupyter, pakketten) al klaarstaat.

1. Kijk bovenaan op deze pagina en zoek de groene knop **`< > Code`** (rechtsboven boven de bestandenlijst).
2. Klik op de knop **`< > Code`**.
3. Selecteer het tabblad **`Codespaces`**.
4. Klik op de grote groene knop **`Create codespace on main`**.

```text
  ┌─────────────────────────────────────────────────────────────┐
  │  < > Code  ▾                                                │
  └──────┬──────────────────────────────────────────────────────┘
         │
         ├── [ Local ]   [ Codespaces ]  <-- Klik op Codespaces
         │
         └─────────────┐
                       │   ┌────────────────────────────────┐
                       └──>│ 🟢 Create codespace on main    │  <-- Klik hier!
                           └────────────────────────────────┘
```

> **⏳ Even geduld:** De allereerste keer duurt het opstarten ongeveer **2 tot 3 minuten**. GitHub richt achter de schermen een virtuele Linux-container in. Zodra het scherm opent, zie je de vertrouwde Visual Studio Code editor in je browser.

---

### Stap 3: Werken in het Jupyter Notebook
Zodra je Codespace geopend is:

1. **Bestanden openen:**
   Kijk aan de linkerzijde in de *Explorer* (bestandenlijst) en klik op de map **`notebooks/`**.
2. **Start de eerste les:**
   Dubbelklik op het bestand **`00_start_hier.ipynb`**.
3. **Code uitvoeren:**
   * Een notebook bestaat uit tekst- en codecellen.
   * Klik in een grijs codeblok en druk op **`Shift` + `Enter`** op je toetsenbord (of klik op het afspeelknopje **`▶`** aan de linkerkant van de cel).
4. **Kernel selecteren (indien gevraagd):**
   Mocht VS Code rechtsboven vragen om een *kernel* of Python-omgeving te kiezen, kies dan **Python 3.12** (of de aanbevolen `Python 3 (ipykernel)`).

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  VS Code Explorer (Links)  │  Jupyter Notebook Werkblad (Midden)            │
├────────────────────────────┼────────────────────────────────────────────────┤
│  📁 notebooks/             │  # 00 · Start hier                             │
│     📄 00_start_hier.ipynb │  ...                                           │
│     📄 01_sensor_...       │  ┌──────────────────────────────────────────┐  │
│     📄 02_mqtt_...         │  │ ▶  import paho.mqtt.client as mqtt       │  │
│     📄 03_echte_...        │  └──────────────────────────────────────────┘  │
│     📄 04_wokwi_...        │     Druk op Shift + Enter om uit te voeren!   │
└────────────────────────────┴────────────────────────────────────────────────┘
```

---

### Stap 4: Na afloop van de les (Codespace stoppen)
GitHub geeft elke student elke maand gratis uren om Codespaces te gebruiken. Sluit na de les je virtuele computer netjes af zodat er geen uren onnodig verloren gaan:

1. Klik linksonder in VS Code op de blauwe of groene balk waarop **`Codespaces: ...`** staat.
2. Kies in het menu bovenaan **`Stop Current Codespace`**.
3. Of ga op GitHub naar [github.com/codespaces](https://github.com/codespaces), klik op de 3 puntjes (`...`) achter je actieve codespace en kies **`Stop codespace`**.

---

## 📚 Inhoud van het Practicum

Het practicum bestaat uit 5 interactieve Jupyter Notebooks. Voer de notebooks in onderstaande volgorde uit:

| Notebook | Onderwerp & Wat je leert | Verwachte Duur |
|---|---|---|
| **`00_start_hier.ipynb`** | **Start & Verbindingstest:** Controle van de Python-omgeving, eerste MQTT-testbericht versturen naar HiveMQ en een eerste HTTP REST API-vraag stellen aan Open-Meteo. | ± 10 min |
| **`01_sensor_kiezen_en_verbinden.ipynb`** | **Hardware & Binaire Payloads:** Keuze van een klimaatsensor in een webshop (Antratek), handleiding raadplegen (Dragino S31-LB), en het **byte-voor-byte handmatig decoderen** van 11-byte LoRaWAN hex-payloads. | ± 45 min |
| **`02_mqtt_live_meekijken.ipynb`** | **MQTT Protocollen & Simulatie:** Zelf een virtuele klimaatsensor in Python starten die live datastromen naar de HiveMQ-broker stuurt. Leren werken met topics, wildcards (`+`/`#`), retained berichten, LWT en Pandas gegevensanalyse. | ± 30 min |
| **`03_echte_sensoren_via_http.ipynb`** | **Echte Sensoren & Hittestress (THI):** Live data ophalen van 60+ burgerwetenschapsstations rond Gent via de REST API van Sensor.Community. Berekenen van de Temperature-Humidity Index (THI) voor melkvee en analyse van sensorverzadiging (DHT22 op 99.9% RV). | ± 30 min |
| **`04_wokwi_virtuele_sensor.ipynb`** | **MicroPython Hardware-simulatie:** Zelf een virtuele ESP32 met DHT22-sensor programmeren in de Wokwi browser-simulator en draadloos via Wi-Fi laten communiceren met MQTT. | ± 30 min |

---

## 💻 Alternatief: Lokaal werken (Voor Gevorderden)

Werk je liever lokaal op je eigen computer zonder GitHub Codespaces? Dat kan op twee manieren:

### Optie A: Lokaal met Docker Compose (Aanbevolen bij lokale installatie)
Zorg dat Docker Desktop geïnstalleerd is en voer in de terminal uit:
```bash
docker compose up
```
Open vervolgens `http://localhost:8888` in je browser.

### Optie B: Lokaal in een Python Virtuele Omgeving
```bash
git clone https://github.com/UGent-i700301/starten-met-iot.git
cd starten-met-iot
python3 -m venv venv
source venv/bin/activate  # Op Windows: venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

---

## 👩‍🏫 Informatie voor Docenten

* De uitgewerkte docentenversies van alle notebooks (inclusief alle voorgevoerde uitvoerblokken, uitgewerkte code-oplossingen en achtergrondinformatie) zijn te vinden in de map **`docent/notebooks/`**.
* Het didactisch lesverloop, de tijdsplanning per onderdeel en de antwoorden op de vragen staan beschreven in **`docent/draaiboek.md`**.
* Achtergrondinformatie over netwerkbeveiliging, eigen API's bouwen met FastAPI en geavanceerde hardwareopstellingen vind je in **`docent/verdieping_beveiliging_en_apis.md`**.

---

## 📖 Bronnen & Referenties

* **Antratek Electronics (België/Nederland):** <https://www.antratek.be/lora/sensor-nodes/temperature-humidity>
* **Dragino Documentatiecentrum S31-LB (LoRaWAN):** <https://wiki.dragino.com/docs/LoRaWAN-End-Node/temperature-humidity-sensors/s31-lb/>
* **Dragino Documentatiecentrum S31-CB (NB-IoT/LTE-M):** <https://wiki.dragino.com/docs/NB-IoT/temperature-humidity-sensors/s31-cb/>
* **Sensor.Community REST API:** <https://data.sensor.community/>
* **Open-Meteo Weather API:** <https://open-meteo.com/>
* **Wokwi ESP32 Simulator:** <https://wokwi.com/>

---

## ⚖️ Licentie

* **Lesmateriaal & Teksten:** Creative Commons Naamsvermelding-NietCommercieel-GelijkDelen 4.0 Internationaal ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.nl)).
* **Broncode & Scripts:** MIT Licentie.
* *Productnamen, merktekens en handleidingen zijn eigendom van de respectieve fabrikanten en worden uitsluitend geciteerd voor onderwijsdoeleinden.*
