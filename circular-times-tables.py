#!/usr/bin/python
#-*- coding: utf-8 -*-
from colorconsole import ColorConsole as Console
import getopt
import math
import matplotlib.pyplot as plt
import os
import sys

class Program(object):
	def __init__(self, base, multiplier):
		self.x_dict = {}
		self.y_dict = {}
		self.setBase(base)
		self.multiplier = multiplier
	##################
	# Public methods #
	##################
	def manual(self):
		print '%s' % (Console.purple('Usage:'))
		print '  python %s %s %s %s' % (os.path.basename(__file__), Console.orange('-b base1'), Console.orange('[-B base2]'), Console.orange('-m multiplier'))
		print ''
		print '%s' % (Console.purple('Arguments:'))
		print '  %s\t\tinteger between 2 and 62. Default 10.' % Console.orange('base1')
		print '\t\tSets the point where the circle starts folding onto'
		print '\t\titself. Can be thought of as modulo, or the base used'
		print '\t\tfor counting.'
		print ''
		print '  %s\t\tInteger between 2 and 62. Optional.' % Console.orange('base2')
		print '\t\tWhen entered, graphs are plotted for the'
		print '\t\trange base1-base2.'
		print ''
		print '  %s\tAny integer. Default 2.' % Console.orange('multiplier')
		print ''
		print '%s' % (Console.purple('Example:'))
		print '  python %s -b 16 -m 2' % (os.path.basename(__file__))
		print '  Draws graph with base 16, multiplier 2'
	def run(self):
		self._createBasePlot()
		self._drawLines()

		self.fig.show()
	def setBase(self,base):
		self.N = base-1
		self.base = base
		self.angle = 2*math.pi/self.N
	def setMultiplier(self, multiplier):
		self.multiplier = multiplier
	def getMinBase(self):
		return 2
	def getMaxBase(self):
		return len("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
	###################
	# Private methods #
	###################
	def _baseN(self,num,b,numerals="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"):
		"""
		len(numerals) sets upper limit for b. Using "0-9A-Za-z" max base is 62.
		Transforms base 10 >> base b. Stringified result.
		"""
		return ((num == 0) and numerals[0]) or (self._baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])
	def _createBasePlot(self):
		"""
		Create figure, draw perimeter dots
		The dict keys are stored in base b, stringified
		"""
		for i in xrange(0,self.N+1):
			ix = self._baseN(i,self.base)
			self.x_dict[ix] = round(math.cos(math.pi/2 - i*self.angle), 5)
			self.y_dict[ix] = round(math.sin(math.pi/2 - i*self.angle), 5)

		self.fig, ax = plt.subplots()
		ax.set_xlim((-1,1))
		ax.set_ylim((-1,1))
		ax.plot(self.x_dict.values(), self.y_dict.values(), 'o', color='black')
		self.fig.suptitle('Modulo %i, multiplier %i' % (self.base, self.multiplier), fontsize=20)
	def _drawLines(self):
		"""
		Counter c
		prev_ix represents starting point of the first line to be drawn.
		"""
		c = 1
		prev_ix = 1
		for i in xrange(1,5*self.N+1):
			c *= self.multiplier

			ix = self._sum_digits_baseN(c,self.base)
			while ix >= self.base:
				ix = self._sum_digits_baseN(ix,self.base)

			xs = [self.x_dict[str(self._baseN(prev_ix,self.base))], self.x_dict[str(self._baseN(ix,self.base))]];
			ys = [self.y_dict[str(self._baseN(prev_ix,self.base))], self.y_dict[str(self._baseN(ix,self.base))]];

			plt.plot(xs, ys, 'k-', lw=1)
			prev_ix = ix
	def _sum_digits_baseN(self,n,b):
		"""
		Digit sum in base b
		Example1. Base 10: digit sum of 16 is 7
		Example2. Base 16: digit sum of 16 is 1
		"""
		s = 0
		while n:
			s += n % b
			n //= b
		return s

class BaseException(Exception):
	"""Custom exception if wrong base entered by user"""
	pass

if __name__ == '__main__':
	"""
	Default number base 10
	Default multiplier is 2
	Extra argument sets base to that argument in the range [2,62]
	62 because len of numerals "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" is 62.
	To increase max base: add more distinct numerals. Anything that makes up a valid string.
	"""
	b = 10
	B = 0
	m = 2
	p = Program(base=b, multiplier=m)
	MinBase = p.getMinBase()
	MaxBase = p.getMaxBase()
	argNum = len(sys.argv)
	if argNum == 1:
		p.manual()
		sys.exit(1)

	try:
		opts, args = getopt.getopt(sys.argv[1:], "b:B:m:", ["base=", "Base=", "multiplier="])
	except getopt.GetoptError as e:
		print Console.red('Error:'), e
		p.manual()
		sys.exit(1)
	if len(opts) == 0:
		p.manual()
		sys.exit(1)
	for opt, arg in opts:
		if opt == '-b':
			try:
				b = int(arg)
				if b < MinBase or b > MaxBase:
					raise BaseException()
				p.setBase(b)
			except BaseException:
				print Console.red('Error:'), 'Base should be between %i and %i.' % (MinBase, MaxBase)
			except Exception:
				print Console.red('Error:'), 'Could not convert \'%s\' to integer.' % (arg)
				sys.exit(1)
		elif opt == '-B':
			try:
				B = int(arg)
				if B < MinBase or B > MaxBase:
					raise BaseException()
			except BaseException:
				print Console.red('Error:'), 'Base should be between %i and %i.' % (MinBase, MaxBase)
			except Exception:
				print Console.red('Error:'), 'Could not convert \'%s\' to integer.' % (arg)
				sys.exit(1)
		elif opt == '-m':
			try:
				m = int(arg)
				p.setMultiplier(m)
			except Exception:
				print Console.red('Error:'), 'Could not convert \'%s\' to integer.' % (arg)
				sys.exit(1)

	if B:
		for bi in xrange(b,B+1):
			p.setBase(bi)
			p.run()
		raw_input('Press Enter to quit')
	else:
		p.run()
		raw_input('Press Enter to quit')
