Crous Alerts Bot

Un petit script Python qui vérifie régulièrement la disponibilité des logements CROUS pour une ville donnée, et envoie une alerte via un bot Telegram. L'exécution est automatisée grâce à GitHub Actions.

🛠️ Prérequis

Un bot Telegram (créé via BotFather)

Un ID de chat Telegram

⚙️ Mise en place
1. Créer un bot Telegram
   
Ouvre une conversation avec @BotFather

Envoie la commande /newbot

Suis les instructions (nom, username…)

Copie le token généré

2. Obtenir ton TELEGRAM_CHAT_ID
   
Démarre une conversation avec ton bot

Envoie un message au bot, puis visite cette URL (en remplaçant <YOUR_BOT_TOKEN>) :
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates : tu verras ton chat_id dans la réponse JSON

3. Modifie la ville cible dans le script alert.py.

4. Ajouter les secrets à GitHub
Dans ton dépôt GitHub :

Settings → Secrets and variables → Actions → New repository secret

Ajoute :

TELEGRAM_BOT_TOKEN → ton token BotFather

TELEGRAM_CHAT_ID → ton ID de chat Telegram

5. Lancer le workflow
Le workflow GitHub Actions est défini dans .github/workflows/alert.yaml

Tu peux le démarrer manuellement la première fois (onglet "Actions" → "Run workflow")

Ensuite, il s'exécutera automatiquement chaque 5min (tu peux le changer dans alert.yaml)
