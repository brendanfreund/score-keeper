from peewee import CharField, ForeignKeyField, IntegerField

from .base import BaseModel

class Player(BaseModel):
	'''Model to store player information'''

	name = CharField(null=True)
	high_score = IntegerField()

	def get_by_name(cls, name):
		'''Get a player by name'''
		try:
			return Player.get(Player.name == name)
		except:
			return None

	def create_player(cls, name):
		'''Create a player'''
		player = Player.create(
			name=name,
			high_score=0
		)
		return player
