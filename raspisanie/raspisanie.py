from tkinter import *

#tunniplaan={}
#file=open("TextFile1.txt",'r')
#for line in file:
#    k, v=line.strip().split('-')
#    tunniplaan[k.strip()]=v.strip()

#print(tunniplaan)



root=Tk()
root.title("Расписание")
root.geometry("1280x1024")

p=['Monday','Tuesday','Wednesday','Thursday','Friday']
j=0
for i in range(1,10,2):
    Monday=Label(root,text=p[j],font="Calibri 18",relief="groove").grid(row=i,column=0,rowspan=2,sticky=N+S+W+E)
    j+=1

for i in range(11):
    tn="t"+str(i)
    t0=Label(root,text=i,font="Calibri 18",relief="groove",width=5).grid(row=0,column=i+1,sticky=N+S+W+E)


Multimeedia1=Button(root,text="Multimeedia",bg="#6495ED",font="Calibri 18").grid(row=1,column=2,columnspan=2,sticky=N+S+W+E)
Multimeedia2=Button(root,text="Multimeedia",bg="#6495ED",font="Calibri 18").grid(row=2,column=5,columnspan=2,sticky=N+S+W+E)
Programmeerimise1=Button(root,text="Programmeerimise alused",bg="#9ACEEB",font="Calibri 18").grid(row=1,column=5,columnspan=3,sticky=N+S+W+E)
Programmeerimise2=Button(root,text="Programmeerimise alused",bg="#9ACEEB",font="Calibri 18").grid(row=2,column=2,columnspan=3,sticky=N+S+W+E)
Rühmajuhatajatund=Button(root,text="Rühmaju\nhataja\ntund",bg="#9ACEEB",font="Calibri 18").grid(row=1,column=8,rowspan=2,sticky=N+S+W+E)
Inglisekeel1=Button(root,text="Inglise keel",bg="#ECEABE",font="Calibri 18").grid(row=3,column=2,columnspan=2,sticky=N+S+W+E)
Operatsioonisüsteemidealused=Button(root,text="Operatsioonisüstee\nmide alused",bg="#C154C1",font="Calibri 18").grid(row=3,column=4,rowspan=2,columnspan=2,sticky=N+S+W+E)
Inglisekeel2=Button(root,text="Inglise keel",bg="#C9A0DC",font="Calibri 18").grid(row=4,column=2,columnspan=2,sticky=N+S+W+E)
Kehalinekasvatus=Button(root,text="Kehaline kasvatus",bg="#DE4C8A",font="Calibri 18").grid(row=3,column=7,rowspan=2,columnspan=2,sticky=N+S+W+E)
Eestikeel1=Button(root,text="Eesti Keel",bg="#C9A0DC",font="Calibri 18").grid(row=3,column=9,sticky=N+S+W+E)
Eestikeel2=Button(root,text="Eesti Keel",bg="#9C9C9C",font="Calibri 18").grid(row=4,column=9,sticky=N+S+W+E)
Inimgeograafia=Button(root,text="Inimgeograafia",bg="#FCDD76",font="Calibri 18").grid(row=3,column=10,rowspan=2,sticky=N+S+W+E)
Programmeerimise1=Button(root,text="Programmeerimise alused",bg="#9ACEEB",font="Calibri 18").grid(row=5,column=2,columnspan=3,sticky=N+S+W+E)
Multimeedia1=Button(root,text="Multimeedia",bg="#6495ED",font="Calibri 18").grid(row=6,column=2,columnspan=3,sticky=N+S+W+E)
Multimeedia2=Button(root,text="Multimeedia",bg="#6495ED",font="Calibri 18").grid(row=5,column=6,columnspan=3,sticky=N+S+W+E)
Programmeerimise2=Button(root,text="Programmeerimise alused",bg="#9ACEEB",font="Calibri 18").grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
Kunstiained=Button(root,text="Kunstiained",bg="#FF43A4",font="Calibri 18").grid(row=5,column=9,rowspan=2,columnspan=2,sticky=N+S+W+E)
Andmebaasisüsteemidealused=Button(root,text="Andmebaasisüstee\nmide alused",bg="#FC6C85",font="Calibri 18").grid(row=7,column=2,rowspan=2,columnspan=2,sticky=N+S+W+E)
Andmebaasisüsteemidealused=Button(root,text="Andmebaasisüstee\nmide alused",bg="#FC6C85",font="Calibri 18").grid(row=7,column=4,rowspan=2,columnspan=3,sticky=N+S+W+E)
Inimgeograafia=Button(root,text="Inimgeograafia",bg="#FCDD76",font="Calibri 18").grid(row=7,column=7,rowspan=2,sticky=N+S+W+E)
Eestikeel1=Button(root,text="Eesti Keel",bg="#C9A0DC",font="Calibri 18").grid(row=7,column=8,sticky=N+S+W+E)
Eestikeel2=Button(root,text="Eesti Keel",bg="#9C9C9C",font="Calibri 18").grid(row=8,column=8,sticky=N+S+W+E)
Keeljakirjandus=Button(root,text="Keel ja kirjandus",bg="#B2EC5D",font="Calibri 18").grid(row=9,column=3,rowspan=2,columnspan=2,sticky=N+S+W+E)
Matemaatika=Button(root,text="Matemaatika",bg="#CB6586",font="Calibri 18").grid(row=9,column=6,rowspan=2,columnspan=2,sticky=N+S+W+E)
Suhtleminejaklienditeenindus=Button(root,text="Suhtlemine ja\nklienditeenindus",bg="#9D81BA",font="Calibri 18").grid(row=9,column=8,rowspan=2,columnspan=2,sticky=N+S+W+E)
Inimgeograafia=Button(root,text="Inimgeograafia",bg="#FCDD76",font="Calibri 18").grid(row=9,column=10,rowspan=2,sticky=N+S+W+E)








root.mainloop()


























#Label(text="Имя:").grid(row=0, column=0)
#table_name=Entry(width=30)
#table_name.grid(row=0, column=1,columnspan=3)

#Label(text="Столбцов:").grid(row=1, column=0)
#table_column=Spinbox(width=7,from_=1,to=50)
#table_column.grid(row=1,column=1)
#Label(text="Строк:").grid(row=1,column=2)
#table_row=Spinbox(width=7,from_=1,to=100)
#table_row.grid(row=1,column=3)

#Button(text="Справка:").grid(row=2,column=0)
#Button(text="Вставить").grid(row=2,column=2)
#Button(text="Отменить").grid(row=2,column=3)