from flask import Blueprint, render_template, request
import mysql.connector




db = mysql.connector.connect(
    host="food.ctei4ke8guph.us-east-2.rds.amazonaws.com",
    user="root",
    password="Koushik1",
    database="FOOD"
)



auth_bp = Blueprint('view', __name__)

@auth_bp.route('/')
def index():
    return render_template('home.html')


@auth_bp.route('/loginpage')
def loginpage():
    return render_template('login.html')

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    if result:
        return render_template('menu.html')
    else:
        return 'Login failed'

@auth_bp.route('/registerpage')
def registerpage():
    return render_template('registerpage.html')

@auth_bp.route('/register', methods=['POST'])
def register():
    cursor = db.cursor()
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    if password != confirm_password:
        return 'Passwords do not match'
    else:
       
        cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        return render_template('login.html')

def get_users():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user")
    return cursor.fetchall()

@auth_bp.route('/tracking')
def tracking():
    return render_template('track.html')

@auth_bp.route('/trackregister')
def trackregister():
    return render_template('trackregister.html')

@auth_bp.route('/track', methods=['POST'])
def track():
    cursor = db.cursor()
    username=request.form['id']
    cursor.execute("SELECT * FROM `orders` where customer_name=%s",(username,))
    result_set = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    return render_template('users.html', users=result_set, column_names=column_names)

@auth_bp.route('/about')
def about():
    return render_template('about.html')

@auth_bp.route('/menu')
def menu():
    return render_template('menu.html')

@auth_bp.route('/registerorder', methods=['POST'])
def registerorder():
    cursor = db.cursor()
    cname = request.form['name']
    nol = request.form['nol']
    dest = request.form['dest']
 



    cursor.execute("INSERT INTO `orders` (customer_name,order_details,address,status) VALUES (%s,%s,%s,'Confirmed')", (cname, nol,dest))
    db.commit()
    return render_template('track.html')


