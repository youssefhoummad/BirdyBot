from src import db
from src.models import Category, Rank, Family, Bird


db.create_all()

avis = Category(name="الطيور") # الطائفة 
db.session.add(avis)

galliformes = Rank(name="الدجاجيات", category=avis)
db.session.add(galliformes)

phasianidae = Family(name="التدرجاوات", rank=galliformes)
db.session.add(phasianidae)

peafowl = Bird( name="Peafowl", 
                image="https://download.ams.birds.cornell.edu/api/v1/asset/29972541/large", 
                voice="https://download.ams.birds.cornell.edu/api/v1/asset/534904", 
                more_info="https://en.wikipedia.org/wiki/Peafowl",
                family=phasianidae,
                )

db.session.add(peafowl)

# canary = Bird( name="Canary", 
#                 image="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Serinus_canaria_-Parque_Rural_del_Nublo%2C_Gran_Canaria%2C_Spain_-male-8a.jpg/640px-Serinus_canaria_-Parque_Rural_del_Nublo%2C_Gran_Canaria%2C_Spain_-male-8a.jpg", 
#                 voice="http://www.orangefreesounds.com/wp-content/uploads/2015/04/Canaries-singing.mp3", 
#                 more_info="https://en.wikipedia.org/wiki/Atlantic_canary"
#                 )
# db.session.add(canary)



# commit all
db.session.commit()
