# ⚖️ Annuaire des Avocats du Barreau de Nice — Scraper

Un scraper Python qui parcourt l'annuaire officiel des avocats du **Barreau de Nice**
et exporte les informations de chaque avocat (nom, adresse, email) dans un fichier texte.

## 📋 Description

Le script parcourt les **127 pages** de l'annuaire [`barreaudenice.com`](https://www.barreaudenice.com/fr/annuaire)
et extrait pour chaque avocat :

- 🧑‍⚖️ **Nom**
- 📍 **Adresse** (adresse + code postal + ville)
- 📧 **Email** (si disponible)

Les résultats sont enregistrés dans un fichier `annuaire_avocat.txt`.

## 🚀 Installation

### Prérequis

- Python 3.8 ou supérieur
- pip

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/[ton-user]/annuaire-avocat-nice.git
cd annuaire-avocat-nice

# 2. (Optionnel) Créer un environnement virtuel
python -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate       # Windows

# 3. Installer les dépendances
pip install -r requirements.txt
```

## 🧑‍💻 Utilisation

```bash
python annuaire_avocat.py
```

Le script va :

1. Générer la liste des URLs de toutes les pages de l'annuaire
2. Parcourir chaque page et extraire les infos de chaque avocat
3. Écrire les résultats dans `annuaire_avocat.txt`

### ⚙️ Configuration du chemin de sortie

Le chemin de sortie est défini dans `annuaire_avocat.py` :

```python
chemin = r"C:\Users\YOGA\Documents\MES_PROJETS\Mes_projets_2026\ws_project\annuaire_avocat.txt"
```

⚠️ **Pense à le modifier** pour l'adapter à ta machine, ou utilise un chemin relatif :

```python
chemin = "annuaire_avocat.txt"
```

## 📄 Format de sortie

Le fichier `annuaire_avocat.txt` contient un bloc par avocat :

```
ABASSIT Florian
2 avenue Georges Clémenceau 06000 NICE
contact@exemple.fr

DUPONT Marie
12 rue de la Paix 06000 NICE
marie.dupont@avocat.fr
```

## 🛠️ Stack technique

- [Python 3](https://www.python.org/)
- [Requests](https://requests.readthedocs.io/) — requêtes HTTP
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) — parsing HTML
- [re](https://docs.python.org/3/library/re.html) — expressions régulières

## ⚠️ Avertissement légal

Ce projet est destiné à un **usage éducatif et personnel**.
Les données scrapées sont publiques (annuaire officiel du Barreau de Nice).
Merci de respecter :

- Les [conditions d'utilisation](https://www.barreaudenice.com/) du site
- Le RGPD pour toute réutilisation des données personnelles
- Un rythme de requêtes raisonnable (le script gagnerait à ajouter un `time.sleep()` entre les pages)

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésite pas à :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit (`git commit -m 'Ajout fonctionnalité X'`)
4. Push (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

## 📝 License

Ce projet est sous licence MIT — voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👤 Auteur

**[Sidi Mohamed SANOU/ SidiMohamedS]**

- GitHub : [@SidiMohamedS](https://github.com/SidiMohamedSr)