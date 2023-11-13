# Utilisez l'image Python 3.8 en tant qu'image de base
FROM python:3.8

# Définissez le répertoire de travail à /app
#WORKDIR /voting-app/azure-vote

# Copiez le fichier requirements.txt dans le conteneur
COPY azure-vote /app

# Installez les dépendances Python
RUN pip install -r  /app/requirements.txt


# Copiez le reste du code source dans le conteneur
COPY . .
EXPOSE 80

# Exécutez l'application Python
CMD ["python", "/app/main.py"]

