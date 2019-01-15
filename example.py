import trevo

pi,h = trevo.ini_tr()
while 1:
	dist = trevo.read_distance(pi,h)
	print(dist)
