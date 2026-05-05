import paho.mqtt.client as mqtt
import requests
import json
import ssl

# --- CONFIGURATION HIVEMQ ---
BROKER = "c69c5ab4c09848f88fe18d9374121871.s1.eu.hivemq.cloud"
PORT = 8883
USER = "davincii5"
PASS = "Davincii123456"
TOPIC = "sirh/attendance"

# --- CONFIGURATION API DJANGO ---
DJANGO_API_URL = "http://127.0.0.1:8000/api/attendance/iot/upload/"
API_KEY = "SMART_ENTERPRISE_KEY_2026"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connecté à HiveMQ Cloud avec succès !")
        client.subscribe(TOPIC)
        print(f"📡 En écoute sur le topic : {TOPIC}\n")
    else:
        print(f"❌ Échec de la connexion, code d'erreur : {rc}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8')
    print(f"📥 Nouveau pointage détecté : {payload}")
    
    try:
        raw_data = json.loads(payload)
        
        # --- CORRECTION ICI ---
        # On transforme les données pour qu'elles correspondent à ton Serializer
        # On envoie 'matricule' dans le champ 'employe'
        formatted_data = {
            "employe": raw_data.get("matricule"), 
            "id_capteur": raw_data.get("id_capteur"),
            "timestamp": raw_data.get("timestamp"),
            "type_pointage": raw_data.get("type_pointage"),
            "est_justifie": raw_data.get("est_justifie", False)
        }
        
        headers = {
            'X-IoT-Key': API_KEY,
            'Content-Type': 'application/json'
        }
        
        # On envoie formatted_data au lieu de raw_data
        response = requests.post(DJANGO_API_URL, json=formatted_data, headers=headers)
        
        if response.status_code == 201:
            print("🟢 Succès : Pointage inséré dans la base de données Django !\n")
        else:
            print(f"🔴 Erreur Django ({response.status_code}) : {response.text}\n")
            
    except json.JSONDecodeError:
        print("⚠️ Erreur : Le message reçu n'est pas un JSON valide.\n")
    except requests.exceptions.ConnectionError:
        print("⚠️ Erreur : Impossible de contacter Django. Le serveur (runserver) est-il allumé ?\n")

# --- INITIALISATION DU CLIENT ---
# Utilisation de la version 2 du protocole Callback pour éviter le DeprecationWarning
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1, client_id="Bridge_SIRH_Python")

client.tls_set(tls_version=ssl.PROTOCOL_TLS)
client.username_pw_set(USER, PASS)

client.on_connect = on_connect
client.on_message = on_message

print("⏳ Lancement du Bridge IoT...")
print("Tentative de connexion vers le cluster HiveMQ...")

client.connect(BROKER, PORT, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\n🛑 Arrêt manuel du Bridge.")