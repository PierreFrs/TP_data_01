echo "=== Instalation du systeme de sauvegarde de fichiers ==="

mkdir -p data/{work,backup,reports} logs 

chmod +x scripts/*.sh scripts/*.py

if ! python3 -c "import json, os, sys" 2>/dev/null; then
    echo "Python3 requis"
    exit  1
fi

echo "📄 Création de fichiers de test..."

# Fichier CSV de test
cat > data/work/ventes_test.csv << 'EOF'
date,produit,quantite,prix
2024-01-15,Produit_A,10,25.50
2024-01-15,Produit_B,5,15.00
2024-01-16,Produit_A,8,25.50
2024-01-16,Produit_C,12,35.75
EOF

# Fichier TXT de test  
cat > data/work/log_test.txt << 'EOF'
Rapport d'activité du serveur
============================

Le serveur a fonctionné correctement aujourd'hui.
Aucune erreur critique détectée.
Performances optimales maintenues.

Statistiques:
- Requêtes traitées: 1250
- Temps de réponse moyen: 45ms
- Erreurs: 0

Le système fonctionne parfaitement.
Maintenance programmée demain.
EOF

echo "Installation terminée"
echo ""
echo "Pour commencer :"
echo "1. ./scripts/backup.sh pour une sauvegarde ponctuelle"
echo "2. ./scripts/watch.sh pour lancer la surveillance du dossier work"
echo "3. python scripts/daily_report.py pour un rapport quotidien"

