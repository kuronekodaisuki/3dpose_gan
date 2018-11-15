
import pygame
#from werkzuek.utils import secure_filename

labels = [
    'Hip',
    'R_Hip',
    'R_Knee',
    'R_Foot',
    'L_Hip',
    'L_Knee',
    'L_Foot',
    'Thorax',
    'Spine',
    'L_Shoulder',
    'L_Elbow',
    'L_Wrist',
    'R_Shoulder',
    'R_Elbow',
    'R_Wrist'
]

skeleton = [
    [0, 1],
    [1, 2],
    [2, 3],
    [0, 4],
    [4, 5],
    [5, 6],
    [0, 7],
    [7, 8],
    [8, 9],
    [9, 10],
    [8, 11],
    [11, 12],
    [12, 13],
    [8, 14],
    [14, 15],
    [15, 16]
]


class Skeleton():
    def __init__(self, keypoints):
        self.keypoints = keypoints

    def draw(self):
        glBegin(GL_LINES)
        for bone in skeleton:
            for vertex in bone:
                glVertex3fv(self.keypoints[vertex])
            glEnd()

    def run(self):
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
        gluPerspective(45, (display[0] / display[1]), 0, 1, 50.0)
        glTranslatef(0.0, 0.0, -5)
        glRotate(180, 1, 0, 0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                glRotate(1, 9, 1, 0)
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                self.draw()
                pygame.display.flip()
                pygame.time.wait(10)

