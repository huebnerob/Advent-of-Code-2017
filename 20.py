import re


data = open('20.txt').readlines()


def parse_particle(s):
	garb = r'[ <>=pva]+'
	s = re.sub(garb, '', s.strip())
	p = [int(n) for n in s.split(',')]
	return ((p[0],p[1],p[2]),(p[3],p[4],p[5]),(p[6],p[7],p[8]))


particles = []
for i in range(len(data)):
	line = data[i]
	p = parse_particle(line)
	particles += [p]
	

def tick_particle(p):
	p_p, v_p, a_p = p[0], p[1], p[2]
	v_p = (v_p[0]+a_p[0], v_p[1]+a_p[1], v_p[2]+a_p[2])
	p_p = (p_p[0]+v_p[0], p_p[1]+v_p[1], p_p[2]+v_p[2])
	return (p_p, v_p, a_p)

def check_collisions(particles):
	colliding = set()
	for i in range(len(particles)):
		p = particles[i]
		if p in colliding:
			continue
		for j in range(i+1, len(particles)):
			q = particles[j]
			if q in colliding:
				continue
			if p[0][0] == q[0][0] and p[0][1] == q[0][1] and p[0][2] == q[0][2]:
				colliding.add(p)
				colliding.add(q)
				print("found collision at " + str(i) + " and " + str(j))
	for p in colliding:
		particles.remove(p)
	return particles
	
	
for i in range(1000):
	particles = [tick_particle(p) for p in particles]
	particles = check_collisions(particles)
	print("done with t=" + str(i))
