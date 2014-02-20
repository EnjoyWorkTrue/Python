# getGCal
from xml.etree import ElementTree
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom.data
import time

class getGcal:
    def __init__(self):
        self.user_id = None
        self.password = None
    def login(self,user_id,password):
        self.client = gdata.calendar.client.CalendarClient(source='yourCo-yourAppName-v1')
        self.client.ClientLogin(user_id, password, self.client.source)
        self.feed = self.client.GetCalendarEventFeed()
        self.events = [i for i in self.feed.entry]
    def addEvent(self,y,m,d):        
        title = raw_input('Title: ')
       
        
        starttime = raw_input('Hour Minute: ')            
        endtime = raw_input('Hour Minute: ')
        ####
        
        if title == '' or starttime =='' or endtime == '':
            return True
        starttime = starttime.split(' ')
        if int(starttime[0])<10:
            starttime[0] = '0'+str(int(starttime[0]))
        if int(starttime[1])<10:
             starttime[1] = '0'+str(int(starttime[1]))
            
        endtime = endtime.split(' ')
        if int(endtime[0])<10:
            endtime[0] = '0'+str(int(endtime[0]))
        if int(endtime[1])<10:
             endtime[1] = '0'+str(int(endtime[1]))
        
        starttime = '{0}:{1}:00'.format(*starttime)
        endtime = '{0}:{1}:00'.format(*endtime)
        
        if m<10:
            m = '0'+str(m)
        else:
            m = str(m)
        if d<10:
            d = '0'+str(d)
        else:
            d = str(d)
        date = '{0}-{1}-{2}'.format(y,m,d)
        startTime = date + 'T' + starttime + '.000'
        endTime = date + 'T' + endtime + '.000'
        
        event = gdata.calendar.data.CalendarEventEntry()
        event.title = atom.data.Title(text=title)
        event.when.append(gdata.calendar.data.When(start = startTime,end = endTime))
        self.client.InsertEvent(event)
        print 'Successfully add it'
        return False

    def getAllEvent(self):
        self.des = []
        self.when = []
        for i in self.feed.entry:
            self.des.append(i.title.text)
            self.when.append(i.when[0].start.split('T')[0])
    def showEvent(self,year,m,d):
        if m<10:
            m = '0' + str(m)
        if d<10:
            d = '0' + str(d)
        date = '-'.join([str(year),str(m),str(d)])
        
        count = self.when.count(date)
        if count == 0:
            return None,1,1,1
        if count >=1 :
            num = self.when.index(date)
        
            for i in range(count):
                print str(i+1)+'. ' + self.des[num+i]
            return m,d,num,count
    def deleteEvent(self,year,m,d):
        m,d,idx,count = self.showEvent(year,m,d)
        if m == None:
            print "no Schedule"
        else:
            print "choooose Options"
            idx = int(raw_input("Enter the number: ")) - 1+idx
            
            print self.events[idx].title.text+'?'
            answer = raw_input("y or n: ")
            if answer == 'y':        
                self.client.Delete(self.events[idx])
                self.des.pop(idx)
                self.when.pop(idx)
                self.events.pop(idx)
                print 'Deleting Susccess'
                # count and deleteo
                return count

        
        
            
        
def main():
    google = getGcal()
    userid = 'dldytpq234@gmail.com'
    password = 'dlfdlf11'
    google.login(userid,password)
    google.getAllEvent()
    google.getEvent(2014,01,18)

