"""
Password Strength Analyzer
Auteur: ME SOYA6A
Description: Analyse la force d'un mot de passe et donne des conseils
"""

import sys  # Pour récupérer ce que l'utilisateur tape en ligne de commande

def analyser_password(password):
    """
    Cette fonction analyse un mot de passe et lui donne un score
    """
    # Je commence avec un score à 0
    score = 0

    # Je vais stocker tous mes commentaires ici
    conseils = []
    
     # ========== VÉRIFICATION 1 : LA LONGUEUR ==========
    # Je compte combien de caractères il y a
    longueur = len(password)
    
    # Si le mot de passe est long (12+ caractères) : super !
    if longueur >= 12:
        score = score + 40  # J'ajoute 40 points
        conseils.append("✅ Longueur excellente (12+ caractères)")
    
    # Si entre 8 et 11 caractères : correct mais peut mieux faire
    elif longueur >= 8:
        score = score + 25  # J'ajoute 25 points
        conseils.append("🟡 Longueur correcte, mais essayez 12+ caractères")
    
    # Si moins de 8 caractères : trop court !
    else:
        score = score + 10  # J'ajoute quand même 10 points
        conseils.append("❌ Trop court ! Utilisez au moins 12 caractères")
        
        # ========== VÉRIFICATION 2 : LES MAJUSCULES ==========
    # Je vérifie s'il y a au moins une majuscule (A, B, C, etc.)
    a_des_majuscules = False
    for caractere in password:
        if caractere.isupper():  # isupper() vérifie si c'est une majuscule
            a_des_majuscules = True
            break  # J'arrête de chercher, j'en ai trouvé une
    
    if a_des_majuscules:
        score = score + 15
        conseils.append("✅ Contient des majuscules")
    else:
        conseils.append("❌ Ajoutez des majuscules (A-Z)")

        # ========== VÉRIFICATION 3 : LES MINUSCULES ==========
    # Pareil mais pour les minuscules (a, b, c, etc.)
    a_des_minuscules = False
    for caractere in password:
        if caractere.islower():  # islower() vérifie si c'est une minuscule
            a_des_minuscules = True
            break
    
    if a_des_minuscules:
        score = score + 15
        conseils.append("✅ Contient des minuscules")
    else:
        conseils.append("❌ Ajoutez des minuscules (a-z)")

        # ========== VÉRIFICATION 4 : LES CHIFFRES ==========
    # Je vérifie s'il y a au moins un chiffre (0, 1, 2, etc.)
    a_des_chiffres = False
    for caractere in password:
        if caractere.isdigit():  # isdigit() vérifie si c'est un chiffre
            a_des_chiffres = True
            break
    
    if a_des_chiffres:
        score = score + 15
        conseils.append("✅ Contient des chiffres")
    else:
        conseils.append("❌ Ajoutez des chiffres (0-9)")

        # ========== VÉRIFICATION 5 : LES SYMBOLES ==========
    # Je vérifie s'il y a des caractères spéciaux (!, @, #, etc.)
    symboles = "!@#$%^&*(),.?:{}|<>_-+=[]\\/"
    a_des_symboles = False
    
    for caractere in password:
        if caractere in symboles:
            a_des_symboles = True
            break
    
    if a_des_symboles:
        score = score + 15
        conseils.append("✅ Contient des symboles")
    else:
        conseils.append("❌ Ajoutez des symboles (!@#$%...)")

    # ========== VÉRIFICATION 6 : MOTS DE PASSE DANGEREUX ==========
    # Liste des mots de passe les plus utilisés (très dangereux !)
    mots_de_passe_nuls = [
        'password', '123456', 'qwerty', 'azerty', 'admin',
        'password123', 'admin123', '111111', '123123'
    ]
    
    # Je vérifie si le mot de passe est dans cette liste
    # .lower() transforme tout en minuscules pour comparer
    if password.lower() in mots_de_passe_nuls:
        score = 0  # Score à ZÉRO si c'est un mot de passe ultra courant !
        conseils.append("🚨 DANGER ! Ce mot de passe est très connu des hackers !")
    
    # ========== CALCUL FINAL ==========
    # Je m'assure que le score reste entre 0 et 100
    if score > 100:
        score = 100
    if score < 0:
        score = 0
    
    # Je retourne le score et la liste des conseils
    return score, conseils


def afficher_resultat(password, score, conseils):
    """
    Cette fonction affiche joliment les résultats
    """
    
    print("\n" + "="*50)
    print("🔐 RÉSULTAT DE L'ANALYSE")
    print("="*50)
    
    # J'affiche le mot de passe masqué (avec des étoiles)
    print(f"\nMot de passe: {'*' * len(password)}")
    print(f"Longueur: {len(password)} caractères")
    
    # J'affiche tous les conseils
    print("\n📋 DÉTAILS:\n")
    for conseil in conseils:
        print(f"  {conseil}")
    
    # J'affiche le score
    print("\n" + "="*50)
    print(f"⭐ SCORE: {score}/100")
    print("="*50)
    
    # Je donne un verdict selon le score
    if score >= 80:
        print("\n🟢 MOT DE PASSE FORT")
        print("Super ! Ce mot de passe est très sécurisé.")
    elif score >= 60:
        print("\n🟡 MOT DE PASSE MOYEN")
        print("Correct, mais vous pouvez faire mieux.")
    elif score >= 40:
        print("\n🟠 MOT DE PASSE FAIBLE")
        print("Attention ! Changez ce mot de passe rapidement.")
    else:
        print("\n🔴 MOT DE PASSE TRÈS FAIBLE")
        print("DANGER ! Ce mot de passe est trop facile à deviner !")
    
    # Quelques conseils généraux
    print("\n💡 RAPPEL DES BONNES PRATIQUES:")
    print("  • Minimum 12 caractères")
    print("  • Mélanger majuscules + minuscules + chiffres + symboles")
    print("  • Ne jamais utiliser d'infos personnelles")
    print("  • Activer la double authentification (2FA)")
    print()


# ========== PROGRAMME PRINCIPAL ==========
if __name__ == "__main__":
    
    print("\n🔐 ANALYSEUR DE FORCE DE MOT DE PASSE")
    print("="*50)
    
    # Si l'utilisateur a tapé un mot de passe en ligne de commande
    if len(sys.argv) > 1:
        # sys.argv[1] = le premier argument après le nom du script
        password = sys.argv[1]
    else:
        # Sinon je lui demande de taper un mot de passe
        password = input("\nEntrez un mot de passe à analyser: ")
    
    # Je vérifie qu'il a bien tapé quelque chose
    if not password:
        print("❌ Vous n'avez rien tapé !")
        sys.exit(1)  # Je quitte le programme
    
    # J'appelle ma fonction d'analyse
    score, conseils = analyser_password(password)
    
    # J'affiche les résultats
    afficher_resultat(password, score, conseils)