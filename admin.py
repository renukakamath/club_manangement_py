from flask import *
from database import *
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')



@admin.route('/admin_managestaff',methods=['POST','GET'])
def admin_managestaff():
    if 'submit' in request.form:
        username=request.form['Email']
        password=request.form['Password']
        fname=request.form['Firstname']
        lname=request.form['Lastname']
        phone=request.form['Phone_number']
        gender=request.form['gender']
        state=request.form['State']
        City=request.form['City']
        district=request.form['District']
        pincode=request.form['Pincode']
        date=request.form['Date']
        q="insert into login values('%s','%s','staff','1')"%(username,password)
        insert(q)
        q="insert into staff values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',1)"%(username,fname,lname,phone,gender,City,district,state,pincode,date)
        insert(q)
       

   
        return redirect(url_for("admin.admin_managestaff"))

        

        
    data={}
    q="select * from staff"
    res=select(q)
    data['view']=res

    
        
    if 'action' in request.args:
        action=request.args['action']
        sid=request.args['sid']
    else:
        action=None

    if action=="inactive":
          q="update staff set staff_status='0' where staff_id='%s'"%(sid)
          update(q)
          return redirect(url_for("admin.admin_managestaff"))
    if action=="active":
          s="update staff set staff_status='1' where staff_id='%s'"%(sid)
          update(s)
          return redirect(url_for("admin.admin_managestaff"))

    if action == "update":
        q="select * from staff where staff_id='%s'"%(sid)
        val=select(q)
        data['staff']=val

        if 'update' in request.form:
            
            fname=request.form['Firstname']
            lname=request.form['Lastname']
            phone=request.form['Phone_number']
            gender=request.form['gender']
            state=request.form['State']
            City=request.form['City']
            district=request.form['District']
            pincode=request.form['Pincode']
            date=request.form['Date']

            q="update staff set staff_fname='%s', staff_lname='%s',staff_phone='%s',staff_gen='%s',staff_city='%s',staff_district='%s',staff_state='%s',staff_pin='%s',sdoj='%s' where staff_id='%s' "%(fname,lname,phone,gender,City,district,state,pincode,date,sid)
            update(q)
            return redirect(url_for("admin.admin_managestaff"))
       

    return render_template('admin_managestaff.html',data=data)


    return render_template('eventadd.html',data=data)
@admin.route('/admin_category',methods=['POST','GET'])
def admin_category():

    if 'submit' in request.form:
        name=request.form['Name']
        description=request.form['Description']
        q="insert into category values(null,'0','%s','%s')"%(name,description)
        insert(q)
        return redirect(url_for("admin.admin_category"))

    data={}
    q="select * from category"
    res=select(q)
    data ['view']=res
    if 'action' in request.args:
        action=request.args['action']
        cid=request.args['cid']
    else:
        action=None

    if action == "update":
        q="select * from category where cat_id='%s'"%(cid)
        val=select(q)
        data['category']=val

        if 'update' in request.form:
    
            name=request.form['Name']
            description=request.form['Description']
           

            q="update category set Name='%s', Description='%s' where cat_id='%s'"%(name,description,cid)
            update(q)
            return redirect(url_for("admin.admin_category"))
        
    return render_template('admin_category.html',data=data)


@admin.route('/admin_subcategory',methods=['POST','GET'])
def admin_subcategory():

    if 'submit' in request.form:
        name=request.form['Name']
      
        q="insert into subcat values(null,'%s')"%(name)
        insert(q)
        return redirect(url_for("admin.admin_subcategory"))

    data={}
    q="select * from subcat"
    res=select(q)
    data ['view']=res


    if 'action' in request.args:
        action=request.args['action']
        cid=request.args['cid']
    else:
        action=None

    if action == "update":
        q="select * from subcat where subcat_id='%s'"%(cid)
        val=select(q)
        data['category']=val

        if 'update' in request.form:
    
            name=request.form['Name']
          
           

            q="update subcat set subcat_name='%s' where subcat_id='%s'"%(name,cid)
            update(q)
            return redirect(url_for("admin.admin_subcategory"))
        
    return render_template('admin_subcategory.html',data=data)


@admin.route('/admin_managehall',methods=['POST','GET'])
def admin_managehall():

    data={}
    q="select * from subcat"
    res=select(q)
    data['subcat']=res


    q="select * from category"
    res=select(q)
    data['cat']=res




    q="select * from hall inner join subcat using (subcat_id) inner join category using (cat_id)"
    res=select(q)
    data['hallss']=res




    if 'submit' in request.form:
        subcat=request.form['subcat']
        category=request.form['category']
      
        q="insert into hall values(null,'%s','%s')"%(subcat,category)
        insert(q)
        return redirect(url_for("admin.admin_managehall"))


    
    if 'action' in request.args:
        action=request.args['action']
        cid=request.args['cid']
    else:
        action=None

    if action == "update":
        q="select * from hall where hall_id='%s'"%(cid)
        val=select(q)
        data['category']=val

        if 'update' in request.form:
    
            subcat=request.form['subcat']
            category=request.form['category']
          
           

            q="update hall set cat_id='%s' , subcat_id='%s' where hall_id='%s'"%(subcat,category,cid)
            update(q)
            return redirect(url_for("admin.admin_managehall"))
        
    return render_template('admin_managehall.html',data=data)




@admin.route('/admin_manageevent',methods=['POST','GET'])
def admin_manageevent():
    data={}


    hid=request.args['hid']

    q="select * from event inner join hall using (hall_id)  where hall_id='%s'"%(hid)
    res=select(q)
    data['hallss']=res




    if 'submit' in request.form:
        date=request.form['date']
        rate=request.form['rate']
        eventtype=request.form['eventtype']
        hid=request.args['hid']
      
        q="insert into event values(null,'%s','%s','%s','%s')"%(hid,date,rate,eventtype)
        insert(q)
        return redirect(url_for("admin.admin_manageevent",hid=hid))


    
    if 'action' in request.args:
        action=request.args['action']
        cid=request.args['cid']
    else:
        action=None

    if action == "update":
        q="select * from hall where hall_id='%s'"%(cid)
        val=select(q)
        data['category']=val

        if 'update' in request.form:
    
            date=request.form['date']
            rate=request.form['rate']
            eventtype=request.form['eventtype']
            hid=request.args['hid']
          
           

            q="update event set hall_id='%s' , b_date='%s',h_rate='%s',event_type='%s' where hall_id='%s'"%(hid,date,rate,eventtype,hid)
            update(q)
            return redirect(url_for("admin.admin_manageevent",hid=hid))
        
    return render_template('admin_manageevent.html',data=data,hid=hid)


@admin.route('/admin_Viewmember',methods=['POST','GET'])
def admin_Viewmember():
    data={}


    if "action" in request.args:
        action=request.args['action']
        mid=request.args['mid']


    else:
        action=None



    if action=='accept':
        q="update men set men_status='1' where username='%s'"%(mid)
        update(q)
        q="update login set status='1' where username='%s'"%(mid)
        update(q)
        return redirect(url_for('admin.admin_Viewmember'))


    if action=='reject':
        q="update men set men_status='0' where username='%s'"%(mid)
        update(q)
        q="update login set status='0' where username='%s'"%(mid)
        update(q)
        return redirect(url_for('admin.admin_Viewmember'))


    q="select * from  men inner join login using (username)"
    res=select(q)
    data['mens']=res

        
    return render_template('admin_Viewmember.html',data=data)


@admin.route('/admin_vieweventbooking',methods=['POST','GET'])
def admin_vieweventbooking():
    data={}


    q="    SELECT * FROM `hallpay` INNER JOIN `event` USING (`event_id`) INNER JOIN `men` USING (`men_id`) INNER JOIN hall USING (hall_id) INNER JOIN category USING (cat_id) INNER JOIN subcat USING (subcat_id)"
    res=select(q)
    data['mens']=res

        
    return render_template('admin_vieweventbooking.html',data=data)





@admin.route('/admin_viewpayment',methods=['POST','GET'])
def admin_viewpayment():
    data={}


    q="SELECT * FROM `pay` INNER JOIN `fee` USING (fee_id) INNER JOIN `men` USING (`men_id`) INNER JOIN `hallpay` USING (`hpay_id`)"
    res=select(q)
    data['pay']=res

        
    return render_template('admin_viewpayment.html',data=data)




    




    
    