class ColorConsole(object):
	"""Colorize the console"""
	BOLD = '\033[1m'
	BLUE = '\033[94m'
	ENDC = '\033[0m'
	GREEN = '\033[92m'
	ORANGE = '\033[93m'
	PURPLE = '\033[95m'
	RED = '\033[91m'
	UNDERLINE = '\033[4m'

	@staticmethod
	def red(s):
		return ColorConsole.RED +s+ ColorConsole.ENDC
	@staticmethod
	def blue(s):
		return ColorConsole.BLUE +s+ ColorConsole.ENDC
	@staticmethod
	def purple(s):
		return ColorConsole.PURPLE +s+ ColorConsole.ENDC
	@staticmethod
	def orange(s):
		return ColorConsole.ORANGE +s+ ColorConsole.ENDC
