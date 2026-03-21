from Radio import Receiver

def move_forward():
    print("Robot moving forward")

def stop_robot():
    print("Robot stopping")

def turn_left():
    print("Robot turning left")

def unknown_command(msg):
    print("Unknown command:", msg)

rx = Receiver()

#To DO Change to binary package
rx.add_handler("FORWARD", move_forward)
rx.add_handler("STOP", stop_robot)
rx.add_handler("LEFT", turn_left)
rx.set_default_handler(unknown_command)

rx.listen()