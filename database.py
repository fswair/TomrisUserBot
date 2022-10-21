from submodules.MentoDB import MentoConnection, Mento
from models import TomrisConfigModel

connection = MentoConnection(database="./database/tomris.db")
db = Mento(connection=connection)


db.create(table="tomris", model=TomrisConfigModel)
