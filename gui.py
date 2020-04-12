from Tkinter import * #Kutuphanemizi projeye dahil ediyoruz.
import tkFont #Yazitipi secimi yapmak icin tkFont'a ihtiyacimiz olacak.
import RPi.GPIO as GPIO #GPIO pinlerini kontrol etmemizi saglayacak olan kutuphanemizi cagiriyoruz.

GPIO.setmode(GPIO.BCM) #GPIO pinlerine BCM numaralari ile atif yapacagimizi belirttik.
GPIO.setup(17, GPIO.OUT) #17.pini cikis olarak ayarladik.
GPIO.setup(27, GPIO.OUT) #27.pini cikis olarak ayarladik.
GPIO.setup(22, GPIO.OUT) #22.pini cikis olarak ayarladik.

r = GPIO.PWM(22,100) #r isimli bir PWM nesnesi olusturduk ve PWM frekansini 100 olarak belirledik.
g = GPIO.PWM(27,100) #g isimli bir PWM nesnesi olusturduk ve PWM frekansini 100 olarak belirledik
b = GPIO.PWM(17,100) #b isimli bir PWM nesnesi olusturduk ve PWM frekansini 100 olarak belirledik


win = Tk() #win ile tk'yi cagirdigimizi belirttik.

myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold') #Yazitipimizi belirledik.

def exitProgram(): #Programdan cikmamizi saglayan kisim
        GPIO.cleanup() #Cikista GPIO pinlerini temizliyoruz.
	win.quit() #Bu komutla cikiyoruz

def kirmizi_led(deger): #Kirmizi rengin siddetini PWM ile ayarlamamizi saglayan kisim.
	r.start(int(deger)) #Kirmizi LED'e PWM sinyal gonderiyoruz.

def yesil_led(deger): #Yesil rengin siddetini PWM ile ayarlamamizi saglayan kisim.
	g.start(int(deger)) #Yesil LED'e PWM sinyal gonderiyoruz.

def mavi_led(deger): #Mavi rengin siddetini PWM ile ayarlamamizi saglayan kisim.
	b.start(int(deger)) #Mavi LED'e PWM sinyal gonderiyoruz.


win.title("RGB RENK DEGISTIRICI") #Uygulamamizin basligi, ancak tam ekranda olunca gorunmuyor.
win.geometry('800x480') #Uygulamamizin boyutlari.
win.attributes('-fullscreen', True) #Tam ekran moduna gecis.
win.configure(bg='black') #Arkaplan rengini siyah yapiyoruz.

cikis_buton  = Button(win, text = "CIKIS", font = myFont, command = exitProgram, height =2 , width = 6)
cikis_buton.place(x=310,y=340) #Cikis butonu olusturup, parametrelerini belirliyoruz.

etiket = Label(win, text="Lutfen asagidan RGB LED'e uygulanacak renk degerlerini girin...",bg="black",fg="white")
etiket.place(x=50, y=20) #Aciklama metni olusturup, parametrelerini belirliyoruz.

kirmizi_slider = Scale(win, from_=0, to=100, label="KIRMIZI", fg="white", orient=HORIZONTAL, length=700, width=30,  bg='red', command=kirmizi_led)
kirmizi_slider.place(x=50, y=50) #Kirmizi renk icin Slider olusturup, parametrelerini belirliyoruz.

yesil_slider = Scale(win, from_=0, to=100, label="YESIL", fg="white", orient=HORIZONTAL, length=700, width=30, bg='green', command=yesil_led)
yesil_slider.place(x=50, y=150) #Yesil renk icin Slider olusturup, parametrelerini belirliyoruz.

mavi_slider = Scale(win, from_=0, to=100, label="MAVI", fg="white", orient=HORIZONTAL, length=700, width=30, bg='blue', command=mavi_led)
mavi_slider.place(x=50, y=250) #Mavi renk icin Slider olusturup, parametrelerini belirliyoruz.

mainloop() 
