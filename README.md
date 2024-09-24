<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/fr/thumb/1/1d/Logo_T%C3%A9l%C3%A9com_SudParis.svg/153px-Logo_T%C3%A9l%C3%A9com_SudParis.svg.png" alt="TSP logo">
</p>


# CSC 8567 - Architectures distribuées et applications web

Auteurs : Timothée Mathubert, Gatien Roujanski, Arthur Jovart

## Emails

Lorsque vous envoyez un mail, pensez bien à mettre "CSC 8567" au début de l'objet !
- timothee.mathubert@telecom-sudparis.eu
- gatien.roujanski@telecom-sudparis.eu
- arthur.jovart@telecom-sudparis.eu

## Consignes

1. **Allez avant tout à la rubrique "Installation" ci-dessous pour installer ce dont vous aurez besoin pour le cours !**

2. Formez des groupes en trinômes, les plus hétérogènes possibles en niveau, et communiquez votre groupe à un enseignant.

3. **Ce cours est exclusivement un cours-projet : il n'y aura pas d'examen à la fin.** En revanche, il y aura deux rendus de projet (24 septembre et 21 novembre) ainsi qu'une soutenance à la fin du cours (21 novembre).

4. Vous pouvez faire le projet que vous souhaitez sous certaines conditions :
- **Vous devez disposer de deux applications Django**, une pour **un frontend** et l'autre pour **une API retournant des données au format JSON**. 
- Votre site web doit être accessible depuis votre interface loopback (sur l'IP 127.0.0.1) de votre PC, et contenir au moins deux pages : une pour faire des requêtes à l'API, l'autre pour afficher une liste d'objets.
- **Votre site doit utiliser une base de données non locale (pas de fichier).** Celle-ci doit contenir un schéma relationnel de données similaire à celui ci-dessous :

<p align="center">
    <img src="https://github.com/user-attachments/assets/4cd224f5-5f64-48b7-bd6f-c25f301275ca" alt="BDD">
</p>

- Pour le rendu du 24 septembre, vous devez déployer une infrastructure similaire à celle ci-dessous en utilisant un fichier `docker-compose.yml` et des Dockerfiles. **L'application Django de l'API et du frontend devront être placées dans deux conteneurs différents. La base de données et le proxy seront dans deux conteneurs différents.**

<p align="center">
    <img src="https://github.com/user-attachments/assets/877dfc8f-ae0b-41e0-a934-19480d839d0c" alt="Infra à reproduire">
</p>

- Pour vous aider tout au long du projet, __**consultez ces différentes pages de documentation et demandez de l'aide aux enseignants**__ :
    - Django : https://docs.djangoproject.com/en/5.1/
    - Docker : https://docs.docker.com/manuals/ 
    - Kubernetes (rendu final seulement) : https://kubernetes.io/fr/docs/home/
    - Nginx (Proxy) : https://nginx.org/en/docs/
- *Vous pouvez ajouter des applications, ajouter de la forme (Styles CSS, Bootstrap, Bulma) et des pages supplémentaires si vous le souhaitez.*
- Les consignes pour le rendu final avec Kubernetes vous seront communiquées après le rendu du CC Django + Docker.


## Installation

**Il est recommandé d'utiliser un système d'exploitation type Linux.**
L'installation suivante fonctionne sous Ubuntu. En fonction de votre OS, il est possible qu'apt ne soit pas le gestionnaire de paquets. Remplacez simplement apt dans les commandes suivantes par votre gestionnaire de paquets.

1. Créez votre propre répo de groupe en cliquant sur "Use this template"
   
2. Créer un environnement virtuel Python avec Pyenv (non nécessaire si vous avez déjà un gestionnaires d'environnements virtuels pour Python)
```
sudo apt update -y
sudo apt install python pip
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
curl https://pyenv.run | bash
```
Si vous utilisez Bash comme exécuteur de commande dans votre Shell :
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```
Si vous utilisez autre chose, allez voir la [documentation Pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#set-up-your-shell-environment-for-pyenv).

Ensuite :
```
pyenv install 3.12
```
3. Installer les dépendances utiles
```
pip install django psycopg2-binary
```
4. Créer le projet Django & vérifier qu'il tourne correctement
```
cd django-site
django-admin startproject [nom-de-votre-projet] <-- A REMPLACER
python manage.py runserver
```
Allez sur 127.0.0.1:8000 sur un navigateur. Si une page "Congratulations!" s'affiche, c'est que tout fonctionne bien !

5. Créer les applications utiles
```
python manage.py startapp public
python manage.py startapp api
```

6. Installer Docker
```
sudo apt install docker
docker -v
```
Si la dernière commande vous affiche la version de Docker, c'est qu'il est correctement installé.

7. Créer un compte Docker Hub

Allez sur https://hub.docker.com et créez vous un compte.

8. Installer kubectl
```
sudo apt install kubectl
```

Et c'est parti !




Q1 : Vous disposez d'un projet Django dans lequel une application public a été créée. Décrivez la suite de requêtes et d'exécutions permettant l'affichage d'une page HTML index.html à l'URL global / via une application public, ne nécessitant pas de contexte de données. Vous décrirez la position exacte dans l'arborescence des répertoires des différents fichiers utiles à cette exécution.

Réponse : 
Voici les différentes étapes : 

Création de la vue public 
Dans le répertoir CSC8567-Proj/django-site/projet/public
Ajouter les lignes dans le fichier views.py : 
	from django.shortcuts import render
	def vue(request):
return render(request, 'public/templates/index.html')	

Configuration de l’url dans public
Dans le répertoir CSC8567-Proj/django-site/projet/public

Ajouter dans “urlpatterns” la ligne dans le fichier urls.py de projet:
path(‘ ‘, views.vue, name='vue')

Configuration de l’url dans le projet
Dans le répertoir CSC8567-Proj/django-site/projet/projet
Ajouter dans “urlpatterns” la ligne dans le fichier urls.py du projet: 
path(' ', include("public.urls")) 


Création de la page index.html
Dans le répertoir CSC8567-Proj/django-site/projet/public
Créer le répertoire “ templates”
Dans ce répertoire, créer le fichier “index.html” et le compléter

Lancement du server
Taper la commande : “ python manage.py runserver ” dans un terminal dans le répertoir CSC8567-Proj/django-site/projet



Q2: Dans quelle(s) section(s) de quel(s) fichier(s) peut-on configurer la base de données que l'on souhaite utiliser pour un projet Django ?

Réponse : 
On peut configurer la base de donnée que l’on souhaite utiliser dans le fichier “settings.py” présent dans le répertoire  CSC8567-Proj/django-site/projet/projet


Q3: Dans quel(s) fichier(s) peut-on configurer le fichier de paramètres que l'on souhaite faire utiliser par le projet Django ? Si plusieurs fichiers sont à mentionner, expliquez le rôle de chaque fichier.
Réponse : 
On peut configurer le fichier de paramètres que l'on souhaite faire utiliser par le projet Django dans le fichier  “manage.py” (qui est utiliser pour lancer le serveur par exemple), “asgi.py”et “wsgi.py”. Ces deux fichiers servent au déploiement de l’application Django sur des serveur web
 
Q4:  Nous nous plaçons à la racine de votre projet Django. Quel effet a l'exécution python manage.py makemigrations ? Et l'exécution python manage.py migrate ? Quel(s) fichier(s) sont mis en oeuvre pendant ces exécutions ?
Réponse : 
“python manage.py makemigrations” affiche les migrations de base de données qui seront faites
“python manage.py migrate” effectue les migrations de base de données

Les fichiers mis en oeuvre seront créés dans un dossier appelé “migrations”

Q5: Expliquez l'effet et la syntaxe de ces commandes, communément vues dans des fichiers Dockerfile : FROM, RUN, WORKDIR, EXPOSE, CMD 

Réponse:
FROM: Spécifie l’image sur laquelle l'image Docker sera construite
RUN: Lance une commande
WORKDIR: Définit le répertoire de travail dans le conteneur
EXPOSE: Indique à Docker le port à utiliser pour le conteneur
CMD: Spécifie la commande par défaut à lancer dans le conteneur

Q6: Dans la définition d'un service dans le fichier docker-compose.yml, expliquez l'effet des mentions :

ports:
    - "80:80"
Réponse:
Elle sert à mapper des ports entre le conteneur et la machine “physique”

build: 
   		context: .
    	dockerfile: Dockerfile.api
Réponse:
Indique que le service doit être construit à partir d’une image Docker (définie par Dockerfile.api)




depends_on:
   		 - web
    	- api
Réponse:
Indique que le service dépend des services nommés “web” et “api”

environment:
  		POSTGRES_DB: ${POSTGRES_DB}
    		POSTGRES_USER: ${POSTGRES_USER}
    		POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
Réponse:
Spécifie la base de donnée externe à utiliser pour la ou les applications Django ainsi que comment l’atteindre (via un user et un mot de passe). Des variables d’environnement sont ici utilisées

Q7: Citez une méthode pour définir des variables d'environnement dans un conteneur.

Réponse:
Il est possible de les spécifier dans le fichier “docker-compose.yml”. Par exemple :              

environment:
      		- POSTGRES_USER=django
      		- POSTGRES_PASSWORD=django
      		- POSTGRES_DB=cj_proj


Q8: Dans un même réseau Docker, nous disposons d'un conteneur nginx (utilisant l'image nginx:latest) et d'un conteneur web (utilisant une image contenant un projet web Django, ayant la commande python manage.py runserver 0.0.0.0:8000 de lancée au démarrage du conteneur). Comment adresser le serveur web tournant dans le conteneur web depuis le conteneur nginx, sans utiliser les adresses IP des conteneurs ?

Réponse:
Tout d’abord, il faut ajouter dans le fichier “docker-compose.yml” les lignes suivantes : 

version: '3.9'
volumes:
  volume-pgdata:

services:
  nginx:
    image: nginx:alpine
    ports:
      - 80:80
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf:ro
    depends_on:
      - web
    networks:
      cj:
  web:
    command: python manage.py runserver 0.0.0.0:8000
    expose:
      - "8000"
    networks:
      - web

Puis dans le fichier nginx.conf : 

server {
    listen 80 default_server;
    
    location /web/ {
        proxy_pass http://public:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}



