"""HKUST D104 mini-project"""
"""Farm Simulation"""
"""
Animal
-> Fish:
    maxsize(dev later)
    feed
    sleep
    exercise

-> Duck:
    feed
    sleep
    exercise
    
-> Sheep:
    feed
    sleep
    exercise
   -> Ewe:
       feed
       sleep
       exercise => lamb exercise with ewe
   -> Lamb:
       feed  => Ewe hunger tiredness +
       sleep
       exercise
"""
import tkinter as tk

class Animal:

    def __init__(self, s, n):
        self.state = s
        self.size = n
        self.__happiness = 5
        self.__hunger = 5
        self.__tiredness = 5
        
    def SetHappiness(self, NewHappiness):
        self.__happiness = NewHappiness
        
    
    def GetHappiness(self):
        return self.__happiness
    
    def SetHunger(self, NewHunger):
        self.__hunger = NewHunger
        
    
    def GetHunger(self):
        return self.__hunger
    
    def SetTiredness(self, NewTiredness):
        self.__tiredness = NewTiredness
        
    
    def GetTiredness(self):
        return self.__tiredness
    
    def feed(self):
        """Feed the animal"""
        self.size += 1
   
    def sleep(self):
        """The animal sleeps"""
        self.__tiredness -= 5
        
    def exercise(self):
        """The animal moves around"""
        self.__tiredness += 2
        self.__hunger += 2
   
    def getState(self):
        """Get the state of the animal"""
        return self.state
    
    def getSize(self):
        """Get the size of the animal"""
        return self.size
    
    
class Fish(Animal):
    
    def __init__(self, s, n):
        Animal.__init__(self, s, n)
        self.maxSize = 5.0
    
    def setMaxSize(self, m):
        """Set maximum size of fish"""
        self.maxSize = m
        
    def feed(self): #overriding the Animal.feed()
        """Feed the fish"""
        self.size += 2
        if self.size >= self.maxSize:
            self.state = "BIG FISH"
        
class Duck(Animal):
    
    def __init__(self, s, n):
        Animal.__init__(self, s, n)
        
    def feed(self): #overriding the Animal.feed()
        """Feed the duck"""
        Animal.feed(self)
        if self.size == 3:
            self.state = "BIG DUCK"
            
class Sheep(Animal):
    
    def __init__(self, s, n):
        Animal.__init__(self, s, n)
        
    def feed(self):
        """Feed the sheep"""
        Animal.feed(self)
        if self.size == 7:
            self.state = "FAT SHEEP"
        elif self.size == 5:
            self.state = "Big SHEEP"
    
class Ewe(Sheep):
    
    def __init__(self, s, n):
      Sheep.__init__(self, s, n)


class Lamb(Sheep):
    
    def __init__(self, s, n):
        Sheep.__init__(self, s, n)
        
    def feed(self):
        Sheep.feed(self)
        if self.size > 3:
            self.state = "Small Sheep"


def thisFish_feed():
    thisFish.feed()
    NewHappiness = thisFish.GetHappiness() + 1
    NewHunger = thisFish.GetHunger() - 2
    thisFish.SetHappiness(NewHappiness)
    thisFish.SetHunger(NewHunger)
    fish_txt.delete("1.0", tk.END)
    fish_txt.insert(tk.END, f"{thisFish.getState()} fed\n")
    fish_label3["text"] = f"Hunger={thisFish.GetHunger()}"
    fish_label2["text"] = f"Happiness={thisFish.GetHappiness()}"

def thisFish_sleep():
    thisFish.sleep()
    fish_txt.delete("1.0", tk.END)
    fish_txt.insert(tk.END, f"{thisFish.getState()} slept\n")
    fish_label4["text"] = f"Tiredness={thisFish.GetTiredness()}"
    thisFish.SetHunger(thisFish.GetHunger() + 3)
    fish_label3["text"] = f"Hunger={thisFish.GetHunger()}"

def thisFish_exercise():
    thisFish.exercise()
    fish_txt.delete("1.0", tk.END)
    fish_txt.insert(tk.END, f"{thisFish.getState()} exercised\n")
    fish_label4["text"] = f"Tiredness={thisFish.GetTiredness()}"
    fish_label3["text"] = f"Hunger={thisFish.GetHunger()}"

def thisDuck_feed():
    thisDuck.feed()
    NewHappiness = thisDuck.GetHappiness() + 5
    NewHunger = thisDuck.GetHunger() - 1
    thisDuck.SetHappiness(NewHappiness)
    thisDuck.SetHunger(NewHunger)
    duck_txt.delete("1.0", tk.END)
    duck_txt.insert(tk.END, f"{thisDuck.getState()} fed\n")
    duck_label3["text"] = f"Hunger={thisDuck.GetHunger()}"
    duck_label2["text"] = f"Happiness={thisDuck.GetHappiness()}"

def thisDuck_sleep():
    thisDuck.sleep()
    duck_txt.delete("1.0", tk.END)
    duck_txt.insert(tk.END, f"{thisDuck.getState()} slept\n")
    duck_label4["text"] = f"Tiredness={thisDuck.GetTiredness()}"
    thisDuck.SetHunger(thisDuck.GetHunger() + 2)
    duck_label3["text"] = f"Hunger={thisDuck.GetHunger()}"

def thisDuck_exercise():
    thisDuck.exercise()
    duck_txt.delete("1.0", tk.END)
    duck_txt.insert(tk.END, f"{thisDuck.getState()} exercised\n")
    duck_label4["text"] = f"Tiredness={thisDuck.GetTiredness()}"
    duck_label3["text"] = f"Hunger={thisDuck.GetHunger()}"

def thisEwe_feed():
    thisEwe.feed()
    NewHappiness = thisEwe.GetHappiness() + 3
    NewHunger = thisEwe.GetHunger() - 3
    thisEwe.SetHappiness(NewHappiness)
    thisEwe.SetHunger(NewHunger)
    ewe_txt.delete("1.0", tk.END)
    ewe_txt.insert(tk.END, f"{thisEwe.getState()} fed\n")
    ewe_label3["text"] = f"Hunger={thisEwe.GetHunger()}"
    ewe_label2["text"] = f"Happiness={thisEwe.GetHappiness()}"

def thisEwe_sleep():
    thisEwe.sleep()
    ewe_txt.delete("1.0", tk.END)
    ewe_txt.insert(tk.END, f"{thisEwe.getState()} slept\n")
    ewe_label4["text"] = f"Tiredness={thisEwe.GetTiredness()}"
    thisEwe.SetHunger(thisEwe.GetHunger() + 3)
    ewe_label3["text"] = f"Hunger={thisEwe.GetHunger()}"

def thisEwe_exercise():
    thisEwe.exercise()
    ewe_txt.delete("1.0", tk.END)
    ewe_txt.insert(tk.END, f"{thisEwe.getState()} exercised\n")
    ewe_label4["text"] = f"Tiredness={thisEwe.GetTiredness()}"
    ewe_label3["text"] = f"Hunger={thisEwe.GetHunger()}"
    # lamb follows ewe
    thisLamb_exercise()
    
    
def thisLamb_feed():
    thisLamb.feed()
    NewHappiness = thisLamb.GetHappiness() + 3
    NewHunger = thisLamb.GetHunger() - 1
    thisLamb.SetHappiness(NewHappiness)
    thisLamb.SetHunger(NewHunger)
    #since the lamb is fed by the milk of ewe
    ewe_new_hunger = thisEwe.GetHunger() + 2
    ewe_new_tiredness = thisEwe.GetTiredness() + 2
    thisEwe.SetTiredness(ewe_new_tiredness)
    thisEwe.SetHunger(ewe_new_hunger)
    
    lamb_txt.delete("1.0", tk.END)
    ewe_txt.delete("1.0", tk.END)
    lamb_txt.insert(tk.END, f"{thisLamb.getState()} fed\n")
    lamb_label3["text"] = f"Hunger={thisLamb.GetHunger()}"
    lamb_label2["text"] = f"Happiness={thisLamb.GetHappiness()}"
    ewe_label3["text"] = f"Hunger={thisEwe.GetHunger()}"
    ewe_label4["text"] = f"Tiredness={thisEwe.GetTiredness()}"
    ewe_txt.insert(tk.END, f"{thisEwe.getState()}\n")
    
def thisLamb_sleep():
    thisLamb.sleep()
    lamb_txt.delete("1.0", tk.END)
    lamb_txt.insert(tk.END, f"{thisLamb.getState()} slept\n")
    lamb_label4["text"] = f"Tiredness={thisLamb.GetTiredness()}"
    thisLamb.SetHunger(thisLamb.GetHunger() + 3)
    lamb_label3["text"] = f"Hunger={thisLamb.GetHunger()}"
    
def thisLamb_exercise():
    thisLamb.exercise()
    lamb_txt.delete("1.0", tk.END)
    lamb_txt.insert(tk.END, f"{thisLamb.getState()} exercised\n")
    lamb_label4["text"] = f"Tiredness={thisLamb.GetTiredness()}"
    lamb_label3["text"] = f"Hunger={thisLamb.GetHunger()}"
 
thisFish = Fish("little fish", 0)
thisFish.setMaxSize(6)
thisFish.SetHappiness(3)
thisFish.SetHunger(5)
thisFish.SetTiredness(1)

thisDuck = Duck("little duck", 0)

thisEwe = Ewe("small sheep", 2)
thisEwe.SetHappiness(3)
thisEwe.SetHunger(10)
thisEwe.SetTiredness(5)
thisLamb =  Lamb("little lamb", 0)
thisLamb.SetHunger(20)



root = tk.Tk()
root.configure(background = "light yellow")
root.title("Farm")
root.geometry("900x400")


fish_txt = tk.Text(root, width=25, height=1)
fish_label1 = tk.Label(root, text="Fish", height=3, width=12)
fish_label2 = tk.Label(root,text=f"Happiness={thisFish.GetHappiness()}", height=3, width=12)
fish_label3 = tk.Label(root,text=f"Hunger={thisFish.GetHunger()}", height=3, width=12)
fish_label4 = tk.Label(root,text=f"Tiredness={thisFish.GetTiredness()}", height=3, width=12)
fish_bt1 = tk.Button(root, text="Feed", command=thisFish_feed, height=3, width=12)
fish_bt2 = tk.Button(root, text="Sleep", command=thisFish_sleep, height=3, width=12)
fish_bt3 = tk.Button(root, text="Exercise", command=thisFish_exercise, height=3, width=12)
fish_label1.grid(row=1, column=2)
fish_label2.grid(row=2, column=2)
fish_label3.grid(row=3, column=2)
fish_label4.grid(row=4, column=2)
fish_bt1.grid(row=5, column=2)
fish_bt2.grid(row=6, column=2)
fish_bt3.grid(row=7, column=2)
fish_txt.grid(row=8, column=2)

duck_txt = tk.Text(root, width=25, height=1)
duck_label1 = tk.Label(root, text="Duck", height=3, width=12)
duck_label2 = tk.Label(root,text=f"Happiness={thisDuck.GetHappiness()}", height=3, width=12)
duck_label3 = tk.Label(root,text=f"Hunger={thisDuck.GetHunger()}", height=3, width=12)
duck_label4 = tk.Label(root,text=f"Tiredness={thisDuck.GetTiredness()}", height=3, width=12)
duck_bt1 = tk.Button(root, text="Feed", command=thisDuck_feed, height=3, width=12)
duck_bt2 = tk.Button(root, text="Sleep", command=thisDuck_sleep, height=3, width=12)
duck_bt3 = tk.Button(root, text="Exercise", command=thisDuck_exercise, height=3, width=12)
duck_label1.grid(row=1, column=3)
duck_label2.grid(row=2, column=3)
duck_label3.grid(row=3, column=3)
duck_label4.grid(row=4, column=3)
duck_bt1.grid(row=5, column=3)
duck_bt2.grid(row=6, column=3)
duck_bt3.grid(row=7, column=3)
duck_txt.grid(row=8, column=3)

ewe_txt = tk.Text(root, width=25, height=1)
ewe_label1 = tk.Label(root, text="Ewe\n (mother sheep)", height=3, width=12)
ewe_label2 = tk.Label(root,text=f"Happiness={thisEwe.GetHappiness()}", height=3, width=12)
ewe_label3 = tk.Label(root,text=f"Hunger={thisEwe.GetHunger()}", height=3, width=12)
ewe_label4 = tk.Label(root,text=f"Tiredness={thisEwe.GetTiredness()}", height=3, width=12)
ewe_bt1 = tk.Button(root, text="Feed", command=thisEwe_feed, height=3, width=12)
ewe_bt2 = tk.Button(root, text="Sleep", command=thisEwe_sleep, height=3, width=12)
ewe_bt3 = tk.Button(root, text="Exercise", command=thisEwe_exercise, height=3, width=12)
ewe_label1.grid(row=1, column=4)
ewe_label2.grid(row=2, column=4)
ewe_label3.grid(row=3, column=4)
ewe_label4.grid(row=4, column=4)
ewe_bt1.grid(row=5, column=4)
ewe_bt2.grid(row=6, column=4)
ewe_bt3.grid(row=7, column=4)
ewe_txt.grid(row=8, column=4)

lamb_txt = tk.Text(root, width=25, height=1)
lamb_label1 = tk.Label(root, text="Lamb", height=3, width=12)
lamb_label2 = tk.Label(root,text=f"Happiness={thisLamb.GetHappiness()}", height=3, width=12)
lamb_label3 = tk.Label(root,text=f"Hunger={thisLamb.GetHunger()}", height=3, width=12)
lamb_label4 = tk.Label(root,text=f"Tiredness={thisLamb.GetTiredness()}", height=3, width=12)
lamb_bt1 = tk.Button(root, text="Feed", command=thisLamb_feed, height=3, width=12)
lamb_bt2 = tk.Button(root, text="Sleep", command=thisLamb_sleep, height=3, width=12)
lamb_bt3 = tk.Button(root, text="Exercise", command=thisLamb_exercise, height=3, width=12)
lamb_label1.grid(row=1, column=5)
lamb_label2.grid(row=2, column=5)
lamb_label3.grid(row=3, column=5)
lamb_label4.grid(row=4, column=5)
lamb_bt1.grid(row=5, column=5)
lamb_bt2.grid(row=6,column=5)
lamb_bt3.grid(row=7, column=5)
lamb_txt.grid(row=8, column=5)


root.mainloop()