# Virtuele stalsensor: ESP32 + DHT22 in de Wokwi-simulator, publiceert via MQTT
# in een JSON-formaat dat lijkt op dat van de Dragino S31-CB (zie notebook 01, stap 4).
#
# Pas enkel de drie regels onder INSTELLINGEN aan.

import network, time, json, machine, dht
from umqtt.simple import MQTTClient

# ---------- INSTELLINGEN ----------
KLASCODE  = "i700301-2026-xyz"      # dezelfde code als in de notebooks (docent geeft ze)
AFDELING  = "wokwi-groep01"         # jouw groepsnaam, uniek in de klas
INTERVAL  = 5                       # seconden tussen twee uplinks (echt toestel: 600)
# ----------------------------------

BROKER = "broker.hivemq.com"
TOPIC  = "ugent/{}/stal/{}".format(KLASCODE, AFDELING)
IMEI   = "8685080656" + "{:05d}".format(sum(ord(c) for c in AFDELING) % 100000)

# 1. Wifi: Wokwi simuleert een open netwerk "Wokwi-GUEST" met internettoegang
print("Verbinden met wifi", end="")
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Wokwi-GUEST", "")
while not wlan.isconnected():
    print(".", end="")
    time.sleep(0.3)
print(" ok, IP-adres:", wlan.ifconfig()[0])

# Klok gelijkzetten via NTP (zoals een LoRaWAN-server dat doet bij de join); mislukt het, dan loopt de klok vanaf 2000
try:
    import ntptime
    ntptime.settime()
    print("Klok gelijkgezet (UTC):", time.localtime()[:6])
except Exception as e:
    print("NTP mislukt:", e)

# 2. Sensor: DHT22 op pin 15 (zie diagram.json)
sensor = dht.DHT22(machine.Pin(15))

# 3. MQTT: één uitgaande verbinding naar de broker
client = MQTTClient(client_id="esp32-" + AFDELING, server=BROKER, port=1883, keepalive=60)
client.connect()
print("Verbonden met MQTT-broker", BROKER, "-> topic", TOPIC)

teller = 0
batterij = 3.60
while True:
    sensor.measure()
    T, RV = sensor.temperature(), sensor.humidity()
    teller += 1
    batterij = max(batterij - 0.001, 2.6)          # 'ontlaadt' langzaam, zoals een echt toestel
    jaar, maand, dag, uur, minuut, sec, _, _ = time.localtime()
    bericht = {
        "IMEI": IMEI, "Model": "S31x-CB (Wokwi)",
        "temperature": round(T, 1), "humidity": round(RV, 1),
        "interrupt": 1 if (T >= 30 or RV >= 90) else 0,     # alarmvlag zoals bij Dragino
        "interrupt_level": 0, "count": teller,
        "battery": round(batterij, 2), "signal": 20,
        "time": "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(jaar, maand, dag, uur, minuut, sec),
    }
    client.publish(TOPIC, json.dumps(bericht), qos=0)
    print("uplink", teller, "->", bericht["temperature"], "C /", bericht["humidity"], "%",
          "ALARM" if bericht["interrupt"] else "")
    time.sleep(INTERVAL)
