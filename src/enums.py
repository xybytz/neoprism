import enum

class RawEventType(enum.Enum):

	KEY_DOWN = 0
	KEY_UP = 1
	MOUSE_DOWN = 2
	MOUSE_UP = 3
	MOUSE_MOVE = 4

class EventCategoryType(enum.Enum):

	KEYSTATUS = 0
	MOUSESTATUS = 1
	MOUSELOCATE = 2

class MKStatus(enum.Enum): # mk as in mouse/keyboard

	PRESS = 0
	RELEASE = 1