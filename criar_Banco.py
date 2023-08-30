from fakepinterest import database,app
from fakepinterest.models import Usuario,Foto

with app.app_context():
    user = Foto.query.all()
    for foto in user:
       print(foto)




