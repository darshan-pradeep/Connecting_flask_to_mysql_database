from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_USER']='root'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_PASSWORD']='kartikeya'
app.config['MYSQL_DB']='flask'

mysql=MySQL(app)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        user_name=request.form['username']
        email_id=request.form['emailid']
        cursor=mysql.connection.cursor()
        query=(f"insert into flask.user_details values ('{user_name}','{email_id}')")
        cursor.execute(query)
        mysql.connection.commit()
        cursor.close()
        return "success"
    return render_template('index.html')

    
@app.route('/users')
def users():
    cursor=mysql.connection.cursor()
    cursor.execute('select * from flask.user_details')
    user_details=cursor.fetchall()
    if len(user_details) > 0:
        return render_template('users.html',user_details=user_details)
    else:
        return 'Empty database'


if __name__=='__main__':
    app.run(debug=True)