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
Mot de passe faible 🟠
Résultat :
```bash
python3 password_analyzer.py "spongebob123"
```

<img width="770" height="503" alt="image" src="https://github.com/user-attachments/assets/18c934b7-ecff-4793-affa-311105a4699d" />

Mot de passe fort 🟢
Resultat:
``` bash
 password_analyzer.py "SpØngBØb!C#246"
```
<img width="783" height="503" alt="image" src="https://github.com/user-attachments/assets/3730f20a-03d3-4135-ab7b-909ca34b7ef1" />

## 🎯 Critères de notation

### Longueur du mot de passe :
- 12+ caractères : 40 points
- 8-11 caractères : 25 points  
- Moins de 8 caractères : 10 points

### Complexité :
- Majuscules (A-Z) : 15 points
- Minuscules (a-z) : 15 points
- Chiffres (0-9) : 15 points
- Symboles (!@#$%...) : 15 points

### Niveaux de sécurité
- 🟢 **80-100 points** : Mot de passe FORT
- 🟡 **60-79 points** : Mot de passe MOYEN
- 🟠 **40-59 points** : Mot de passe FAIBLE
- 🔴 **0-39 points** : Mot de passe TRÈS FAIBLE

### 💡 Bonnes pratiques
- ✅ Utilisez au minimum 12 caractères
- ✅ Mélangez majuscules, minuscules, chiffres et symboles
- ✅ Évitez les mots du dictionnaire et informations personnelles
- ✅ Activez l'authentification à deux facteurs (2FA)
- ✅ Un mot de passe unique par compte
