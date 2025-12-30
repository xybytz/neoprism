class Event:

	def __init__(self, timestamp, event_type, data):

		self.timestamp = timestamp
		self.event_type = event_type
		self.data = data

class KeyboardEvent(Event):

	def __init__(self,timestamp,):
		super().__init__(timestamp,)