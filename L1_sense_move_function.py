#Modify the move function to accommodate the added 
#probabilities of overshooting or undershooting 
#the intended destination.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
	#normalization:
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = [0,0,0,0,0]
    for i in range(len(p)):
		#the computation using the old p[i], then we need a temp s.
        s=0
        s=s+(p[(i-U)%len(p)]*pExact)
        s=s+p[(i-U+1)%len(p)]*pUndershoot
        s=s+p[(i-U-1)%len(p)]*pOvershoot
        q[i]=s
		#pExact+pUndershoot+pOvershoot==1, so we don't need normalization
    return q
    

print move(p, 1)