## 🔐 Password Strength Analyzer
Un outil simple pour analyser la force d'un mot de passe et obtenir des recommandations personnalisées.

## 📋 Description
Cet analyseur évalue la sécurité d'un mot de passe selon plusieurs critères:
- Detection des mots de passe courants
- La longeur (minimum 12 caractères)
- Majucules (A-Z)
- Minuscules (a-z)
- Chiffres (0-9)
- Symboles (!éç&à"-)
  
Le script attribu un score sur 100 et fourit des conseils pour améliorer les securité.
##  📱Installation:
cloner le repository (aucune dépendance requise python 3 uniquement)
```bash
git clone https://github.com/SOYA6A/password-strength-analyzer.git
cd password-strength-analyzer
```

💻 Utilisation
Méthode simple
```bash
python3 password_analyzer.py "MonMotsDePa$$£123"
```
Mode interactif
```
python3 password_analyzer.py
```
Le script vous demandera d'entrer un mot de passe.

## 📊 Exemples d'utilisation
Mot de passe faible
Résultat :
```bash
python3 password_analyzer.py "spongebob123"
```

<img width="770" height="503" alt="image" src="https://github.com/user-attachments/assets/18c934b7-ecff-4793-affa-311105a4699d" />
