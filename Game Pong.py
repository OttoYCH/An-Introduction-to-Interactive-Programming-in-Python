# Game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ACCELERATE = 0.25

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [random.randrange(60, 180) / 60, random.randrange(120, 240) / 60] 

    if direction == RIGHT:
        ball_vel[0] *= 1
        ball_vel[1] *= -1
 
    else:
        ball_vel[0] *= -1
        ball_vel[1] *= -1

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  
    global score1, score2  
    
    paddle1_pos, paddle2_pos = HEIGHT / 2, HEIGHT / 2
    paddle1_vel, paddle2_vel = 0, 0
    score1, score2 = 0, 0
    
    spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
         
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0] 
    ball_pos[1] += ball_vel[1] 
    
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH) or ball_pos[0] >= WIDTH - (BALL_RADIUS + PAD_WIDTH):
        ball_vel[0] *= -1
        
        # Player1
        if ball_pos[0] < WIDTH / 2:
            if paddle1_pos <= ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
                ball_vel[0] += ACCELERATE * ball_vel[0]
               
            else:
                score2 += 1
                spawn_ball(RIGHT)
        # Player2
        if ball_pos[0] > WIDTH / 2:
            if paddle2_pos <= ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
                ball_vel[0] += ACCELERATE * ball_vel[0]
                
            else:
                score1 += 1
                spawn_ball(LEFT)
        
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] *= -1
    
       
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Yellow", "Yellow")
    
    # update paddle's vertical position, keep paddle on the screen
    if (0 <= paddle1_pos and paddle1_vel < 0) or (paddle1_pos <= HEIGHT - PAD_HEIGHT and paddle1_vel > 0):
        paddle1_pos += paddle1_vel
    if (0 <= paddle2_pos and paddle2_vel < 0) or (paddle2_pos <= HEIGHT - PAD_HEIGHT and paddle2_vel > 0):
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos],[HALF_PAD_WIDTH, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, "Red")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos],[WIDTH - HALF_PAD_WIDTH, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, "Red")
   
    # draw scores
    canvas.draw_text(str(score1), [200, 60], 40, "White")
    canvas.draw_text(str(score2), [400, 60], 40, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    vel = 7
    # Player1
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = vel
        
    # Player2
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = vel

def keyup(key):
    global paddle1_vel, paddle2_vel

    # Player1
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
        
    # Player2
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)

# start frame
new_game()
frame.start()            