from ivy.std_api import *

nbAgent = 0
msg = ""

def nbAgent():
    global nbAgent
    nbAgent = 1 + nbAgent

def creat_agent(name, readMsg=""):
    """
    """
    IvyInit(name, readMsg, 0, on_connection_change, on_die)
    IvyStart()
    IvyBindMsg(get_msg, "(.*)")


def get_msg(*args):
    global msg
    print(f"{args[0]} a envoyé {str(args[1:])}, taille : {len(args[1:])}")
    msg = str(args[1:])

def msg_sur_bus():
    return msg
 
def sendMsg(msg):
    IvySendMsg(msg)
     
def on_die(*arg):
    print(f"L'ordre de terminaison de l'agent {arg[0]} de l'identifiant {str(arg[1])}")
    IvyStop()

def on_connection_change(agent, event):
    print(len(IvyGetApplicationList()))

    if event == IvyApplicationDisconnected:
        print(f"L'agent {agent} vient de se deconnecter.")
        
    if event == IvyApplicationConnected:
        nbAgent()
        print(f"mise à jour des agents : {IvyGetApplicationList()}")
