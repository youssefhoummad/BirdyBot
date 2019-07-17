from src import db
from src.models import Category, Rank, Family, Bird


db.create_all()

avis = Category(name="الطيور") # الطائفة 
db.session.add(avis)



galliformes = Rank(name="الدجاجيات", category=avis)
db.session.add(galliformes)

passeriformes = Rank(name="	عصفوريات", category=avis)
db.session.add(passeriformes)



phasianidae = Family(name="التدرجاوات", rank=galliformes)
db.session.add(phasianidae)

fringillidae = Family(name="شرشوريات", rank=galliformes)
db.session.add(fringillidae)



peafowl = Bird( name="طاووس", 
                image="https://cdn.pixabay.com/photo/2017/03/27/14/51/animal-2179187_960_720.jpg", 
                voice="https://download.ams.birds.cornell.edu/api/v1/asset/534904", 
                more_info="https://ar.wikipedia.org/wiki/طاووس",
                family=phasianidae,
                )

db.session.add(peafowl)

canary = Bird( name="كناري", 
                image="https://cdn.pixabay.com/photo/2019/06/24/22/03/canary-4296994_960_720.jpg", 
                voice="http://www.orangefreesounds.com/wp-content/uploads/2015/04/Canaries-singing.mp3", 
                more_info="https://ar.wikipedia.org/wiki/كناري",
                family=phasianidae,
                )

db.session.add(canary)



# الطاووس
# https://cdn.pixabay.com/photo/2017/03/27/14/51/animal-2179187_960_720.jpg
# كناري
# https://cdn.pixabay.com/photo/2019/06/24/22/03/canary-4296994_960_720.jpg
# الطنان
# https://cdn.pixabay.com/photo/2017/03/13/10/25/hummingbird-2139279_960_720.jpg
# حمام
# https://cdn.pixabay.com/photo/2017/07/18/18/24/dove-2516641_960_720.jpg
# إوزة
# https://cdn.pixabay.com/photo/2017/02/28/23/00/swan-2107052_960_720.jpg
# بومة
# https://cdn.pixabay.com/photo/2014/06/25/15/05/eagle-owl-377192_960_720.jpg
# نسر
# https://cdn.pixabay.com/photo/2017/06/09/09/39/adler-2386314_960_720.jpg
# غراب
# https://cdn.pixabay.com/photo/2017/03/21/18/46/raven-2162966_960_720.jpg
# لقلاق
# https://cdn.pixabay.com/photo/2017/05/12/21/42/stork-2308235_960_720.jpg
# فلامنغو
# https://cdn.pixabay.com/photo/2019/06/27/20/14/flamingo-4303036_960_720.jpg
# دجاجة
# https://cdn.pixabay.com/photo/2017/05/31/22/56/the-hen-2361934_960_720.png
# بطة
# https://cdn.pixabay.com/photo/2019/03/11/02/49/mallard-4047693_960_720.jpg
# هدهد
# https://cdn.pixabay.com/photo/2017/07/04/19/53/hoopoe-2472362_960_720.jpg


db.session.commit()
