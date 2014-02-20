#calGui

from graphics import *
import time
import random
import datetime
import hi
import getGCal as tgc

class GuiCal:
    
    def __init__(self,year):
        self.today = datetime.date.today()
        self.year = year
        self.firstday = datetime.date(self.year,1,1).weekday()
        self.monAnddate = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        self.month = ['Jan','Feb','March','April','May','June','July','August','September','October','November','December']
        self.day = [Text(Point(55+idx*30,50),i) for idx,i in enumerate(['Su','Mo','Tu','We','Th','Fr','Sa'])]
    def getWhen(self,when):
        self.when = when
    def drawdate(self,window,month):
        self.date = []
        firstday = datetime.date(self.year,month,1).weekday()
        x = 30*(firstday+1)
        if x ==210:
            x=0
        y = 70
        
        for i in range(self.monAnddate[month]):
            self.date.append(Text(Point(55+x,y),str(i+1)))
            x += 30
            if x ==210:
                x=0
                y+=25
        [i.draw(window) for i in self.date]
        
    def drawday(self,window):
        [i.draw(window) for i in self.day]
    def drawmonth(self,window,month):
        self.dmonth = Text(Point(150,25),self.month[month-1])
        self.dmonth.draw(window)

    def undrawdate(self):
        [i.undraw() for i in self.date]        
    def undrawday(self):
        [i.undraw() for i in self.day]
    def undrawmonth(self):
        self.dmonth.undraw()
##################
    def draw(self,window,month):           
        window.master.title(str(self.year))
        self.drawdate(window,month)
        self.drawday(window)
        self.drawmonth(window,month)
        if self.year==self.today.year and month == self.today.month:
            self.date[self.today.day-1].setFill("blue")
            self.date[self.today.day-1].setSize(15)


            
    def undraw(self):
        self.undrawdate()
        self.undrawday()
        self.undrawmonth()
        self.undraw_ExistDay()
###################

###

    def draw_month_choice(self,window):
        self.months = []

        changex = 70
        changey = 45
        
        x = 50
        y = 50

        for i in range(12):
            self.months.append(Text(Point(x,y),self.month[i][:3]))
            self.months[i].draw(window)
            x += changex
            if x == 50 + changex*3:
                x = 50
                y +=changey
    def m_cUndraw(self):
        for i in self.months:
            i.undraw()
        
    def draw_year_choice(self,window):
        self.year_choice = []
        for i in range(3):
            self.year_choice.append(Text(Point(260,80+i*20),str(self.year+1-i)))
            self.year_choice[i].draw(window)
            if i == 1:
                self.year_choice[i].setSize(15)
    def y_cUnDraw(self):
        for i in self.year_choice:
            i.undraw()

#####################
    def draw_months_years_choice(self,window):
        self.draw_month_choice(window)
        self.draw_year_choice(window)
    def undraw_m_y_c(self):
        self.m_cUndraw()
        self.y_cUnDraw()
##################### Underline Exist day
    def getExistday(self,month):
        self.existday = []
        date = '{0}-{1}'.format(str(year),str(month))
        for i in self.when:
            if date in i:
                day = date.split('-')[2]
                self.existday.append(int(day))

        
        
        
            
        
        

def main1():
    today = datetime.date.today()
    win = GraphWin(str(today.year),300,300)
    cal = GuiCal(today.year)
    month = today.month
    cal.draw(win,month)
    
    while True:
        p = win.getMouse()
        if (p.getY() - 20)%25<13:
            y = p.getY() - (p.getY()-20)%25
        if (p.getY()-20)%25>=13:
            y =  p.getY() + 25 - (p.getY()-20)%25

        if (p.getX()-25)%30<15:
            x =  p.getX() - (p.getX()-25)%30
        if (p.getX()-25)%30>=15:
            x =  p.getX()+ 30 - (p.getX()-25)%30

        x = (x-55)/30
        y = (y-70)/25
        print 'date= ', y*7+x+1
        
def whichdate(p):
    if (p.getY() - 20)%25<13:
            y = p.getY() - (p.getY()-20)%25
    if (p.getY()-20)%25>=13:
        y =  p.getY() + 25 - (p.getY()-20)%25

    if (p.getX()-25)%30<15:
        x =  p.getX() - (p.getX()-25)%30
    if (p.getX()-25)%30>=15:
        x =  p.getX()+ 30 - (p.getX()-25)%30

    x = (x-55)/30
    y = (y-70)/25
    return y*7+x+1
    
  
def main():
   
    today = datetime.date.today()
    win = GraphWin(str(today.year),300,300)
    cal = GuiCal(today.year)
    month = today.month
  
    
    google = tgc.getGcal()
    user_id = 'dldytpq234@gmail.com'
    password = 'dlfdlf11'

      # If its offline
    # mainLogin Off Mode()
    # return None
    # If login Succcess
    
    google.login(user_id,password)
    google.getAllEvent()

    cal.getWhen(google.when)
    #### Last
    
    cal.draw(win,month)
    

    ###
    
    
    
    
    while True:
        p = win.getMouse()
        #finish program
        if p.getX()<20 and p.getY()<20:
            break
        #come back to home
        if p.getX()<20 and p.getY()>280:
            cal.undraw()
            cal = GuiCal(today.year)
            month = today.month
            cal.draw(win,month)

        # next month
        if 260<p.getX()<280 and p.getY()<20:
            cal.undraw()
            month-=1
            if month == 0 :
                month = 12
                cal.year -= 1
            cal.draw(win,month)
        # before month
        if 280<p.getX()<300 and p.getY()<20:
            cal.undraw()
            month+=1
            if month == 13:
                month = 1
                cal.year +=1
            cal.draw(win,month)

        # When you clicked the date 
        if 45<p.getX()<247 and 60<p.getY()<182:
            date = None
        
            if datetime.date(cal.year,month,1).weekday()-1!=5:
                tempdate =  whichdate(p) - datetime.date(cal.year,month,1).weekday()-1
            else:
                tempdate =  whichdate(p)
            if 1<=tempdate <= cal.monAnddate[month]:
                date = tempdate
            if date == None:
                pass
            if date != None:
                for i in cal.date:
                    i.setSize(10)
                cal.date[date-1].setSize(18)

                
                while True:
                    p = win.getMouse()
                    choice =  hi.main(cal.date[date-1].anchor.getX(),cal.date[date-1].anchor.getY(),p)
                    if choice == 'left':
                      
                        break
                    if choice == 'right':
                        google.addEvent(cal.year,month,date)
                        cal.update1(date,win)
                       
                        break
                    if choice == 'down':
                        google.showEvent(cal.year,month,date)
                
                        break
                    if choice == 'up':
                        google.deleteEvent(cal.year,month,date)
                        cal.getWhen(google.when)                                
                        break


                [i.setSize(13) for i in cal.date]
                  
                            
                    

            
        
            
        # when you clicked the month
        #150 25
        if(120<p.getX()<180 and 15< p.getY()<35):
            cal.undraw()
            cal.draw_months_years_choice(win)
            On = True
            first = True
            while On:

                p = win.getMouse()
                # click! up year
                if 245<p.getX()<275 and 50<p.getY()<70:
                    cal.year-=1
                    cal.y_cUnDraw()
                    cal.draw_year_choice(win)
                    
                    
                    
                # click down year
                if 245<p.getX()<275 and 130<p.getY()<150:
                    cal.year+=1
                    cal.y_cUnDraw()
                    cal.draw_year_choice(win)
                    
                
                if 245<p.getX()<275 and 70<p.getY()<130:
                    if not first:
                        [i.setSize(13) for i in cal.year_choice]
                        for i in cal.year_choice:
                            pointY = i.anchor.getY()
                            if pointY-10 < p.getY() < pointY+10:
                                i.setSize(17)
                                cal.year = int(i.getText())
                    if first:
                        [i.setSize(13) for i in cal.year_choice]
                        for i in cal.year_choice:                            
                            pointY = i.anchor.getY()
                            if pointY-10 < p.getY() < pointY+10:
                                i.setSize(17)
                                first = False
                                cal.year = int(i.getText())
                    
                            
                if p.getX()<20 and p.getY()>280:
                    cal.undraw_m_y_c()
                    cal = GuiCal(today.year)
                    month = today.month
                    cal.draw(win,month)
                    break
                for idx,i in enumerate(cal.months):
                    if idx==3:
                        break
                    PointX = i.anchor.getX()
                    if PointX - 20 < p.getX() < PointX+20:
                        for j in range(4):
                            PointY = cal.months[j*3].anchor.getY()
                            if PointY-10 < p.getY() < PointY + 10:
                                month = idx + j*3 + 1
                                cal.undraw_m_y_c()
                                cal.draw(win,month)
                                On = False
                                break   
                        break
            
                
                

        
    win.close()
main()
