import requests
from collections import defaultdict

USERNAME = "Mikhail-Kuri"

url = f"https://api.github.com/users/{USERNAME}/events/public"

response = requests.get(url)
events = response.json()

print("\n📊 GITHUB DASHBOARD\n")
print(f"Utilisateur: {USERNAME}\n")

stats = defaultdict(int)

for event in events:
    event_type = event["type"]
    stats[event_type] += 1

print("📌 Résumé des activités récentes:\n")

for event_type, count in stats.items():
    print(f"- {event_type}: {count}")

print("\n🕒 Derniers événements:\n")

for event in events[:10]:
    print(f"- {event['type']} sur {event['repo']['name']}")