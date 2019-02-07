import turtle  as t
import time 

def drawline(draw):
	t.pendown() if draw else t.penup()
	t.fd(40)
	t.right(90)
def drawDigit(digit):
	drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
	drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
	drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
	drawline(True) if digit in [0,2,6,8] else drawline(False)
	t.left(90)
	drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
	drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
	drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
	t.left(180)
	t.penup()
	t.fd(20)
def drawdot1():
	t.penup();t.right(90);t.fd(30);t.pendown();
	t.write(':',font=("Arial",38,"normal"))
	t.penup();t.left(180); t.fd(30);t.right(90);
	t.fd(20)

def drawdot():
	t.penup();	t.left(90);	t.fd(10);	t.pendown()
	t.dot(5)
	t.penup();	t.left(180);	t.fd(20);	t.pendown()
	t.dot(5)
	t.penup();	t.left(180);	t.fd(10);	t.right(90)
	t.fd(20)

def drawDate(date):
	for i in date:
		if i=='-':
				drawdot1()
		else:
				drawDigit(eval(i))

def main():
	t.setup(800,350,200,200)
	t.speed(10)
	t.penup()
	t.fd(-300)
	t.pensize(5)
	t.pencolor("red")
	while(True):
		dat1=time.strftime('%H-%M-%S',time.localtime())
		drawDate(dat1)
		t.bk(400)
		time.sleep(5)
		t.clear()
	t.hideturtle()
	t.done()
	
main()


