from moviepy.editor import *
import pygame


def launch(movie):
    pygame.display.set_caption('Hello World!')
    clip = VideoFileClip(movie)
    clip.preview()
    pygame.quit()
    launch("Let Me In.mp4")

def main():
    pygame.display.set_caption('Hello World!')
    pygame.display.set_mode((0,0), 0, 32)
    clip = VideoFileClip('Let Me In.mp4')
    clip.preview()

    pygame.quit()


main()


