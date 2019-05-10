from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from portal_database import Team, Base, Tregister 

engine = create_engine('sqlite:///pythonportal.db')
Base.metadata.bind=engine
DBSession=sessionmaker(bind=engine)
session=DBSession()

team1=Team(name='Python')
session.add(team1)
session.commit()


trainer1=Tregister(name="Saral Kumar",
                   tid="AO1215371",
                   tdate="20-07-1994",
                   designation="Trainer cum Developer",
                   email="saralkumar238@gmail.com",
                   mobile="7207366926",
                   photo="https://lh3.googleusercontent.com/-jfYjLj1Mo2M/WOM6oVNZA5I/AAAAAAAAPkg/lHSWU_ZQZHoyNIgVPlkrL0-jBdpDfcmuwCEwYBhgL/w139-h140-p/DSC09228.JPG",
                   trainer_id=1)
session.add(trainer1)
session.commit()
print('added.....')

