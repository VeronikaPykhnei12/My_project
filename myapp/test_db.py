from myapp.models import *
# db.create_all()
# db.drop_all()

f3 = Film(title='fffff', duration=1.24, rating=3.8)
f4 = Film(title='rrrr', duration=1.6, rating=1.5)

admin3 = Admin(nickname='lololololo', firstname='a', lastname='b', email='aca', phone='1234', password='1111')

hall1 = Hall(opacity=140)


db.session.add(f3)
db.session.add(f4)
db.session.add(admin3)
db.session.add(hall1)
db.session.commit()
t4 = Timetable(Admin_id=admin3.id)
db.session.add(t4)
db.session.commit()
r1 = Records(timetable_id=t4.id, film_id=f3.id, hall_id=hall1.id)
r2 = Records(timetable_id=t4.id, film_id=f4.id, hall_id=hall1.id)
db.session.add(r1)
db.session.add(r2)
db.session.commit()