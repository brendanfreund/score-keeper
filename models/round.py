import datetime
from peewee import DateTimeField, ForeignKeyField, IntegerField

from .base import BaseModel
from .player import Player

class Round(BaseModel):
	'''Model to store a round'''

	player = ForeignKeyField(Player, index=True)
	finish_time = DateTimeField(null=True)
	score = IntegerField()

	def get_all_rounds(cls):
		'''Retrieves all scores in descending order'''
		try:
			return Round.select().order_by(Round.score.desc())
		except:
			return None

	@classmethod
	def get_scores_for_player(cls, player):
		'''Retrieve all scores for a given player'''
		try:
			return Round.select().where(Round.player == player).order_by(
				Round.finish_time.desc()
			)
		except:
			return None

	def save_round(cls, player, score):
		'''Saves the score for the player after a completed round'''
		_round = Round.create(
			player=player,
			score=score,
			finish_time=datetime.datetime.utcnow()
		)
		return _round


