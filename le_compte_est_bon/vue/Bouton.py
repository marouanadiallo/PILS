#encoding:utf-8
from tkinter import Button
class Bouton(Button):
    """
    """
    
    def __init__(self, master, label, function_callbak):
        Button.__init__(self, master)
        self._nom_fn_callback = function_callbak
        self._label = label
        
        self.config(text=self._label, command=self._nom_fn_callback)
    
    def fixer_des_options(self, **options):
        """
            Définie quelques options pour la mise en forme du bouton
        """
        self.config(options)
        