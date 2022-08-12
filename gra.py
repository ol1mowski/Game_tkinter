from cProfile import label
from distutils.cmd import Command
import tkinter as tk
from tkinter import N, ttk
from tkinter.messagebox import showinfo
import random
from turtle import back, bgcolor

from PIL import Image, ImageTk

aLiczbaJestWieksza = "\nSzukana liczba jest większa, \nspróbuj ponownie wpisać jakąś liczbę\n"
bLiczbaJestMniejsza = "\nSzukana liczba jest mniejsza, \nspróbuj ponownie wpisać jakąś liczbę\n"
cZgadzaSie = "\nBrawo, gratuluję, zgadłeś liczbę!\mTo faktycznie ta liczba: "

a = 0
b = 99
n = random.randint(a, b)

text_color = "#ffeeee"
bg_color = "#111133"


def global_n_randint(a1, b1):
    global n
    n = random.randint(a1, b1)

class Podaj_liczbe_poczatek:
    
    def __init__(self):
        self.okno = tk.Toplevel()
        self.okno.wm_title("Podaj liczbe a")
        self.okno.grab_set()
        self.l = tk.Label(self.okno, text="Podaj liczbę początku przedziału losowania")
        self.l.grid(row=0, column=0)
        
        self.text1 = tk.Entry(self.okno)
        self.text1.grid(row=1, column=0)
        self.b = ttk.Button(self.okno, text="OK", command=self.sprawdzenie_poprawnosci)
        self.b.grid(row=1, column=1)
        
    def sprawdzenie_poprawnosci(self):
        global b
        global a
        t = self.text1.get()
        podany_tekst = t
        try:
            liczba = int(podany_tekst)
            a = liczba
            if a > b:
                popup_showinfo("Błąd", "Podana liczba jest większa niż górna granica.\nNajpierw zwiększ górną granicę.")
            else:
                app.l1text.set(
                    "\nAby rozpocząć grę,\nwpisz liczbę całkowitą z przedziału od " + str(a) + " do " + str(b) + "\nktóra Twoim zdaniem zostanie wylosowana :\n")
                global_n_randint(a,b)
        except:
            popup_showinfo("Błąd", "Podane znaki to nie jest liczba całkowita")
        self.okno.grab_release()
        self.okno.destroy()
        
class Podaj_liczbe_koniec:
    
    def __init__(self):
        self.okno = tk.Toplevel()
        self.okno.wm_title("Podaj liczbe b")
        self.okno.grab_set()
        self.l = tk.Label(self.okno, text="Podaj liczbę końca przedziału losowania")
        self.l.grid(row=0, column=0)
        
        self.text1 = tk.Entry(self.okno)
        self.text1.grid(row=1, column=0)
        self.b = ttk.Button(self.okno, text="OK", command=self.sprawdzenie_poprawnosci)
        self.b.grid(row=1, column=1)
    
    def sprawdzenie_poprawnosci(self):
        global b
        global a
        t = self.text1.get()
        podany_tekst = t
        try:
            liczba = int(podany_tekst)
            a = liczba
            if a > b:
                popup_showinfo("Błąd", "Podana liczba jest mniejsza niż górna granica.\nNajpierw zwiększ górną granicę.")
            else:
                app.l1text.set(
                    "\nAby rozpocząć grę,\nwpisz liczbę całkowitą z przedziału od " + str(a) + " do " + str(b) + "\nktóra Twoim zdaniem zostanie wylosowana :\n")
                global_n_randint(a,b)
        except:
            popup_showinfo("Błąd", "Podane znaki to nie jest liczba całkowita")
        self.okno.grab_release()
        self.okno.destroy()
    
def popup_showinfo(title="Window", tekst="Hello World!"):
    showinfo(title, tekst)

class EntryRozszerzone(tk.Entry):
    #konstruktor klasy
    def __init__(self, master = None, tekst_zastepczy = "Podaj liczbe", color = "grey"):
        super().__init__(master, width=26)
        
        #Zmienna wyświetlająca siegdy input jest pusty
        self.tekst_zastepczy = tekst_zastepczy
        self.tekst_zastepczy_color = color
        self.default_fg_color = self["fg"]

        #Sprawdzenire czy user wcisnął coś
        self.bind("<Key>", self.foc_in)
        
        #Sprawdzenire czy user opuścił pole
        self.bind("<Leave>", self.foc_out)
        
        self.put_tekst_zastepczy()
        
    def put_tekst_zastepczy(self):
        self.delete('0', 'end')
        self.insert(0, self.tekst_zastepczy)
        self['fg'] = self.tekst_zastepczy_color
    
    def foc_in(self, *args):
        if self['fg'] == self.tekst_zastepczy_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color
    
    def foc_out(self, *args):
        if not self.get():
            self.put_tekst_zastepczy()

class Aplikacja(ttk.Frame):
    
    def __init__(self, master):
        self.z = tk.Frame.__init__(self, master)
        self.pack()
        menubar = tk.Menu(root) #Menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Zmień liczbę początku przedziału", command=Podaj_liczbe_poczatek)
        filemenu.add_command(label="Zmień liczbę końca przedziału", command=Podaj_liczbe_koniec)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="Program", menu=filemenu)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="O programie", command = lambda: popup_showinfo("O programie, gra 'Zgadnij Liczbę'"))
        helpmenu.add_command(label="O autorze", command=lambda: popup_showinfo("O autorze", "Autor: Oliwier Markiewicz"))
        menubar.add_cascade(label="Pomoc", menu=helpmenu)
        root.config(menu=menubar)
        
        #Górna część okna
        self.hight_frame = tk.Frame(self.z)
        self.hight_frame.configure(background=bg_color)
        self.hight_frame.pack()
        
        #baner
        self.load = Image.open("baner.png")
        self.img = ImageTk.PhotoImage(self.load)
        self.l0 = tk.Label(self.hight_frame, image=self.img, bg=bg_color)
        self.l0.grid(row=0, column=0, sticky="N")
        
        self.l001 = tk.Label(self.hight_frame, text="Witaj", bg=bg_color, fg=text_color, font="none 16 bold").grid(row=1, column=0)
        
        self.l1text = tk.StringVar()
        self.l1text.set("\nAby rozpocząć grę,\nwpisz liczbę całkowitą z przedziału od " +str(a)+ " do " + str(b) +", \nktóra Twoim zdaniem została wylosowana :\n")
        self.l1 = tk.Label(self.hight_frame, textvariable=self.l1text, bg=bg_color, fg=text_color, font="none 12 bold").grid(row=2, column=0, sticky="W")
        
        
        #Środek aplikacji - pobieranie informacjo od użytkowników
        
        self.middle_Frame = tk.Frame(self.z)
        self.middle_Frame.configure(background=bg_color)
        self.middle_Frame.pack(padx=5)
        
        self.tekst1 = EntryRozszerzone(self.middle_Frame, tekst_zastepczy="podaj liczbe")
        self.tekst1.grid(row=0, column=0)
        
        tk.Label(self.middle_Frame,text="", width=5, bg=bg_color).grid(row=0, column=1)
        self.b1 = tk.Button(self.middle_Frame, text="Podaj liczbę", width=9, command=self.click).grid(row=0, column=2)
        
        #Wyświetlanie elementów gry
        self.low_frame = tk.Frame(self.z)
        self.low_frame.configure(background=bg_color)
        self.low_frame.pack()
        
        self.l4text = tk.StringVar()
        self.l4text.set("\n\n\n")
        self.l2 = tk.Label(self.low_frame, textvariable=self.l4text, bg=bg_color, fg=text_color, font="none 16 bold").grid(row=3, column=0, sticky="W")
        
        #dolna część programu
        self.lowest_frame = tk.Frame(self.z)
        self.lowest_frame.configure(background=bg_color)
        self.lowest_frame.pack()
        l4 = tk.Label(self.lowest_frame, text="Naciśnij, aby opuścić program", bg=bg_color, fg=text_color, font="none 16 bold").grid(row=5, column=0)
        
        tk.Button(self.lowest_frame, text="Wyjście", width=6, command=self.close_window).grid(row=4, column=0)
    
    def click(self):
        global a
        global b
        podany_tekst = self.tekst1.get()
        try:
            liczba = int(podany_tekst)
            if liczba == n:
                liczba = cZgadzaSie + str(liczba) + "\n"
                self.l4text.set(liczba)
                MsgBox = tk.messagebox.askquestion('Wygrałeś', 'Gratulacje, czy chcesz zagrać jeszcze raz?')
                if MsgBox == 'yes':
                    global_n_randint(a,b)
                else:
                    pass
            elif liczba > n:
                liczba = bLiczbaJestMniejsza
            else:
                liczba = aLiczbaJestWieksza
        except:
            liczba = "\nPodane znaki '" + podany_tekst+"' to nie liczba\nSpróbuj ponownie.\n"
        self.l4text.set(liczba)
        self.tekst1.put_tekst_zastepczy()
    
    
    def close_window(self):
        root.destroy()
        exit()
            
        
root = tk.Tk()
root.title("Gra zgadnij liczbę_V1")
root.geometry("500x400")
root.configure(background=bg_color)
app = Aplikacja(root)

root.mainloop()               