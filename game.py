from curses import *
from random import randrange
initscr()
start_color()
curs_set(0)
init_pair(1,COLOR_RED,COLOR_BLACK)
init_pair(2,COLOR_GREEN,COLOR_BLACK)
init_pair(3,COLOR_BLUE,COLOR_BLACK)
init_pair(4,COLOR_YELLOW,COLOR_BLACK)
init_pair(5,COLOR_CYAN,COLOR_BLACK)
init_pair(6,COLOR_BLUE,COLOR_YELLOW)
class game:
	def __init__(self):
		self.win= newwin(30,100,5,10)
		self.win.keypad(1)
		self.win.nodelay(1)
		self.win.border('|','|','-','-','+','+','+','+')
		self.a=30
		self.b=7
		self.snake=[]
		for i in xrange(30,36):
			for j in xrange(7,11):
				self.snake.append([i,j])
		self.count=0
		self.flag=0
		self.level=1
	def start(self):
		self.win.addstr(8,15,"              Instructions  ",color_pair(1))
		self.win.addstr(9,15,"  --------------------------------------------- ",color_pair(5))
		self.win.addstr(10,15,"1.  USE THE 'ESC' KEY TO QUIT THE GAME  ",color_pair(2))
		self.win.addstr(11,15,"2.  TAKE ALL DIFFUSE KITS TO DIFFUSE THE BOMB  ",color_pair(2))
		self.win.addstr(12,15,"3.  YOU WIN IF YOU DON'T HIT THE WALLS AND DIFFUSE THE BOMB ",color_pair(2))
		self.win.addstr(13,15,"4.  YOU CAN PRESS THE 'P' KEY TO PAUSE THE GAME ",color_pair(2))
		self.win.addstr(22,1,"-----> please wait while the game is loading... ",color_pair(6))
		for i in xrange(2,50):
			self.win.addch(25,i,'~',color_pair(4))
			self.win.timeout(100)
			getkey=self.win.getch()
		for i in xrange(2,50):
			self.win.addch(25,i,' ',color_pair(4))
			self.win.timeout(1)
			getkey=self.win.getch()
		for i in xrange(2,50):
			self.win.addch(25,i,'~',color_pair(4))
			self.win.timeout(100)
			getkey=self.win.getch()
		for i in xrange(1,98):
			for j in xrange(1,28):
				self.win.addch(j,i,' ')
		self.key = KEY_RIGHT
		self.keyflag=1
	def type2(self):
	    u=randrange(1,10,1)
	    self.win.addstr(self.b,self.a,"  ii ",color_pair(u%5))    #5 units
	    self.win.addstr(self.b+1,self.a," [xx]",color_pair(u%4)) #5units
	    self.win.addstr(self.b+2,self.a,"/|__|\\",color_pair(u%3)) # 7units
	    self.win.addstr(self.b+3,self.a," d  b",color_pair(4)) #5 units
	def type3(self):
	    u=randrange(1,10,1)
	    self.win.addstr(self.b,self.a,"  ^  ",color_pair(u%5))    #5 units
	    self.win.addstr(self.b+1,self.a," <()>",color_pair(u%4)) #5units
	    self.win.addstr(self.b+2,self.a,"-|RR|- ",color_pair(u%3)) # 7units
	    self.win.addstr(self.b+3,self.a," d  b",color_pair(4)) #5 units
	def type1(self):
	    u=randrange(1,10,1)
	    self.win.addstr(self.b,self.a," ----",color_pair(u%5))    #5 units
	    self.win.addstr(self.b+1,self.a,"\@_@/",color_pair(u%4)) #5units
	    self.win.addstr(self.b+2,self.a,"|R-R|- ",color_pair(u%3)) # 7units
	    self.win.addstr(self.b+3,self.a,"00000",color_pair(4)) #5 units
	def funckey(self,kflag):
	        if kflag==1:
			if (self.win.inch(self.b,self.a+5) & 255== 32) and (self.win.inch(self.b+1,self.a+5) & 255==32) and (self.win.inch(self.b+2,self.a+7) & 255== 32) and (self.win.inch(self.b+3,self.a+5) & 255==32):
				 self.a=self.a+1
			else:
	      			 if (self.win.inch(self.b,self.a+5) & 255==ord('D')) or (self.win.inch(self.b+1,self.a+5) & 255==ord('D')) or (self.win.inch(self.b+2,self.a+7) & 255==ord('D')) or (self.win.inch(self.b+3,self.a+5) & 255==ord('D')):
					self.a=self.a+1
					self.count=self.count+1
	        		 elif (self.win.inch(self.b,self.a+5) & 255==ord('B')) or (self.win.inch(self.b+1,self.a+5) & 255==ord('B')) or (self.win.inch(self.b+2,self.a+7) & 255==ord('B')) or (self.win.inch(self.b+3,self.a+5) & 255==ord('B')):
					if self.count>=3*self.level:
					        self.count=3*self.level
						self.flag=1
					else :self.flag=2
    		  		 else: self.flag=2
  	        elif kflag==2:
  		  	if (self.win.inch(self.b,self.a-1)&255==32) and (self.win.inch(self.b+1,self.a-1) &255==32) and (self.win.inch(self.b+2,self.a-1)&255==32) and (self.win.inch(self.b+3,self.a-1) &255==32) :
				self.a=self.a-1
   			else :
    				if (self.win.inch(self.b,self.a-1)&255==ord('D')) or (self.win.inch(self.b+1,self.a-1) &255==ord('D')) or (self.win.inch(self.b+2,self.a-1)&255==ord('D')) or (self.win.inch(self.b+3,self.a-1) &255==ord('D')) :
						self.a=self.a-1
						self.count=self.count+1
   		 		elif (self.win.inch(self.b,self.a-1) & 255==ord('B')) or (self.win.inch(self.b+1,self.a-1) & 255==ord('B')) or  (self.win.inch(self.b+2,self.a-1) & 255==ord('B')) or (self.win.inch(self.b+3,self.a-1) & 255==ord('B')):
					if self.count>=3*self.level:
						self.count=3*self.level
						self.flag=1
					else :self.flag=2
    				else: self.flag=2
                elif kflag==3:
    			if (self.win.inch(self.b+4,self.a) & 255==32) and (self.win.inch(self.b+4,self.a+1) & 255==32) and  (self.win.inch(self.b+4,self.a+2) & 255==32) and (self.win.inch(self.b+4,self.a+3) & 255==32) and  (self.win.inch(self.b+4,self.a+4) & 255==32) and (self.win.inch(self.b+4,self.a+5) & 255==32):
				self.b=self.b+1
			else:
				if (self.win.inch(self.b+4,self.a) & 255==ord('D')) or (self.win.inch(self.b+4,self.a+1) & 255==ord('D')) or  (self.win.inch(self.b+4,self.a+2) & 255==ord('D')) or (self.win.inch(self.b+4,self.a+3) & 255==ord('D')) or (self.win.inch(self.b+4,self.a+4) & 255==ord('D')) or (self.win.inch(self.b+4,self.a+5) & 255==ord('D')) or (self.win.inch(self.b+3,self.a+6)&255==ord('D')):
						self.b=self.b+1
						self.count=self.count+1
				elif (self.win.inch(self.b+4,self.a) & 255==ord('B')) or (self.win.inch(self.b+4,self.a+1) & 255==ord('B')) or  (self.win.inch(self.b+4,self.a+2) & 255==ord('B')) or (self.win.inch(self.b+4,self.a+3) & 255==ord('B')) or (self.win.inch(self.b+4,self.a+4) & 255==ord('B')) or (self.win.inch(self.b+4,self.a+5) & 255==ord('B')) or (self.win.inch(self.b+3,self.a+6)&255==ord('B')):
					if self.count>=3*self.level:
						self.count=3*self.level
						self.flag=1
					else :self.flag=2
    				else: self.flag=2
	        elif kflag==4:
    			if (self.win.inch(self.b-1,self.a)&255==32) and (self.win.inch(self.b-1,self.a+1)&255==32) and (self.win.inch(self.b-1,self.a+2)&255==32) and (self.win.inch(self.b-1,self.a+3)&255==32) and (self.win.inch(self.b-1,self.a+4)&255==32) and (self.win.inch(self.b-1,self.a+5)&255==32):
				self.b=self.b-1
			else:
				if (self.win.inch(self.b-1,self.a) & 255==ord('D')) or (self.win.inch(self.b-1,self.a+1) & 255==ord('D')) or (self.win.inch(self.b-1,self.a+2) & 255==ord('D')) or (self.win.inch(self.b-1,self.a+3) & 255==ord('D')) or (self.win.inch(self.b-1,self.a+4) & 255==ord('D')) or (self.win.inch(self.b-1,self.a+5) & 255==ord('D')):
						self.b=self.b-1
						self.count=self.count+1
				elif (self.win.inch(self.b-1,self.a) & 255==ord('B')) or (self.win.inch(self.b-1,self.a+1) & 255==ord('B')) or (self.win.inch(self.b-1,self.a+2) & 255==ord('B')) or (self.win.inch(self.b-1,self.a+3) & 255==ord('B')) or (self.win.inch(self.b-1,self.a+4) & 255==ord('B')) or (self.win.inch(self.b-1,self.a+5) & 255==ord('B')):
					if self.count>=3*self.level:
						self.count=3*self.level
						self.flag=1
					else: self.flag=2
				else: self.flag=2
	def play(self):
			global robono
			while self.key != 27:
		    		if robono == ord('1'):
		   		 	self.type1()
		    		elif robono==ord('2'):
		       		 	self.type2()
		    		elif robono==ord('3'):
		    			self.type3()
		    		tempa=self.a;tempb=self.b
		    		self.win.addstr(0,2,' Score: '+str(self.count)+' ')
				self.win.addstr(29,70," COPYRIGHT : Prateek Sachdev",color_pair(4))
		    		self.win.timeout(180)
		    		getkey = self.win.getch()
		    		self.key = self.key if getkey==-1 else getkey
		    		if self.key==KEY_RIGHT:
		    			self.keyflag=1
		    		elif self.key==KEY_LEFT:
		    			self.keyflag=2
		    		elif self.key==KEY_DOWN:
		    			self.keyflag=3
		  		elif self.key==KEY_UP:
		    			self.keyflag=4
				elif self.key==ord('p'):
					self.win.timeout(-1)
					self.win.getch()
		   		else: break
		    		if self.flag==1:
		    			break
		    		if self.flag==2:
		    			break;
				self.funckey(self.keyflag)
		   		self.win.addstr(tempb,tempa,"     ")		
		    		self.win.addstr(tempb+1,tempa,"     ")		
		    		self.win.addstr(tempb+2,tempa,"       ")		
		   		self.win.addstr(tempb+3,tempa,"     ")		
	def robo(self):
			for i in xrange(1,98):
				for j in xrange(1,28):
					self.win.addch(j,i,' ')
			c = [n for n in [[randrange(1,98,1),randrange(1,28,1)] for x in range(10)] if n not in self.snake]
			self.win.addch(c == [] and 4 or c[0][1],c == [] and 44 or c[0][0],'D',color_pair(2))
			self.win.addch(c == [] and 4 or c[1][1],c == [] and 44 or c[1][0],'D',color_pair(2))
			self.win.addch(c == [] and 4 or c[2][1],c == [] and 44 or c[2][0],'D',color_pair(2))
			self.win.addch(c == [] and 4 or c[3][1],c == [] and 44 or c[3][0],'B',color_pair(1))
			while(1):
				self.play()
				if self.flag!=1:
					for i in xrange(1,29):
						for j in xrange(1,98):
							u=randrange(1,10,1)
							self.win.addch(i,j,'*',color_pair(u%5))
							self.win.timeout(1)
							self.win.getch()
					for i in xrange(1,98):
						for j in xrange(1,28):
							self.win.addch(j,i,' ')
					self.win.addstr(14,40,"SORRY YOUR GAME IS OVER :(",color_pair(4))
					self.win.timeout(2000)
					self.win.getch()
					endwin()
					break
				else:
					self.flag=0
					for i in xrange(1,98):
						for j in xrange(1,28):
							self.win.addch(j,i,' ')
					self.level=self.level+1
					self.a=30
					self.b=7
					self.key = KEY_RIGHT
					self.keyflag=1
					self.count=0
					if self.level==4:
						for i in xrange(1,98):
							for j in xrange(1,28):
								self.win.addch(j,i,' ')
						self.win.addstr(14,40,"!!!!CONGRATULATIONS YOU WIN !!!!!!",color_pair(4))
						self.win.timeout(200)
						self.win.getch()
						endwin()
						break
			
					self.win.addstr(15,28,"PRESS ANY KEY TO PLAY LEVEL "+str(self.level),color_pair(1));
					self.win.timeout(-1)
					self.win.getch()
					for i in xrange(1,98):
						for j in xrange(1,28):
							self.win.addch(j,i,' ')
					c = [n for n in [[randrange(1,98,1),randrange(1,28,1)] for x in range(40)] if n not in self.snake]
					l=3*self.level
					mineno=2*self.level+1
					for i in range(l):
						self.win.addch(c == [] and 4 or c[i][1],c == [] and 44 or c[i][0],'D',color_pair(2))
					x=i
					for i in xrange(x,x+mineno):
						self.win.addstr(c == [] and 4 or c[i+1][1],c == [] and 44 or c[i+1][0],"x----x")
					self.win.addch(c == [] and 4 or c[i+1][1],c == [] and 44 or c[i+1][0],'B',color_pair(1))
class selectrobo(game):
	def __init__(self):
		a=game()
		a.win.addstr(6,4,"  choose your ROBOT  ",color_pair(2))
		a.win.addstr(8,4,"  PRESS 1 FOR ",color_pair(1))

		a.win.addstr(7,50," ----",color_pair(4))    #5 units
		a.win.addstr(8,50,"\@_@/",color_pair(4)) #5units
		a.win.addstr(9,50,"|R-R|- ",color_pair(4)) # 7units
		a.win.addstr(10,50,"00000",color_pair(4)) #5 units

		a.win.addstr(14,4,"  PRESS 2 FOR",color_pair(1))

		a.win.addstr(12,50,"  ii ",color_pair(4))    #5 units
		a.win.addstr(13,50," [xx]",color_pair(4)) #5units
		a.win.addstr(14,50,"/|__|\\",color_pair(4)) # 7units
		a.win.addstr(15,50," d  b",color_pair(4)) #5 units

		a.win.addstr(18,4,"  PRESS 3 FOR ",color_pair(1))
		a.win.addstr(17,50,"  ^  ",color_pair(4))    #5 units
		a.win.addstr(18,50," <()>",color_pair(4)) #5units
		a.win.addstr(19,50,"-|RR|- ",color_pair(4)) # 7units
		a.win.addstr(20,50," d  b",color_pair(4)) #5 units
		a.win.timeout(-1)
		global robono
		robono=a.win.getch()
	#	return a.robono
#here main begins
obj=game()
obj.start()
obj2=selectrobo()
obj.robo()
