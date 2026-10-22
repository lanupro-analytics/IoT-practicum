# IoT-practicum: van webshop tot datastroom

Practicum bij **I700301 Precisielandbouw – toepassingen voor plant en dier** (UGent), les *Klimaatbeheersing in de veehouderij*, onderdeel 2.3 *IoT: verbindingstypes en gegevensuitwisseling*.

Je leert in dit practicum, zonder fysieke sensor:

1. een draadloze klimaatsensor kiezen in een webshop (Antratek) en in de handleiding (Dragino) terugvinden wat je nodig hebt om hem te verbinden;
2. de ruwe bytes die zo'n sensor via **LoRaWAN** verstuurt met de hand decoderen, en dat controleren met de officiële decoder van de fabrikant;
3. live meekijken op een **MQTT**-broker en zelf een "virtuele sensor" laten publiceren;
4. echte klimaatsensoren in België uitlezen via **HTTP/JSON** en er de THI uit berekenen;
5. een virtuele ESP32 met temperatuur-/vochtsensor bouwen in de **Wokwi**-simulator.

---

## 1. Starten in GitHub Codespaces (aanbevolen)

1. Klik bovenaan op **Code ▸ Codespaces ▸ Create codespace on main**.
2. Wacht tot de omgeving klaar is (eerste keer 2–3 minuten; Python 3.12, Node.js en alle afhankelijkheden worden automatisch geïnstalleerd via `.devcontainer`).
3. Open de map `notebooks/` en begin met `00_start_hier.ipynb`.
4. De kernel **Python 3 (ipykernel)** staat automatisch geselecteerd.

> **Tip:** Een Codespace is een volledige VS Code-omgeving in je browser. Vergeet niet om je Codespace na de les te stoppen (**Code ▸ Codespaces ▸ ⋯ ▸ Stop**) om geen gratis uren te verbruiken.

---

## 2. Lokaal werken met Docker

Werk je liever lokaal met Docker? Dat kan op twee manieren:

### Optie A: Via Docker Compose (JupyterLab)
```bash
docker compose up
```
Open vervolgens `http://localhost:8888` in je browser om JupyterLab te openen.

### Optie B: Via VS Code Dev Containers
1. Installeer Docker Desktop en de **Dev Containers**-extensie in VS Code.
2. Open deze map in VS Code, druk op `F1` en kies **Dev Containers: Reopen in Container**.
3. VS Code bouwt de container op basis van `.devcontainer/devcontainer.json`.

---

## 3. Lokaal werken met Python (optioneel, zonder Docker)

```bash
git clone <deze-repo>
cd iot_practicum
pip install -r requirements.txt
jupyter lab
```

---

## Inhoud

| Bestand | Inhoud | Duur |
|---|---|---|
| `notebooks/00_start_hier.ipynb` | Omgeving testen, basisbegrippen, verbinding met de MQTT-broker controleren | 10 min |
| `notebooks/01_sensor_kiezen_en_verbinden.ipynb` | Antratek → Dragino-handleiding → checklist → LoRaWAN-payload byte voor byte decoderen → NB-IoT-variant en protocolkeuze | 45 min |
| `notebooks/02_mqtt_live_meekijken.ipynb` | Abonneren op een topic, publiceren, een virtuele S31-CB die Dragino-JSON streamt | 30 min |
| `notebooks/03_echte_sensoren_via_http.ipynb` | Sensor.Community en Open-Meteo via HTTP, pandas, THI | 30 min |
| `notebooks/04_wokwi_virtuele_sensor.ipynb` + `wokwi/` | ESP32 + DHT22 in de browser-simulator, publiceert naar de broker | 30 min |
| `docent/draaiboek.md` | Lesverloop, timing, oplossingen, valkuilen | — |
| `data/` | Reservekopieën van de Sensor.Community-data (19 okt. 2026) voor als de API niet bereikbaar is | — |

## Oplossingen in de notebooks

Elke opdracht heeft een oplossing in het notebook zelf. Die cellen dragen de celtag **`oplossing`**: tekstoplossingen staan in een inklapbaar blok (*Oplossing tonen*), code-oplossingen starten **ingeklapt** (klik op de cel of op het pijltje om de code te tonen). Ze blijven gewoon uitvoerbaar.

Wil je een studentenversie zonder oplossingen, dan verwijder je alle getagde cellen in één keer:

```bash
jupyter nbconvert --to notebook --TagRemovePreprocessor.enabled=True \
  --TagRemovePreprocessor.remove_cell_tags=oplossing \
  --output-dir studentenversie notebooks/*.ipynb
```

## Bronnen (geraadpleegd oktober 2026)

- Antratek Electronics (NL productpagina's): <https://www.antratek.be/lora/sensor-nodes/temperature-humidity>
- Dragino documentatiecentrum, S31-LB (LoRaWAN): <https://wiki.dragino.com/docs/LoRaWAN-End-Node/temperature-humidity-sensors/s31-lb/>
- Dragino documentatiecentrum, S31-CB (NB-IoT/LTE-M): <https://wiki.dragino.com/docs/NB-IoT/temperature-humidity-sensors/s31-cb/>
- Officiële payload-decoders van Dragino: <https://github.com/dragino/dragino-end-node-decoder>
- Publieke MQTT-brokers: test.mosquitto.org, broker.hivemq.com, broker.emqx.io
- Sensor.Community API: <https://data.sensor.community/>
- Open-Meteo API: <https://open-meteo.com/>
- Wokwi-simulator: <https://wokwi.com/> en <https://docs.wokwi.com/guides/esp32-wifi>

## Licentie

Lesmateriaal: CC BY-NC-SA 4.0. Code: MIT. Productnamen en handleidingen zijn eigendom van de respectieve fabrikanten; fragmenten worden geciteerd voor onderwijsdoeleinden.
