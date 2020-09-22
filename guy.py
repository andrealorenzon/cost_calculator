from tkinter import *
import pandas as pd

try:
	data = pd.read_csv("dati.csv")
except Exception as ex:
	print(ex)
	quit()

macchine = set(data["Macchina"])
processi = set(data["Processo"])

window = Tk()

window.title("Process Cost")
window.geometry('300x300')

lbl = Label(window, text="{} data loaded.\nSelect parameters.".format(len(data)))
lbl.grid(column=0, row=1)

from tkinter.ttk import *

outcome = StringVar()
outcome.set("")

def callback_M(eventObject):
    # you can also get the value off the eventObject
    selected = eventObject.widget.get()
    proc = data[data['Macchina']==selected]
    p['values'] = tuple(set(proc['Processo']))
    p.configure(state='enabled')

m = Combobox(window)
m['values'] = tuple(macchine)
m.bind("<<ComboboxSelected>>", callback_M)
m.grid(column=0, row=2)

def callback_P(eventObject):
	macchina = m.get()
	print(macchina)
	processo = p.get()
	print(processo)
	selected = data[data['Macchina']==macchina][data['Processo']==processo]
	result = selected[['Nome S.','costo Unitario']]
	totale = float(selected[['costo Unitario']].sum())
	to_show = "Component --> Unit Cost\n"+"="*20+"\n"
	for item in result.iterrows():
		to_show+=str(item[1]['Nome S.'])+" --> "+str(item[1]['costo Unitario'])+"\n"
		
	to_show+="\n"+"="*20+"\nTotal: {}".format(totale)

	outcome.set(to_show)

p = Combobox(window)
p.bind("<<ComboboxSelected>>", callback_P)
p.configure(state='disabled')
p.grid(column=0, row=3)

out = Label(window, textvariable=outcome)
out.grid(column=0, row=5)

window.mainloop()