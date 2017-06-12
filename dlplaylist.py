# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 20:47:06 2017

@author: Théophile
"""
import os

import Replace


def dl_playlist(arglien_playlist, current_path):
   
        # Commandes 
        # 0 : dl de la musique
        # 1 : on récupère le titre de la playlist
        import subprocess
        #arglien_playlist= "https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re"
    
        
        titre_playlist = input("\nNom de la playlist : ")

        nom_dossier = str(titre_playlist)        
        
        #Nouveau chemin
        newpath = current_path + '\Musique\{}'.format(nom_dossier) 
        
        command4 = 'youtube-dl -x -o ' + '"{}'.format(newpath) + '\%(title)s.%(ext)s" --audio-format mp3 ' + arglien_playlist
        
        #Si la musique est déjà téléchargé
        if not os.path.exists(newpath):           
            #Création du Dossier
            print("Création du dossier!")
            os.makedirs(newpath)
            
        else:
            print("Dossier existe deja!")


        #On effectue le téléchargement
        do_dl = subprocess.run(command4, shell=False)
        if do_dl:
            print("Musique téléchargée!")
        else:
            print("Erreur")
            
        