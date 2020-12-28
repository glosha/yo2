# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

import simple_draw_m as sd
import pygame as pg

def bubble(point, step, color):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2, color=color)



def smile(point, radius, color):
    radius = 60
    r4 = radius//4
    ryx = radius//5
    ryy = radius//10
    sd.circle(center_position=point, radius=radius, width=2, color=color)
    p1 = sd.get_point(point.x-2*r4, point.y - 2*r4)
    p2 = sd.get_point(point.x+2*r4, point.y + 2*r4)
    rect = sd._to_screen_rect(p1,p2);
    sd.arc(rect, 3.5, 5.9, color = color)
    p1 = sd.get_point(point.x-2*ryx, point.y + r4)
    p2 = sd.get_point(point.x+2*ryx, point.y + r4)
    sd.circle(center_position=p1, radius=ryy, width=2, color=color)
    sd.circle(center_position=p2, radius=ryy, width=2, color=color)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  sd.resolution = (1200, 600)


    # for y in range(50, 151, 50):
    #     for x in range(100, 1100, 100):
    #         point = sd.get_point(x, y)
    #         bubble(point=point, step=5)


# for _ in range(2):
#     step = random.randint(2,10)
#     color = sd.random_color()
#     point=sd.random_point()
#     bubble(point=point, step=step, color=color)

#rect = pg.Rect((50, 50, 100, 100))
#p2 = sd.get_point(200, 200)
#rect = sd._to_screen_rect(p1,p2);

#sd.rectangle(rect.bottomleft, rect.topright);
#sd.rectangle(p1, p2 );
#sd.circle(p1, radius=50, width=2)
for _ in range(10):
    color = sd.random_color()
    p1=sd.random_point()
    smile(p1,radius=50,color=color)

#rect = sd._to_screen_rect(sd.get_point(100, 200), sd.get_point(200, 100))
#sd.arc(rect, 4, 5.4)
#sd.arc(rect, 0, 6.2)
#         point = sd.get_point(x, y)


sd.pause()