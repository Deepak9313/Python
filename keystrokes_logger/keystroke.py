from pynput.mouse import Button,Controller
mouse = Controller()
print("Current mouse position : {}".format(mouse.position))
# set mouter position
mouse.position = (200,200)
print("Current mouse position : {}".format(mouse.position))
mouse.move(10,100)
mouse.press(Button.left)