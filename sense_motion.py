    def sense(self): #do not change the name of this function
        Z = []

        # ENTER CODE HERE
        # HINT: You will probably need to use the function atan2()
        for i in range(len(landmarks)):
            dx=landmarks[i][1]-self.x
            dy=landmarks[i][0]-self.y
            Z.append((atan2(dy,dx)-self.orientation+(2*pi))%(2*pi))

        return Z #Leave this line here. Return vector Z of 4 bearings.
      
      

    def move(self, motion): # Do not change the name of this function

        # ADD CODE HERE
        result=robot(self.length)
        turn=random.gauss( motion[0],self.steering_noise)
        forward=random.gauss(motion[1],self.distance_noise)
        #print tan(turn), forward, self.length
        beta=(forward*tan(turn)/self.length)
        #print beta
        
        if abs(beta)<0.001:
            result.x=self.x+(forward*cos(self.orientation))
            result.y=self.y+(forward*sin(self.orientation))
        else:
            R=forward/beta
            cx=self.x-(sin(self.orientation)*R)
            cy=self.y+(cos(self.orientation)*R)
            result.x=cx+(sin(self.orientation+beta)*R)
            result.y=cy-(cos(self.orientation+beta)*R)
        
        #result.x%=(world_size)
        #result.y%=(world_size)
        result.orientation=(self.orientation+beta)%(2*pi)
        result.set_noise(0.,0., 0.)
        return result # make sure your move function returns an instance
                      # of the robot class with the correct coordinates.
                    