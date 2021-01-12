import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


delay = 0.01
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)



mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()

# figure out to run this program 


# from pynput.mouse import Button, Controller
# import time
# import random
# import sys

# mouse = Controller()

# def clicks(limit):
#     t = limit
#     start_time = time.time()
#     while t > 1:
#         mouse.click(Button.left, random.randint(13,15))
#         t -= 1
#         sys.stdout.write("\r")
#         sys.stdout.write(f'Clicks left: {t}')
#         sys.stdout.flush()
#         time.sleep(.36)

#     else:
#         elapsed_time = time.time() - start_time
#         print('  DONE!')
#         time.sleep(.5)
#         print(f'Elapsed Time: {round(elapsed_time)} Secs')

# limit = int(input("Enter desired amount of clicks!"))

# clicks(limit)


                

