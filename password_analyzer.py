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