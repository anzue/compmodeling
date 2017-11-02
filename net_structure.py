import Tkinter as tk
from random import random
counter = 0



root = tk.Tk()
root.title("site visitors")
label = tk.Label(root, fg="dark green")
label.place()


xMul = 1000
yMul = 600

w = tk.Canvas(root, width=xMul, height=yMul)
w.pack()

#button = tk.Button(root, text='2', width=1, command=root.destroy)
#button.place(relx = .1,rely = .1)





selected = 0


def pressed(site):
    global selected
    if selected == 0:
        selected = site
    else:
        if selected == site:
            return
        add = 0
        if selected.y>site.y:
            add = 30
        w.create_line(selected.x*xMul+30, selected.y*yMul+add, site.x*xMul+30, site.y*yMul+add,arrow=tk.LAST)
        selected.links.append(site)
        #site.links.append(selected)
        selected = 0
        #site.recalc(6,0)
        recalc()


class Site:


    def __init__(self,nom):
        self.links = []
        self.value = 100.
        self.x = random();
        self.y = random();
        self.nom = nom
        self.button = tk.Button(root, text=str(nom) + " " + str(self.value), width=5, command= lambda:pressed(self))
        self.button.place(relx = self.x,rely = self.y)

    def getValue(self):
        return self.value

    def recalc(self,deep,added):
        self.value+=added
        if(deep == 0):
            return 0
        tsum = 0.
        oldc = []
        for c in self.links:
            oldc.append(c.getValue())
            tsum+= c.getValue()

        self.value/=2.
        i = 0
        for c in self.links:
            c.recalc(deep-1,self.value*oldc[i]/tsum)
            i = i+1

        self.update()

    def update(self):
        self.button.config(text = str(self.nom) + " " + str(round(self.value,1)))
    def addLink(self,link):
        self.links.append(link)

x = []
for i in range(1,10):
    x.append(Site(i))

def recalc():
    sum = 100.*len(x)

    for it in range(1,100):
        for s in x:
            toRemove = s.value/sum*s.value
            removed = 0.
            for to in s.links:
                q = toRemove*to.value/(sum - s.value)
                removed += q
                to.value += q
                to.update()
            s.value -= removed
            s.update()
            print (removed,toRemove)

root.mainloop()
