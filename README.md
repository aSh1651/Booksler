# Booksler

<<<<<<< HEAD
Welcome to Codespaces! You are on our default image. 
   - It includes runtimes and tools for Python, Node.js, Docker, and more. See the full list here: https://aka.ms/ghcs-default-image
   - Want to use a custom image instead? Learn more here: https://aka.ms/configure-codespace

🔍 To explore VS Code to its fullest, search using the Command Palette (Cmd/Ctrl + Shift + P or F1).

📝 Edit away, run your app as usual, and we'll automatically make it available for you to access.
=======
# moi
platform promoted by booktokers or books related influencers to their own community for them to connect within the community and with the admin= the influencere.
first aspect: a book with the photo of profile of the influencer you can open it with a button like botom rigth of the book  then the book opens summary appears 1 current reads 2 past reads and just that 

# ia
Cahier des Charges : OpenBook Connect
Concept principal :
Une plateforme sociale dédiée aux lecteurs et aux communautés littéraires (type BookTok), permettant de journaliser ses lectures sous la forme d'un carnet virtuel et de créer des espaces d'échanges privés ou publics.

Fonctionnalités clés (MVP - Minimum Viable Product) :

Journal de lecture visuel (Le "Livre Ouvert") : Une interface utilisateur simulant un livre. Sur la page de gauche : la couverture du livre (récupérée automatiquement via API) et ses métadonnées. Sur la page de droite : la critique, la note et l'avis de l'utilisateur.

Intégration API : Un moteur de recherche connecté à l'API publique de Google Books pour que l'utilisateur n'ait pas à saisir manuellement l'auteur ou à télécharger la couverture.

Système d'authentification : Création de comptes utilisateurs (profils lecteurs et profils "Créateurs/Booktokeurs").

Clubs de lecture / Groupes de discussion : Espaces (salons ou fils de commentaires) créés par un influenceur où seuls ses abonnés peuvent interagir et débattre du livre du mois.

Architecture Technique (Ta future stack sur le CV)
Pour réaliser cette vision, voici les technologies que tu vas devoir utiliser et apprendre au fil de l'eau :

Backend (Le moteur) : Python avec le framework Django. Django est parfait pour cela. C'est le framework avec lequel Instagram ou Pinterest ont démarré. Il gère automatiquement la création d'utilisateurs, les mots de passe et les bases de données.

Base de données : SQLite (intégrée par défaut dans Python) pour gérer les relations complexes : Un utilisateur appartient à un groupe, un groupe possède plusieurs messages, un utilisateur possède plusieurs critiques de livres.

Frontend (Le visuel "Livre ouvert") : HTML et CSS. C'est ici que tu créeras l'animation et le design des deux pages côte à côte. Tu utiliseras le moteur de "templates" de Django pour injecter tes données Python directement dans ton design web.

La Feuille de Route (Roadmap en 5 Étapes)
C'est un gros projet. Pour ne pas te noyer, l'ingénierie logicielle impose de découper le travail en "sprints" (étapes de développement). Tu ne passes à l'étape suivante que lorsque la précédente fonctionne parfaitement.

Étape 1 : Le cœur de données (API Google Books)
Objectif : Créer un script Python autonome qui recherche un livre et télécharge ses informations.

Livrable : Un fichier Python où tu tapes un titre dans la console, et qui te renvoie l'URL de la couverture de l'image, le titre exact et l'auteur.

Étape 2 : L'initialisation du framework Django
Objectif : Configurer l'environnement web.

Livrable : Installer Django, créer le projet, et réussir à afficher une simple page blanche sur ton navigateur web local affichant "Bienvenue sur OpenBook".

Étape 3 : La Base de données et l'Interface "Livre Ouvert"
Objectif : Connecter la logique visuelle et le stockage.

Livrable : Créer tes modèles de données (Table "Livre", Table "Critique"). Développer le design HTML/CSS avec l'esthétique du livre ouvert (un grand conteneur séparé en deux colonnes), et afficher une critique de test enregistrée dans ta base.

Étape 4 : Le système social (Comptes et Groupes)
Objectif : Rendre l'application multi-utilisateurs.

Livrable : Activer le système de connexion/inscription de Django. Créer la fonctionnalité permettant à un utilisateur de créer un "Groupe", à d'autres de le rejoindre, et d'y poster des messages liés à un livre.

Étape 5 : Le déploiement (Mise en ligne)
Objectif : Rendre ton site accessible au monde entier (et aux recruteurs).

Livrable : Héberger ton code sur GitHub, puis utiliser un service gratuit comme Render ou PythonAnywhere (ou Microsoft Azure, si tu veux valider tes acquis) pour que ton site ait une vraie URL (ex: openbook-connect.onrender.com).
>>>>>>> b4ff38b8800a6a99ebd977460d3318e46a6a0a80


<img width="2374" height="1394" alt="image" src="https://github.com/user-attachments/assets/a855a145-6ac0-49f3-8378-a470869ccb30" />
