#!/usr/bin/env pythonw

import wolframalpha
import Tkinter as tk


class App:
	def __init__(self):
		self.root = tk.Tk()
		
		self.frame = tk.Frame(self.root)
		
		self.label = tk.Label(self.frame, text='Ask Away...')
		
		self.label.pack(pady=20)
		
		self.textfield = tk.Entry(self.frame, width = 25)
		
		self.textfield.pack(pady=20)
		
		self.sendButton = tk.Button(self.frame, text = 'Ask', width = 15, command = self.sendQuestion)
		
		self.sendButton.pack(pady=20)
		
		self.frame.pack()
				
		self.setup()
	
	
	def sendQuestion(self):
		self.question = self.textfield.get()
	
		self.answer = wolfram(self.question)
	
		self.label.configure(text=self.answer)
	
	
	def start(self):
		self.root.title('Wolfram')
	
		self.root.mainloop()
		
	
	def setup(self):
		self.root.bind('<Return>', self.returnPressed)
		
	def returnPressed(self, event):
		self.sendQuestion()
		
def wolfram(question):
	app_id = "PQX3KR-U8XAGE4X75"
	client = wolframalpha.Client(app_id)
	res = client.query(question)
	answer = next(res.results).text
	return answer


def main():
	App().start()

	

if __name__ == '__main__':
	main()