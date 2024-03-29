from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as NP
import tkinter as T
from tkinter import ttk
from tkinter import *
from ttkbootstrap.toast import ToastNotification
import time
import datetime
import json
from tkinter import messagebox
import subprocess
import requests

#def __init__():
log_file=open('logs.txt',"a+")
S=open('settings.txt',"r")
settings=eval(S.read())
S.close()

conn_time=0
state_time = "Connection {} / Operating time {}"#avalible conn_timer

#Функция определения расположения всплывающего уведомления
def __c__():
    s=wnd.geometry()
    x=int(s[0:s.find('x')])+int(s[s.find('+')+1:s.rfind("+")])-295#
    y=int(s[s.find("x")+1:s.find("+")])+int(s[s.rfind("+")+1:])-45#
    return[x,y,'nw']#


def showGr(pole, type):
    #global CONN_STATE
    if not CONN_STATE.get():
        #warning msgbox
        messagebox.showwarning(title='',message='You are not connect to database, there is no data to show!')
        return
    
    fig = Figure(figsize=(5,5))
    ax=fig.add_subplot(1,1,1)

    ox=NP.linspace(0,2*NP.pi,100)
    if type=='a':
        oy=NP.sin(ox)
    elif type=='b':
        oy=NP.cos(ox)
    elif type == 'c':
        oy=NP.sin(ox)
    else:
        oy=NP.cos(ox)
    ax.plot(ox,oy)
    
    toast=ToastNotification(title="",duration=3000,bootstyle="DARK", position=__c__(),message="Graphic accomplish")
    toast.show_toast()
    for i in list(pole.children.values()):
        i.destroy()
    v=FigureCanvasTkAgg(fig,master=pole)#wnd
    v.draw()
    v.get_tk_widget().pack()#wnd,width=200,height=200,bg='white'

#Method to display & update time of currient connection    
def conn_timer():
    global conn_time
    global state_time
    #global CONN_STATE
    if CONN_STATE.get():
        t=datetime.timedelta(seconds=time.time()-conn_time)
        status.config(text=state_time.format("available",t))#str(),"%H:%M:%S"time.strptime(str(time.localtime()),"%H : %M : %S")
        status.after(10, conn_timer)
    else:
        status.config(text=state_time.format("unavailable", str(0)))

def ttt(a,b,c):
    CURR_TIME.set(time.strftime("%d-%m-%Y %H:%M:%S"))

#Method to sent request to API
def bindBD(a):#addr
    #global CONN_STATE
    global conn_time
    global settings
    addr=addr_input.get()
    settings["address"]=addr
    print(settings)
    if CONN_STATE.get():
        btn_conn['text']="Connect"
        addr_input['state']='normal'
        CONN_STATE.set(False)
        addLog(f"user disconnect from database \"{addr}\" at {CURR_TIME.get()}. The connection lasted = {datetime.timedelta(seconds=time.time()-conn_time)}\n")
        conn_time=0
    else:
        if addr=="":# or 
            messagebox.showwarning(title='',message='Wrong address of Database!')
            return
        
        #проверка подключения
        #----------------------------------------------------------------
        response = requests.get(addr)
        # print(type(response), response.text)
        data = """{ "NetworkDevices" : """ + response.text + "}"
        data = json.loads(data)
        print(type(data))
        with open('Data.json', 'r') as file:
            json.dump(data, file, indent = 3)
            # data = json.load(file)
        print(data)
        #----------------------------------------------------------------
        #if connection is successful conn_time start/status = available
        btn_conn['text']="Disconnect"
        addr_input['state']="disabled"
        conn_time = time.time()
        CONN_STATE.set(True)
        addLog(f"successful connect to database \"{addr}\" at {CURR_TIME.get()}\n")
        #else
            #addLog("fail connection to database \"{addr}\" at {CURR_TIME.get()}\n")
        toast=ToastNotification(title="Warning!", duration=3000, bootstyle="DARK", position=__c__(), message=addr)# 
        toast.show_toast()

#
def getLogs():
    #new window file. open(logs) readline()
    subprocess.run('start C:\\Users\\Admn\\Documents\\test.txt', check=True)
    #print(graph_pole_1.winfo_geometry())
    #info['text']=LOGS.get()#=T.Label(f_log,text=LOGS.get())
    #info.pack(side = LEFT, expand=True, fill='x')

def addLog(str):
    log_file.write(str)
    log_file.truncate()
    info.insert(END, str)
#
def changeStat(a,b,c):
    conn_timer()

#def logsChanged():
#   global from_log
#   from_log=log_file.readlines()

def getGraph(ev, fr): #fr=frame  
    if fr==1:
        pole=graph_pole_1
        msg=graph_type_1.get()
        types=_t.copy()
        types.remove(msg)
        graph_type_2['values']=types
    else:
        msg=graph_type_2.get()
        pole=graph_pole_2
        types=_t.copy()
        types.remove(msg)
        graph_type_1['values']=types
    log_file.write(f"GRAPH APPEARANCE {msg} successful\n")
    log_file.truncate()
    showGr(pole,msg)#убрать?

#MAIN()
#Create main window
wnd =T.Tk()
wnd.title("GRAPH")
wnd.geometry('1300x900')

#Create frame for a BD connection and tracking it status
f_conn=T.LabelFrame(wnd,text='0')
l=settings["address"]

addr_input = T.Entry(f_conn)#input address of database
addr_input.insert(0,l)
addr_input.bind('<Return>', bindBD)
addr_input.pack(side=LEFT, expand=True, fill='x', padx=20, pady=30)
addr_input.focus_set()

btn_conn=T.Button(f_conn, text="Connect",command = lambda: bindBD(1))#=>disconnect
btn_conn.pack(side=LEFT, pady=30)

status =T.Label(f_conn, text=state_time,width=100)#"Connection{un/avalible}/Operating time {conn_timer}"
status.pack(side=RIGHT,padx=20, pady=30)
f_conn.pack(side=TOP, fill='x')

#Create frame for visualization graphics
F_graph=T.Frame(wnd)
f_graph1=T.LabelFrame(F_graph,text='1')
#Названия графиков
types=['a','b','c','d'] 
_t=['a','b','c','d']
graph_type_1 =ttk.Combobox(f_graph1,values=types, state='readonly')#state=Disabled if value already choose
graph_type_1.bind("<<ComboboxSelected>>", lambda ev, f=1:getGraph(ev,f))
graph_type_1.pack(side=TOP)
graph_pole_1=T.Canvas(f_graph1,width=500,height=500,bg='black')
graph_pole_1.pack(side=BOTTOM)
f_graph1.pack(side=LEFT,expand=True, fill=BOTH)

#Create frame for visualization graphic #2
f_graph2=T.LabelFrame(F_graph,text='2')
graph_type_2 =ttk.Combobox(f_graph2,values=types)
graph_type_2.bind("<<ComboboxSelected>>", lambda ev, f=2:getGraph(ev,f))
graph_type_2.pack(side=TOP)
graph_pole_2=T.Canvas(f_graph2,width=500,height=500,bg='black')
graph_pole_2.pack(side=BOTTOM)
f_graph2.pack(side=RIGHT,expand=True, fill=BOTH)
F_graph.pack(side=TOP, anchor='center', fill=BOTH)

#Create frame for getting logs of the program
f_log=T.LabelFrame(wnd,text="LOG")
info=T.Text(f_log,state="normal",wrap="word")#.Label(f_log, text=str)
scrl=T.Scrollbar(orient="vertical", command=info.yview)
info.pack(side = LEFT, expand=True, fill='x')
btn_log=T.Button(f_log, text="Open LogFile",command = getLogs)
btn_log.pack(side=LEFT)
f_log.pack(side = LEFT, expand=True, fill='x') #side=BOTTOM, fill='x'

CURR_TIME=StringVar()
CURR_TIME.trace_add('read',ttt)
CONN_STATE=BooleanVar()
CONN_STATE.trace_add('write',changeStat)

log_file.write("app_start at {}\n".format(CURR_TIME.get()))
log_file.truncate()


wnd.mainloop()

#when app close 
#def destroy():
log_file.write("app_end at {}\n".format(CURR_TIME.get()))
log_file.truncate()
log_file.close()
S=open('settings.txt',"w")
S.write(str(settings))
S.truncate()
#Backend TkAgg is interactive backend. Turning interactive mode on.