from turtle import Turtle
import random
from turtle import Turtle

Color = ["red", "orange", "blue", "green", "purple"]
class Cars:
    def __init__(self) -> None:
        # super().__init__()
        self.traffic = []
        

    def create_car(self, lev):
        chance = random.randint(0,3)
        if chance == 1 or chance == 2:
            t = Turtle()
            t.speed(lev)
            
            t.color(random.choice(Color))
            t.shape('square')
            # t.setheading(90)
            t.shapesize(1,2)
            # old_pos_y = 0
            # pos_y = 0
            
            # if abs(old_pos_y - pos_y) < 20:
            pos_y = random.randint(-260,260)
            #     old_pos_y = pos_y
            
            t.penup()
            t.goto(300, pos_y)
            self.traffic.append(t)
            

    def move(self):
        for i in self.traffic:
            i.backward(20)
    
    # def collision(self, pos):
    #     flag = True
    #     for car in self.traffic:
    #         if car.distance(pos):
    #             flag = False
        
    #     return flag
                
        
        # return flag
    
    