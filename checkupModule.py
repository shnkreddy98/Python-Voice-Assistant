import datetime
import os
from speachModule import speak
from takecommandModule import takeCommand

flag = 1

def medical_report():
    current_dir_path = os.getcwd()
    try:
        date = datetime.datetime.utcnow().strftime('%m-%d-%Y ')
        speak('welcome....i will be writing a virtual prescription for you')
        speak('what is the patient name')
        name = takeCommand(flag)
        speak('how old is patient')
        age = takeCommand(flag)
        speak('tell me about the symptoms')
        Symptoms = takeCommand(flag)
        speak('thank you.......what was the final diagnostics report')
        Diagnostic = takeCommand(flag)
        speak('okay.......so what medicines will you suggest')
        Medicine = takeCommand(flag)
        speak('Any Recommendations?')
        Recommendation = takeCommand(flag)
        speak('okay.......who is the doctor in charge ')
        doctor = takeCommand(flag)
        speak('thank you......i will be generating a pescription now')
        doc_fun(name,date,age,Symptoms,Diagnostic,Medicine,Recommendation,doctor)
        query = takeCommand(flag).lower()
        if "yes" in query:
            os.startfile(current_dir_path + "\\patient_"+ name +".html")

        else:
            speak("okay...i have saved the prescription for future reference")

    except:
        speak('I think you missed something ............. please try again')
        medical_report()

#Doctor function
def doc_fun(name,date,age,Symptoms,Diagnostic,Medicine,Recommendation,doctor):
    current_dir_path = os.getcwd()

    with open(current_dir_path + "\\medical_report\\patient_" + name + ".html", 'w') as file:
        file.write("<html><head><meta name='viewport' content='width=device-width, initial-scale=1'>"
        "<title>AI Medical Report</title><link rel='stylesheet' type='text/css' href='https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css'>"
        "<link rel='stylesheet' type='text/css' href='a.css'></head>"
        "<body><div class = 'row'><div class = 'col-md-2'></div>"
        "<div  class = 'col-md-8'><div class = 'row header' ></div>"
        "<div class='row' ><div class = 'col-md-5'></div><h1>H</h1><div class = 'col-md-4'><h4 id='date'>Date : <p>"+date+"</p></h4></div></div>"
        "<div class='row' ><div class = 'col-md-5'></div><h5><b>&nbsp;Hamilton Hospital</b></h5></div>"
        "<div class='row' ><div class = 'col-md-5'></div><h6><b>Mangalore,Karnataka</b></h6></div><hr><br>"
        "<div class='row' ><div class = 'col-md-1'></div><div class = 'col-md-6'><h5>Patient Name : </h5><p>"+name+"</p></div><div class = 'col-md-1'></div>"
        "<div class = 'col-md-3'><h5>Patient Age : </h5><p>"+age+"</p></div></div><br>"
        "<div class='row' ><div class = 'col-md-1'></div><div class = 'col-md-7'><h5>Symptoms : </h5><p>"+Symptoms+"</p></div></div>"
        "<br><div class='row' ><div class = 'col-md-1'></div><div class = 'col-md-7'><h5>Diagnostic : </h5><p>"+Diagnostic+"</p></div></div>"
        "<br><div class='row' ><div class = 'col-md-1'></div><div class = 'col-md-7'><h5>Medicine : </h5><p>"+Medicine+"</p></div></div>"
        "<br><div class='row' ><div class = 'col-md-1'></div><div class = 'col-md-7'><h5>Recommendation : </h5><p>"+Recommendation+"</p></div></div>"
        "<br><div class='row' ><div class = 'col-md-7'></div><div class = 'col-md'><h5 id = 'ad'>Doctor in Charge : </h5><p id = 'ad'>"+doctor+"</p></div></div>"
        "<div class = 'row footer' ><div class='col-md-12'><br><span>Made by your Personal assistant SEREAH</span></div></div>"
        "</div></div></body></html>")