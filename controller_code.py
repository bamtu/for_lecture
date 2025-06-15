def on_right_released():
    radio.send_number(0)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_down_released():
    radio.send_number(0)
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def on_left_released():
    radio.send_number(0)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_up_released():
    radio.send_number(0)
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)



def on_forever():
    if controller.up.is_pressed():
        radio.send_string("A1")
    if controller.down.is_pressed():
        radio.send_string("A2")
    if controller.left.is_pressed():
        radio.send_string("A3")
    if controller.right.is_pressed():
        radio.send_string("A4")
    if controller.A.is_pressed():
        radio.send_string("A5")
    if controller.B.is_pressed():
        radio.send_string("A6")

number = 30
radio.set_group(number)
forever(on_forever)
