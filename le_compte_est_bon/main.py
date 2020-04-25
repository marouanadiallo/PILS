#encoding:utf-8
from controller.controller import Controller
"""import tkinter as t

app = t.Tk()

l = t.Label(app, text="0 secondes")
l.pack()

sec = 0
id = None

def change_legende( id, s = 45,):
    global l
    
    s -=1
    l.config(text="%d secondes" %s)
    id = l.after(1000, lambda:change_legende(id, s))
    if s >= 0:
        l.after_cancel(id)
        
l.after(1000, lambda:change_legende(id, sec))

app.mainloop()"""

controller = Controller()

controller.lancer_la_vue()


#while s < 45:
#    s += sec.second