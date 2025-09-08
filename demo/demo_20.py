from py5 import *

frame = 1
numFrames = 8
runAnimation = []


def load_sprites(frames_in_sprite):
    sprites = []
    for i in range(0, frames_in_sprite):
        sprites.append(load_image("./sprites/Run (" + str(i + 1) + ").png"))

    return sprites


def settings():
    size(1280, 720)


def setup():
    global runAnimation
    frame_rate(12)
    runAnimation = load_sprites(numFrames)


def draw():
    global runAnimation
    global frame

    background(255, 255, 255)
    image(runAnimation[frame], 100, 100)

    if frame < numFrames - 1:
        frame = frame + 1
    else:
        frame = 0


run_sketch()
