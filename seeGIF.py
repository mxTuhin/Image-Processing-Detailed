import pyglet
from time import sleep

animation=pyglet.image.load_animation('see.gif')
animSprite=pyglet.sprite.Sprite(animation)

w=animSprite.width
h=animSprite.height
window=pyglet.window.Window(caption='', resizable=True, style=pyglet.window.Window.WINDOW_STYLE_DIALOG, height=480, width=940)
# window.set_fullscreen(True)

r,g,b,alpha=255.0,255.0,255.0,0.0

pyglet.gl.glClearColor(r,g,b,alpha)

@window.event
def on_draw():
    window.clear()
    animSprite.draw()
    # window.flip()

@window.event
def on_close():
    print("I'm closing now") #<- this never happens



pyglet.app.run()