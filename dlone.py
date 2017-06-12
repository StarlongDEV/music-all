# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 20:14:52 2017

@author: Théophile
"""
import subprocess
import os
import Replace

def dl(arglien, current_path):
    
        # Commandes 
        # 0 : dl de la musique
        # 1 : on récupère le titre
        
        command1 = 'youtube-dl --get-title ' + arglien
        
        # On récupère le titre
        titre = subprocess.check_output(command1.split(), shell = False)

        # On decode le texte en utf 8
        titre=titre.decode('UTF-8')

        #On supprime les caractères spéciaux du titre \ / : * ? " < > | 
        titre = Replace.replace(titre)
        
        # Il affiche du caratere 1 (ça part de 0), et s'arrete 2 caracteres avant la fin : 
        # Si titre = "Bonjour", titre[1:-2] => onjo
        titre=titre[0:-1]

        
        print("\nNom de la musique : ", titre, "\n")
    
    
        # on définit le nom du dossier
        nom_dossier = str(titre)        
        
        #Nouveau chemin
        newpath = current_path + '\Musique\{}'.format(nom_dossier) 
    
        
        command0 = 'youtube-dl -x -o ' + '"{}'.format(newpath) + '\%(title)s.%(ext)s" --audio-format mp3 ' + arglien
        
        
        #Si la musique est déjà téléchargé
        if not os.path.exists(newpath):           
            #Création du Dossier
            print("Création du dossier!")
            os.makedirs(newpath)
            
        else:
            print("Dossier existe deja!")


        #On effectue le téléchargement
        do_dl = subprocess.run(command0, shell=False)
        if do_dl:
            print("Musique téléchargée!")
        else:
            print("Erreur")
            
        