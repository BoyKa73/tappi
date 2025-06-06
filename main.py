from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import render_template


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tappi.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=True)
    fname = db.Column(db.String(100), nullable=True)
    lname = db.Column(db.String(100), nullable=True)
    street = db.Column(db.String(100), nullable=True)
    streetnr = db.Column(db.String(5), nullable=True)
    postal_code = db.Column(db.Integer, nullable=True)
    town = db.Column(db.String(100), nullable=True)
    area = db.Column(db.String(100), nullable=True)
    areac = db.Column(db.String(4), nullable=True)
    country = db.Column(db.String(100), nullable=True) 
    dob = db.Column(db.DateTime, nullable=True)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animalname = db.Column(db.String(150), nullable=True)
    fname = db.Column(db.String(100), nullable=True)
    lname = db.Column(db.String(100), nullable=True)
    street = db.Column(db.String(100), nullable=True)
    streetnr = db.Column(db.String(5), nullable=True)
    postal_code = db.Column(db.Integer, nullable=True)
    town = db.Column(db.String(100), nullable=True)
    area = db.Column(db.String(100), nullable=True)
    areac = db.Column(db.String(4), nullable=True)
    country = db.Column(db.String(100), nullable=True) 
    dob = db.Column(db.DateTime, nullable=True)
    birthtown = db.Column(db.String(100), nullable=True)
    nr_pre_owner = db.Column(db.Integer, primary_key=False)
    vaccination = db.Column(db.String(150), nullable=True)
    chipped = db.Column(db.Boolean, default =False, nullable=False)
    race = db.Column(db.String(150), nullable=True)
    colour = db.Column(db.String(100), nullable=True)
    origin = db.Column(db.String(200), nullable=True)
    date_of_death = db.Column(db.Date)


class VetShop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vetshop_name = db.Column(db.String(100))
    vetshop_street = db.Column(db.String(100))
    vetshop_streetnr = db.Column(db.String(5))
    vetshop_postal_code = db.Column(db.Integer)
    vetshop_town = db.Column(db.String(100))
    vetshop_area = db.Column(db.String(100))
    vetshop_areac = db.Column(db.String(4))
    vetshop_country = db.Column(db.String(100))
    vetshop_start = db.Column(db.Date)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=True)
    fname = db.Column(db.String(100), nullable=True)
    lname = db.Column(db.String(100), nullable=True)
    street = db.Column(db.String(100), nullable=True)
    streetnr = db.Column(db.String(5), nullable=True)
    postal_code = db.Column(db.Integer, nullable=True)
    town = db.Column(db.String(100), nullable=True)
    area = db.Column(db.String(100), nullable=True)
    areac = db.Column(db.String(4), nullable=True)
    country = db.Column(db.String(100), nullable=True) 
    dob = db.Column(db.DateTime, nullable=True)
    vetshop_id = db.Column(db.Integer, db.ForeignKey('vet_shop.id'))
    vetshop = db.relationship('VetShop', backref='doctors')

class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shopname = db.Column(db.String(100), nullable=True)
    shopfname = db.Column(db.String(100), nullable=True)
    shoplname = db.Column(db.String(100), nullable=True)
    shopstreet = db.Column(db.String(100), nullable=True)
    shopstreetnr = db.Column(db.String(5), nullable=True)
    shoppostal_code = db.Column(db.Integer, nullable=True)
    shoptown = db.Column(db.String(100), nullable=True)
    shoparea = db.Column(db.String(100), nullable=True)
    shopareac = db.Column(db.String(4), nullable=True)
    shopcountry = db.Column(db.String(100), nullable=True) 
    shopstart = db.Column(db.Date, nullable=True)
    shopcontent = db.Column(db.String(200), nullable=True)
    shopcategories = db.Column(db.String(200), nullable=True)

# Startseite öffnen
@app.route("/")
def index():
    return render_template("index.html")

#@app.route("/")
#def start_page():
#    return "<h1>Herzlich Willkommen bei t.App i , Deiner TierApp! </h1><a href ='hhtps://google.de'>Google</a>"

# Formular neuen User hinzuzufügen
@app.route("/add_user_form")
def add_user_form():
    return render_template("add_user_form.html")

# Neuen User hinzufügen
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    data = request.form # Erwartete ursprünglich JSON in der Anfrage (.get_json() )
    new_user = User(
        username=data['username'],
        fname=data['fname'],
        lname=data['lname'],
        street=data['street'],
        streetnr=data['streetnr'],
        postal_code=data['postal_code'],
        town=data['town'],
        area=data['area'],
        areac=data['areac'],
        country=data['country'],
        dob=datetime.strptime(data['dob'], '%Y-%m-%d')  # Datum umwandeln
    )
    db.session.add(new_user)
    db.session.commit()
    return "<h3>User hinzugefügt!</h3><a href='/'>Zurück</a>"    #{"message": "User hinzugefügt!"}, 201

# Formular neues Tier hinzufügen
@app.route("/add_animal_form")
def add_animal_form():
    return render_template("add_animal_form.html")

# Neues Tier hinzuzufügen
@app.route('/add_animal', methods=['GET', 'POST'])
def add_animal():
    data = request.form                      #Erwartet ursprünglich (.get_json() )
    new_animal = Animal(
        animalname=data['animalname'],
        fname=data['fname'],
        lname=data['lname'],
        street=data['street'],
        streetnr=data['streetnr'],
        postal_code=data['postal_code'],
        town=data['town'],
        area=data['area'],
        areac=data['areac'],
        country=data['country'],
        dob=datetime.strptime(data['dob'], '%Y-%m-%d'),
        birthtown=data['birthtown'],
        nr_pre_owner=data['nr_pre_owner'],
        vaccination=data['vaccination'],
        chipped=data['chipped'],
        race=data['race'],
        colour=data['colour'],
        origin=data['origin'],
        date_of_death=datetime.strptime(data['dod'], '%Y-%m-%d'),
    )
    db.session.add(new_animal)
    db.session.commit()
    return "<h3>Neues Tier hinzugefügt!</h3><a href='/'>Zurück</a>"       #{"message": "Tier hinzugefügt!"}, 201

# Formular neuer VetShop
@app.route("/add_vetshop_form")
def add_vetshop_form():
    return render_template("add_vetshop_form.html")

# Neuen VetShop hinzuzufügen
@app.route('/add_vetshop', methods=['GET','POST'])
def add_vetshop():
    data = request.form                # Erwartete ursprünglich JSON (.get_json()  )
    new_vetshop = VetShop(
        vetshop_name=data['vetshop_name'],
        vetshop_street=data['vetshop_street'],
        vetshop_streetnr=data['vetshop_streetnr'],
        vetshop_postal_code=data['vetshop_postal_code'],
        vetshop_town=data['vetshop_town'],
        vetshop_area=data['vetshop_area'],
        vetshop_areac=data['vetshop_areac'],
        vetshop_country=data['vetshop_country'],
        vetshop_start=datetime.strptime(data['vetshop_start'], '%Y-%m-%d')
    )
    db.session.add(new_vetshop)
    db.session.commit()
    return "<h3>VetShop hinzugefügt!</h3><a href='/'>Zurück</a>"         #{"message": "VetShop hinzugefügt!"}, 201

# Formular neuer Doctor hinzufügen
@app.route("/add_doctor_form")
def add_doctor_form():
    return render_template("add_doctor_form.html")

# Neuen Doctor hinzuzufügen
@app.route('/add_doctor', methods=['GET', 'POST'])
def add_doctor():
    data = request.form                            #Erwartetes JSON (.get_json()  )
    new_doctor = Doctor(
        username=data['username'],
        fname=data['fname'],
        lname=data['lname'],
        street=data['street'],
        streetnr=data['streetnr'],
        postal_code=data['postal_code'],
        town=data['town'],
        area=data['area'],
        areac=data['areac'],
        country=data['country'],
        dob=datetime.strptime(data['dob'], '%Y-%m-%d'),
        vetshop_id=data['vetshop_id']  # Verweis auf VetShop
    )
    db.session.add(new_doctor)
    db.session.commit()
    return "<h3>Doctor hinzugefügt!</h3><a href='/'>Zurück</a>"         #{"message": "Doctor hinzugefügt!"}, 201

# Formular neuer Shop hinzufügen
@app.route("/add_shop_form")
def add_shop_form():
    return render_template("add_shop_form.html")

# Neuen Shop hinzuzufügen
@app.route('/add_shop_form', methods=['GET', 'POST'])
def add_shop():
    data = request.form            #Erwartetes JSON Format (.get_json()  )
    new_shop = Shop(
        shopname=data['shopname'],
        shopfname=data['shopfname'],
        shoplname=data['shoplname'],
        shopstreet=data['shopstreet'],
        shopstreetnr=data['shopstreetnr'],
        shoppostal_code=data['shoppostal_code'],
        shoptown=data['shoptown'],
        shoparea=data['shoparea'],
        shopareac=data['shopareac'],
        shopcountry=data['shopcountry'],
        shopstart=datetime.strptime(data['shopstart'], '%Y-%m-%d'),
        shopcontent=data['shopcontent'],
        shopcategories=data['shopcategories']
    )
    db.session.add(new_shop)
    db.session.commit()
    return "<h3>Shop hinzugefügt!</h3><a href='/'>Zurück</a>"        #{"message": "Shop hinzugefügt!"}, 201


if __name__ == "__main__":
   with app.app_context():
        try:
            db.create_all() #Alle tabellen erstellen
            print("✅ Datenbanktabellen erstellt.")
        except Exception as e:
            print("❌ Fehler beim Erstellen der DB:", e)
   app.run()
