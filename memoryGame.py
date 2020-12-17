from tkinter import *
import time
import random
from PIL import ImageTk, Image  

def start5() :
    pattern = 5
    button.destroy()  
    label_name.destroy()
    labelk.destroy()
    game(pattern)

def game(pattern):
    def create_randomnumber(a,b):
        return random.randint( a,b )
    
    created_number = ""   
    for x in range ( pattern ) : 
        root = Canvas( width = 550 , height = 500 , bg = 'SeaGreen2' )
        root.pack ( expand = YES , fill = BOTH )
        x = create_randomnumber ( 50 , 400 )
        y = create_randomnumber ( 50 , 400 )
        shown_number = create_randomnumber(0,9)
        created_number += str ( shown_number )
        if pattern>10:
           root.create_text ( x , y , text = shown_number , fill = 'purple1' , font = ( "arial" , 30 , "bold" ) )
           app.update()
           time.sleep( 0.5 )
           root.pack_forget()
           app.update()
           time.sleep( 0.55 )
        else:
           root.create_text ( x , y , text = shown_number , fill = 'purple1' , font = ( "arial" , 80-(pattern*5) , "bold" ) ) #Level attırkça sayı boyutu küçülecek ve zorluk artacak
           app.update()
           time.sleep( 1-(pattern*0.03) )   #Level arttıkça süre kısalır
           root.pack_forget()
           app.update()
           time.sleep( 1 -(pattern*0.029))
    print ( created_number )    

    def get_number(new_number) :        
       new_number.get()
       if new_number.get() != created_number :
           text_box.pack_forget()
           try_button.pack_forget()
           if pattern==5:
               textgameover="Game Over \n Your Score:"+str(pattern-5)
           else:
               textgameover="Game Over \n Your Score:"+str(pattern-5)+"\n Last Known Digits: "+str(pattern-1)
           image1 = Image.open("fish_lost.jpg")
           test = ImageTk.PhotoImage(image1)
           label1 = Label(image=test)
           label1.image = test
           label1.place(x=0, y=0)
           label_game_over = Label ( app , anchor = CENTER , text = textgameover , font = ( "arial" , 20 , "bold" ) , bg = 'SeaGreen2' , fg = 'steelblue' )
           label_game_over.pack( expand = 1 , ipadx = "20" , ipady = "15" )
           app.update()
           time.sleep( 1.1 )
       if new_number.get() == created_number :
           new_pattern = pattern + 1
           text_box.pack_forget()
           try_button.pack_forget()
           image = Image.open("win.jpg")
           test_2 = ImageTk.PhotoImage(image)
           label_kazanma = Label(image=test_2)
           label_kazanma.image = test_2
           label_kazanma.place(x=0, y=0)
           text_cong="Go To Level "+str(pattern-3)+"\n Your Score: "+str(pattern-4)+"\n Digits: "+str(pattern)
           label_cong = Label ( app , anchor = CENTER , text = text_cong , bg = 'SeaGreen2' , fg = 'steelblue' ,
           font = ( "arial" , 20  ,"bold" ) )
           label_cong.pack ( expand = 1 , ipadx = "20" , ipady ="15" )
           app.update()
           time.sleep( 1.8 )
           app.update()
           label_kazanma.destroy()
           label_cong.pack_forget()
           app.update()
           return game ( new_pattern )
    
    new_number = StringVar()
    text_box = Entry ( app, textvariable = new_number , width = 20 , font = ( "arial" , 20 , "bold" ) , fg = 'black' ,  bg = 'khaki1' )
    text_box.grid(column = 0, row = 1)
    text_box.pack ( expand = "1" , ipadx = "20" , ipady ="15" )
    try_button = Button ( app, text = "Try" , command = lambda : get_number ( new_number ) , 
    bg = 'khaki1' , fg = "black" , font = ( "arial" , 15 , "bold" ), 
    relief = RAISED , activebackground ='LightGoldenrod3' , activeforeground = "black")
    try_button.pack ( expand = "1.5" , ipadx = "20" , ipady = "15" )
    
app = Tk()
app.title ( "MEMORY GAME CHALLENGE" )
app.configure ( background = 'SeaGreen2' )
app.geometry ( "550x500+10+10" )
image1 = Image.open("lost.jpg")
test = ImageTk.PhotoImage(image1)
labelk = Label(image=test)
labelk.image = test
labelk.place(x=0, y=0)
button = Button ( app , text = "Lets Start" , command = start5 , bg = 'khaki1' , fg = "SeaGreen2" , 
font = ( "arial" , 30 , "bold" ) , 
relief = RAISED ,  activebackground = 'LightGoldenrod3' , activeforeground = "PaleGreen3" ) 
button.pack ( expand = "1"  , ipadx = "30" , ipady = "50" )
label_name = Label ( app , anchor = CENTER , text = "Tuğçe Nur ŞAHİN " , font = ( "arial" , 10 , "italic bold" ) , bg = 'SeaGreen2' , fg = 'steelblue' )
label_name.place(x=415, y=450)
app.mainloop()