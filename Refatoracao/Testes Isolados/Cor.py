
class Cor:
	"""Define cores"""
	r = 1.0
	g = 1.0
	b = 1.0

	def __init__(ri=1.0, gi=1.0, bi=1.0):
		self.setR(ri)
		setG(gi)
		setB(bi)

	def setR(self, sr):
		self.r = sr
	def getR():
		return self.r

	def setG(self, sg):
		self.g = sg
	def getG():
		return self.g

	def setB(self, sb):
		self.b = sb
	def getB():
		return self.b

	def print():
		print(getR(),getG(),getB())

branco = Cor(1, 1, 1)
branco.print()
