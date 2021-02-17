import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import sys

hyurMid=0
hyurHigh=0
catSun=0
catMoon=0
eleWild=0
eleDusk=0
roeSea=0
roeHell=0
lalaPlain=0
lalaDusk = 0
auraRae=0
auraXae=0
furroHelion=0
furroLost=0
vieraRav=0
vieraVeen=0

hyurM=0
hyurF=0
catM=0
catF=0
eleM=0
eleF=0
roeM=0
roeF=0
lalaM=0
lalaF = 0
auraM=0
auraF=0

m=0
f=0
razas = "hyur","Miqo\'te",'Elezen','Roegadyn','Lalafell','Au Ra','Hrothgar','Viera'
clanes = 'Midland','Highland','Seekers of the sun','Keepers of the moon','Wildwood','Duskwight','Sea wolf','Hellguard','Plainsfolk','Dunesfolk','Raen','Xaela','Helion','The Lost','Rava','Veena'

if(len(sys.argv)>1):
  fcId=sys.argv[len(sys.argv)-1]
else:
  print("Introduce the lodestone id of the free company: ")
  fcId=input()

url = 'https://eu.finalfantasyxiv.com/lodestone/freecompany/{}/member'.format(fcId)
page = requests.get(url)

miembros = []

soup = BeautifulSoup(page.content,'html.parser')

numeroDePaginas = int(soup.find('li',class_="btn__pager__current").text[-1])
nommbreFC = soup.find('p',class_='entry__freecompany__name').text
print("Checking out the FC: " + nommbreFC)

  
for pagina in range(1,numeroDePaginas+1):
  newurl = "https://eu.finalfantasyxiv.com/lodestone/freecompany/{}/member?page={}".format(fcId,pagina)
  newPage = requests.get(newurl)
  soup = BeautifulSoup(newPage.content,'html.parser')
  results = soup.find_all('a',class_='entry__bg')
  print("scraping page: " + newurl)
  for member in results:
    miembros.append(member['href'][21:-1])

print('User ids had been collected, now the analissi of user profiles will begin')

for uid in miembros:
  newurl = "https://eu.finalfantasyxiv.com/lodestone/character/{}/".format(uid)
  newPage = requests.get(newurl)
  soup = BeautifulSoup(newPage.content,'html.parser')
  results = soup.find('p',class_='character-block__name')
  print("{:.2f}%".format(((m+f)*100)/len(miembros)))
  if(results.text[0:-4]=='HyurMidlander'):
    if(results.text[-1]=='♂'):
      m+=1
      hyurM+=1
    else:
      f+=1
      hyurF+=1
    hyurMid+=1
  elif(results.text[0:-4]=='HyurHighlander'):
    if(results.text[-1]=='♂'):
      m+=1
      hyurM+=1
    else:
      f+=1
      hyurF+=1
    hyurHigh+=1
  elif(results.text[0:-4]=='Miqo\'teSeeker of the Sun'):
    if(results.text[-1]=='♂'):
      catM+=1
      m+=1
    else:
      catF+=1
      f+=1
    catSun+=1
  elif(results.text[0:-4]=='Miqo\'teKeeper of the Moon'):
    if(results.text[-1]=='♂'):
      m+=1
      catM+=1
    else:
      catF+=1
      f+=1
    catMoon+=1
  elif(results.text[0:-4]=='ElezenDuskwight'):
    if(results.text[-1]=='♂'):
      m+=1
      eleM+=1
    else:
      eleF+=1
      f+=1
    eleDusk+=1
  elif(results.text[0:-4]=='ElezenWildwood'):
    if(results.text[-1]=='♂'):
      m+=1
      eleM+=1
    else:
      eleF+=1
      f+=1
    eleWild+=1
  elif(results.text[0:-4]=='RoegadynSea Wolf'):
    if(results.text[-1]=='♂'):
      m+=1
      roeM+=1
    else:
      roeF+=1
      f+=1
    roeSea+=1
  elif(results.text[0:-4]=='RoegadynHellsguard'):
    if(results.text[-1]=='♂'):
      m+=1
      roeM+=1
    else:
      roeF+=1
      f+=1
    roeHell+=1
  elif(results.text[0:-4]=='LalafellPlainsfolk'):
    if(results.text[-1]=='♂'):
      lalaM+=1
      m+=1
    else:
      lalaF+=1
      f+=1
    lalaPlain+=1
  elif(results.text[0:-4]=='LalafellDunesfolk'):
    if(results.text[-1]=='♂'):
      m+=1
      lalaM+=1
    else:
      lalaF+=1
      f+=1
    lalaDusk+=1
  elif(results.text[0:-4]=='Au RaRaen'):
    if(results.text[-1]=='♂'):
      auraM+=1
      m+=1
    else:
      auraF+=1
      f+=1
    auraRae+=1
  elif(results.text[0:-4]=='Au RaXaela'):
    if(results.text[-1]=='♂'):
      auraM+=1
      m+=1
    else:
      auraF+=1
      f+=1
    auraXae+=1
  elif(results.text[0:-4]=='HrothgarHelions'):
    if(results.text[-1]=='♂'):
      m+=1
    else:
      f+=1
    furroHelion+=1
  elif(results.text[0:-4]=='HrothgarThe Lost'):
    if(results.text[-1]=='♂'):
      m+=1
    else:
      f+=1
    furroLost+=1
  elif(results.text[0:-4]=='VieraRava'):
    if(results.text[-1]=='♂'):
      m+=1
    else:
      f+=1
    vieraRav+=1
  elif(results.text[0:-4]=='VieraVeena'):
    if(results.text[-1]=='♂'):
      m+=1
    else:
      f+=1    
    vieraVeen+=1
  
print("\n-------------------------------------------------------------------------------\n\nThere are {} members in {}\n".format(len(miembros),nommbreFC) +
      "{} play a female PJ and {} play with a male PJ\n".format(f,m) +
      "{} are Hyur, {} are female and {} are male \n{} Midland and {} Highland\n".format(hyurHigh+hyurMid,hyurF,hyurM,hyurMid,hyurHigh) +
      "{} are Miqo\'te, {} are female and {} are male \n{} Seekers of the sun and {} Keepers of the moon\n".format(catMoon+catSun,catF,catM,catSun,catMoon) +
      "{} are Elezen, {} are female and {} are male \n{} Wildwood and {} Duskwight\n".format(eleDusk+eleWild,eleM,eleF,eleWild,eleDusk) +
      "{} are Roegadyn, {} are female and {} are male \n{} Sea wolf and {} Hellguard\n".format(roeHell+roeSea,roeF,roeM,roeSea,roeHell) +
      "{} are Lalafell, {} are female and {} are male \n{} Plainfolk and {} Dunesfolk\n".format(lalaDusk+lalaPlain,lalaF,lalaM,lalaPlain,lalaDusk) +
      "{} are Au Ra, {} are female and {} are male \n{} son Raen and {} Xaela\n".format(auraRae+auraXae,auraF,auraM,auraRae,auraXae) +
      "{} are Hrothgar \n{} Helion and {} The Lost\n".format(furroHelion+furroLost,furroHelion,furroLost) +
      "{} are Viera \n{} Rava and {} Veena".format(vieraRav+vieraVeen,vieraRav,vieraVeen))

# Pie chart sexos
explode = (0,0.1)
fig1, ax1 = plt.subplots()  
ax1.pie((m,f),
        explode=explode,
        labels=('Male','Female'),
        autopct='%1.1f%%',
        shadow=True,
        startangle=90
        )
ax1.axis('equal')
plt.savefig('sex distribution.png', transparent=True)

# Pie chart hyur
explode = (0,0.1)
fig2, ax2 = plt.subplots()  
ax2.pie((hyurMid,hyurHigh),
        explode=explode,
        labels=clanes[0:2],
        autopct='%1.1f%%',
        shadow=True,
        startangle=90
        )
ax2.axis('equal')
plt.savefig('clans Hyur.png', transparent=True)

# Pie chart miqote
explode = (0,0.1)
fig3, ax3 = plt.subplots()  
ax3.pie((catSun,catMoon),
        explode=explode,
        labels=clanes[2:4],
        autopct='%1.1f%%',
        shadow=True,
        startangle=90
        )
ax3.axis('equal')
plt.savefig('clans Miqote.png', transparent=True)

# Pie chart elezen
explode = (0,0.1)
fig4, ax4 = plt.subplots()  
ax4.pie((eleWild,eleDusk),
        explode=explode,
        labels=clanes[4:6],
        autopct='%1.1f%%',
        shadow=True,
        startangle=90
        )
ax4.axis('equal')
plt.savefig('clans Elezen.png', transparent=True)

# Pie chart roe
explode = (0,0.1)
fig5, ax5 = plt.subplots()  
ax5.pie((roeSea,roeHell),
        explode=explode,
        labels=clanes[6:8],
        autopct='%1.1f%%',
        shadow=True,
        startangle=90
        )
ax5.axis('equal')
plt.savefig('clans Roegadyn.png', transparent=True)

# Pie chart lala
explode = (0,0.1)
fig6, ax6 = plt.subplots()  
ax6.pie((lalaPlain,lalaDusk),
        explode=explode,
        labels=clanes[8:10],
        autopct='%1.1f%%',
        shadow=True,
        startangle=90
        )
ax6.axis('equal')
plt.savefig('clans lalafell.png', transparent=True)

# Pie chart aura
explode = (0,0.1)
fig7, ax7 = plt.subplots()  
ax7.pie((auraRae,auraXae),
        explode=explode,
        labels=clanes[10:12],
        autopct='%1.1f%%',
        shadow=True,
        startangle=90
        )
ax7.axis('equal')
plt.savefig('clans aura.png', transparent=True)

# Pie chart furro
explode = (0,0.1)
fig8, ax8 = plt.subplots()  
ax8.pie((furroHelion,furroLost),
        explode=explode,
        labels=clanes[12:14],
        autopct='%1.1f%%',
        shadow=True,
        startangle=90
        )
ax8.axis('equal')
plt.savefig('clans Hrothgar.png', transparent=True)

# Pie chart viera
explode = (0,0.1)
fig9, ax9 = plt.subplots()  
ax9.pie((vieraRav,vieraVeen),
        explode=explode,
        labels=clanes[14:16],
        autopct='%1.1f%%',
        shadow=True,
        startangle=90
        )
ax9.axis('equal')
plt.savefig('clans Viera.png', transparent=True)

# Pie chart global
explode = (0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2)
fig10, ax10 = plt.subplots()  
ax10.pie(((hyurHigh+hyurMid),(catMoon+catSun),(eleDusk+eleWild),(roeHell+roeSea),(lalaDusk+lalaPlain),(auraRae+auraXae),(furroHelion+furroLost),(vieraRav+vieraVeen)),
        labels=razas,
        autopct='%1.1f%%',
        explode=explode,
        shadow=True,
        startangle=90
        )
ax10.axis('equal')
plt.savefig('razas.png', transparent=True)
