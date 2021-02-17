# FFXIV-free-company-census-script
Upon providing the id of the FC lodestone page the software will return a list of all the races present in the game and how many of each one are in the selected FC

# Instrucciones / Tutorial:

[Download](https://github.com/ROMthesheep/FFXIV-free-company-census-script/archive/v1.0.zip) the lateless release of the software, unzip the folder you will se the following:

![](https://i.gyazo.com/192e61230942ee91b12161451aba350d.png)

Hold the windows key adn press 'R', the run window will pop up, type 'cmd' and press enter. Navigate to the folder directory by entering somewhat this command: `cd C:\Users\*your username*\Downloads\FFXIV-free-company-census-script-1.0` once you are located on the desired folder, type this exact command: `webscraper\Scripts\activate` if everything went well you will see this `(webscraper) C:\Users\*your username*\Downloads\....`, now type the following command: `python censusScript.py *Your FC id from the lodestone*` annnd wait, once the script is completed something like this will pop out:

`There are 251 members in Prisma
126 play a female PJ and 125 play with a male PJ
57 are Hyur, 17 are female and 40 are male
41 Midland and 16 Highland
88 are Miqo'te, 54 are female and 34 are male
7 are Elezen, 6 are female and 1 are male
3 Wildwood and 4 Duskwight
6 are Roegadyn, 3 are female and 3 are male
1 Sea wolf and 5 Hellguard
34 are Lalafell, 13 are female and 21 are male
13 Plainfolk and 21 Dunesfolk
35 are Au Ra, 19 are female and 16 are male
20 son Raen and 15 Xaela
5 are Hrothgar
2 Helion and 3 The Lost
19 are Viera
11 Rava and 8 Veena`

and on the root folder you will se some pie charts representing some data studies.
