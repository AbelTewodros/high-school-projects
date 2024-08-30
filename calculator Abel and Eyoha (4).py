from math import*
import tkinter as tk
from typing import Text

def addition(variable1,variable2):#fonction pour l'addition de deux variables
    resultat=variable1+variable2
    return resultat
def soustraction(variable1,variable2):#fonction pour la soustraction de deux variables
    resultat=variable1-variable2
    return resultat
def multiplication(variable1,variable2):#fonction pour la multiplication de deux variables
    resultat=variable1*variable2
    return resultat
def division(variable1,variable2):#fonction pour la division de deux variables
    if variable2==0:
        print("Erreur")
        return
    else:
        resultat=variable1/variable2
        return resultat
def divisioneuclidiennes(variable1,variable2):#fonction pour la division euclidienneds de deux variables
    if variable2==0:
        print("Erreur")
        return
    else:
        reste = variable1%variable2
        resultat=variable1//variable2,"reste=",reste
        return resultat
def modulo(variable1,variable2):#fonction pour le reste d'une division de deux variables
    if variable2==0:
        print("Erreur")
        return
    else:
        resultat=variable1%variable2
        return resultat
def puissance(variable):#fonction pour mettre les variables au puissance
    puissance=float(input("puissance-->"))
    variable=variable**puissance
    return variable
def racine_carre():#fonction pour prendre le racine carre 
    variable1=float(input("valeur-->")) 
    return sqrt(variable1) 
def trig():

    trigtype=input("type trig-->")
    if trigtype=="cos":
        valeur=float(input("valeur-->"))
        resultat=cos(valeur)
        return resultat
    if trigtype=="sin":
        valeur=float(input("valeur-->"))
        resultat=sin(valeur)
        return resultat
    if trigtype=="tan":
        valeur=float(input("valeur-->"))
        resultat=tan(valeur)
        return resultat
def fraction_simple(v1,v2):
    simple = v1/gcd(v1,v2),v2/gcd(v1,v2)
    return simple
def absolute_value():
    variable=float(input("valeur-->"))
    resultat=abs(variable)
    return resultat
def resoudre_Equation_PremierDegre():
  print("Résolution d'une équation du type ax + b = c ") 
  a =float((input("a=")))
  b =float((input("b=")))
  c =float((input("c=")))
  x =(c-b)/a
  return x
def resoudre_Equation_2ndDegre():
    print ("Résolution d'une équation du type ax²+bx+c ")
    a = float(input("a="))
    b = float(input("b="))
    c = float(input("c="))
    d = (b**2)-(4*a*c) #calcule du discriminant
    if d < 0:
     return "Cette equation n'a pas une solution reel"
    elif d == 0:
     x = (-b+sqrt(d))/2*a
     return "Cette equation une solution: ", x
    else:
     x1 = (-b+sqrt(d))/2*a
     x2 = (-b-sqrt(d))/2*a
     return "Cette equation a deux solution: ", x1, " et ", x2



while True:
     print("Calculatrice Æ")
     calculatricetype=input("tu veux faire des calculs simple ou avancer? Saisir 'off' pour Eteindre")
     if calculatricetype=="avancer":
         variable1type=(input(" || **=puissance || trig=trigonométrie || normal=entier relatif || sqrt=racine carrée || décimal=nombre décimal || abs=valeur absolue || equation = equation 1er ou 2nd degree || ...choisissez l'un d'eux pour le type de la variable 1-->"))
         if variable1type == "equation":
             variable1 = (input("Resoudre une equation de 1er degree ou 2nd degree? || 1=1er degree || 2=2nd degree ||"))
             if variable1 == "1":
                variable1 = resoudre_Equation_PremierDegre()
                print(variable1)
             elif variable1 == "2":
                  variable1 = resoudre_Equation_2ndDegre()
                  print(variable1)
         if variable1type=="**":
             variable1=float(input("valeur-->"))
             variable1=puissance(variable1)
             print(variable1)
         elif variable1type=="sqrt":
             variable1=racine_carre()
             print(variable1)
         elif variable1type=="normal":
             variable1=int(input("valeur-->"))
         elif variable1type=="decimal":
             variable1=float(input("valeur-->"))
         elif variable1type=="trig":
             variable1=trig()
             print(variable1)
         elif variable1type=="abs":
             variable1=absolute_value()
             print(variable1)
         variable2type=(input(" || **=puissance || trig=trigonométrie || normal=entier relatif || sqrt=racine carrée || décimal=nombre décimal || abs=valeur absolue || equation = equation 1er ou 2nd degree || ...choisissez l'un d'eux pour le type de la variable 2-->"))
         if variable1type == "equation":
             variable1 = (input("Resoudre une equation de 1er degree ou 2nd degree? || 1=1er degree || 2=2nd degree ||"))
             if variable1 == "1":
                  variable1 = resoudre_Equation_PremierDegre()
                  print(variable1)
             elif variable1 == "2":
                  variable1 = resoudre_Equation_2ndDegre()
                  print(variable1)
         if variable2type=="**":
             variable2=float(input("valeur-->"))
             variable2=puissance(variable2)
             print(variable2)
         elif variable2type=="sqrt":
             variable2=racine_carre()
             print(variable2)
         elif variable2type=="normal":
             variable2=int(input("valeur-->"))
         elif variable2type=="decimal":
              variable2=float(input("valeur-->"))
         elif variable2type=="trig":
             variable2=trig()
             print(variable2)
         elif variable2type=="abs":
             variable2=absolute_value()
             print(variable2)
         operateur=input("Vous pouvez utiliser différents opérateurs.'+' pour l'addition, '-' pour la soustraction, '*' pour la multiplication, '/' pour la division,'//' pour la division euclidienne, '%' pour le reste et '_ ' pour simplifier une fraction (cet opérateur ne fonctionne que pour les entiers, donc les deux variables doivent être 'normales'. Operateur-->")
         if operateur=="+":
             print(variable1,"+",variable2,"=",addition(variable1,variable2))
         elif operateur=="-":    
             print(variable1,"-",variable2,"=",soustraction(variable1,variable2))
         elif operateur=="*":
            print(variable1,"*",variable2,"=",multiplication(variable1,variable2))
         elif operateur=="/":
             if variable2==0:
                 print("ERREUR, pas de division avec un zero comme denominateur, svp retourne toi au primaire")
             else:
                 print(variable1,"/",variable2,"=",division(variable1,variable2))
         elif operateur=="//":
             if variable2==0:
                 print("ERREUR, pas de division avec un zero comme denominateur, svp retourne toi au primaire")
             else:
                 print(variable1,"//",variable2,"=",divisioneuclidiennes(variable1,variable2))
         elif operateur=="%":
             if variable2==0:
                 print("ERREUR, pas de division avec un zero comme denominateur, svp retourne toi au primaire")
             else:
                 print(variable1,"%",variable2,"=",modulo(variable1,variable2))
         elif operateur=="_":
                 if variable2==0:
                     print("ERREUR, pas de fraction possible avec un zero comme denominateur, svp retourne toi au primaire")
                 else:
                     print(fraction_simple(variable1, variable2))
     elif calculatricetype=="simple":
         ORANGE = "#FF7D33"
         DARK_GRAY = "#444444"
         COULEUR_ETIQUETTES = "#FFFFFF"
         PETIT_TAILLE_POLICE = ( "Arial", 16)
         GRAND_TAILLE_POLICE = ( "Arial", 40, "bold")
         BLANC = "#FFFFFF"
         CHIFFRE_POLICE = ("ARIAL", 24, "bold")
         DEFAULT_TAILLE_POLICE = ("ARIAL", 20)
         BLACK = "#111111"
         class Calculatrice:
             def __init__(self): #__init__est le constructeur d'une classe et self est une paramètre qui fait référence à l'instance de l'objet 
                 self.page = tk.Tk() # Cree la page principale en utilisant la classe tk du tkinter
                 self.page.geometry("380x670")  # Hauteur et largeur de la page
                 self.page.resizable(0,0)  #désactiver le redimensionnement
                 self.page.title("Calculatrice Æ") #Nom du application
             #notre calculatrice a deux étiquettes d'affichage. Un pour afficher l'expression courante
             #Un pour afficher l'expression totale:
                 self.expression_totale = ""
  #Un pour afficher l'expression courante:
                 self.expression_courante = ""
  # pour créer des cadres pour l'ecrans et les boutons on fait:
                 self.cadre_affichage = self.cree_cadre_affichage()

                 self.etiquettes_totale, self.etiquettes = self.cree_etiquettes_affichage()

                 self.chiffre = {          #On place les chiffre 
                                 7: (1, 1), 8: (1, 2), 9: (1, 3),
                                 4: (2, 1), 5: (2, 2), 6: (2, 3),
                                 1: (3, 1), 2: (3, 2), 3: (3, 3),
                                 0: (4, 2), ".": (4, 1)
                                                      }
                 self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-","+": "+"}  #c'est un dictionnaire qui attribue l'opération arithmétique en python aux symboles de l'opérateur. Les valeurs représentent le symbole de division et de multiplication
                 self.boutons_cadre = self.cree_boutons_cadre()
  
                 self.boutons_cadre.rowconfigure(0,weight=1)
                 for x in range(1,5):
                     self.boutons_cadre.rowconfigure(x,weight=1)
                     self.boutons_cadre.columnconfigure(x,weight=1)
                     self.cree_bouton_chiffre()
                     self.cree_operateur_bouton()
                     self.cree_bouton_special()
                     self.lier_cles()
 
             def lier_cles(self):         #ceci fait que la calculatrice fonctionne avec le clavier
                 self.page.bind("<Return>", lambda event: self.evaluer())
                 for key in self.chiffre:
                     self.page.bind(str(key), lambda event, chiffre = key: self.add_expression(chiffre))
    
                 for key in self.operations:
                     self.page.bind(key, lambda event, operateur=key: self.add_operateur(operateur))

             def cree_bouton_special(self):
                 self.cree_bouton_supprimer() 
                 self.cree_bouton_egal()
                 self.cree_bouton_carre()
                 self.cree_bouton_raccine_carre()

  #méthode appelée étiquettes affichage pour créer ces étiquettes:
             def cree_etiquettes_affichage(self):
                 etiquettes_totale = tk.Label(self.cadre_affichage, text = self.expression_totale, anchor=tk.E, bg=DARK_GRAY, fg=COULEUR_ETIQUETTES, 
                 padx= 25, font=PETIT_TAILLE_POLICE) #anchor=tk.E va position le texte vers le cote E qui veut dire cote droite. padx met un peu d'espace entre le bouton et le bord droit de la fenêtre
   
                 etiquettes_totale.pack(expand=True, fill="both")
   
                 etiquettes = tk.Label(self.cadre_affichage, text = self.expression_totale, anchor=tk.E, bg=DARK_GRAY, fg=COULEUR_ETIQUETTES, 
                 padx= 25, font=GRAND_TAILLE_POLICE) 

                 etiquettes.pack(expand=True, fill="both")

                 return etiquettes_totale,etiquettes


             def cree_bouton_chiffre(self):
                 for chiffre,grid_value in self.chiffre.items():
                        bouton = tk.Button(self.boutons_cadre, text=str(chiffre), bg=BLANC, fg=ORANGE, font = CHIFFRE_POLICE, borderwidth=0, command=lambda x=chiffre: self.add_expression(x)) #puisque la commande doit être une fonction, je vais envelopper notre méthode avec lambda
                        bouton.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)  #pour placer des boutons dans la grille. sticky=tk.NSEW fait que les boutons collent de chaque côté et remplissent toute la grille.
 
             def cree_cadre_affichage(self):
                 cadre = tk.Frame(self.page, height = 220, bg=DARK_GRAY)  #donne de la taille ey du couleur pour le cadre d'affichage
                 cadre.pack(expand=True, fill="both")   #cet argument permettra à notre cadre de se développer et de remplir tous les espaces vides autour de lui
                 return cadre
             def add_expression(self, valeur):
                 self.expression_courante += str(valeur)
                 self.changer_ethiquettes()
 
             def add_operateur(self, operateur):
                 self.expression_courante += operateur
                 self.expression_totale += self.expression_courante
                 self.expression_courante = ""
                 self.changer_etiquettes_totale()
                 self.changer_ethiquettes()

             def cree_operateur_bouton(self):
                 i = 0
                 for operateur,symbole in self.operations.items():
                     bouton = tk.Button(self.boutons_cadre, text=symbole, bg=BLACK, font=DEFAULT_TAILLE_POLICE, borderwidth=0,command= lambda x=operateur: self.add_operateur(x))
                     bouton.grid(row=i, column=4,sticky=tk.NSEW)
                     i+=1

             def supprimer(self):   #ceci fait le bouton supprimer fonctioner
                 self.expression_courante = ""
                 self.expression_totale = ""
                 self.changer_etiquettes_totale()
                 self.changer_ethiquettes()

             def cree_bouton_supprimer(self):
                 bouton = tk.Button(self.boutons_cadre, text="C", bg=DARK_GRAY, font=DEFAULT_TAILLE_POLICE, borderwidth=0, command= self.supprimer)
                 bouton.grid(row=0, column=1, sticky=tk.NSEW)
 
             def carre(self):
                 self.expression_courante = str(eval(f"{self.expression_courante}**2"))
                 self.changer_ethiquettes()
             def cree_bouton_carre(self):
                 bouton = tk.Button(self.boutons_cadre, text="x\u00b2", bg=DARK_GRAY, font=DEFAULT_TAILLE_POLICE, borderwidth=0, command= self.carre) #Le valeur x\u00b2 représentent le symbole du carre
                 bouton.grid(row=0, column=2, sticky=tk.NSEW)

             def raccine_carre(self):
                 self.expression_courante = str(eval(f"{self.expression_courante}**0.5"))
                 self.changer_ethiquettes()
             def cree_bouton_raccine_carre(self):
                 bouton = tk.Button(self.boutons_cadre, text="\u221ax", bg=DARK_GRAY, font=DEFAULT_TAILLE_POLICE, borderwidth=0, command= self.raccine_carre)  #Le valeur \u221ax représentent le symbole du carre
                 bouton.grid(row=0, column=3, sticky=tk.NSEW)


             def evaluer(self): #ceci est une fonction qui evalue le resulta quand le bouton egal est toucher
                 self.expression_totale += self.expression_courante
                 self.changer_etiquettes_totale()
                 try:
                     self.expression_courante = str(eval(self.expression_totale))

                     self.expression_totale = ""
                 except Exception as e:
                         self.expression_courante = "Erreur"
                 finally:
                             self.changer_ethiquettes()

             def cree_bouton_egal(self):
                 bouton = tk.Button(self.boutons_cadre, text="=", bg=DARK_GRAY, font=DEFAULT_TAILLE_POLICE, borderwidth=0, command=self.evaluer)
                 bouton.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)


             def cree_boutons_cadre(self):
                 cadre = tk.Frame(self.page)
                 cadre.pack(expand=True, fill="both")
                 return cadre
 
             def changer_etiquettes_totale(self):
                     expression = self.expression_totale
                     for operateur,symbole in self.operations.items():
                         expression = expression.replace(operateur, f' {symbole} ')
                         self.etiquettes_totale.config(text=expression)

             def changer_ethiquettes(self):
                 self.etiquettes.config(text=self.expression_courante[:11])

             def run(self):  #fonction qui demarre la calculatrcie
                 self.page.mainloop() #boucle infinie utilisée pour exécuter l'application.

         if __name__ == "__main__": #permet de faire la distinction entre si on se trouve dans le module principal ou autre module importé.
                     calculatrice = Calculatrice()     #ne s'exécutera que si calculatrice.py est exécuté en tant que script à partir du terminal
                     calculatrice.run()
         
     elif calculatricetype=="off":
         break
     else:
         print("Je suis désolé mais je ne comprends pas ce que vous avez entré. Vous avez entré autre chose que '1','2' ou 'off'. Je ne comprends que ces 3 commandes donc je vous suggère de les utiliser. Si vous choisissez 1, vous pourrez saisir une variable et obtenir différents résultats tels que sa valeur absolue, sa racine carrée... Si vous choisissez 2, vous pourrez saisir 2 variables et les calculer. Vous pouvez additionner, multiplier, soustraire, simplifier des fractions... Vous avez également la possibilité de prendre la valeur absolue racine carrée... des variables. Mais n'essayez pas de simplifier une fraction avec un nombre flottant car cela ne fonctionnera malheureusement pas. Si vous choisissez de désactiver, la calculatrice s'éteindra. Entrez donc '1', '2' ou 'off', merci.")