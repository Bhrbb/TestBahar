


import tkinter  as tk
import ctypes

importdll=ctypes.CDLL("C:\\Users\\bhrbz\\source\\repos\\Bahar_DLL\\x64\\Debug\\Bahar_DLL.dll")
importdll.Toplam.argtypes=ctypes.c_float, ctypes.c_float
importdll.Toplam.restype=ctypes.c_float
 




pencere =tk.Tk()
pencere.geometry("300x300")

sayi1label=tk.Label(text="1.Sayiyi giriniz:")
sayi1label.place(x=10,y=20)



sayi1=tk.Entry(width=10)
sayi1.place(x=100,y=20)


sayi2label=tk.Label(text="2.Sayiyi giriniz:")
sayi2label.place(x=10,y=50)


sayi2=tk.Entry(width=10)
sayi2.place(x=100,y=50)

def topla():
    s1=float(sayi1.get())
    s2=float(sayi2.get())

    
    sonuc['text']=importdll.Toplam(s1,s2)
   



    
btopla=tk.Button(text="Hesapla",command=topla)
btopla.place(x=100,y=80)



sonuclabel=tk.Label(text="Sonuc")
sonuclabel.place(x=10,y=150)


sonuc=tk.Label(text="Sonuc")
sonuc.place(x=100,y=150)



pencere.mainloop()