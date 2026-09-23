import re # regex pour enlever les espaces et les caractères spéciaux
import requests
from bs4 import BeautifulSoup

# dans cette partie on va chercher à récupérer toutes les pages de l'annuaire des avocats du barreau de Nice
# tout dans une fonction get_all_pages() qui va retourner une liste de toutes les urls des pages de l'annuaire

# r = requests.get("https://www.barreaudenice.com/fr/annuaire")
# print(r.status_code)
def get_all_pages():
    urls = []
    page_number = 1
    
    for i in range(127):
        i = f"https://www.barreaudenice.com/fr/annuaire?page={page_number}"
        # on a utiliser f-string pour mettre la variable page_number dans l'url
        
        page_number += 1
        urls.append(i) # on ajoute l'url à la liste urls
        
    return urls
        
def parse_avocat(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    
    avocats = soup.find_all("div", class_="js-annuaire-contents")
    # on récupère tous les avocats de la page 1 de l'annuaire
    for avocat in avocats:
        try:
            nom = avocat.find("h2").text.strip() # .strip() permet de supprimer les espaces avant et après le texte
        except AttributeError as e:
            nom = ""
        # on récupère le nom de l'avocat
        info = avocat.find("p").text.strip() # on récupère l'adresse de l'avocat
        try:
            info_finale = re.sub(r'\s+', ' ', info) # on enlève les espaces et les caractères spéciaux de l'adresse
        except AttributeError as e:
            info_finale = ""
        #print(info_finale)
        try:
            email = avocat.find("a", href=re.compile(r"mailto:")).text.strip() # on récupère l'email de l'avocat
        except AttributeError as e:
            email = ""
        # print(email)
        
        
        chemin = r"C:\Users\YOGA\Documents\MES_PROJETS\Mes_projets_2026\ws_project\annuaire_avocat.txt"
        with open(chemin, "a", encoding="utf-8") as f:
            f.write(f"{nom}\n")
            f.write(f"{info_finale}\n")
            f.write(f"{email}\n\n")
# ici on a créer un fichier texte annuaire_avocat.txt dans lequel on va stocker les informations des avocats
def parese_all_avocats():
    pages = get_all_pages()
    for page in pages:
        parse_avocat(url=page)
        print(f"On scrape {page} avec succès !")
        
parese_all_avocats()
# ici on a créé une fonction parse_all_avocats() qui va parcourir toutes les pages de l'annuaire et appeler la fonction parse_avocat() pour chaque page.