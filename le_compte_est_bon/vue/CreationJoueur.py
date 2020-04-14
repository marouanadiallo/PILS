#encoding:utf-8

from tkinter import Frame, Entry, Label, Canvas, PhotoImage, StringVar
from vue.Bouton import Bouton
from datas.donnees_vue import PATH_CONNEXION

class CreationJoueur(Frame):
    """
    """
    
    def __init__(self, master):
        Frame.__init__(self,master)
        
        self.label_champ()
        #self.icon_creer()
        self.champ_saisie()
        
    
    def champ_saisie(self):
        self._pseudo = StringVar()
        Entry(self, font=("Helvetica", 10), textvariable=self._pseudo).grid(row=2, column=0)
    
    def bouton_creer(self, label, fn_callback):
        self._creer = Bouton(self, label, fn_callback).grid(row=4, column=0)
    
    def icon_creer(self):
        _t_icon = (50,50)
        _image = PhotoImage(file = PATH_CONNEXION).zoom(20).subsample(18)
        _icon = Canvas(self, width = _t_icon[0], height= _t_icon[1], bd=0, highlightthickness=0)
        _icon.create_image(_t_icon[0]/2, _t_icon[1]/2, image = _image)
        _icon.grid(row=1, column=0)
    
    def label_champ(self):
        Label(self, text="Veuillez saisir un pseudo s'il vous plaît :", font=("Helvetica", 10)).grid(row=0, column=0)