from django.shortcuts import render
import pyrebase

from django.views.generic import View
   
from rest_framework.views import APIView
from rest_framework.response import Response
 
 


config = {
    "apiKey": "AIzaSyDYC_y6NxtMLizSN4oD46vC8PG_DLuE9DQ",
    "authDomain": "fir-hostingninja-992b6.firebaseapp.com",
    "databaseURL": "https://fir-hostingninja-992b6-default-rtdb.firebaseio.com",
    "projectId": "fir-hostingninja-992b6",
    "storageBucket": "fir-hostingninja-992b6.appspot.com",
    "messagingSenderId": "171937270816",
    "appId": "1:171937270816:web:8117d5d5bfc4222b910045",
    "measurementId": "G-J5JQ9VCB1R"
}
# Initialising database,auth and firebase for further use
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def signIn(request):
    return render(request, 'signIn.html')

def admin_signIn(request):
    return render(request, 'admin_signIn.html')

def home(request):
    return render(request,"index.html")

def postsignIn_admin(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")

    #a_email=request.POST.get('a_email')
    #a_passw = request.POST.get("a_pass")
    #print(a_email)
    #print(a_passw)
    
    try:
        #user = authe.sign_in_with_email_and_password(email,passw)
        if (email == "shruti@gmail.com") and (passw == "Shruti"):
            return render(request, "a_wel.html",{"e":email})
    except:
        message="invalid credentials"
        return render(request,"admin_signIn.html",{"messg":message})
    return render(request,"admin_signIn.html")
    #print(user['idToken'])
    
 
def postsignIn(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")

    #a_email=request.POST.get('a_email')
    #a_passw = request.POST.get("a_pass")
    #print(a_email)
    #print(a_passw)
    
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message="invalid credentials"
        return render(request,"signIn.html",{"messg":message})
    #print(user['idToken'])
    return render(request, "wel.html",{"e":email})
 

from difflib import SequenceMatcher
def comparison(request):
    num_plate = database.child('number_plate_data').get()
    rfid_data = database.child('rfid_data').get()
    rfid_dect = database.child('rfid_detection_data').get()

    num = []
    rfid_d = []
    rfid_dt = []

    for user in num_plate.each():
        num.append(user.val())
        #print(num)
    
    for user in rfid_data.each():
        rfid_d.append(user.val())
        #print(rfid_d)
    
    for user in rfid_dect.each():
        rfid_dt.append(user.val())
        #print(rfid_dt)
    
    rfid_val = rfid_dt[-1]['rfid']
    match_num = rfid_d[0][rfid_val]
    extract_num = num[-1]['number_plate']
    #extract_percent = num[-1]['percentage']

    per = SequenceMatcher(None, match_num, extract_num).ratio() 
    perc = "{:.2f}".format(per*100)

    context = {
        "rfid_val": rfid_val,
        "match_num": match_num,
        "extract_num":extract_num,
        "extract_percent":perc
    }

    return render(request,'compare.html',context)


def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"index.html")
 
def signUp(request):
    return render(request,"signUp.html")
 
def postsignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    name = request.POST.get('name')
    try:
        user=authe.create_user_with_email_and_password(email,passs)
        uid = user['localId']
        data={"name":name,"status":"1"}
        #database.child(“users“).child(uid).child(“details“).set(data)
    except:
        message="Unable to create account try again"
        return render(request,"signUp.html",{"message":message})
    return render(request,"signIn.html")

def reset(request):
    return render(request, "Reset.html")
 
def postReset(request):
    email = request.POST.get('email')
    try:
        authe.send_password_reset_email(email)
        message  = "A email to reset password is successfully sent"
        return render(request, "Reset.html", {"msg":message})
    except:
        message  = "Something went wrong, Please check the email you provided is registered or not"
        return render(request, "Reset.html", {"msg":message})

'''
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format = None):

        name = database.child('number_plate_data').get()
        la = []
        da = []
        li = []
        for i in range(1,40):
            m = str(i)
            framework = database.child(m).child('BookingID').get().val()
            frame = database.child(m).child('KM').get().val()
            la.append(framework)
            da.append(frame)
        for user in name.each():
            #print(user.val())
            li.append(user.val())

        for i in range(len(li)):
            la.append(li[i]['Number_Plate'])
            da.append(li[i]['Timestamp'][:10])

        
        labels = la
        chartLabel = "Distance in KM"
        chartdata = da
        data ={
                     "labels":labels,
                     "chartLabel":chartLabel,
                     "chartdata":chartdata,
             }
        return Response(data)'''