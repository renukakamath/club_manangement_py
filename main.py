from flask import Flask
from public import public
from admin import admin
from staff import staff
from member import member

app=Flask(__name__)


app.secret_key='key' 
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(staff,url_prefix="/staff")
app.register_blueprint(member,url_prefix="/member")
app.run(debug=True,port=5034)