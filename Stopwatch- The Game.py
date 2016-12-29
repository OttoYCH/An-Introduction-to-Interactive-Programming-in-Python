import simplegui

time = 0
run = False
time_stop = 0     # number of successful stops
time_match = 0    # number of total stops

# Time format A:BC.D
def format(t):
    minutes = t // 600
    amount_second = t // 10
    tens_second = amount_second % 60
    tens_second //= 10
    second = amount_second % 10
    tenths_second = t % 10
    return str(minutes) + ":" + str(tens_second) + str(second) + "." + str(tenths_second)
 
# Eevent handlers for buttons; "Start", "Stop", "Reset"
def start():
    global run
    run = True
    timer_handler()

def stop():
    global time, run, time_stop, time_match
    run = False
    time_stop += 1
    if (time % 10 == 0):
        time_match += 1

def reset():
    global time, run, time_stop, time_match
    run = False
    time = 0
    time_stop = 0
    time_match = 0

# Timer with 0.1 sec interval
def timer_handler():
    global time, run
    
    if run:
        time += 1

# define draw handler
def draw(canvas):
    global time
    canvas.draw_text(format(time), (60, 80), 30, 'White')
    canvas.draw_text(str(time_match) + "/" + str(time_stop), (140, 20), 20, 'Green')
    
# create frame
frame = simplegui.create_frame("Stopwatch", 180, 140)
frame.set_draw_handler(draw)
start = frame.add_button("Start", start)
stop = frame.add_button("Stop", stop)
reset = frame.add_button("Reset", reset)

# register event handlers
creat_timer = simplegui.create_timer(100, timer_handler)
creat_timer.start()

# start frame
frame.start()            