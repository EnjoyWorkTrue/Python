import calGui as cg
import getGCal as tgc
import point
import datetime
from graphics import*

def main():
   
    today = datetime.date.today()
    win = GraphWin(str(today.year),300,300)
    cal = cg.GuiCal(today.year)
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

    cal.update(google.when)
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
                tempdate =  point.whichdate(p) - datetime.date(cal.year,month,1).weekday()-1
            else:
                tempdate =  point.whichdate(p)
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
                    choice =  point.whichWay(cal.date[date-1].anchor.getX(),cal.date[date-1].anchor.getY(),p)
                    if choice == 'left':
                      
                        break
                    if choice == 'right':
                        if google.addEvent(cal.year,month,date):
                            print 'you entered wrong value'
                            pass
                        else:
                            cal.update1(date,win)
                       
                        break
                    if choice == 'down':
                        google.showEvent(cal.year,month,date)
                
                        break
                    if choice == 'up':
                        google.deleteEvent(cal.year,month,date)
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
