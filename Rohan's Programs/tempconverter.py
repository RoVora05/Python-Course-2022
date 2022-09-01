print("What would you like to convert?")
question = eval(input("Type 1 for Celsius to Farenheit, or 2 for Farenheit to Celsius. "))
if question == 1:
	celsius = eval(input("How many degrees Celcius would you like to convert to Farenheit? "))
	x = (celsius*1.8)+32 
	print(x, ("degrees Farenheit"))
elif question == 2:
	farenheit = eval(input("How many degrees Farenheit would you like to convert to Celsius? "))
	y = (farenheit-32)/1.8
	print(y, ("degrees Celsius"))
else:
	print("Invalid input")