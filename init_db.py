from models.base import db_proxy, use_db

from models.player import Player
from models.round import Round

use_db()
db_proxy.connect()
print "Connected to database, creating tables"

db_proxy.create_tables([
	Player,
	Round
])