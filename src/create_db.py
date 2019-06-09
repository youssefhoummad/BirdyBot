from src import db
from src.models import Bird


db.create_all()

peafowl = Bird( name_en="Peafowl", 
                image="https://download.ams.birds.cornell.edu/api/v1/asset/29972541/large", 
                voice="https://download.ams.birds.cornell.edu/api/v1/asset/534904", 
                more_info="https://en.wikipedia.org/wiki/Peafowl"
                )
db.session.add(peafowl)

canary = Bird( name_en="Peafowl", 
                image="https://en.wikipedia.org/wiki/Atlantic_canary#/media/File:Serinus_canaria_-Parque_Rural_del_Nublo,_Gran_Canaria,_Spain_-male-8a.jpg", 
                voice="http://www.orangefreesounds.com/wp-content/uploads/2015/04/Canaries-singing.mp3", 
                more_info="https://en.wikipedia.org/wiki/Atlantic_canary"
                )
db.session.add(canary)



# commit all
db.session.commit()
