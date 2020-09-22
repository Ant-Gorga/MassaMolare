import tkinter as tk
import MassaMolare as mm

def btncliccato():
    global input_box , risultato_box , str_risposta
    formula = input_box.get()
    ris = mm.MassaMolare(formula)
    if ris!=ValueError:
        str_risposta.set("La massa molare di " + formula +" è : " +str(ris)+" ")
    else:
        str_risposta.set("Controlla la formula")

    risultato_box.grid(row=3,column=0)


windows = tk.Tk()
input_box = tk.Entry(windows)
input_box.focus()
str_risposta = tk.StringVar() #StringVar definita da tk appositamente per questo, si aggiorna ad ogni set

button = tk.Button(windows,text="Calcola",command=btncliccato)
msg = tk.Label(windows,text="Inserisci la formula del composto:")
risultato_box = tk.Label(windows,textvariable=str_risposta)


windows.geometry("300x200")
windows.title("Calcola La Massa Molare")
windows.resizable(False,False)

msg.grid(row=0,column=0, sticky="N",padx=50)
input_box.grid(row=1,column=0,pady=20)
button.grid(row=2,column=0,pady=20)

windows.mainloop()
