from . import assistant_gui# import engine_speak , record_audio

def addItem():
	item = assistant_gui.record_audio("enter the item you wish to add to the shopping list")
	with open("shopping_list.txt","a+") as f:
		f.close()
	with open("shopping_list.txt","a+") as f:
		content=f.readlines()
		f.close()
	item+="\n"
	with open("shopping_list.txt","w") as f:
		for i in content:
			f.write(i) 
		f.write(item)
		f.close()
	assistant_gui.engine_speak(item+"has been added to the shopping list")

def displaylist():
	with open("shopping_list.txt","a+") as f:
		f.close()
	with open("shopping_list.txt","r+") as f:
		content=f.readlines()
		f.close()
	text="Things in your list are "
	for line in content:
		text+=line.strip("\n")
	assistant_gui.engine_speak(text)
		

def removeItem():
	item= assistant_gui.record_audio("enter the item you wish to remove from the shopping list")
	with open("shopping_list.txt","a+") as f:
		f.close()
	with open("shopping_list.txt","r+") as f:
		content=f.readlines()
		f.close()
	item+="\n"
	if item in content:
		content.remove(item)
		with open("shopping_list.txt","w") as f:
			f.write(item)
			f.close()
		assistant_gui.engine_speak(item+"has been removed from the shopping list")
	else:
		assistant_gui.record_audio(item+"not found in the shopping list")	

def checkItem():
	item= assistant_gui.record_audio("what item would you like to check on the shopping list")
	with open("shopping_list.txt","a+") as f:
		f.close()
	with open("shopping_list.txt","r+") as f:
		content=f.readlines()
		f.close()
	if item+"\n" in content:
		assistant_gui.engine_speak("yes "+item +" is on the shopping list")
	else:
		assistant_gui.engine_speak("No "+item +" is not on the shopping list")
def listLength():
	with open("shopping_list.txt","a+") as f:
		f.close()
	with open("shopping_list.txt","r+") as f:
		content=f.readlines()
		f.close()
	assistant_gui.engine_speak("there are", len(content), "items on the shopping list")
	
def clearList():
	with open("shopping_list.txt","a+") as f:
		f.close()
	with open("shopping_list.txt","w") as f:
		f.write("")
		f.close()
	assistant_gui.engine_speak("the shopping list is now empty")
