from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template('home.html')

@public.route('/login',methods=['get','post'])
def login():
    if 'submit' in request.form:
        username=request.form['name']
        password=request.form['password']

        print(username,password)
        q="select * from login where username='%s' and password='%s' "%(username,password)
        res=select(q)
        print("test1")
        if res:
            session['username']=res[0]['username']
            Username=session['username']

            print("f")
            if res[0]['user_type']=="admin":
                return redirect(url_for('admin.adminhome'))
            elif res[0]['user_type']=="staff":
                return redirect(url_for('staff.staffhome'))
            elif res[0]['user_type']=="member":
                print("t")
                q="select * from men where username='%s'"%(Username)
                res=select(q)
                if res:
                    session['men_id']=res[0]['men_id']
                    men_id=session['men_id']
                return redirect(url_for('member.member_home'))

    return render_template("login.html")
   

@public.route('/registartion',methods=['get','post'])
def registartion():
    if 'submit' in request.form:
        email=request.form['Email']
        fname=request.form['Firstname']
        lname=request.form['Lastname']
        phone=request.form['Phone_number']  
        housename=request.form['House_name']
        state=request.form['State']
        city=request.form['city']
        district=request.form['District']
        pincode=request.form['Pincode']
        password=request.form['Password']
      
   

        
        q="insert into login values('%s','%s','member','1')"%(email,password)
        insert(q)

        q="insert into men values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','1')"%(email,fname,lname,housename,city,district,state,pincode,phone,password)
        insert(q)
        return redirect(url_for('public.login'))

    return render_template("registartion.html")