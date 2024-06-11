from flask import *
from database import *
import uuid

member=Blueprint('member',__name__)

@member.route('/member_home')
def member_home():
    return render_template('member_home.html')


@member.route('/member_viewhall')
def member_viewhall():
	data={}
	q="select * FROM `hall` INNER JOIN `category` USING (`cat_id`) INNER JOIN `subcat` USING (`subcat_id`) inner join event using (hall_id)"
	res=select(q)
	data['hall']=res


	if "action" in request.args:
		action=request.args['action']
		hid=request.args['hid']
		eid=request.args['eid']
		amt=request.args['amt']
		men_id=session['men_id']
		q="insert into hallpay values(null,'%s','%s','%s',curdate(),'Booked')"%(eid,men_id,amt)
		insert(q)
		flash('successfully')
		return redirect(url_for('member.member_viewhall'))
	return render_template('member_viewhall.html',data=data)


@member.route('/member_viewbooking')
def member_viewbooking():
	data={}
	q="SELECT * FROM `hallpay` INNER JOIN `event` USING (`event_id`) INNER JOIN `men` USING (`men_id`)"
	res=select(q)
	data['hallpay']=res
	return render_template('member_viewbooking.html',data=data)



@member.route('/Member_makepayment',methods=['post','get'])
def Member_makepayment():
	data={}

	amt=request.args['amt']
	data['amt']=amt

	if "payment" in request.form:
		cname=request.form['cname']
		cnum=request.form['cnum']
		cvv=request.form['cvv']
		date=request.form['date']
		amt=request.args['amt']
		men_id=session['men_id']
		hpay_id=request.args['hpay_id']
		q="insert into card values(null,'%s','%s','%s','%s','%s')"%(men_id,cnum,cname,date,cvv)
		cid=insert(q)
		q="insert into fee values(null,'%s','%s','%s',curdate(),'Paid')"%(men_id,cid,amt)
		fid=insert(q)
		q="insert into pay values(null,'%s','%s')"%(hpay_id,fid)
		insert(q)
		q="update hallpay set fee_status='Paid' where hpay_id='%s'"%(hpay_id)
		update(q)
		return redirect(url_for('member.member_viewbooking'))

	return render_template('Member_makepayment.html',data=data)

