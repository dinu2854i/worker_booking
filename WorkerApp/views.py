from django.shortcuts import render
import pymysql

# Create your views here.
def login(request):
    return render(request,'sp/Login.html')

def SPRegister(request):
    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("select * from service ")
    data=cur.fetchall()
    table=""
    for d in data:
        table+="<option value="+str(d[1])+">"+str(d[1])+"</option>"

    context={'d':table}
    return render(request,'sp/SPRegister.html', context)

def RegAction(request):
    servicename=request.POST['servicename']
    email=request.POST['email']
    workername=request.POST['name']
    username=request.POST['username']
    password=request.POST['password']
    w_hours=request.POST['w_hours']
    cost=request.POST['cost']
    mobile=request.POST['mobile']



    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("select * from sregister where service='"+servicename+"' and email='"+email+"' and mobile='"+mobile+"'")
    d=cur.fetchone()
    if d is not None:
     cur=con.cursor()
     cur.execute("select * from service ")
     data=cur.fetchall()
     table="<select class='contactus' name='servicename'>"
     for d in data:
         table+="<option value="+str(d[1])+">"+str(d[1])+"</option>"
     table+="</select>"
     context={'msg':'User Already Exist...!!','data':table}
     return render(request,'sp/SPRegister.html', context)
    else:
        cur=con.cursor()
        cur.execute("insert into sregister values(null,'"+servicename+"','"+email+"','"+username+"','"+password+"','"+w_hours+"','"+cost+"','"+mobile+"')")
        con.commit()
        cur=con.cursor()
        cur.execute("select * from service ")
        data=cur.fetchall()
        table="<select class='contactus' name='servicename'>"
        for d in data:
            table+="<option value="+str(d[1])+">"+str(d[1])+"</option>"
        table+="</select>"
        context={'data':table,'msg':'Successfully Registered Your Details...!!'}
        return render(request,'sp/SPRegister.html', context)


def LoginAction(request):
    uname=request.POST['username']
    pwd=request.POST['password']

    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("select * from sregister where username='"+uname+"' and password='"+pwd+"'")
    d=cur.fetchone()
    if d is not None:
        request.session['userid']=d[0]
        request.session['servicename']=d[1]
        request.session['email']=d[2]
        return render(request,'sp/SPHome.html')
    else:
        context={'msg':'Login Failed...!!'}
        return render(request,'sp/Login.html', context)


def SPHome(request):
    return render(request,'sp/SPHome.html')

def viewMessage(request):
    u_id=request.session['userid']
    spid=str(u_id)
    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("select * from message where w_id='"+spid+"'")
    data=cur.fetchall()
    table="<table><tr><th>User ID</th><th>User Message</th><th>Your Reply</th><th>Reply</th></tr>"
    for d in data:
        table+="<tr><td>"+str(d[3])+"</td><td>"+str(d[4])+"</td><td>"+str(d[5])+"</td><td><a href='/workerapp/ReplyUser?id="+str(d[0])+"'>Click</a></td></tr>"
    table+="</table>"
    context={'data':table}
    return render(request,'sp/ViewMessages.html',context)
def ReplyUser(request):
    id=request.GET['id']
    context={'id':id}
    return render(request,'sp/ReplyUser.html',context)
def ChatAction(request):
    id=request.POST['id']
    msg=request.POST['message']
    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("update message set replay='"+msg+"' where id='"+id+"'")
    con.commit()
    u_id=request.session['userid']
    spid=str(u_id)
    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("select * from message where w_id='"+spid+"'")
    data=cur.fetchall()
    table="<table><tr><th>User ID</th><th>User Message</th><th>Your Reply</th><th>Reply</th></tr>"
    for d in data:
        table+="<tr><td>"+str(d[3])+"</td><td>"+str(d[4])+"</td><td>"+str(d[5])+"</td><td><a href='/workerapp/ReplyUser?id="+str(d[0])+"'>Click</a></td></tr>"
    table+="</table>"
    context={'data':table,'msg':"Reply Sent Successful..!!"}
    return render(request,'sp/ViewMessages.html',context)






def viewBooking(request):
    u_id=request.session['userid']
    spid=str(u_id)
    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("select * from service_book sb, register r where sb.userid=r.id and sb.service_id='"+spid+"'")
    data=cur.fetchall()
    table="<table><tr><th>Customer Name</th><th>Email</th><th>Mobile</th><th>Booked Date</th><th>Status</th><th>adresses</th></tr>"
    for d in data:
        status=d[4]
        if status=='waiting':
            table+="<tr><td>"+str(d[6])+"</td><td>"+str(d[7])+"</td><td>"+str(d[8])+"</td><td>"+str(d[3])+"</td><td><a href='AcceptService?sid="+str(d[0])+"'>Accept</a><td>"+str(d[9])+"</td></td></tr>"
        else:
            table+="<tr><td>"+str(d[6])+"</td><td>"+str(d[7])+"</td><td>"+str(d[8])+"</td><td>"+str(d[3])+"</td><td>"+str(d[4])+"</td></tr>"
    table+="</table>"
    context={'data':table}
    return render(request,'sp/ViewBooking.html', context)

def AcceptService(request):
    sid=request.GET['sid']
    u_id=request.session['userid']
    spid=str(u_id)
    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("update service_book set status='Accepted' where id='"+sid+"'")
    cur=con.cursor()
    con.commit()
    cur.execute("select * from service_book sb, register r where sb.userid=r.id and sb.service_id='"+spid+"'")
    data=cur.fetchall()
    table="<table><tr><th>Customer Name</th><th>Email</th><th>Mobile</th><th>Booked Date</th><th>Status</th></tr>"
    for d in data:
        status=d[4]
        if status=='waiting':
            table+="<tr><td>"+str(d[6])+"</td><td>"+str(d[7])+"</td><td>"+str(d[8])+"</td><td>"+str(d[3])+"</td><td><a href='AcceptService?sid="+str(d[0])+"'>Accept</a></td></tr>"
        else:
            table+="<tr><td>"+str(d[6])+"</td><td>"+str(d[7])+"</td><td>"+str(d[8])+"</td><td>"+str(d[3])+"</td><td>"+str(d[4])+"</td></tr>"
    table+="</table>"
    context={'data':table,'msg':'Successfully Accepted Request...!!'}
    return render(request,'sp/ViewBooking.html', context)

def GroupChat(request):
    uid=request.session['userid']
    uuid=str(uid)
    print(uuid)
    con = pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur = con.cursor()
    cur.execute("select * from register where id!='"+uuid+"'")
    data = cur.fetchall()
    count=0
    for d1 in data:
        count=count+1

    cur1 = con.cursor()
    cur1.execute("select * from group_chat where uid!='"+uuid+"'")
    data1=cur1.fetchall()
    table="<table><tr><th>Message</th><th>Sent From</th><th>Action</th></tr>"
    for d in data1:
        table+="<tr><td>"+str(d[2])+"</td><td>"+str(d[1])+"</td><td><a href='ReplyNow.html?id="+str(d[0])+"&uid="+uuid+"'>Click</a></td></tr>"
    table+="</table>"

    context = {'data': count,'table':table}
    return render(request,'Customer/CustomerChat.html',context)


def ReplyNow(request):
    id=request.GET['id']
    uid=request.GET['uid']
    context={'id':id,'uid':uid}
    return render(request,'Customer/ReplyNow.html', context)

def ReplyChatAction(request):
    id=request.POST['id']
    uid=request.POST['uid']
    message=request.POST['message']
    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("update group_chat set s_id='"+uid+"',reply='"+message+"' where id='"+id+"'")
    con.commit()
    context={'msg':"Chat Replied Successfully...!!"}
    return render(request,'Customer/CustomerHome.html', context)



def GroupChatAction(request):
    uid=request.session['userid']
    d=str(uid)
    message=request.POST['message']
    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("insert into group_chat values(null,'"+d+"','"+message+"','waiting','waiting')")
    con.commit()
    cur = con.cursor()
    cur.execute("select * from register where id!='"+d+"'")
    data = cur.fetchall()
    count=0
    for d in data:
        count=count+1
    context={'data': count,'msg':"Chat Submitted Successfully...!!"}
    return render(request,'Customer/CustomerChat.html', context)


def GroupReply(request):
    uid=request.session['userid']
    d=str(uid)
    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("select * from group_chat gc,register r where r.id=gc.s_id and gc.uid='"+d+"'")
    data=cur.fetchall()
    table="<table><tr><th>Your Message</th><th>Reply From</th><th>Mobile</th><th>Reply</th></tr>"
    for d in data:
        table+="<tr><td>"+str(d[2])+"</td><td>"+str(d[6])+"</td><td>"+str(d[8])+"</td><td>"+str(d[4])+"</td></tr>"
    table+="</table>"
    context={'data':table}
    return render(request,'Customer/GroupChatReply.html', context)


def ViewService(request):
    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()

    cur.execute("select * from sregister")
    data=cur.fetchall()
    table="<table><tr><th>Woker Name</th><th>Email</th><th>Mobile</th><th>Working Hours</th><th>Cost</th><th>Chat</th><th>Book Worker</th></tr>"
    for d in data:
        table+="<tr><td>"+str(d[1])+"</td><td>"+str(d[2])+"</td><td>"+str(d[7])+"</td><td>"+str(d[5])+"</td><td>Rs."+str(d[6])+"</td><td><a href='ChatWroker?sid="+str(d[0])+"&name="+str(d[1])+"'>Click</a></td><td><a href='BookService?sid="+str(d[0])+"'>Book</a></td></tr>"
    table+="</table>"
    context={'data':table}
    return render(request,'Customer/ViewServices.html', context)

def ChatWroker(request):
    w_id=request.GET['sid']
    w_name=request.GET['name']
    uid=request.session['userid']
    context={'w_id':w_id,'w_name':w_name,'uid':uid}
    return render(request,'Customer/ChatPage.html', context)

def ChatAction(request):
    w_id=request.POST['w_id']
    u_id=request.POST['uid']
    w_name=request.POST['w_name']
    msg=request.POST['message']
    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("insert into message values(null,'"+w_id+"','"+w_name+"','"+u_id+"','"+msg+"','waiting')")
    con.commit()
    context={'msg':'Your Message Sent...!!'}
    return render(request,'Customer/ChatPage.html', context)
def ViewReplay(request):
    uid=request.session['userid']
    user_id=str(uid)
    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("select * from message where u_id='"+user_id+"'")
    data=cur.fetchall()
    table="<table><tr><th>Worker</th><th>Your Message</th><th>Reply</th><th>Chat</th></tr>"
    for d in data:
        table+="<tr><td>"+str(d[2])+"</td><td>"+str(d[4])+"</td><td>"+str(d[5])+"</td><td><a href='/ChatWroker?sid="+str(d[1])+"&name="+str(d[2])+"'>Click</a></td></tr>"
    table+="</table>"
    context={'data':table}
    return render(request,'Customer/ViewReply.html', context)





