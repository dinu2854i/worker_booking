from django.shortcuts import render
import pymysql

# Create your views here.
def login(request):
    return render(request,'AdminApp/Login.html')
def AdminAction(request):
    uname=request.POST['username']
    pwd=request.POST['password']

    if uname=='Admin' and pwd =='Admin':
        return render(request,'AdminApp/AdminHome.html')
    else:
        return render(request,'AdminApp/Login.html')
def addservice(request):
    return render(request,'AdminApp/AddServices.html')
def AdminHome(request):
    return render(request,'AdminApp/AdminHome.html')

def serviceaction(request):
    servicename=request.POST['servicename']

    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("select * from service where service='"+servicename+"'")
    d=cur.fetchone()
    if d is not None:
     context={'msg':'Service Name Already Exist...!!'}
     return render(request,'AdminApp/AddServices.html', context)
    else:
        cur=con.cursor()
        cur.execute("insert into service values(null,'"+servicename+"')")
        con.commit()
        context={'msg':'Worker Category Added Successfully...!!'}
        return render(request,'AdminApp/AddServices.html', context)


def viewserivces(request):
    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("select * from service ")
    data=cur.fetchall()
    table="<table><tr><th>ID</th><th>Service Name</th></tr>"
    for d in data:
        table+="<tr><td>"+str(d[0])+"</td><td>"+str(d[1])+"</td></tr>"
    table+="</table>"
    context={'data':table}
    return render(request,'AdminApp/ViewServices.html', context)
