# FFXIV-free-company-census-script
Upon providing the id of the FC lodestone page the software will return a list of all the races present in the game and how many of each one are in the selected FC

# Instrucciones / Tutorial:

[Download](https://github.com/ROMthesheep/FFXIV-free-company-census-script/archive/V1.1.zip) the lateless release of the software, unzip the folder you will se the following:

[Descarga](https://github.com/ROMthesheep/FFXIV-free-company-census-script/archive/V1.1.zip) la ultima version del software, descomprime el archivo y veras lo siguiente:

![](https://i.gyazo.com/192e61230942ee91b12161451aba350d.png)

Hold the windows key adn press 'R', the run window will pop up, type 'cmd' and press enter. Navigate to the folder directory by entering somewhat this command: `cd C:\Users\*your username*\Downloads\FFXIV-free-company-census-script-1.0` once you are located on the desired folder, type this exact command: `webscraper\Scripts\activate` if everything went well you will see this `(webscraper) C:\Users\*your username*\Downloads\....`, now type the following command: `python censusScript.py *Your FC id from the lodestone*` annnd wait, once the script is completed something like this will pop out:


Manten pulsada la tecla windows y pulsa la 'R', la ventana ejecutar aparecera, escribe 'cmd' y pulsa enter. navega hasta la carpeta del proyecto introduciendo un comando similara  este: `cd C:\Users\*your username*\Downloads\FFXIV-free-company-census-script-1.0` una vez estes ubicado en la carpeta deseada, escribe este comando en la consola: `webscraper\Scripts\activate` si todo fue bien en la cabecera del log veras algo parecido a esto: `(webscraper) C:\Users\*your username*\Downloads\....`, nahora y por ultimo introcude este comando sustituyendo el campoo por el valor deseado o simplmente sin el valor: `python censusScript.py *Your FC id from the lodestone*` ahora espera a que el programa analice las paginas de la lodestone, tardara unos minutos y deberias verun porcentaje subir. Una vez llegue al 100% deberias ver esto aparecer en al consola:

![](https://i.gyazo.com/43f062b7bdb7fdb4c96221f22af72d54.png)

and on the root folder you will se some pie charts representing some data studies.

Si miras en la carpeta original deberias poder ver unas imagenes con graficos radiales de diferentes estadisticas.
