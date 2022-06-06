from tkinter import *
from tkinter import messagebox

root =Tk()

root.title('Knopka_v2')
root.config(bg='#00FFFF')

calc =Entry(root, justify =RIGHT, font=('Arial',15), width=15,bg='white',bd='7')
calc.insert(0,'0')
calc.grid(row='0', column='0', columnspan=4, stick='wesn')

def add(digit):
	value =calc.get()
	if value =='0' and len(value)==1:
		value = value[1:]
	calc.delete(0,END)
	calc.insert(0,value + digit)

def res():
	value =calc.get()
	if value[-1] in '+-*/':
		value = value +value[:-1]
	calc.delete(0,END)
	try:
		calc.insert(0,eval(value))
	except (NameError, SyntaxError):
		messagebox.showinfo('Caution!!!', 'You entered invalid key \nOnly numbers are permetted!!!')
		calc.insert(0,'0')
	except ZeroDivisionError:
		messagebox.showinfo('Caution!!!', 'Zero cannot be devided in zero number!!!')

def clear():
	calc.delete(0,END)
	calc.insert(0,'0')

def backspace():
	value =calc.get()
	backspace =value[:-1]
	lenth =str(value)
	if len(lenth) >1:
		calc.delete(0,END)
		calc.insert(0,backspace)
	elif len(lenth) <2:
		calc.delete(0,END)
		calc.insert(0,'0')

def oper(oper):
	value =calc.get()
	if value[-1] in '-+*/':
		value =value[:-1]
	elif value[-1] in '1234567890':
		res()
		value =calc.get()
	calc.delete(0,END)
	calc.insert(0,value + oper)

def press_key(event):
	if event.char.isdigit():
		add(event.char)
	elif event.char in '*-+/':
		oper(event.char)
	elif event.char == '\r':
		res()

def btn(digit):
	return Button(text=digit, bd=5, bg='gray', font=('Arial',13), command=lambda: add(digit))

def btn_clear(result):
	return Button(text=result, bd=5, bg='red', fg='white', font=('Arial',13), command=clear)	

def btn_eval(result):
	return Button(text=result, bd=5, bg='#110066', fg='white', font=('Arial',13), command=lambda: res())

def btn_oper(operation):
	return Button(text=operation, bd=5, bg='#110066',fg='white', font=('Arial',13), command=lambda: oper(operation))

def btn_back(back):
	return Button(text=back, bd=5, bg='red',fg='white', font=('Arial',13), command=backspace)

btn('1').grid(row='2', column='0', stick='wens',padx=5, pady=5)
btn('2').grid(row='2', column='1', stick='wens',padx=5, pady=5)
btn('3').grid(row='2', column='2', stick='wens',padx=5, pady=5)
btn('4').grid(row='3', column='0', stick='wens',padx=5, pady=5)
btn('5').grid(row='3', column='1', stick='wens',padx=5, pady=5)
btn('6').grid(row='3', column='2', stick='wens',padx=5, pady=5)
btn('7').grid(row='4', column='0', stick='wens',padx=5, pady=5)
btn('8').grid(row='4', column='1', stick='wens',padx=5, pady=5)
btn('9').grid(row='4', column='2', stick='wens',padx=5, pady=5)
btn('0').grid(row='5', column='0', stick='wens',padx=5, pady=5,columnspan='3')

btn_oper ('+').grid(row='2', column='3', stick='wens',padx=5, pady=5)
btn_oper ('-').grid(row='3', column='3', stick='wens',padx=5, pady=5)
btn_oper ('*').grid(row='4', column='3', stick='wens',padx=5, pady=5)
btn_oper ('/').grid(row='1', column='3', stick='wens',padx=5, pady=5)
btn_eval ('=').grid(row='5', column='3', stick='wens',padx=5, pady=5)
btn_clear('c').grid(row='1', column='0', stick='wens',padx=5, pady=5,columnspan='2')

btn_back('<').grid(row='1', column='2', stick='wens',padx=5, pady=5)


root.grid_columnconfigure(0,minsize=60)
root.grid_columnconfigure(1,minsize=60)
root.grid_columnconfigure(2,minsize=60)
root.grid_columnconfigure(3,minsize=60)

root.grid_rowconfigure(0,minsize=60)
root.grid_rowconfigure(1,minsize=60)
root.grid_rowconfigure(2,minsize=60)
root.grid_rowconfigure(3,minsize=60)
root.grid_rowconfigure(4,minsize=60)


root.mainloop()