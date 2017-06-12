# -*- coding: utf-8 -*-
"""

DOWNLOADER AUTO
@Théophile Louvart 2017


"""

# On importe les modules utiles 
import dlone as dlONE
import dlplaylist as dlPla
import os

#musique https://www.youtube.com/watch?v=IM-xWd7Zeps
#playlist https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re

# On récupere le dossier actuel du script
__file__ = "Script.py"
current_path = os.path.dirname(os.path.abspath(__file__))
end_use = 2

while int(end_use) != (0,1):
    end_use = input("Voulez-vous télécharger une musique ou une playlist : [Musique:0/Playlist:1] : ")
    
    if int(end_use) == 0:      
        
        arglien = input('[YOUTUBE DOWNLOADER] Lien de la musique à télécharger : ')        
        print("\nTéléchargement de la musique...")
          
        #On effectue
        dlONE.dl(arglien, current_path)
        
    if int(end_use) == 1:
        
        arglien_playlist = input('[YOUTUBE DOWNLOADER] Lien de la playlist à télécharger : ')                
        print("\nTéléchargement de la playlist")
        
        #On effectue
        dlPla.dl_playlist(arglien_playlist, current_path)          
    
    else:
        print("\n\nFin du programme")
        break
    
    
