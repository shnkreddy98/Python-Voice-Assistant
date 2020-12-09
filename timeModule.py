import datetime

def my_time():
	try:
		strTime = datetime.datetime.now().strftime("%H:%M")
		d = datetime.datetime.now().strptime(strTime, "%H:%M")
		a = d.strftime("%I:%M %p")
		return(f"the time is {a}")
	except:
		my_time()

def my_date():
	try:
		strTime = datetime.datetime.utcnow().strftime('%m-%d-%Y ')
		return(f"today's date is {strTime}")
	except:
		my_date()