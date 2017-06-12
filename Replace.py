# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 15:00:02 2017

@author: Théophile
"""

def replace(titre):
        titre = titre.replace('\ ','')
        titre = titre.replace('/','')
        titre = titre.replace(':','')
        titre = titre.replace('*','')
        titre = titre.replace('?','')
        titre = titre.replace('"','')
        titre = titre.replace('<','')
        titre = titre.replace('>','')
        titre = titre.replace('|','')
        
        return titre