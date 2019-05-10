from flask import Flask,render_template,url_for,redirect,request
from werkzeug import secure_filename
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from portal_database import Team, Base, Tregister
app=Flask(__name__)

engine = create_engine(
    'sqlite:///pythonportal.db', connect_args={'check_same_thread': False},
    echo=True)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/worklogs')
def worklog():
    team = session.query(Team).all()
    return render_template('team_profile.html',team=team)

@app.route('/python')
def python_worklog():
    return render_template('python_work.html')

@app.route('/worklogs/new', methods=['GET','POST'])
def newTeam():
    if request.method=='POST':
        newTeam=Team(name=request.form['name'])
        session.add(newTeam)
        session.commit()
        return redirect(url_for('team_profile.html'))
    else:
        
        return render_template(url_for('newTeam.html'))
    
@app.route('/tregister')
def tregister():
    return render_template('trainer_reg.html')

@app.route('/trainer-login')
def tlogin():
    return render_template('trainerlogin.html')
if __name__=='__main__':
    app.run(debug=True)
