from tkinter import *
from random import randrange

 
 
############################################################################################
 
## Fonctions ##

def restart():
    global x,y,dx,dy,xx,yy,dxx,dyy,pX,pY,food,score,score2,rectangle,rectangle2,direction,texte,texte1,texte2,perdu,can,fen,bouton2,bouton3,bouton4,bouton5,bouton6,bouton7,bouton8,line,vitesse,vite,aze
    texte1.destroy()
    texte2.destroy()
    bouton2.destroy()
    bouton3.destroy()

    #Serpent1
    
    x = [245,245]
    y = [245,245]
    dx = 10
    dy = 0

    #Serpent2

    xx=[245,245]
    yy=[140,140]
    dxx = -10
    dyy = 0

    #Autre
    
    pX = randrange(5, 495)
    pY = randrange(5, 495)
    food = 0
    score = 0
    score2 = 0
    rectangle = []
    rectangle2 =[]
    direction = 0
    texte = []
    texte1 = []
    texte2 = []
    perdu = 0
    
    lancement()


## Lancement du Jeu - 1 Joueur ##
    
def Start():
    global x,y,dx,dy,xx,yy,dxx,dyy,pX,pY,food,score,score2,rectangle,rectangle2,direction,texte,texte1,texte2,perdu,can,fen,bouton2,bouton3,bouton4,bouton5,bouton6,bouton7,bouton8,line,vitesse,vite,aze

    can.destroy()
    can = Canvas(fen, width=500, height=500, bg='#96c102')
    can.pack()

    vitesse = 100-vite
    rectangle.append (can.create_rectangle(x[0], y[0], x[0]+10, y[0]+10, outline=line, fill=couleur))
    
          
    aze = 0

    
    food = can.create_oval(pX, pY, pX+10, pY+10, fill="red")
    
    deplacement()
    
    fen.bind('<Right>', right)
    fen.bind('<Left>', left)
    fen.bind('<Up>' , up)
    fen.bind('<Down>', down)
    fen.bind('<KeyPress-d>', right)
    fen.bind('<KeyPress-q>', left)
    fen.bind('<KeyPress-z>' , up)
    fen.bind('<KeyPress-s>', down)
    fen.bind('<KeyPress-D>', right)
    fen.bind('<KeyPress-Q>', left)
    fen.bind('<KeyPress-Z>' , up)
    fen.bind('<KeyPress-S>', down)



## Lancement du Jeu - 2 Joueurs ##

def Start2():
    global x,y,dx,dy,xx,yy,dxx,dyy,pX,pY,food,score,score2,rectangle,rectangle2,direction,texte,texte1,texte2,perdu,can,fen,bouton1,bouton2,bouton3,bouton4,bouton5,bouton6,bouton7,bouton8,line,vitesse,vite,aze

    can.destroy()
    can = Canvas(fen, width=500, height=500, bg='#96c102')
    can.pack()

    vitesse = 100-vite
    rectangle.append (can.create_rectangle(x[0], y[0], x[0]+10, y[0]+10, outline=line, fill=couleur))
    rectangle2.append(can.create_rectangle(xx[0], yy[0], xx[0]+10, yy[0]+10, outline='black', fill='white'))
    
    if perdu == 1:
        return

    if param == 1:
        bouton1.destroy()
        texte3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton7.destroy()
        bouton8.destroy()
            
    if aze == 1 :
        bouton1.destroy()
        bouton3.destroy()
        background_label.destroy()
                 
    aze = 0

    
    food = can.create_oval(pX, pY, pX+10, pY+10, fill="red")
    
    deplacement()
    deplacement2()
    
    fen.bind('<Right>', right)
    fen.bind('<Left>', left)
    fen.bind('<Up>' , up)
    fen.bind('<Down>', down)
    fen.bind('<KeyPress-d>', right2)
    fen.bind('<KeyPress-q>', left2)
    fen.bind('<KeyPress-z>' , up2)
    fen.bind('<KeyPress-s>', down2)
    fen.bind('<KeyPress-D>', right2)
    fen.bind('<KeyPress-Q>', left2)
    fen.bind('<KeyPress-Z>' , up2)
    fen.bind('<KeyPress-S>', down2)



## Deplacement Serpent 1 ##    
    
def deplacement():
    
    global x,y,dx,dy,xx,yy,dxx,dyy,pX,pY,food,score,score2,rectangle,rectangle2,direction,texte,texte1,texte2,perdu,can,fen,bouton2,bouton3,bouton4,bouton5,bouton6,bouton7,bouton8,line,vitesse,vite
    lon = score
    lon += 1

    if perdu == 1:
        return
    
    ## TETE ##

    x[0]  += dx
    y[0]  += dy
    
    can.coords(rectangle[0], x[0], y[0], x[0]+10, y[0]+10)

    ## CORPS ##
    while lon!=0 :
        lonn = lon-1
        x[lon] = x[lonn]
        y[lon] = y[lonn]
        lon = lon-1
        can.coords(rectangle[lon],x[lon],y[lon],x[lon]+10,y[lon]+10)

    amanger()
    aperdu()
    scorea()
    
    fen.after(vitesse, deplacement)

## Deplacement Serpent 2 ##

def deplacement2():
    global x,y,dx,dy,xx,yy,dxx,dyy,pX,pY,food,score,score2,rectangle,rectangle2,direction,texte,texte1,texte2,perdu,can,fen,bouton2,bouton3,bouton4,bouton5,bouton6,bouton7,bouton8,line,vitesse,vite
    lon2 = score2 +1
    
    if perdu == 1:
        return
    
    ## TETE ##

    xx[0]  += dxx
    yy[0]  += dyy
    
    can.coords(rectangle2[0], xx[0], yy[0], xx[0]+10, yy[0]+10)
    
    ## CORPS ##
    
    while lon2!=0 :
        lonn2 = lon2-1
        xx[lon2] = xx[lonn2]
        yy[lon2] = yy[lonn2]
        lon2 = lon2-1
        can.coords(rectangle2[lon2],xx[lon2],yy[lon2],xx[lon2]+10,yy[lon2]+10)

    fen.after(vitesse, deplacement2)




## A Manger ? ##

def amanger():
    global x,y,dx,dy,xx,yy,dxx,dyy,pX,pY,food,score,score2,rectangle,rectangle2,direction,texte,texte1,texte2,perdu,can,fen,bouton2,bouton3,bouton4,bouton5,bouton6,bouton7,bouton8,line,vitesse,vite
    if x[0] in range(pX-8,pX+8) and y[0] in range(pY-8,pY+8):
        score=score+1
        pX = randrange(10, 480)
        pY = randrange(10, 480)
        can.coords(food, pX, pY, pX+10, pY+10)
        x.append(245)
        y.append(245)
        rectangle.append(can.create_rectangle(600, 600, 610, 610, outline=line, fill=couleur))
        
    if xx[0] in range(pX-8,pX+8) and yy[0] in range(pY-8,pY+8):
        score2 += 1
        pX = randrange(10, 480)
        pY = randrange(10, 480)
        can.coords(food, pX, pY, pX+10, pY+10)
        xx.append(245)
        yy.append(245)
        rectangle2.append(can.create_rectangle(600, 600, 610, 610, outline='black', fill='white'))


## Perdu ? ##

def aperdu():
    global x,y,dx,dy,xx,yy,dxx,dyy,pX,pY,food,score,score2,rectangle,rectangle2,direction,texte,texte1,texte2,perdu,can,fen,bouton2,bouton3,bouton4,bouton5,bouton6,bouton7,bouton8,line,vitesse,vite,v,niveau
    
    ## Sortie du cadre - UN SERPENT ##

    if v==1:
        if (y[0] > 496 or y[0] <0) and perdu==0 :

            can.destroy()
            can = Canvas(fen, width=500, height=500, bg='#96c102')
            can.pack()
            perdu = 1
            food = 0

            
            texte3 = Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text=("Sur le niveau"))
            texte3.place(x=100,y=40)
            texte4 = Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text=(niveau))
            texte4.place(x=280,y=40)
            texte2 =Label(fen, fg="#232d08", bg="#96c102", font="System 40 bold" , text="Votre score est")
            texte2.place(x=55,y=80)
            texte1 =Label(fen, fg="#232d08", bg="#96c102", font="System 40 bold" , text=(score))
            texte1.place(x=240,y=150)

            x = [1000,1000]
            y = [1000,1000]
            xx = [1000,1000]
            yy = [1000,1000]

            bouton2=Button(fen, text="REJOUER",relief=FLAT,fg="#232d08",bg="#96c102", font="System 40 bold", command=restart)
            bouton2.place(x=98,y=250)
            bouton3=Button(fen, text="PARAMETRES",relief=FLAT,fg="#232d08",bg="#96c102", font="System 40 bold",command=parametre)
            bouton3.place(x=40,y=350)
            
            
            
            return
        
        if (x[0] > 496 or x[0] < 0) and perdu==0:

            can.destroy()
            can = Canvas(fen, width=500, height=500, bg='#96c102')
            can.pack()

            
            perdu=1
            food = 0

            texte3 = Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text=("Sur le niveau"))
            texte3.place(x=100,y=40)
            texte4 = Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text=(niveau))
            texte4.place(x=280,y=40)
            texte2 =Label(fen, fg="#232d08", bg="#96c102", font="System 40 bold" , text="Votre score est")
            texte2.place(x=55,y=80)
            texte1 =Label(fen, fg="#232d08", bg="#96c102", font="System 40 bold" , text=(score))
            texte1.place(x=240,y=150)

            x = [1000,1000]
            y = [1000,1000]
            xx = [1000,1000]
            yy = [1000,1000]

            bouton2=Button(fen, text="REJOUER",relief=FLAT,fg="#232d08",bg="#96c102", font="System 40 bold", command=restart)
            bouton2.place(x=98,y=250)
            bouton3=Button(fen, text="PARAMETRES",relief=FLAT,fg="#232d08",bg="#96c102", font="System 40 bold",command=parametre)
            bouton3.place(x=40,y=350)

            
            return

        
    ## Sortie du Cadre - DEUX SERPENTS ##
        
    if v==2:
##        print("1:",score)
##        print("2:",score2)
        if (y[0] > 496 or y[0] <0) and perdu==0 :

            can.destroy()
            can = Canvas(fen, width=500, height=500, bg='#96c102')
            can.pack()

            
            perdu = 1
            food = 0
            score = int(score/2)

            texte5 = Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text=("Sur le niveau"))
            texte5.place(x=100,y=40)
            texte4 = Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text=(niveau))
            texte4.place(x=280,y=40)         
            texte2 =Label(fen, fg="#232d08", bg="#96c102", font="System 40 bold" , text="Votre score est")
            texte2.place(x=55,y=80)
            texte1 =Label(fen, fg=couleur, bg="#96c102", font="System 40 bold" , text=(score))
            texte1.place(x=350,y=150)
            texte3 =Label(fen, fg="white", bg="#96c102", font="System 40 bold" , text=(score2))
            texte3.place(x=150,y=150)
            
            x = [1000,1000]
            y = [1000,1000]
            xx = [1000,1000]
            yy = [1000,1000]

            bouton2=Button(fen, text="REJOUER",relief=FLAT,fg="#232d08",bg="#96c102", font="System 40 bold", command=restart)
            bouton2.place(x=98,y=250)
            bouton3=Button(fen, text="PARAMETRES",relief=FLAT,fg="#232d08",bg="#96c102", font="System 40 bold",command=parametre)
            bouton3.place(x=40,y=350)
            
            
            return
        
        
        if (x[0] > 496 or x[0] < 0) and perdu==0:

            can.destroy()
            can = Canvas(fen, width=500, height=500, bg='#96c102')
            can.pack()

            
            perdu=1
            food = 0
            score = int(score/2)

            texte5 = Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text=("Sur le niveau"))
            texte5.place(x=100,y=40)
            texte4 = Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text=(niveau))
            texte4.place(x=280,y=40)           
            texte2 =Label(fen, fg="#232d08", bg="#96c102", font="System 40 bold" , text="Votre score est")
            texte2.place(x=55,y=80)
            texte1 =Label(fen, fg=couleur, bg="#96c102", font="System 40 bold" , text=(score))
            texte1.place(x=350,y=150)
            texte3 =Label(fen, fg="white", bg="#96c102", font="System 40 bold" , text=(score2))
            texte3.place(x=150,y=150)

            x = [1000,1000]
            y = [1000,1000]
            xx = [1000,1000]
            yy = [1000,1000]

            bouton2=Button(fen, text="REJOUER",relief=FLAT,fg="#232d08",bg="#96c102", font="System 40 bold", command=restart)
            bouton2.place(x=98,y=250)
            bouton3=Button(fen, text="PARAMETRES",relief=FLAT,fg="#232d08",bg="#96c102", font="System 40 bold",command=parametre)
            bouton3.place(x=40,y=350)

            
            return

        
        if (yy[0] > 496 or yy[0] <0) and perdu==0 :

            can.destroy()
            can = Canvas(fen, width=500, height=500, bg='#96c102')
            can.pack()

            
            perdu = 1
            food = 0
            score2 = int(score2/2)

            texte5 = Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text=("Sur le niveau"))
            texte5.place(x=100,y=40)
            texte4 = Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text=(niveau))
            texte4.place(x=280,y=40)
            texte2 =Label(fen, fg="#232d08", bg="#96c102", font="System 40 bold" , text="Votre score est")
            texte2.place(x=55,y=80)            
            texte1 =Label(fen, fg=couleur, bg="#96c102", font="System 40 bold" , text=(score))
            texte1.place(x=350,y=150)
            texte3 =Label(fen, fg="white", bg="#96c102", font="System 40 bold" , text=(score2))
            texte3.place(x=150,y=150)


            x = [1000,1000]
            y = [1000,1000]
            xx = [1000,1000]
            yy = [1000,1000]


            bouton2=Button(fen, text="REJOUER",relief=FLAT,fg="#232d08",bg="#96c102", font="System 40 bold", command=restart)
            bouton2.place(x=98,y=250)
            bouton3=Button(fen, text="PARAMETRES",relief=FLAT,fg="#232d08",bg="#96c102", font="System 40 bold",command=parametre)
            bouton3.place(x=40,y=350)
            
            return
        
        
        if (xx[0] > 496 or xx[0] < 0) and perdu==0:
            
            can.destroy()
            can = Canvas(fen, width=500, height=500, bg='#96c102')
            can.pack()

            
            predu = 1
            food = 0
            score2 = int(score2/2)

            texte2 = Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text=("Sur le niveau"))
            texte2.place(x=100,y=40)
            texte4 = Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text=(niveau))
            texte4.place(x=280,y=40)         

            texte1 =Label(fen, fg=couleur, bg="#96c102", font="System 40 bold" , text=(score))
            texte1.place(x=350,y=150)
            texte3 =Label(fen, fg="white", bg="#96c102", font="System 40 bold" , text=(score2))
            texte3.place(x=150,y=150)


            x = [1000,1000]
            y = [1000,1000]
            xx = [1000,1000]
            yy = [1000,1000]


            bouton2=Button(fen, text="REJOUER",relief=FLAT,fg="#232d08",bg="#96c102", font="System 40 bold", command=restart)
            bouton2.place(x=98,y=250)
            bouton3=Button(fen, text="PARAMETRES",relief=FLAT,fg="#232d08",bg="#96c102", font="System 40 bold",command=parametre)
            bouton3.place(x=40,y=350)
            return
    
    ## Se touche ##
    lon = score +1
    lon2 = score2 + 1
    
    while lon!=1 :   
        if x[0]==x[lon] and y[0]==y[lon] and perdu==0:

            can.destroy()
            can = Canvas(fen, width=500, height=500, bg='#96c102')
            can.pack()
            
            if v==2:
                score = int(score/2)
            
            perdu = 1
            food = 0
            
            texte3 = Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text=("Sur le niveau"))
            texte3.place(x=100,y=40)
            texte4 = Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text=(niveau))
            texte4.place(x=280,y=40)  
            texte2 =Label(fen, fg="#232d08", bg="#96c102", font="System 40 bold" , text="Votre score est")
            texte2.place(x=55,y=80)
            texte1 =Label(fen, fg=couleur, bg="#96c102", font="System 40 bold" , text=(score))
            if v==1:
                texte1.place(x=235,y=150)
            if v==2:
                texte1.place(x=350,y=150)
                texte3 =Label(fen, fg="white", bg="#96c102", font="System 40 bold" , text=(score2))
                texte3.place(x=150,y=150)

            
            x = [1000,1000]
            y = [1000,1000]
            xx = [1000,1000]
            yy = [1000,1000]
            
            bouton2=Button(fen, text="REJOUER",relief=FLAT,fg="#232d08",bg="#96c102", font="System 40 bold", command=restart)
            bouton2.place(x=98,y=250)
            bouton3=Button(fen, text="PARAMETRES",relief=FLAT,fg="#232d08",bg="#96c102", font="System 40 bold",command=parametre)
            bouton3.place(x=40,y=350)
            
            return        
        lon = lon-1
    
    while lon2!=1 :   
        if xx[0]==xx[lon2] and yy[0]==yy[lon2] and perdu==0:

            can.destroy()
            can = Canvas(fen, width=500, height=500, bg='#96c102')
            can.pack()
            
            
            perdu = 1
            food = 0
            score2 = int(score2/2)
            
            texte3 = Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text=("Sur le niveau"))
            texte3.place(x=100,y=40)
            texte4 = Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text=(niveau))
            texte4.place(x=280,y=40)     
            texte2 =Label(fen, fg="#232d08", bg="#96c102", font="System 40 bold" , text="Votre score est")
            texte2.place(x=55,y=80)
            texte1 =Label(fen, fg=couleur, bg="#96c102", font="System 40 bold" , text=(score))
            
            if v==1:
                texte1.place(x=235,y=150)
                
            if v==2:
                texte1.place(x=350,y=150)
                texte3 =Label(fen, fg="white", bg="#96c102", font="System 40 bold" , text=(score2))
                texte3.place(x=150,y=150)

            
            x = [1000,1000]
            y = [1000,1000]
            xx = [1000,1000]
            yy = [1000,1000]
            
            bouton2=Button(fen, text="REJOUER",relief=FLAT,fg="#232d08",bg="#96c102", font="System 40 bold", command=restart)
            bouton2.place(x=98,y=250)
            bouton3=Button(fen, text="PARAMETRES",relief=FLAT,fg="#232d08",bg="#96c102", font="System 40 bold",command=parametre)
            bouton3.place(x=40,y=350)
            
            return
        lon2 = lon2-1
    
    

## Affichage du Score ##
        
def scorea():
    global score,score2,v
    if score<10 :
        scoreaffiche =Label(can, font="System 15", text=score, fg=couleur, bg="#96c102")
        scoreaffiche.place(x=483, y=472)
    if score>9 :
        scoreaffiche =Label(can, font="System 15", text=score, fg=couleur, bg="#96c102")
        scoreaffiche.place(x=473, y=472)
    if score2<10 and v==2 :
        scoreaffiche2 =Label(can, font="System 15", text=score2, fg="white", bg="#96c102")
        scoreaffiche2.place(x=2, y=472)
    if score2>9 and v==2 :
        scoreaffiche2 =Label(can, font="System 15", text=score2, fg="white", bg="#96c102")
        scoreaffiche2.place(x=2, y=472)
    return



## Paramètre ##

def parametre():
    global bouton1,bouton3,bouton4,bouton5,bouton6,bouton7,bouton8,texte3,line, param,can,rougee,bleuu,jaunee,noirr,vite,f1,f2,n1,n2,d1,d2
    param = 1
    
    if perdu==1:
        texte2.destroy()
        texte1.destroy()
        bouton3.destroy()
        bouton2.destroy()
        can.destroy()
        can = Canvas(fen, width=500, height=500, bg='#96c102')
        can.pack()
        bouton1=Button(fen, text="JOUER",relief=FLAT,fg="#232d08", bg="#96c102", font="System 40 bold",command=restart)
        bouton1.place(x=133,y=380)
    else:
        bouton1.destroy()
        bouton3.destroy()
        background_label.destroy()
        can.destroy()
        can = Canvas(fen, width=500, height=500, bg='#96c102')
        can.pack()
        bouton1=Button(fen, text="JOUER",relief=FLAT,fg="#232d08", bg="#96c102", font="System 40 bold",command=lancement)
        bouton1.place(x=133,y=385)


    
    texte3 =Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text="Couleur du Serpent")
    texte3.place(x=130,y=20)
    
    bouton4=Button(fen,relief=FLAT, image=rougee ,bg="#96c102",command=rouge)
    bouton4.place(x=60,y=70)
    bouton5=Button(fen, relief=FLAT,image=bleuu ,bg="#96c102",command=bleu)
    bouton5.place(x=160,y=70)
    bouton7=Button(fen, relief=FLAT,image=jaunee,bg="#96c102",command=jaune)
    bouton7.place(x=260,y=70)
    bouton8=Button(fen, relief=FLAT,image=noirr ,bg="#96c102",command=noir)
    bouton8.place(x=360,y=70)



    texte4 =Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text="Difficulté (Vitesse)")
    texte4.place(x=130,y=180)
    

    bouton9=Button(fen, relief=FLAT,fg="#232d08", bg="#96c102", font="System 20 bold" , text="Facile",command=facile)
    bouton9.place(x=70,y=210)
    bouton10=Button(fen, relief=FLAT,fg="#232d08", bg="#96c102", font="System 20 bold" , text="Normale",command=normal)
    bouton10.place(x=185,y=210)
    bouton11=Button(fen, relief=FLAT,fg="#232d08", bg="#96c102", font="System 20 bold" , text="Difficile",command=difficile)
    bouton11.place(x=330,y=210)
    bouton12=Button(fen, relief=FLAT,fg="#232d08", bg="#96c102", font="System 20 bold" , text="Beaucoup trop rapide pour toi",command=impossible)
    bouton12.place(x=50,y=248)

    texte5 =Label(fen, fg="#232d08", bg="#96c102", font="System 20 bold" , text="Mode de Jeu")
    texte5.place(x=160,y=320)
    bouton12=Button(fen, relief=FLAT,fg="#232d08", bg="#96c102", font="System 20 bold" , text="1 Joueur",command=unserp)
    bouton12.place(x=70,y=350)
    bouton13=Button(fen, relief=FLAT,fg="#232d08", bg="#96c102", font="System 20 bold" , text="2 Joueurs (VS)",command=deuxserp)
    bouton13.place(x=230,y=350)



## Recupère les Touches ##

def left(event):
    global dx,dy,direction
    if direction == "droite":
        direction = "droite"
    else :
        dx = -10
        dy = 0
        direction = "gauche"
     
def right(event):
    global dx,dy,direction
    if direction == "gauche":
        direction = "gauche"
    else :
        dx = 10
        dy = 0
        direction = "droite"
    
def up(event):
    global dy,dx,direction
    if direction == "bas":
        direction = "bas"
    else :    
        dy = -10
        dx = 0
        direction = "haut"
    
def down(event):
    global dy,dx,direction
    if direction == "haut":
        direction = "haut"
    else :
        dy = 10
        dx = 0
        direction = "bas"

def left2(event):
    global dxx,dyy,direction
    if direction == "droite2":
        direction = "droite2"
    else :
        dxx = -10
        dyy = 0
        direction = "gauche2"
     
def right2(event):
    global dxx,dyy,direction
    if direction == "gauche2":
        direction = "gauche2"
    else :
        dxx = 10
        dyy = 0
        direction = "droite2"
    
def up2(event):
    global dyy,dxx,direction
    if direction == "bas2":
        direction = "bas2"
    else :    
        dyy = -10
        dxx = 0
        direction = "haut2"
    
def down2(event):
    global dyy,dxx,direction
    if direction == "haut2":
        direction = "haut2"
    else :
        dyy = 10
        dxx = 0
        direction = "bas2"



## Couleur ##


        
def rouge():
    global couleur
    couleur="#fe5252"
def bleu():
    global couleur
    couleur="#036db1"
def jaune():
    global couleur,line
    couleur="#ffec35"
    line="black"
def noir():
    global couleur
    couleur="#232d08"



## Difficulté ##


    
def facile():
    global vite,niveau
    vite = 0
    niveau = "Facile"
def normal():
    global vite,niveau
    vite = 30
    niveau = "Normal"
def difficile():
    global vite,niveau
    vite = 70
    niveau = "Difficile"
def impossible():
    global vite,niveau
    vite = 90
    niveau = "Hardcore"


## Selection de la Version de Jeu ##

def unserp():
    global v
    v = 1

def deuxserp():
    global v
    v = 2

def lancement():
    global v
    if v == 1:
        Start()
        
    if v == 2:
        Start2()


## Règles ##

def regle() :
    global can, bouton1,bouton3
    bouton1.destroy()
    bouton3.destroy()
    background_label.destroy()
    can.destroy()
    can = Canvas(fen, width=500, height=500, bg='#96c102')
    can.pack()
    
    texte1 =Label(fen, fg="#232d08", bg="#96c102", font="System 30 bold" , text="REGLES DU JEU")
    texte1.place(x=30,y=35)
    texte2 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="VOUS DEVEZ DIRIGER LE")
    texte2.place(x=30,y=100)
    texte3 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="SERPENT GRÂCE AUX FLÈCHES")
    texte3.place(x=30,y=130)
    texte4 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="DIRECTIONNELLES DU CLAVIER")
    texte4.place(x=30,y=160)
    texte5 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="POUR LE FAIRE NAVIGUER DANS")
    texte5.place(x=30,y=190)
    texte6 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="LE CADRE SANS TOUCHER LES")
    texte6.place(x=30,y=220)
    texte7 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="BORDS ET MANGER LES POINTS")
    texte7.place(x=30,y=250)
    texte8 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="ROUGES QUI VOUS FERONT")
    texte8.place(x=30,y=280)
    texte9 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="GAGNER DES POINTS, ET ")
    texte9.place(x=30,y=310)
    texte10 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="ALLONGERA VOTRE SERPENT.")
    texte10.place(x=30,y=340)
    bouton1=Button(fen, text="SUIVANT -->",relief=FLAT,fg="#232d08", bg="#96c102", font="System 20 bold",command=regle2)
    bouton1.place(x=20,y=420)


def regle2():
    global can
    can.destroy()
    can = Canvas(fen, width=500, height=500, bg='#96c102')
    can.pack()
    
    texte1 =Label(fen, fg="#232d08", bg="#96c102", font="System 30 bold" , text="REGLES DU JEU")
    texte1.place(x=30,y=35)
    texte11 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="VOTRE BUT EST D'AVOIR LE ")
    texte11.place(x=30,y=100)
    texte12 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="PLUS GRAND SERPENT !")
    texte12.place(x=30,y=130)
    texte13 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="MODE VS (2 JOUEURS)")
    texte13.place(x=30,y=210)
    texte14 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="LE SERPENT BLANC SE ")
    texte14.place(x=30,y=250)
    texte15 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="CONTROLE AVEC LES TOUCHES ")
    texte15.place(x=30,y=280)
    texte16 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="Z,Q,S,D ET L'AUTRE SERPENT ")
    texte16.place(x=30,y=310)
    texte17 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="AVEC LES FLECHES ")
    texte17.place(x=30,y=340)
    texte18 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="DIRECTIONNELLES.  ")
    texte18.place(x=30,y=370)
    
    bouton1=Button(fen, text="SUIVANT -->",relief=FLAT,fg="#232d08", bg="#96c102", font="System 20 bold",command=regle3)
    bouton1.place(x=20,y=420)
    bouton2=Button(fen, text="<-- PRECEDENT",relief=FLAT,fg="#232d08", bg="#96c102", font="System 20 bold",command=regle)
    bouton2.place(x=270,y=420)

def regle3():
    global can
    can.destroy()
    can = Canvas(fen, width=500, height=500, bg='#96c102')
    can.pack()
    
    texte1 =Label(fen, fg="#232d08", bg="#96c102", font="System 30 bold" , text="REGLES DU JEU")
    texte1.place(x=30,y=35)
    
    texte17 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="LE PREMIER QUI TOUCHE LE  ")
    texte17.place(x=30,y=100)
    texte18 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="BORD OU QUI SE MORD LA  ")
    texte18.place(x=30,y=130)
    texte19 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="QUEUE VOIT SON SCORE")
    texte19.place(x=30,y=160)
    texte22 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="DIVISER PAR DEUX.")
    texte22.place(x=30,y=190)
    texte20 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="LE JOUEUR AVEC LE PLUS ")
    texte20.place(x=30,y=220)
    texte21 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="GRAND SCORE GAGNE LA PARTIE.")
    texte21.place(x=30,y=250)
    texte21 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="ATTENTION, N'ENCHAINER PAS ")
    texte21.place(x=30,y=300)
    texte22 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="TROP RAPIDEMENT LES ")
    texte22.place(x=30,y=330)
    texte23 =Label(fen, fg="#232d08", bg="#96c102", font="System 17" , text="TOUCHES, OU VOUS PERDEZ ;-)")
    texte23.place(x=30,y=360)
    
    bouton1=Button(fen, text="JOUER !",relief=FLAT,fg="#232d08", bg="#96c102", font="System 20 bold",command=lancement)
    bouton1.place(x=20,y=420)

    bouton2=Button(fen, text="PARAMETRES",relief=FLAT,fg="#232d08", bg="#96c102", font="System 20 bold",command=parametre)
    bouton2.place(x=280,y=420)

    
#######################################################################################################	
	
## Programme principal ##

#Serpent1

x = [245,245]
y = [245,245]
dx = 10
dy = 0

#Serpent2

xx=[245,245]
yy=[140,140]
dxx = -10
dyy = 0

#Autre

pX = randrange(5, 495)
pY = randrange(5, 495)
food = 0
score = 0
score2 = 0
rectangle = []
rectangle2 =[]
direction = 0
texte = []
texte1 = []
texte2 = []
perdu = 0
v = 1
vite = 30
vitesse = 100-vite
niveau = "Normal"


aze = 1
param = 0

couleur="#232d08"
line="white"



fen = Tk()

fen.title("SNAKE - Kévin / Sitpi / Yoan")
fen.geometry("500x500")
fen.configure(bg="#96c102")
can = Canvas(fen, width=500, height=500, bg='#96c102')



fond = PhotoImage(file = "Snakegreen.gif")

rougee = PhotoImage(file = "rouge.gif")
bleuu = PhotoImage(file = "bleu.gif")
jaunee = PhotoImage(file = "jaune.gif")
noirr = PhotoImage(file = "noire.gif")


background_label = Label(fen, image=fond)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.pack()

can.pack()

bouton1=Button(fen, text="JOUER",relief=FLAT,fg="#232d08", bg="#96c102", font="System 40 bold",command=lancement)
bouton1.place(x=133,y=210)
bouton4=Button(fen, text="REGLES",relief=FLAT,fg="#232d08" ,bg="#96c102", font="System 40 bold",command=regle)
bouton4.place(x=117,y=290)
bouton3=Button(fen, text="PARAMETRES",relief=FLAT,fg="#232d08" ,bg="#96c102", font="System 40 bold",command=parametre)
bouton3.place(x=40,y=370)

fen.resizable(width="false",height="false")
fen.mainloop()
