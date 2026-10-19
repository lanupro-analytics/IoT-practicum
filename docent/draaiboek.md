# Docentendraaiboek · IoT-practicum "van webshop tot datastroom"

*Bij les 2 Klimaatbeheersing, onderdeel 2.3 (slides 43–44). Versie 19 oktober 2026.*

## Voorbereiding (één keer, ± 30 min)

1. **Repository op GitHub zetten** (publiek of binnen de UGent-organisatie) en de Codespaces-knop in de README testen: *Code ▸ Codespaces ▸ Create codespace*. De eerste build duurt 2–3 min; daarna start een Codespace in ± 30 s.
2. **Klascode kiezen**, bv. `i700301-2026-k7q2` (iets onvoorspelbaars: de broker is publiek). Zet ze in `02_mqtt_live_meekijken.ipynb` (variabele `KLASCODE`), in `04_…` en in `wokwi/main.py`, en geef ze op het bord.
3. **Eigen Codespace openen** en alle notebooks één keer volledig uitvoeren. Notebook 02, sectie 5 (virtuele S31-CB) laat je tijdens de les in een **apart tabblad** draaien, zodat je zelf ook kunt meekijken.
4. Optioneel: de **HiveMQ Websocket Client** (<https://www.hivemq.com/demos/websocket-client/>) in een browsertab open hebben, verbonden met `broker.hivemq.com:8884` (SSL), geabonneerd op `ugent/<klascode>/#`. Handig als "scherm vooraan" om alle groepen te zien.
5. Antratek- en Dragino-pagina's in tabbladen klaarzetten (adressen in README).

## Lesverloop (± 2 × 50 min)

| Tijd | Wat | Hoe |
|---|---|---|
| 0–10 | Notebook 00 | Iedereen opent een Codespace, voert 00 uit. Wie geen GitHub-account heeft: HiveMQ-webclient (sectie 7 van notebook 02) en meekijken met een buur. |
| 10–25 | Stap 1–2 van notebook 01 | **Jij demonstreert** op het scherm: Antratek ▸ product ▸ artikelnummer EU868 ▸ "meer info op Dragino" ▸ handleiding §2.2, §2.3, §2.4. Studenten volgen op hun eigen scherm en vullen opdracht 1.1 en 2.1 in (5 min, in duo's). |
| 25–50 | Stap 3 van notebook 01 | Byte voor byte samen decoderen (cellen 3a–3f). Daarna opdracht 3.1 met pen en papier; controle met de functie; dan de officiële JS-decoder (3g). |
| 50–60 | pauze | |
| 60–70 | Stap 4 van notebook 01 | S31-CB: `AT+PRO`, JSON-voorbeeld, grafiek. Koppel aan slide 44. |
| 70–95 | Notebook 02 | Jij start de virtuele S31-CB (sectie 5, `DUUR = 1500`). Studenten: sectie 3 (luisteren), 4 (publiceren — laat ze elkaars berichten zien), 6 (tabel + grafiek). |
| 95–110 | Notebook 03 (of 04) | Keuze: echte data + THI (03) als je de link met les 2 wil, of Wokwi (04) als je "zelf een toestel bouwen" wil. Het andere notebook is huiswerk. |
| 110–120 | Afronding | Terugkoppeling naar slides 43–44: waar zat elk verbindingstype en elk protocol in wat we deden? |

**Korte variant (50 min):** 00 (5) → 01 stap 1–3 als demo met opdracht 3.1 (30) → 02 sectie 3 en 5 live (15).

## Oplossingen

Dezelfde oplossingen staan ook in de notebooks zelf, in cellen met de tag `oplossing` (ingeklapt). Zie README voor het commando dat ze in één keer verwijdert.

### Notebook 01, opdracht 3.1 (payloads)

Opbouw: `[bat 2B][timestamp 4B][vlaggen 1B][temp 2B signed ×10][RV 2B ×10]`, alles big-endian.

| | Payload | Batterij | Tijd (UTC) | Alarm | T (°C) | RV (%) |
|---|---|---|---|---|---|---|
| demo | `0B456AD703600001050197` | 2,885 V | 2026-10-20 06:00:00 | nee | 26,1 | 40,7 |
| A | `0BC46AD703600000D60278` | 3,012 V | 2026-10-20 06:00:00 | nee | 21,4 | 63,2 |
| B | `0AE6696486D800FFCE0393` | 2,790 V | 2026-01-12 05:30:00 | nee | **−5,0** (`FFCE` = 65486 → −50) | 91,5 |
| C | `0B866A4671380101400320` | 2,950 V | 2026-07-02 14:10:00 | **ja** (byte 6 = `01`) | 32,0 | 80,0 |

Bespreking: C is een alarm-uplink (temperatuur boven de ingestelde drempel, hittestress in juli); B heeft de laagste batterijspanning (koude verlaagt de spanning van een Li-SOCl₂-cel tijdelijk — leuk zijspoor). De voorbeeldpayload bevat exact de getallen uit de handleiding (`0B45`, `0105`, `0197`), zodat studenten hun werk daar kunnen aftoetsen.

Veelgemaakte fouten: little-endian lezen (`450B`), het teken vergeten bij B, de vlaggenbyte als decimaal lezen, de temperatuur niet door 10 delen.

### Notebook 01, opdracht 2.1
Groene led brandt 5 s continu na een geslaagde join (§2.2 stap 3). Zendinterval: `AT+TDC=600` (seconden); via downlink `01 00 02 58` (0x258 = 600) — exacte syntaxis in §3.3.1.

### Notebook 01, opdracht 4.1
```
AT+PRO=3,5
AT+SERVADDR=broker.hivemq.com,1883
AT+CLIENT=s31cb-afdeling3
AT+PUBTOPIC=ugent/i700301/stal/afdeling3
AT+MQOS=1
AT+TDC=600
AT+APN=<apn van de operator>
```
(Zonder `AT+UNAME`/`AT+PWD`: de publieke broker vraagt geen aanmelding. Bij een eigen broker wel, plus `AT+TLSMOD` voor versleuteling.)

### Notebook 01, opdracht 4.2
LoRaWAN op 868 MHz: wettelijke *duty cycle* van 1 % (max. 36 s zendtijd per uur), lage bitsnelheid (0,3–50 kbit/s), en elke byte kost zendtijd dus batterij; het netwerk (TTN) hanteert bovendien een fair-use-beleid. NB-IoT: gelicentieerd spectrum, tientallen kbit/s, en je betaalt per sim/maand, niet per byte (binnen de bundel) — JSON van 300 bytes is dan geen probleem.

### Notebook 02
- 4.1: de statusberichten komen meteen binnen omdat ze *retained* zijn (derde element `True`).
- Opdracht 1: afdeling 3 komt het vaakst in alarm (start op 27,8 °C, drempel 30 °C).
- Opdracht 3: meting QoS 0 of 1 (een gemiste meting is niet erg, de volgende komt over 10 min); alarm QoS 1 of 2 (mag niet verloren gaan; bij 2 geen dubbele alarmen).
- Opdracht 4: bv. `bedrijf/stal<1-2>/afdeling<1-4>/<grootheid>`; alle NH₃: `bedrijf/+/+/nh3`.

### Notebook 03
- 2.1: DHT22 satureert op 99,9 % RV en is daar onnauwkeurig (±2–5 % RV, traag na condensatie); SHT31 ±2 % over het hele bereik, met anticondensbehuizing in de Dragino. In een stal met > 80 % RV is een DHT22 onbetrouwbaar.
- 3: herbemonsteren naar 20 min vlakt pieken af; de maximale THI daalt licht. Voor THI-alarmen is een kort interval belangrijker dan voor dagelijkse gemiddelden.
- 5: plausibiliteit (sprong > x °C per minuut), bevroren waarde (zelfde getal gedurende uren → sensor defect), tijdstempel te oud (verbinding weg), batterij < drempel, waarden buiten sensorspecificatie.

### Notebook 04
- 1: bij `INTERVAL = 600` wacht je 10 min; batterijduur schaalt ongeveer lineair met het interval (Dragino §4 geeft de tabel).
- 2: na deep sleep moet de ESP32 opnieuw wifi associëren (1–4 s, tientallen mA) en de MQTT-verbinding opzetten; bij LoRaWAN blijft de sessie bewaard en kost een uplink enkele tientallen ms zendtijd.

## Valkuilen

- **Publieke broker:** iedereen kan meelezen en publiceren. Unieke klascode, geen persoonsgegevens, en reken erop dat er af en toe vreemde berichten verschijnen (goede aanleiding om over authenticatie en TLS te praten).
- **Poort 1883 geblokkeerd** (campuswifi): vanuit een Codespace nooit een probleem; lokaal → websockets op 8884 (tip in notebook 00).
- **Codespaces-uren:** 60 uur/maand gratis per account (2 cores). Studenten laten stoppen na de les.
- **Sensor.Community:** de API is traag rond het hele uur en geeft soms 502/503; de notebooks vallen dan terug op de reservebestanden in `data/`. De archief-CSV van *gisteren* is pas 's ochtends volledig.
- **Websites veranderen:** Antratek-URL's en Dragino-sectienummers zijn van oktober 2026. Controleer vóór de les. Maak tijdens je eigen voorbereiding screenshots van de drie sleutelpagina's (Antratek-product, Dragino §2.3.2, Dragino S31-CB §2.2) als reserve voor als een site offline is.
- **Wokwi:** zonder account kun je simuleren maar niet bewaren; de publieke gateway is soms traag (wifi-verbinding tot 10 s). De `umqtt.simple`-bibliotheek zit in de MicroPython-firmware van Wokwi.
- **Node.js** is nodig voor cel 3g (officiële decoder); zit in de devcontainer. Lokaal zonder Node: de cel slaat zichzelf over.

## Codefragmenten voor slides 43–44

Slide 44 (protocollen), MQTT — publiceren zoals de S31-CB:
```python
client.publish("ugent/stal1/afdeling3", '{"temperature": 21.4, "humidity": 63.2}', qos=1)
#               topic (adres bij de broker)   payload (JSON)                       QoS 1 = minstens één keer
```
LoRaWAN-payload decoderen (slide 43, LoRaWAN):
```python
b = bytes.fromhex("0BC46AD703600000D60278")
temperatuur = int.from_bytes(b[7:9], "big", signed=True) / 10    # 21.4 °C
```
Modbus (slide 44), lezen van een klimaatcomputer of RS485-LB:
```python
client.read_holding_registers(address=0, count=2, slave=1)       # register 0 = T×10, register 1 = RV×10
```
HTTP (slide 44):
```python
requests.get("https://data.sensor.community/airrohr/v1/sensor/82001/").json()
```
