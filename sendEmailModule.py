from speachModule import speak
from takecommandModule import takeCommand
from userPref import db
import smtplib

flag = 1

def send_mail():
    speak("i i boss")
    docs = db.collection(u'current').stream()
    for doc in docs:
        a = doc.to_dict()["email"]

    if(a == ""):
        speak("you are not logged in....please login first")
    else:
        docs = db.collection(u'Gmail').where(u'user', u'==', a).stream()
        for doc in docs:
            id = doc.to_dict()["userid"]
            ps = doc.to_dict()["acc_pass"]
        lst_name = []
        lst_mail = []
        docs = db.collection(u'GmailAdd').where(u'user', u'==', a).stream()
        for doc in docs:
            name = doc.to_dict()["name"].lower().split(" ")
            email = doc.to_dict()["email"].lower()
            lst_mail.append(email)
            lst_name.append(name[0])
        print(lst_name,lst_mail)
        speak("whom should i write the email")

        try:
            z = takeCommand(flag).lower().split(" ")
            z = z[0]

            if z in lst_name:
                    eid = lst_name.index(z)
                    rec = lst_mail[eid]
                    print(rec)
                    
                    speak("okay.....what should i say")
                    msg = takeCommand(flag)
                    server = smtplib.SMTP_SSL('smtp.gmail.com', port=465)
                    server.set_debuglevel(1)
                    server.ehlo
                    server.login(id,ps)
                    server.sendmail(id, [rec], msg)
                    server.quit()
                    speak("Email sent successfully")
                    
            else:
                    speak("you dont have any contact with that name")
                    #break  

        except:
            speak("sorry......i guess you email or password doesnot match")