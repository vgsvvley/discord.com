from flask import Flask, request, redirect
import datetime
import uuid

app = Flask(__name__)

# ================== CONFIGURATION ==================
# Mets ici ton vrai lien d'invitation Discord (ex: https://discord.gg/abc123)
DISCORD_INVITE_URL = "https://discord.gg/TA_CODE_DE_TON_INVITE"

# Pour rendre le lien unique (optionnel mais recommandé)
@app.route('/invite/<invite_code>')
def track_invite(invite_code):
    # Récupération des informations du visiteur
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Inconnu')
    referer = request.headers.get('Referer', 'Direct')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    unique_id = str(uuid.uuid4())[:8]  # ID unique court pour chaque clic

    # Affichage dans la console (tu verras ça quand quelqu'un clique)
    print("=" * 70)
    print(f"[{timestamp}] NOUVEL CLIC SUR L'INVITATION !")
    print(f"Code d'invite utilisé : {invite_code}")
    print(f"ID unique          : {unique_id}")
    print(f"Adresse IP          : {ip}")
    print(f"Navigateur/Appareil : {user_agent}")
    print(f"Provenance (Referer): {referer}")
    print("=" * 70)

    # Ici tu pourras plus tard ajouter une sauvegarde dans SQLite ou un fichier

    # Redirection vers le vrai lien Discord
    return redirect(DISCORD_INVITE_URL, code=302)


# Route principale (optionnelle - page d'accueil)
@app.route('/')
def home():
    return """
    <h1>Tracker d'invitation Discord</h1>
    <p>Utilise le lien : <strong>https://ton-domaine.com/invite/abc123</strong></p>
    """


if __name__ == '__main__':
    print("🚀 Serveur de tracking d'invitation Discord démarré !")
    print("Utilise Ctrl + C pour arrêter")
    app.run(host='0.0.0.0', port=5000, debug=True)