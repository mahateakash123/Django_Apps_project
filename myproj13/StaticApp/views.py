from django.shortcuts import render
import datetime

def input(request):
    dt = datetime.datetime.now()
    hour = float(dt.strftime("%H"))
    msg="Hello.........Puneeeeee"
    msg2 = "The current date and time is: {}"
    if (hour<=12):
        msg=msg+"Very Good morning!!!"+ msg2.format(str(dt))
    elif (hour<=17.00):
        msg=msg+"Very Good Afternoon!!!"+ msg2.format(str(dt))
    elif (hour<=20.00):
        msg=msg+"Very Good evening!!!"+ msg2.format(str(dt))
    else:
        msg=msg+"Very Good Night!!!"+ msg2.format(str(dt))

    dict1 = {'message':msg}
    return render(request, 'base.html',context=dict1)

