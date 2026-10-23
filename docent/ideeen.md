# 💡 Ideeën & Toekomstige Uitbreidingen voor het IoT-Lesmateriaal

Dit document bevat een verzameling concrete ideeën, didactische uitbreidingen en geavanceerde lesmodules om het IoT-lesmateriaal verder te verrijken of aan te passen voor vervolgmodules.

---

## 1. Zelfstandig Werken met API-Documentatie (Opdracht-aanpassing)

### Concept & Didactisch Doel
In plaats van cursisten/studenten vooraf opgebouwde Python-code te laten kopiëren of minimaal aan te passen, wordt de opdracht expliciet opgebouwd rond het **zelfstandig raadplegen van officiële API-documentatie** (zoals Open-Meteo, Sensor.Community, of custom REST API's).

### Concrete Uitwerking in de Opdracht
* **Expliciete Instructie:** "Pas de bestaande Python-voorbeeldcode aan op basis van de officiële documentatie van de REST API."
* **Hints & Zoekopdrachten voor de Cursist:**
  1. **API Endpoints & URL-opbouw:** Laat opzoeken welk specifiek endpoint nodig is (bijv. `/v1/forecast` vs. `/v1/historical`).
  2. **Query Parameters:** Welke parameters zijn verplicht (bijv. `latitude`, `longitude`) en welke specifieke variabelen zijn beschikbaar (bijv. `temperature_2m`, `relative_humidity_2m`, `wind_speed_10m`)?
  3. **Respons-formaat & JSON Key Selection:** Hoe ziet het JSON-antwoord eruit? Cursisten moeten opzoeken onder welke sleutel (`"current"`, `"hourly"`, of `"current_units"`) de gewenste gegevens staan.
  4. **Statuscodes & Foutafhandeling:** Wat gebeurt er als je een verkeerde parameter meestuurt? Cursisten controleren de HTTP statuscode (bijv. `400 Bad Request` vs. `200 OK`).

---

## 2. Vergelijkende Opdracht: LoRaWAN vs. NB-IoT Sensoren (Hardware, SIM-kaarten & Gateways)

### Concept & Didactisch Doel
Cursisten zoeken en vergelijken twee fysieke klimaatsensoren uit een webshop of fabrikantencatalogus (bijv. Dragino S31-LB LoRaWAN vs. Dragino S31-CB NB-IoT). Ze documenteren de specificaties en analyseren de operationele kostenstructuur op een landbouwbedrijf.

### Opdrachtinstructies voor Cursisten
1. **Opzoeken van 2 Sensoren met Bepaalde Eigenschappen:**
   * **Sensor 1 (LoRaWAN):** Een sensor die communiceert via het licentievrije 868 MHz radiospectrum.
   * **Sensor 2 (NB-IoT):** Een sensor die communiceert via het mobiele celnetwerk en is uitgerust met een ingebouwde SIM-kaart.
2. **Eigenschappen Documenteren:**
   * Zenderfrequentie & Netwerkprotocol.
   * Voeding (batterijduur, zonnepaneel, accuspanning).
   * IP-behuizingsklasse (bijv. IP65/IP67 voor stalomgevingen).
   * Datatransmissie-formaat (binaire hex-payload vs. JSON over MQTT/CoAP).

### Discussie & Kosten-Analyse (Kritische Reflectie)
* **NB-IoT (Cellulair / SIM per Node):**
  * Elk NB-IoT apparaat heeft een **eigen SIM-kaart** nodig met een mobiel dataconnectiviteits-abonnement.
  * **Terugkerende maandelijkse kost:** Aan elke SIM-kaart is een abonnement verbonden bij een telecomprovider (bijv. € 1 – € 3 per SIM per maand).
  * *Schaalbaarheid:* Bij 50 sensoren in een stallencomplex betekent dit 50 afzonderlijke SIM-abonnementen (€ 600 – € 1800/jaar aan data-abonnementen).
* **LoRaWAN (Gateway + Licentievrij Radiospectrum):**
  * LoRaWAN-sensoren zenden via 868 MHz radio naar een **lokale LoRaWAN Gateway**.
  * **Gateway Connectiviteit:** De gateway zelf vereist slechts **1 SIM-kaart** (4G/5G) óf wordt direct aangesloten op een lokale **LAN/Wi-Fi netwerkkabel**.
  * *Schaalbaarheid:* Bij LoRaWAN schalen extra sensoren zonder bijkomende abonnementskosten per node. De eenmalige investering in een gateway verdient zich bij meerdere sensoren snel terug.

---

## 3. Samenwerkingsopdracht: Data Hosten voor Medestudenten (Excel / SQL via API of MQTT)

### Concept & Didactisch Doel
Groepen cursisten/studenten hosten hun eigen dataset (afkomstig uit een `.xlsx` Excel-bestand of een lokale SQLite-database) als een live datastroom via een **MQTT-broker** of een **HTTP REST API** (bijv. met FastAPI). Medestudenten halen data bij elkaar op en voeren hierop gezamenlijke berekeningen uit.

### Mogelijke Uitvoeringsvormen
1. **Data Beschikbaar Maken / Hosten:**
   * **Optie A (HTTP API):** Een FastAPI-server leest een `.xlsx` of SQLite-database uit en biedt een REST-endpoint aan via `ngrok` (bijv. `https://groep1.ngrok.app/api/klimaat`).
   * **Optie B (MQTT Stream):** Een Python-script leest periodiek rijen uit een Excel/SQL-bestand en publiceert deze als JSON-berichten op een afgesproken MQTT-topic (bijv. `ugent/klas/groep1/stal_data`).
2. **Data Consumeren & Berekeningen Uitvoeren:**
   * **THI (Temperature-Humidity Index) voor Melkvee:** Groep A haalt temperatuur op bij Groep B en luchtvochtigheid bij Groep C, combineert de data en berekent de actuele hittestress.
   * **Voeder- en Ventilatiebehoefte bij Varkens:** Een script haalt bezettingsgraad en stalrijpheid op uit een gedeelde SQL-database van medestudenten en berekent dynamisch de benodigde luchtverversing ($m^3/uur/dier$) of de dagelijkse voederbehoefte op basis van het stalklimaat.

---

## 4. Live Demo Opstelling: Fysieke LoRaWAN Sensor + 4G Gateway

### Concept & Didactisch Doel
De docent brengt een fysieke hardware-opstelling mee naar de klas om het volledige, end-to-end IoT-proces van sensor tot MQTT live te demonstreren.

### Onderdelen van de Demo-Opstelling
* **Hardware:**
  * 1× Fysieke LoRaWAN-sensor (bijv. Dragino S31-LB temperatuur/luchtvochtigheid).
  * 1× LoRaWAN Gateway (bijv. Dragino DLOS8 of LPS8N).
  * 1× Mobiele 4G-router (met actieve SIM-kaart) of mobiele hotspot.
* **Dataketen Demonstratie:**
  1. **868 MHz Transmissie:** De sensor verzendt een binaire hex-payload in het lokaal radiospectrum.
  2. **Gateway Ontvangst:** De gateway ontvangt het radiosignaal en stuurt het via de 4G-router over het mobiele netwerk naar een netwerkserver (zoals *The Things Network* of *ChirpStack*).
  3. **Payload Decoding:** De netwerkserver decodeert de 11 binaire bytes naar JSON.
  4. **MQTT Integratie:** De gedecodeerde JSON-data wordt direct doorgezet naar de HiveMQ MQTT-broker op het les-topic (`ugent/klas/live_hardware`).
  5. **Live Inschrijving in Notebook:** Cursisten voeren in hun Jupyter Notebook de MQTT-subscriber uit en zien binnen enkele seconden de live data binnenkomen.

---

## 5. Beeldverwerking & AI: IP-Camera Streaming, Activiteitsmeting & Neurale Netwerken (NN)

### Concept & Didactisch Doel
Uitbreiding van IoT naar **Computer Vision**: het ontvangen van een videostream van een IP-camera (bijv. gericht op een stalbox of weide) en deze verwerken met Python voor gedragsanalyse, activiteitsmeting of dierherkenning.

### Mogelijke Uitwerkingsstappen
1. **RTSP / HTTP Videostream Ontvangen:**
   * Python leest de camerastream frame-per-frame in met bibliotheken zoals OpenCV (`cv2.VideoCapture("rtsp://...")`).
2. **Toepassing A: Activiteitsmeting (Frame Differencing / Motion Detection):**
   * Het verschil tussen opeenvolgende videoframes wordt berekend (*frame differencing* of *optical flow*).
   * **Resultaat:** Een kwantitatieve grafiek van activiteit in de tijd (bijv. is er onrust of verhoogde activiteit in de stal gedurende de nacht?).
3. **Toepassing B: Dataset Annotatie & Neuraal Netwerk (NN):**
   * Cursisten annoteren beelden (bounding boxes rond varkens, runderen of pluimvee).
   * **Object Detection & Gedragsanalyse:** Inzet van een lichtgewicht neuraal netwerk (bijv. YOLOv8 Nano of een custom CNN in PyTorch/TensorFlow) om het aantal dieren te tellen, hun positie bij de voederbak te registreren of afwijkend gedrag automatisch te detecteren.
