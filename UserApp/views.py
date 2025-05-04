from django.shortcuts import render
import pymysql

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'Customer/Login.html')

def Register(request):
    return render(request,'Customer/Register.html')


def RegAction(request):
    name=request.POST['name']
    email=request.POST['email']
    mobile=request.POST['mobile']
    address=request.POST['address']
    username=request.POST['username']
    password=request.POST['password']


    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("select * from register where  email='"+email+"' and mobile='"+mobile+"'")
    d=cur.fetchone()
    if d is not None:

     context={'msg':'Already Exist These Details...!!'}
     return render(request,'Customer/Register.html', context)
    else:
        cur=con.cursor()
        cur.execute("insert into register values(null,'"+name+"','"+email+"','"+mobile+"','"+address+"','"+username+"','"+password+"')")
        con.commit()
        context={'msg':'Successfully Registered Your Details...!!'}
        return render(request,'Customer/Register.html', context)

def LogAction(request):
    uname=request.POST['username']
    pwd=request.POST['password']

    con=pymysql.connect(host='localhost', user='root', password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("select * from register where username='"+uname+"' and password='"+pwd+"'")
    d=cur.fetchone()
    if d is not None:
        request.session['userid']=d[0]
        request.session['name']=d[1]
        request.session['email']=d[2]
        return render(request, 'Customer/CustomerHome.html')
    else:
        context={'msg':'Login Failed...!!'}
        return render(request, 'Customer/Login.html',context)

def CustomerHome(request):
    return render(request,'Customer/CustomerHome.html')

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
    table="<table><tr><tr><th>Woker name</th><th>Woker category</th><th>Email</th><th>Mobile</th><th>Working Hours</th><th>Cost</th><th>Chat</th><th>Book Worker</th></tr>"
    for d in data:
        table+="<tr><td>"+str(d[3])+"</td><td>"+str(d[1])+"</td><td>"+str(d[2])+"</td><td>"+str(d[7])+"</td><td>"+str(d[5])+"</td><td>Rs."+str(d[6])+"</td><td><a href='ChatWroker?sid="+str(d[0])+"&name="+str(d[1])+"'>Click</a></td><td><a href='BookService?sid="+str(d[0])+"'>Book</a></td></tr>"
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

def BookService(request):
    service_id=request.GET['sid']
    uid=request.session['userid']
    user_id=str(uid)

    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("insert into service_book values(null,'"+user_id+"','"+service_id+"',now(),'waiting')")
    con.commit()
    cur.execute("select * from sregister")
    data=cur.fetchall()
    table="<table><tr><th>Worker Name</th><th>Email</th><th>Mobile</th><th>Working Hours</th><th>Cost</th><th>Book</th></tr>"
    for d in data:
        table+="<tr><td>"+str(d[1])+"</td><td>"+str(d[2])+"</td><td>"+str(d[7])+"</td><td>"+str(d[5])+"</td><td>Rs."+str(d[6])+"</td><td><a href='BookService?sid="+str(d[0])+"'>Book Now</a></td></tr>"
    table+="</table>"
    context={'data':table,'msg':'Booking Successful ...!!'}
    return render(request,'Customer/ViewServices.html', context)





def viewbookings(request):
    uid=request.session['userid']
    user_id=str(uid)
    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur1=con.cursor()
    cur1.execute("select * from service_book sb, sregister sr where sb.service_id=sr.id and sb.userid='"+user_id+"'")
    data=cur1.fetchall()
    srtable="<table><tr><th>Worker category </th><th>Woker name</th><th>Email</th><th>Mobile</th><th>Working Hours</th><th>Cost</th><th>Booked Date</th><th>Booking Status</th></tr>"
    for d in data:
        srtable+="<tr><td>"+str(d[6])+"</td><td>"+str(d[8])+"</td><td>"+str(d[7])+"</td><td>"+str(d[12])+"</td><td>"+str(d[10])+"</td><td>Rs."+str(d[11])+"</td><td>"+str(d[3])+"</td><td>"+str(d[4])+"</td></tr>"
    srtable+="</table>"
    context={'servicetable':srtable}
    return render(request,'Customer/ViewAllBookings.html', context)




