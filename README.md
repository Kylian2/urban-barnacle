# README

Ces programmes ont été créés dans le cadre du mini-projet de communication bas niveau à l'IUT d'Orsay. Il permettent de faciliter la conversion "chaine ascii" - "chaine lisble" dans les deux sens, ils ont pour but d'êtres utilisé dans la RAM LOGISIM (entête attendue par logisim). 

## chaineToAscii

Ce programme convertis chaque caractère d'une chaine et écris dans un fichier leur conversion. Le fichier contient en première ligne l'entete attendue par LOGISIM. Ensuite la première valeur écrite est la taille de la chaine puis le code ascii de chaque caractère. 

## asciiToChaine

Ce programme permet de convertir des codes ascii téléchargés depuis la mémoire RAM du microprocesseur Logisim en chaine de caractère lisible par l'humain. 
