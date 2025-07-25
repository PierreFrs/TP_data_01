# TP : Système de Sauvegarde et d'Analyse Automatisé

## **Contexte**

Vous travaillez pour une petite entreprise qui génère quotidiennement des fichiers de données (logs, rapports, exports). Il faut automatiser la sauvegarde de ces fichiers et générer des rapports simples d'activité.

## **Objectifs**

Créer un système qui :

- Surveille un répertoire de travail
- Sauvegarde automatiquement les nouveaux fichiers
- Analyse le contenu des fichiers texte/CSV
- Génère des rapports simples
- Nettoie les anciens fichiers

## **Structure Simplifiée**

```markdown
backup_project/
├── data/
│   ├── work/           # Répertoire surveillé
│   ├── backup/         # Sauvegardes
│   └── reports/        # Rapports générés
├── scripts/
│   ├── backup.sh       # Script principal
│   └── analyze.py      # Analyse simple
│   └── watch.sh        # Surveille un répertoire de travail
│   └── daily_report.py # Génère des rapports simples
│   └── install.sh      # initialise le fonctionement
├── logs/              # Journaux
└── config.txt         # Configuration simple
```

- **Phase 1** : Script de Sauvegarde **(backup.sh)**
>
>- Script de sauvegarde automatique : copie les fichiers avec horodatage, analyse les .csv/.txt, archive les originaux, nettoie les vieux backups et log tout.

- **Phase 2** : Analyseur Python **(analyze.py)**
>
>- Ce script Python analyse un fichier CSV ou TXT, extrait des statistiques (lignes, mots, colonnes, mots fréquents...), puis génère deux rapports (au format JSON et HTML) dans un dossier spécifié.

- **Phase 3** : Script de Surveillance Continue **(watch.sh)**
>
>- Ce script Bash surveille en boucle le dossier data/work toutes les 30 secondes.
S’il détecte des fichiers, il lance automatiquement le script de sauvegarde (backup.sh), sinon il attend.

- **Phase 4** : Générateur de Rapport Quotidien **(daily_report.py)**
>
>- Ce script Python génère un rapport HTML quotidien résumant l'activité de traitement de fichiers (CSV et TXT) dans un dossier donné. Il compte les fichiers, extrait certaines statistiques (lignes, mots) et liste les détails des fichiers analysés

- **Phase 5** : Script d'installation **(install.sh)**
>
>- Ce script installe le système de sauvegarde :
il crée les dossiers nécessaires, donne les droits d’exécution aux scripts, vérifie Python3, génère des fichiers de test (CSV et TXT), puis affiche les commandes pour démarrer.
