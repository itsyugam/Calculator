#packages import from kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#package for math calculation
from math import *


#class for first screen

class Display(FloatLayout):
   string=""
   def __init__(self,*args):
      super().__init__(*args)
      self.t=TextInput(font_size=60,hint_text="Enter the values here",text="",size_hint=(1,0.1),pos_hint={'x':0,'y':0.9})
      self.add_widget(self.t)
      
      self.b2=Button(font_size=60,text="Del",size_hint=(0.25,0.2),pos_hint={'x':0.75,'y':0.7}, background_color=(0,0,0,1))
      self.add_widget(self.b2)
      self.b2.bind(on_press=self.s)
      
      b1list=["sin","cos","tan","pow","%","(",")","log","pi","sqrt"]
      p=0
      q=0.8
      m=0
      
      for i in range(len(b1list)):
         self.b=Button(font_size=60,text=b1list[i], background_color=(0,0,0,1),size_hint=(0.15,0.10),pos_hint={'x':p,'y':q})
         self.add_widget(self.b)
         p=p+0.15
         if p==0.75:
            q=q-0.10
            p=0
         
         self.b.bind(on_press=self.s)
      
      
      blist=["7","8","9","/","4","5","6","*","1","2","3","+",".","0",",","-"]
      x=0
      y=0.55
      n=0
      
      for i in range(len(blist)):
         self.b=Button(color=(1,1,1,1),font_size=80,text=blist[i], background_color=(0,0,0,1),size_hint=(0.25,0.15),pos_hint={'x':x,'y':y})
         self.add_widget(self.b)
         x=x+0.25
         if x==1:
            y=y-0.15
            x=0
         
         self.b.bind(on_press=self.s)
       
      self.equal=Button(font_size=60,text="Equal",background_color=(0,0,0,1),size_hint=(0.75,0.1),pos_hint={'x':0.25,'y':0})
      self.add_widget(self.equal)
      self.equal.bind(on_press=self.s)
      
      self.clear=Button(font_size=60,text="Clear",background_color=(0,0,0,1),size_hint=(0.25,0.1),pos_hint={'x':0,'y':0})
      self.add_widget(self.clear)
      self.clear.bind(on_press=self.s)
    
   def s(self,instance):
      a=instance.text
      if a=="Equal":
         try:
           self.string=self.t.text
           self.t.text=str(eval(self.string))
           self.string=self.t.text
         except  SyntaxError:
           self.t.text="syntax error!"
           self.string=""
         except TypeError:
            self.t.text="pass wrong input!"
            self.string=""
         except NameError:
           self.t.text="syntax error!"
           self.string=""
         except:
            self.t.text="syntax error!"
            self.string=""
            
      elif a=="%":
         try:
            if len(self.t.text)>0:
               self.string=self.t.text
               for i in range(len(self.string)):
                  n=len(self.string)-i-1
                  if self.string[n]=='*':
                     list=self.string.split(self.string[n])
                     print(list)
                     m=len(list)
                     
                     value=1
                     for j in range(m-1):
                        value=str(value)+"*"+str(list[j])
                     print(value)
                     result=float(eval(str(value)))*float(list[m-1])*0.01
                     print(result)
                     self.t.text=str(result)
                     break
                  
                  elif self.string[n]=='+':
                     list=self.string.split(self.string[n])
                     print(list)
                     m=len(list)
                     
                     value=0
                     for j in range(m-1):
                        value=str(value)+"+"+str(list[j])
                     print(value)
                     result=float(eval(str(value)))+float(eval(str(value)))*float(list[m-1])*0.01
                     print(result)
                     self.t.text=str(result)
                     break
                     
                  elif self.string[n]=='-':
                     list=self.string.split(self.string[n])
                     print(list)
                     m=len(list)
                     
                     value=0
                     for j in range(m-1):
                        value=str(value)+"-"+str(list[j])
                     print(value)
                     result=float(eval(str(value)))-float(eval(str(value)))*float(list[m-1])*0.01
                     print(result)
                     self.t.text=str(result)
                     break
                     
                  elif self.string[n]=='/':
                     list=self.string.split(self.string[n])
                     print(list)
                     m=len(list)
                     
                     value=0
                     for j in range(m-1):
                        value=str(value)+"/"+str(list[j])
                     print(value)
                     result=float(eval(str(value)))/float(eval(str(value)))*float(list[m-1])*0.01
                     print(result)
                     self.t.text=str(result)
                     break
                     
                  else:
                     pass
                       
                     
            else:
               self.t.text="Enter some value!"
         except:
            self.t.text="syntax error!"
            self.string=''
      elif a=="Del":
         self.string=self.string[0:-1]
         self.t.text=self.string
      elif a=="Clear":
         self.string=''
         self.t.text=self.string
      else:
         self.string+=a
         self.t.text=self.string
                   
#Main class       
class calci(App):
   def build(self):
      return Display()
      
calci().run()
