from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user,logout_user,login_required, current_user
from config import config
from utils import Utils
from embedded import all_reports, all_workshop2,obtener_report_por_id_user,obtener_report_por_id_user2
from pbiembedservice import PbiEmbedService
import json


# Models
from models.ModelUser import ModelUser

# Entities
from models.entities.User import User


app = Flask(__name__)

# load configuracion
app.config.from_object('config.BaseConfig')

csrf=CSRFProtect()
db = MySQL(app)
login_manager_app=LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        #print(request.form['username'])
        # print(request.form['password'])
        user = User(0,request.form['username'],request.form['password'])
        logged_user=ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                print(user.username)
                return redirect(url_for('home'))
            else:
                flash("invalid password")
                return render_template('auth/login.html')
        else:
            flash("User not found")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home')
@login_required
def home():
    # sacar los reportes que puede acceder el usuario
    id_user=current_user.id
    juegos = obtener_report_por_id_user(db,id_user)
    
    return render_template('home.html', juegos=juegos)


#listado de reports que tiene el usuario
@app.route("/prueba")
def juegos():
    id_user=current_user.id
    juegos = obtener_report_por_id_user(db,id_user)
    return render_template("prueba.html", juegos=juegos)


#recupera el id del reporte para mostrar el embedded
@app.route("/editar_juego/<int:id_repor>")
@login_required
def editar_juego(id_repor):
    
    # obtener id del reporte
    global juego
    juego = obtener_report_por_id_user2(db,id_repor)
   

    #obtener ids de los reportes que puede acceder el usuario
    id_user=current_user.id
    juegos = obtener_report_por_id_user(db,id_user)


    return render_template("editar_juego.html", juego=juego, juegos=juegos)



@app.route('/getembedinfo', methods=['GET'])
def get_embed_info():
    '''Returns report embed configuration'''
    #id=1
    #juego = obtener_report_por_id_user2(db,id)
    id_user=current_user.username
    #print(id_user)
    repor=juego
    #print(repor[3])
    config_result = Utils.check_config(app)
    if config_result is not None:
        return json.dumps({'errorMsg': config_result}), 500

    try:
        #es = PbiEmbedService()
        #print(dir(es))
        #embed_info = PbiEmbedService().get_embed_params_for_single_report(app.config['WORKSPACE_ID'], repor[2])
        embed_info = PbiEmbedService().RLS_roles(app.config['WORKSPACE_ID'], repor[2],id_user,repor[3])
        return embed_info
    except Exception as ex:
        return json.dumps({'errorMsg': str(ex)}), 500




@app.route('/pagina1')
@login_required
def pagina1():
   return "<h1>Pagina 1</h1>" 


@app.route('/pagina2')
@login_required
def pagina2():
   return "<h1>Pagina 2</h1>" 




""" @app.route('/allreports')
def reporte():
    areatrabajo = all_workshop2(app)
    #print(var)
    return all_reports(app,areatrabajo) """


def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Pagina no encontrada<h1>", 404



if __name__=='__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()